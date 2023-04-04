from datatime import datetime
from django.shortcuts import render

# data_em_texto = data_atual.strftime('%d/%m/%Y')
# print(data_em_texto) 

def feriado():
    data_atual = date.now().date()
    print(data_atual)
    if data_atual.month == 12 and data_atual.day == 25:
        return 'É natal'
    elif data_atual.month == 4 and data_atual.day == 21:
        return 'É tiradentes'
    else:
        return 'Não é nenhum dos feriados'

def natal(request):
    mensagem = {
        'mensagem': feriado() == 'É natal'
    }
    return render(request, 'index.html', mensagem)

def tiradentes(request):
    mensagem = {
        'mensagem': feriado() == 'É tiradentes'
    }
    return render(request, 'index.html', mensagem)
