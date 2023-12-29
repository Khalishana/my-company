from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Hana Kuliner',
        'company': 'Food and others'
    }

    return render(request, "index.html", context)