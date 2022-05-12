from django.urls import path
from vwn.views import index, get_cur_month_days
app_name = "vwn"
urlpatterns = [
    path("api/v1/exercises", index, name="index"),
    path("api/v1/exercises/days", get_cur_month_days, name="get_days")]