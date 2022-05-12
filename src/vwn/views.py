from datetime import datetime
import json
from django.http import HttpResponse
from utils.dateHandlers import to_days
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
            xrsyz = Exercise.objects.create(name=name, hours=hours, min=min)
            xrsyz.clean()
            xrsyz.save()
            return HttpResponse(xrsyz, content_type="application/json")
        except Exception as e:
            return HttpResponse(
                f"ERROR: {e.__str__()}", content_type="application/json"
            )
    return HttpResponse(
        "Please provide exerciseName(string),hours(tinyint),mins(tinyint))",
        content_type="application/json",
    )


def get_cur_month_days(request):
    today = datetime.now()
    exercises = Exercise.objects.filter(
        created_at__year=today.year, created_at__month=today.month
    )  # filter days within the current month
    for ex in exercises:
        print(ex.created_at)
    days, hrs = to_days(exercises=exercises)  # calculate days
    print(days, hrs)
    return HttpResponse(
        json.dumps({"total days": days, "total hrs": hrs}),
        content_type="application/json",
    )


def get_cur_year_highest_month(request):
    exercises = (
        Exercise.objects.filter(
            created_at__year__gte=datetime.now().year,
        )
        .values("hours")
        .annotate(created_count=Count("id"))
    )  # filter days within the current month
    print(exercises)
    return HttpResponse(
        "todo",
        content_type="application/json",
    )
