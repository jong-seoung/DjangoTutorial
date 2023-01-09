# minitutorial/urls.py

from django.contrib import admin
from django.urls import path

# 작성한 핸들러를 사용할 수 있게 가져옵니다.
from bbs.views import hello, ArticleListView, ArticleCreateUpdateView, ArticleDetailView          

urlpatterns = [
    path('hello/<to>', hello),           # 'hello/'라는 경로로 접근했을 때 hello 핸들러가 호출되도록 추가합니다.
    path('admin/', admin.site.urls),

    path('article/', ArticleListView.as_view()),
    path('article/create/', ArticleCreateUpdateView.as_view()),
    path('article/<article_id>/', ArticleDetailView.as_view()),
    path('article/<article_id>/update/', ArticleCreateUpdateView.as_view()),
]
