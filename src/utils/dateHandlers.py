from django.db.models.query import QuerySet
def to_days(exercises: QuerySet) -> float:
    hrs = 0
    mins = 0
    for xrsyz in exercises:
        hrs += xrsyz.hours
        mins += xrsyz.min
    hrs += mins / 60
    return hrs / 24

