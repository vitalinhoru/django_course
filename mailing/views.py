from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy

from mailing.forms import MailingForm, ClientForm
from mailing.models import Mailing, Client


class HomePageListView(ListView):
    model = Mailing
    template_name = 'mailing/base.html'


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing/mailing_list.html'


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    # permission_required = 'catalog.add_product'
    success_url = reverse_lazy('mailing:mailing')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ClientListView(ListView):
    model = Client
    template_name = 'mailing/client_list.html'


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:clients')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:clients')
