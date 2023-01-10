from django.shortcuts import render
import requests



def index(request):

    url = "https://v6.exchangerate-api.com/v6/91697ffd3e1ee0d705b57ffe/latest/USD"
    headers = {
        "apikey": "?"
    }
    response = requests.get(url, headers=headers).json()
    result = response.get('conversion_rates')

    if request.method == 'GET':
        context = {'curs': result}
        return render(request, 'myapp/index.html', context)

    if request.method == "POST":
        amount = float(request.POST.get('amount'))
        form_cur = request.POST.get("form_cur")
        out_cur = request.POST.get("out_cur")

        total = round(((result[out_cur]/result[form_cur])*amount),2)
        context = {
            'curs': result,
            'total': total,
        }
        return render(request, 'myapp/index.html', context)
