from datetime import datetime
import json
from django.http import HttpResponse
from utils.dateHandlers import to_days
from vwn.models import Exercise
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
from django.db.models.functions import TruncMonth


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
    days, hrs = to_days(exercises=exercises)  # calculate days
    return HttpResponse(
        json.dumps({"total days": days, "total hrs": hrs}),
        content_type="application/json",
    )


def get_cur_year_highest_month(request):
    today = datetime.now()
    exercises = (
        Exercise.objects.filter(created_at__year=today.year) # filter according this year
        .annotate(month=TruncMonth("created_at")) # extract month from datetime
        .values("month")
        .annotate(total=Count("id")) # get total count
    ).order_by('-total')[0] # order query by total desc
    month =exercises['month'].month
    return HttpResponse(
        json.dumps({"highest_month": month}),
        content_type="application/json",
    )
