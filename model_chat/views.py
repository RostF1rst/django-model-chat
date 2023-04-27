from django.shortcuts import render
from .gpt import GPTModel


def chat(request):
    # if request.session.get('model') is None:
    #     request.session['model'] = {'model': GPTModel()}

    context = {}

    if request.GET.get('prompt'):
        model = GPTModel()
        prompt = request.GET.get('prompt')
        responce = model.get_answer(prompt=prompt, full_answer=False)
        context.update({'prompt': prompt, 'responce': responce})

    return render(request=request, template_name='chat.html', context=context)
