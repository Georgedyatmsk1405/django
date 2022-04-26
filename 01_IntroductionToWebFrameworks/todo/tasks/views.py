from django.http import HttpResponse

from django.views import View


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        import random
        n = ['Установить python', 'Установить python', 'Запустить сервер', 'Порадоваться результату',
             'Еще раз порадоваться']
        b = []
        random.shuffle(n)
        for i in n:
            k = '<li>' + i + '</li>'
            b.append(k)

        c = str(b)
        d = '<ul>' + c + '</ul>'

        return HttpResponse(d)
