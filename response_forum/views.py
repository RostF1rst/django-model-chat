import random
from datetime import timedelta

from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseBadRequest, HttpResponseForbidden
from django.utils import timezone
from django.views.generic import ListView, DetailView
from faker import Faker

from . import models
from .forms import ResponseForm


class ResponseListView(ListView):
    template_name = 'forum/responses.html'
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
            new_resp.author = request.user
            new_resp.save()
            return redirect(reverse('response-forum:details', args=[new_resp.id]))
        else:
            return HttpResponseBadRequest(request)
    else:
        return HttpResponseForbidden(request)


def create_fake_posts(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden(request)

    amount = int(request.GET.get('amount') or 3)

    f = Faker('ru_RU')
    users = User.objects.all()
    for i in range(amount):
        models.Response.objects.create(
            prompt=f.sentence(nb_words=10),
            response=f.sentence(nb_words=10),
            publication_date=f.date_time_between(timezone.now()-timedelta(days=30), timezone.now()),
            author=random.choice(users)
        )
    return redirect('/')
