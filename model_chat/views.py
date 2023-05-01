import random
import requests

from django.shortcuts import render


def chat(request):
    context = {}

    if request.GET.get('prompt'):
        prompt = request.GET.get('prompt')
        if request.GET.get('real'):
            from .llama import LlamaModel
            model = LlamaModel()
            response = model.get_answer(prompt=prompt, full_answer=False)
        else:
            response = random.choice(requests.get('https://type.fit/api/quotes').json())['text']
        context.update({'prompt': prompt, 'response': response, 'real': request.GET.get('real') or ''})

    return render(request=request, template_name='chat.html', context=context)
