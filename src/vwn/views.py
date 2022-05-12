import json
from django.shortcuts import render
from django.http import HttpResponse

from vwn.models import Exercise
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == "POST":
        body_unicode = request.body.decode("utf-8")
        body_data = json.loads(body_unicode)
        try:
            name = body_data.get("exerciseName")
            hours = int(body_data.get("hours"))
            min = int(body_data.get("mins"))
            xrsyz = Exercise.objects.get(name=name)
            if xrsyz:
                xrsyz.hours = xrsyz.hours + hours
                xrsyz.min = xrsyz.min + min
                xrsyz.save()
            else:
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
    exercises = Exercise.objects.all()
    print(exercises)
    for xrsyz in exercises:
        print(xrsyz.hours, " printing hours")
    return HttpResponse(
        "todo",
        content_type="application/json",
    )
