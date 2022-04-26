from django.test import TestCase, Client
from django.urls import reverse
from .models import History, Actions
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
import os

list_data=[1,2,3,4,5]
module_dir = os.path.dirname(__file__)  # get current directory


class test_alls(TestCase):




    def test_register(self):
        url1 = reverse('register')
        response1 = self.client.get(url1)
        self.assertEqual(response1.status_code, 200)
        self.assertTemplateUsed((response1, 'app_panel/register.html'))


    def test_allnews(self):
        url3 = reverse('panel')
        response3 = self.client.get(url3)
        self.assertEqual(response3.status_code, 302)# у нас редирект на логин


    def test_begin(self):
        response0 = self.client.get('/')
        self.assertEqual(response0.status_code, 200)
        self.assertTemplateUsed(response0, 'app_panel/start.html')

    #тесты post операций


    def test_news(self):
        #Логиним пользователя
        user = User.objects.create(username='georges')
        user.set_password('nema1111')
        user.save()

        self.client=Client()
        self.client.login(username='georges', password='nema1111')
        # от его имени отправляем post запрос на создание новостей
        url1 = reverse('panel')
        response1 = self.client.get(url1)
        for i in list_data:
            self.client.post(reverse('panel'), {'name' : 'new_object','description':f'sssss{i}'})
        response1 = self.client.get(url1)

        #проверяем количество создания им истории покупок с количеством появихшихся у него в панели
        self.assertTrue(len(response1.context['history'])==len(list_data))
        print(response1.context['history'])


    def test_registration_post(self):

        family='Katatina'
        response1=self.client.post(reverse('register'),
                             {'username': f'{family}','password1':'nema1111',
                             'password2':'nema1111'})


        self.assertTrue(User.objects.get(id=1).username==family)
        self.assertTrue(response1.status_code == 302) #У нас редирект идет
        print(User.objects.all().count())

        self.assertTrue(User.objects.all().count() == 1)

