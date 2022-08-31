from django.contrib import admin
from django.urls import path
from views import *
from settings import development

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{development.BOT_TOKEN}', get_message)
]
