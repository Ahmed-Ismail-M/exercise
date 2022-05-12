from django.urls import path
from vwn.views import index, get_days
app_name = "vwn"
urlpatterns = [
    path("", index, name="index"),
    path("exercises", get_days, name="get_days")]