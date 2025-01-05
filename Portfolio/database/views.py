from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Producto
from .forms import ProductoForm

@login_required
def producto_list(request):
    productos = Producto.objects.filter(creado_por=request.user)
    return render(request, 'database/producto_list.html', {'productos': productos})

@login_required
def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.creado_por = request.user
            producto.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'database/producto_form.html', {'form': form})

@login_required
def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk, creado_por=request.user)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'database/producto_form.html', {'form': form})

@login_required
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk, creado_por=request.user)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')
    return render(request, 'database/producto_confirm_delete.html', {'producto': producto})
