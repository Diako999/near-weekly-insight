from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class BlocksView(TemplateView):
    template_name = 'blocks.html'

class StakingView(TemplateView):
    template_name = 'staking.html'