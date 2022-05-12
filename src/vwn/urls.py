from django.urls import path
from vwn.views import index, get_cur_month_days
app_name = "vwn"
urlpatterns = [
    path("", index, name="index"),
    path("exercises", get_cur_month_days, name="get_days")]