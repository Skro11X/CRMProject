from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import CreateUser


class SignUpUser(CreateView):
    form_class = CreateUser
    success_url = reverse_lazy("login")
    template_name = "registration/sign_up.html"



