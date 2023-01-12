from django.contrib.auth import get_user_model
from django.views.generic import CreateView

from user.forms import UserRegistrationForm


class UserRegistrationView(CreateView):
    template_name = 'user_model.html'
    model = get_user_model()
    form_class = UserRegistrationForm
    success_url = '/article/'
