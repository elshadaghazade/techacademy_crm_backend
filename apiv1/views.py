from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import *
from django.db.models import Q
from datetime import datetime

def get_response(status=200, message="", data={}):
    return {
        "status": status,
        "error_message": message,
        "data": data
    }

def select_leads ():
    leads = Lead.objects.filter(~Q(status=Lead.STATUS_BLOCK))
    leads_dict = {
        "leads": [],
        "calls": [],
        "recalls": [],
        "meetings": []
    }
    for lead in leads.values('id', 'name', 'surname', 'social', 'phone', 'status', 'call_date', 'recall_date', 'meeting_date'): 
        lead_statuses = dict(Lead.status_choices)
        leads_dict[lead_statuses[lead['status']]].append(lead)
        lead['status'] = dict(Lead.status_choices)[lead['status']]
        lead['full_name'] = lead['name'] + ' ' + lead['surname']

    return leads_dict


@require_http_methods(['GET'])
@csrf_exempt
def get_leads(request):
    result = select_leads()

    return JsonResponse(get_response(data=result))


@require_http_methods(['POST'])
@csrf_exempt
def change_status(request):
    lead_id = request.POST.get('lead_id')
    status = request.POST.get('status')

    try:
        lead = Lead.objects.get(pk=lead_id)
    except:
        return JsonResponse(get_response(status=404, message="Lead was not found"))
    else:
        try:
            if status == 'calls':
                lead.status = Lead.STATUS_CALL
            elif status == 'recalls':
                lead.status = Lead.STATUS_RECALL
            elif status == 'meetings':
                lead.status = Lead.STATUS_MEETING
            elif status == 'block':
                lead.status = Lead.STATUS_BLOCK
            lead.save()
        except:
            pass
    result = select_leads()
    return JsonResponse(get_response(data=result))

@require_http_methods(['POST'])
@csrf_exempt
def update_date(request):
    lead_id = request.POST.get('lead_id')
    dt = request.POST.get('dt')

    try:
        lead = Lead.objects.get(pk=lead_id)
    except:
        return JsonResponse(get_response(status=404, message="Lead was not found"))
    else:
        try:
            if lead.status == Lead.STATUS_CALL:
                lead.call_date = dt
            elif lead.status == Lead.STATUS_RECALL:
                lead.recall_date = dt
            elif lead.status == Lead.STATUS_MEETING:
                lead.meeting_date = dt
            lead.save()
        except:
            pass
    result = select_leads()
    return JsonResponse(get_response(data=result))