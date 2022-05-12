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
        print(request.body, "after printing req" )
        # for k , v in request.POST.items():
        #     print(k, v)
        # xrsyz = Exercise.objects.create(name=request.POST.get('exerciseName'), hours=request.POST.get('hours'),
        # min=request.POST.get('mins'))
        # print(xrsyz)
        return HttpResponse('All good', content_type='application/json')