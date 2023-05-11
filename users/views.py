from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from faker import Faker
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.http import HttpResponseForbidden
import response_forum.models
from . import forms
from .forms import RegistrationForm

app_name = "users"


def user_page(request, pk):
    requested_user = get_object_or_404(User, pk=pk)
    responses = response_forum.models.Response.objects.filter(author__exact=requested_user).order_by('-publication_date')
    return render(request=request, template_name='registration/user_page.html',
                  context={'requested_user': requested_user, 'responses': responses})


@login_required(login_url='users:login')
def user_page_me(request):
    return redirect(reverse('users:user_page', args=[request.user.id]))


def create_fake_user(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden(request)

    amount = int(request.GET.get('amount') or 3)

    f = Faker('ru_RU')
    for i in range(amount):
        p = f.profile()
        passwd = f.password()
        with open('fake_users.txt', 'a+') as file:
            file.write('Username: @{} Password: {}\n'.format(p['username'], passwd))
            file.close()
        User.objects.create(
            username=p['username'],
            email=p['mail'],
            password=make_password(passwd)
        )
    return redirect('/')


def settings(request):
    if request.method == 'POST':
        form = forms.AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['avatar']
            request.user.profile.avatar = file
            request.user.profile.save()
        return redirect(reverse('users:settings'))
    form = forms.AvatarForm()
    return render(request=request, template_name='registration/settings.html', context={'form': form})


class UserRegistrationView(CreateView):
    template_name = 'registration/register.html'
    model = User
    form_class = RegistrationForm

    def get_success_url(self):
        return reverse('users:login')
