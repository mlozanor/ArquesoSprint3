from django.http import JsonResponse
from django.shortcuts import render

from solicitudes.logic.solicitud_logic import getSolicitudById
from .logic.logic_alarm import getAlarms, createAlarm, get_documentos_by_solicitud

def alarm_list(request):
    alarms = getAlarms()
    context = list(alarms.values())
    return JsonResponse(context, safe=False)

def generate_alarm(request, solicitud_id):
    solicitud = getSolicitudById(solicitud_id)
    documentos = get_documentos_by_solicitud(solicitud_id)
    createAlarm = False
    upperDocumento = None
    for documento in documentos:
        if documento.value >= 30:
            createAlarm = True
            upperDocumento = documento

    if createAlarm:
        alarm = createAlarm(solicitud, upperDocumento, 30)
        return JsonResponse(alarm.toJson(), safe=False)
    else:
        return JsonResponse({'message': 'No alarm created'}, status=200)
            