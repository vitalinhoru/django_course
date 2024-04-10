from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy
import random

from blog.models import Blog
from mailing.forms import MailingForm, ClientForm, MessageForm
from mailing.models import Mailing, Client, Message, Logs
from mailing.services import get_cache_mailing_count, get_cache_mailing_active


class HomePageListView(ListView):
    model = Mailing
    template_name = 'mailing/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['mailings_count'] = get_cache_mailing_count()
        context_data['active_mailings_count'] = get_cache_mailing_active()
        context_data['clients_count'] = len(Client.objects.all())
        blog_list = list(Blog.objects.all())
        random.shuffle(blog_list)
        context_data['blog_list'] = blog_list[:3]
        return context_data


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing/mailing_list.html'


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing')

    def form_valid(self, form, *args, **kwargs):
        new_mailing = form.save(commit=False)
        new_mailing.owner = self.request.user
        new_mailing.save()
        return super().form_valid(form)


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'mailing/mailing_detail.html'


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing')


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing')


class ClientListView(ListView):
    model = Client
    template_name = 'mailing/client_list.html'


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:clients')


class ClientDetailView(DetailView):
    model = Client
    template_name = 'mailing/client_detail.html'


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:clients')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:clients')


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:create')


class LogsListView(ListView):
    model = Logs
    template_name = 'mailing/logs_list.html'
