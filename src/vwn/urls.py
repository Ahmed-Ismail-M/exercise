from django.urls import path
from vwn.views import index, get_cur_month_days, get_cur_year_highest_month
app_name = "vwn"
urlpatterns = [
    path("api/v1/exercises", index, name="index"),
    path("api/v1/exercises/days/months", get_cur_month_days, name="get_days"),
    path("api/v1/exercises/month/years", get_cur_year_highest_month, name="get_days")]