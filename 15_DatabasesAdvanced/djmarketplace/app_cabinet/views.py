from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.db.models import Count
from django.shortcuts import render, redirect, HttpResponse
from app_users.models import Profil
from app_cabinet.models import Product, Magasine, Korzina, History
from django.db import transaction
# Create your views here.
from django.views import View
from django.contrib.auth.models import User
from django.db import connection
from django.db import reset_queries
import logging
logger=logging.getLogger(__name__)
class CabinetView(View):

    def get(self, request):
        if request.user.is_authenticated:
            #тест prefetch related
            reset_queries()
            product=Product.objects.all().prefetch_related('magasine')
            for i in product:
                print(i.price)
                print(list(i.magasine.all()))
            print(connection.queries)
            #тест завершен


            user=Profil.objects.get(user=request.user)
            balance=user.balance
            status=user.status
            sum_of_buying=user.sum_buying
            logger.info('Запрошен баланс, сумма покупок, статус пользователя')


            return render(request, 'cabinet.html',context={'balance':balance,'status':status,'sum_of_buying':sum_of_buying})
        else:
            raise PermissionDenied



    def post(self, request):
        balance = int(request.POST.get('balance'))

        obj = Profil.objects.get(user=request.user.id)
        obj.balance +=balance
        obj.save()



        return redirect('cabinet')


class BuyingView(View):

    def get(self, request):
        if request.user.is_authenticated:
            user=Profil.objects.get(user=request.user)
            try:
                korzina=Korzina.objects.get(user=user)
            except ObjectDoesNotExist:
                korzina=None
            if korzina==None:
                return HttpResponse('корзина пуста')


            product=Product.objects.filter(products=korzina)

            print(str(product))
            list_of_buynig=[]
            for i in product:

               list_of_buynig.append(i.price)
            sum_of_buying=sum(list_of_buynig)
            balance=user.balance
            logger.info('Запрошен баланс, сумма покупок в корзине, статус пользователя')



            return render(request, 'korzina.html',context={'balance':balance,'sum_of_buying':sum_of_buying,'product':product})


        else:
            raise PermissionDenied



    def post(self, request):
        user = Profil.objects.get(user=request.user)
        korzina = Korzina.objects.get(user=user)
        product = Product.objects.filter(products=korzina)
        logger.info('Запросили юзера, корзину и продукт для оплаты покупок.')
        list_of_buynig = []
        reset_queries()

        for i in product:
            list_of_buynig.append(i.price)
        print(connection.queries)
        logger.info('Добавили все цены в сумму для выставления чека')
        sum_of_buying = sum(list_of_buynig)
        user = Profil.objects.get(user=request.user)
        obj = Profil.objects.get(user=request.user.id)
        if obj.balance<sum_of_buying:
            return HttpResponse('не достаточно средств')
        with transaction.atomic():

            obj.balance -=sum_of_buying
            obj.sum_buying+=sum_of_buying
            if obj.sum_buying>=1000 and obj.sum_buying< 2000:
                obj.status='medium'
            elif obj.sum_buying>=2000:
                obj.status = 'premium'
            else:
                obj.status='basic'
            obj.save()


            Korzina.objects.filter(user=user).delete()
            for i in product:
                History.objects.create(product=i.name)
                Product.objects.filter(id=i.id).delete()
            logger.info('Провели транзакцию')




        return redirect('cabinet')





class AddProductView(View):
    def get(self, request):

        list_of_products = Product.objects.all().prefetch_related('magasine')
        #for i in product:
            #print(i.price)
            #print(list(i.magasine.all()))
        logger.info('Запрошен лист продуктов')
        return render(request,'addproduct_list.html', context={'list_of_products':list_of_products})



    def post(self, request):
        name = request.POST
        name=list(name.keys())
        name=name[1]
        print("name:"+str(name))
        product=Product.objects.get(id=name)
        user = Profil.objects.get(user=request.user)
        print(user.id)
        korzina=Korzina.objects.filter(user=user).first()
        if korzina:
            pass

        else:
            korzina=Korzina.objects.create(user=user)

        korzina.product.add(product)
        logger.info('Добавили товар в корзину')

        return redirect ('addproduct')




class HistoryView(View):
    def get(self, request):


        list_of_products = History.objects.all().values('product').annotate(total=Count('product'))
        print(list_of_products)
        logger.info('Запрошена история')
        #for i in product:
            #print(i.price)
            #print(list(i.magasine.all()))
        return render(request,'history_list.html', context={'list_of_products':list_of_products})















