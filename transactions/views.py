from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class TransactionsView(TemplateView):
    template_name = 'transactions.html'


class SwapsView(TemplateView):
    template_name = 'swaps.html'