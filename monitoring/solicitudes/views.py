from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import VariableForm
from .logic.solicitud_logic import get_solicitudes, create_solicitud

def solicitud_list(request):
   solicitudes = get_solicitudes()
   context = {
       'solicitud_list': solicitudes
   }
   return render(request, 'solicitudes/solicitud.html', context)


def solicitud_create(request):
    if request.method == 'POST':
         form = VariableForm(request.POST)
         if form.is_valid():
              create_solicitud(form)
              messages.add_massege(request, messages.SUCCESS, 'Solicitud creada')
              return HttpResponseRedirect(reverse('solicitudCreate'))
         else:
            print(form.errors)
    else:
        form = VariableForm()

    context = {
        'form': form
    }
    return render(request, 'solicitudes/solicitudCreate.html', context)
