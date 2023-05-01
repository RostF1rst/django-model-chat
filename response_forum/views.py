from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView

from . import models


class ResponseListView(ListView):
    template_name = 'forum/list.html'
    model = models.Response

    def get_queryset(self):
        filter_value = self.request.GET.get('filter') or ''
        if filter_value:
            new_context = models.Response.objects.filter(prompt__contains=filter_value).all().order_by('-publication_date')
        else:
            new_context = models.Response.objects.all().order_by('-publication_date')
        return new_context


class ResponseDetailView(DetailView):
    template_name = 'forum/show.html'
    model = models.Response


class CreateResponseView(CreateView):
    template_name = 'forum/'
