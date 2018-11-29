from django.shortcuts import render
from .models import Transacao
from .form import TranscaoForm
import datetime


def home(request):
    data={}
    data['now'] = datetime.datetime.now()
    data['transacoes'] = ['t1', 't2', 't3']
    #html = "<html><body>Isso é agora %s</body></html>" % now
    return render(request,'contas/home.html', data)

def listagem(request):
    data={}
    data['transacoes'] = Transacao.objects.all
    return render(request,'contas/listagem.html', data)

def nova_transcao(request):
    data={}
    form = TranscaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return listagem(request)
    data['form']=form
    return render(request,'contas/form.html', data)

def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TranscaoForm(request.POST or None, instance=transacao)
    if form.is_valid():
        form.save()
        return listagem(request)
    data['form']=form
    data['transacao']= transacao
    return render(request,'contas/form.html', data)

def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return listagem(request)