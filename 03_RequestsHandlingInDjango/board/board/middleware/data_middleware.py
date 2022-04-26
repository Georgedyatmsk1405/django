from datetime import datetime, date, time

class datamiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        response=self.get_response(request)
        self.log = open('log.txt', 'a')
        self.log.write('Дата и время запроса: ' + str(datetime.today())[:-7] +
                       ', путь запроса: ' + request.path +
                       ', тип запроса: ' + request.method + '\n')
        self.log.close()
        return response

