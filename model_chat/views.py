from django.shortcuts import render


def chat(request):
    return render(request=request, template_name='chat.html')
