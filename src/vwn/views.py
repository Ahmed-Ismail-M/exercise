from datetime import datetime
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.query import QuerySet
from vwn.models import Exercise
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == "POST":
        body_unicode = request.body.decode("utf-8")
        body_data = json.loads(body_unicode)
        try:
            # assign post data in variables
            name = body_data.get("exerciseName")
            hours = int(body_data.get("hours"))
            min = int(body_data.get("mins"))
            try:
                # check if exercise already exists
                xrsyz = Exercise.objects.get(name=name)
            except Exercise.DoesNotExist:
                xrsyz = None
            if xrsyz:
                # if exists , update the hours and mins
                xrsyz.hours = xrsyz.hours + hours
                xrsyz.min = xrsyz.min + min
                xrsyz.save()
            else:
                # if not exists, create new entry
                xrsyz = Exercise.objects.create(name=name, hours=hours, min=min)
                xrsyz.save()
            return HttpResponse(xrsyz, content_type="application/json")
        except Exception as e:
            return HttpResponse(
                f"ERROR: {e.__str__()}", content_type="application/json"
            )
    return HttpResponse(
        "Please provide user_id(int), exerciseName(string),hours(tinyint),mins(tinyint))",
        content_type="application/json",
    )


def get_days(request):
    currentMonth = datetime.now().month
    exercises = Exercise.objects.all().filter(created_at__month__gte=currentMonth,) # filter days within the current month
    days = calculate_days(exercises=exercises) #calculate days
    return HttpResponse(
        json.dumps({'total days': days}),
        content_type="application/json",
    )


def calculate_days(exercises: QuerySet)-> float:
    hrs = 0
    mins = 0
    for xrsyz in exercises:
        hrs += xrsyz.hours
        mins += xrsyz.min
    hrs += mins/60
    return hrs/24
