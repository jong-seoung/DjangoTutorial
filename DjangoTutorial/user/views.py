from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from user.forms import UserRegistrationForm


class UserRegistrationView(CreateView):
    template_name = 'user_model.html'
    model = get_user_model()
    form_class = UserRegistrationForm
    success_url = '/article/'

class UserLoginView(LoginView):           # 로그인
    template_name = 'login_form.html'

    def form_invalid(self, form):
        messages.error(self.request, '로그인에 실패하였습니다.', extra_tags='danger')
        return super().form_invalid(form)    
