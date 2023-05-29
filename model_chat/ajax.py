import random

import requests
from django.http import JsonResponse
from .llama import LlamaModel


def get_response(request):
    if request.method == 'POST':
        real = request.POST.get('real')
        if real == 'true':
            prompt = request.POST.get('prompt')
            model = LlamaModel()
            response = model.get_answer(prompt)
        else:
            urls = [
                ('http://asdfast.beobit.net/api/', 'text'),
                ('https://evilinsult.com/generate_insult.php?lang=ru&type=json', 'insult')
            ]
            choice = random.choice(urls)
            response = requests.get(choice[0]).json()[choice[1]]
        return JsonResponse({'response': response})
    return JsonResponse({'error': 'forbidden'})
