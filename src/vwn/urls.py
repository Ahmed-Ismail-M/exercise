from django.urls import path
from vwn.views import index
app_name = "vwn"
urlpatterns = [
    path("", index, name="index")]