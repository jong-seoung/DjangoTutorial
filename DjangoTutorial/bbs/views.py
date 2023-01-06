# bbs/views.py

from django.http import HttpResponse

def hello(request):                     # 핸들러 선언. 언제나 첫번째 인자는 request 객체입니다.
    return HttpResponse('Hello world.') # 핸들러의 반환값. HttpResponse 함수를 통해 문자열을 반환합니다.