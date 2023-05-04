from django.shortcuts import render
from response_forum.models import Response


def get_list_of_responses(request):
    search_filter = request.GET.get('filter') or ''
    model_list = Response.objects.filter(prompt__contains=search_filter).order_by('-publication_date')
    return render(request=request, template_name='forum/response_list.html', context={'object_list': model_list})
