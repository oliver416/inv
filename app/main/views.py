from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from .models import Currency


# @login_required
def index(request):
    currencies = Currency.objects.all()
    funds = list()
    ruble = 63.8
    result = 0
    for pack in currencies:
        change = ruble*pack.value - pack.value*pack.price
        result += change
        style = 'red'
        if change >= 0:
            style = 'green'
        funds.append({'pack': str(pack.number) + ' ' + str(pack.date) + ' ' + str(pack.value) + ' ' + str(pack.price),
                      'change': str(change), 'style': style})
    res_style = 'red'
    if result >= 0:
        res_style = 'green'
    return render(request, 'index.html', {'funds': funds, 'result': result, 'res_style': res_style})
