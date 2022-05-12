import json
from django.shortcuts import render
from django.http import HttpResponse

from vwn.models import Exercise
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_http_methods
# # Create your views here.
# @csrf_exempt 
# @require_http_methods(["POST"])
def index(request):
    if request.method == 'GET':
        return HttpResponse('Please provide exerciseName(string),hours(tinyint),mins(tinyint))', content_type='application/json')
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        print(body_data.get('hours'), "after printing req" )
        xrsyz = Exercise.objects.create(name=body_data.get('exerciseName'), hours=body_data.get('hours'),
        min=body_data.get('mins'))
        print(xrsyz)
        return HttpResponse('All good', content_type='application/json')