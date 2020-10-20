import csv

from django.shortcuts import render


def split_inflation_list(inf_list):
    for inf in inf_list:
        return inf[0].split(';')


def inflation_view(request):
    template_name = 'apps/inflation.html'
    inflation_list = []
    # чтение csv-файла и заполнение контекста
    with open('inflation_russia.csv', newline='', encoding='utf-8') as f:
        csv_content = csv.reader(f)
        for row in csv_content:
            inflation_list.append(row)

    context = {
        'title': inflation_list[0],
        'inflation_list': inflation_list[1:],
        'cColor': 'white',
    }

    return render(request, template_name,
                  context)