from django.shortcuts import render, redirect
from front_end.forms import Especiesform
from front_end.models import Especies
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    filtro = {}
    search = request.GET.get ('search')
    if search:
        filtro ['db'] = Especies.objects.filter (Genero__icontains = search)
    else:
        filtro ['db'] = Especies.objects.all ()
    return render(request, 'index.html', filtro)
    data = {}
    #data = {'db': Especies.objects.all()}
    all = Especies.objects.all ()
    paginator = Paginator (all,2)
    pages = request.GET.get ('page')
    data ['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)


def form(request):
    data = {'form': Especiesform()}
    return render(request, 'form.html', data)


def create(request):
    form = Especiesform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {'db': Especies.objects.get(pk=pk)}
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data ['db'] = Especies.objects.get(pk=pk)
    data['form'] = Especiesform(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Especies.objects.get(pk=pk)
    form = Especiesform(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete (request, pk):
    db = Especies.objects.get (pk=pk)
    db.delete ()
    return redirect ('home')

