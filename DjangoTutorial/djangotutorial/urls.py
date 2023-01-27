from django.contrib import admin
from django.urls import path

# 작성한 핸들러를 사용할 수 있게 가져옵니다.
from bbs.views import hello, ArticleListView, ArticleCreateUpdateView, ArticleDetailView
from user.views import UserRegistrationView, UserLoginView, UserVerificationView, ResendVerifyEmailView, SocialLoginCallbackView
from django.contrib.auth.views import LogoutView # 로그아웃

urlpatterns = [
    path('hello/<to>', hello),           # 'hello/'라는 경로로 접근했을 때 hello 핸들러가 호출되도록 추가합니다.
    path('admin/', admin.site.urls),

    path('article/', ArticleListView.as_view()),
    path('article/create/', ArticleCreateUpdateView.as_view()),
    path('article/<article_id>/', ArticleDetailView.as_view()),
    path('article/<article_id>/update/', ArticleCreateUpdateView.as_view()),

    path('user/create/', UserRegistrationView.as_view()), # 회원가입
    path('user/<pk>/verify/<token>/', UserVerificationView.as_view()), # 인증
    path('user/resend_verify_email/', ResendVerifyEmailView.as_view()),
    path('user/login/', UserLoginView.as_view()),         # 로그인
    path('user/logout/', LogoutView.as_view()),    # 로그아웃
    path('user/login/social/<provider>/callback/', SocialLoginCallbackView.as_view()),
]
