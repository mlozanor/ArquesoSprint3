from django.shortcuts import render
from .forms import DocumentoForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_documentos import get_documentos, create_documento


def documento_list(request):
    documentos = get_documentos()
    context = {
        'documento_list': documentos
    }
    return render(request, 'documento/documentos.html', context)

def documento_create(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST)
        if form.is_valid():
            create_documento(form)
            messages.add_message(request, messages.SUCCESS, 'Documento creado exitosamente')
            return HttpResponseRedirect(reverse('documentoCreate'))
        else:
            print(form.errors)
    else:
        form = DocumentoForm()

    context = {
        'form': form
    }

    return render(request, 'documento/documentoCreate.html', context)