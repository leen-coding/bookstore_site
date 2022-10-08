from django.shortcuts import render
from .models import card
# Create your views here.

def all_card(request):
    all_card = card.objects.all()
    # get = card.objects.get()
    print(all_card)
    return render(request,'card_store/all_card.html',locals())