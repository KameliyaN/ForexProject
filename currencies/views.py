import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView

from currencies.forms import CurrencyForm, CategoryForm, LinksForm
from currencies.models import Currency, Category, Links


@login_required
def currencies_live_quotes(request):
    params = {
        'token': 'y4uhurw5suke60rirzzd',
        'currency': 'EUR/USD USD/JPY GBP/USD AUD/USD USD/CAD'
    }
    api_result = requests.get('https://currencydatafeed.com/api/data.php', params)

    api_response = api_result.json()
    currencies = api_response['currency']
    context = {'currencies': currencies}
    return render(request, 'currencies/quotes.html', context)


class CurrencyCreateView(LoginRequiredMixin, CreateView):
    model = Currency
    form_class = CurrencyForm
    template_name = 'currencies/currency_add.html'

    def form_valid(self, form):
        currency = form.save(commit=False)
        currency.save()
        return redirect('all_currency')


class CurrencyDetailView(LoginRequiredMixin, DetailView):
    model = Currency
    context_object_name = 'currency'
    template_name = 'currencies/currency_detail.html'


class CurrencyUpdateView(LoginRequiredMixin, UpdateView):
    model = Currency
    form_class = CurrencyForm
    template_name = 'currencies/currency_edit.html'

    def form_valid(self, form):
        currency = form.save(commit=False)
        currency.save()
        return redirect('detail currency', currency.pk)


class CurrencyDeleteView(LoginRequiredMixin, DeleteView):
    model = Currency
    success_url = reverse_lazy('all_currency')
    template_name = 'currencies/currency_delete.html'


class CurrencyAllView(LoginRequiredMixin, ListView):
    model = Currency
    context_object_name = 'currencies'
    template_name = 'currencies/currency_all.html'
    paginate_by = 3


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'currencies/category_add.html'

    def form_valid(self, form):
        category = form.save(commit=False)
        category.save()
        return redirect('all links')


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'currencies/category_edit.html'

    def form_valid(self, form):
        category = form.save(commit=False)
        category.save()
        return redirect('all links')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('all links')
    template_name = 'currencies/category_delete.html'
    context_object_name = 'category'


class LinkCreateView(LoginRequiredMixin, CreateView):
    model = Links
    form_class = LinksForm
    template_name = 'currencies/links_add.html'

    def form_valid(self, form):
        links = form.save(commit=False)
        links.save()
        return redirect('all links')


class LinkAllView(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'currencies/links_all.html'
    paginate_by = 2

    def get_queryset(self):
        return Category.objects.all()


class LinkUpdateView(LoginRequiredMixin, UpdateView):
    model = Links
    form_class = LinksForm
    template_name = 'currencies/links_edit.html'

    def form_valid(self, form):
        link = form.save(commit=False)
        link.save()
        return redirect('all links')


class LinkDeleteView(LoginRequiredMixin, DeleteView):
    model = Links
    success_url = reverse_lazy('all links')
    template_name = 'currencies/links_delete.html'
    context_object_name = 'link'
