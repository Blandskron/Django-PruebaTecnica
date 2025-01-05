from django.shortcuts import render, redirect
from .forms import ContactoForm

def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gracias')  # Redirige a la página de agradecimiento
    else:
        form = ContactoForm()
    return render(request, 'contactame/contacto.html', {'form': form})

def gracias_view(request):
    return render(request, 'contactame/gracias.html')
