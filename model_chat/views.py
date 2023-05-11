from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='users:login')
def chat(request):
    return render(request=request, template_name='chat.html')
