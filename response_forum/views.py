from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseBadRequest, HttpResponseForbidden
from django.views.generic import ListView, DetailView

from . import models
from .forms import ResponseForm


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


def create_response(request):
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            new_resp = form.save()
            return redirect(reverse('response-forum:details', args=[new_resp.id]))
        else:
            return HttpResponseBadRequest(request)
    else:
        return HttpResponseForbidden(request)
