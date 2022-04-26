from django.test import TestCase, Client
from django.urls import reverse
from app_files.models import  News, Profil, File
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
import os

list_data=[1,2,3,4,5]
module_dir = os.path.dirname(__file__)  # get current directory


class test_alls(TestCase):


    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='george', password='nema1111')


        for i in list_data:
            News.objects.create(name="supertest", user=user, description=f'desc{i}')


    # Тест работы базы данных
    def test_all(self):
        url1 = reverse('alnews')
        response1 = self.client.get(url1)
        self.assertTrue(len(response1.context['allnews'])==len(list_data))
        print(response1.context['allnews'])
    # пользовательские гет тесты


    def test_register(self):
        url1 = reverse('register')
        response1 = self.client.get(url1)
        self.assertEqual(response1.status_code, 200)
        self.assertTemplateUsed((response1, 'app_files/register.html'))


    def test_filecreate(self):
        url2 = reverse('filecreate')
        response2 = self.client.get(url2)
        self.assertEqual(response2.status_code, 200)


    def test_allnews(self):
        url3 = reverse('alnews')
        response3 = self.client.get(url3)
        self.assertEqual(response3.status_code, 200)


    def test_edit_news(self):
        news = News(name="supertest")
        news.save()
        #user = User(username="georgedd", password="nema1111")
        #user.save()
        response4 = self.client.get('/' + str(news.id) + '/edit/')
        self.assertEqual(response4.status_code, 403)




    def test_begin(self):
        response0 = self.client.get('/')
        self.assertEqual(response0.status_code, 200)
        self.assertTemplateUsed(response0, 'app_files/allnews.html')

    #тесты post операций


    def test_news(self):
        #Логиним пользователя
        user = User.objects.create(username='georges')
        user.set_password('nema1111')
        user.save()

        self.client=Client()
        self.client.login(username='georges', password='nema1111')
        # от его имени отправляем post запрос на создание новостей
        url1 = reverse('alnews')
        response1 = self.client.get(url1)
        for i in list_data:
            self.client.post(reverse('alnewss'), {'name' : 'new_object','description':f'sssss{i}'})

        #проверяем количество создания им новостей с количеством появихшихся новостей в ленте
        self.assertTrue(len(response1.context['allnews'])==len(list_data))
        print(response1.context['allnews'])


        # то же самое только с картинкой
    def test_news_picture(self):

        file_path = os.path.join(module_dir, 'ЧДД накопленный.png')
        #Логиним пользователя
        user = User.objects.create(username='georges')
        user.set_password('nema1111')
        user.save()
        newPhoto=File()
        newPhoto.image = SimpleUploadedFile(name='ЧДД накопленный.png', content=open(file_path, 'rb').read(),
                                            content_type='image/png')

        self.client=Client()
        self.client.login(username='georges', password='nema1111')
        # от его имени отправляем post запрос на создание новостей
        url1 = reverse('alnews')
        response1 = self.client.get(url1)
        for i in list_data:
            self.client.post(reverse('alnewss'), {'name' : 'new_object','description':f'sssss{i}','attachments':newPhoto.image})

        #проверяем количество создания им новостей с количеством появихшихся новостей в ленте
        self.assertTrue(len(response1.context['allnews'])==len(list_data))
        print(response1.context['allnews'])


    def test_edit_prof(self):

        user = User.objects.create(username='georges')
        user.set_password('nema1111')
        user.save()
        prof=Profil(user=user,description='fffff')
        prof.save()



        self.client=Client()
        self.client.login(username='georges', password='nema1111')



        response1=self.client.post(reverse('profedit-detail',args=[user.id]), {'username' : 'new_name','description':'sssss'})




        self.assertEqual(response1.status_code, 200)


    def test_edit_news(self):
        #Логиним пользователя

        user = User.objects.create(username='georges')
        user.set_password('nema1111')
        user.save()
        news=News(user=user,name='2222',description='fffff')
        news.save()



        self.client=Client()
        self.client.login(username='georges', password='nema1111')
        response1=self.client.post(reverse('edit-detail',args=[news.id]), {'name' : 'new_name','description':'sssss'})
        self.assertEqual(response1.status_code, 200)


    def test_registration_post(self):
        file_path = os.path.join(module_dir, 'ЧДД накопленный.png')
        # Логиним пользователя
        newPhoto = File()
        newPhoto.image = SimpleUploadedFile(name='ЧДД накопленный.png', content=open(file_path, 'rb').read(),
                                            content_type='image/png')

        family='sssss'
        response1=self.client.post(reverse('register'),
                             {'username': f'katarina','password1':'nema1111','familyname':family,
                             'password2':'nema1111','description': f'sssss', 'file': newPhoto.image})


        self.assertTrue(Profil.objects.get(id=1).familyname==family)
        self.assertTrue(response1.status_code == 302) #У нас редирект идет
        print(User.objects.all().count())

        self.assertTrue(Profil.objects.all().count()==1)
        self.assertTrue(User.objects.all().count() == 2)#За вычетом сетапа




















