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
            response = requests.get('https://evilinsult.com/generate_insult.php?lang=ru&type=json').json()['insult']
        return JsonResponse({'response': response})
    return JsonResponse({'error': 'forbidden'})
