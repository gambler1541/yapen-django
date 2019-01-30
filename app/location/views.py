from django.shortcuts import render

from .models import Pensions

def location_list(request):
    pension = Pensions.objects.all()
    context = {
        'pension' : pension
    }
    return render(request, 'pension/pension_list.html', context)