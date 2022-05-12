from typing import Tuple
from django.db.models.query import QuerySet
def to_days(exercises: QuerySet) -> Tuple:
    hrs = 0
    mins = 0
    for xrsyz in exercises:
        hrs += xrsyz.hours
        mins += xrsyz.min
    hrs += mins / 60
    remained_hrs = hrs % 24
    return int(hrs / 24), remained_hrs