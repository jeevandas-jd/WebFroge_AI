
from django.contrib import admin
from django.urls import path

from  .views import getGemini

urlpatterns=[
	path("getGemini/",getGemini,name="getGemini")
	]
