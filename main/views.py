from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse

# Create your views here.
def show_main(request):
    context = {
        'name': 'Hana Kuliner',
        'company': 'Food and others'
    }

    return render(request, "index.html", context)