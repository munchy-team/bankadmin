from django.urls import path

from . import views
from django.contrib import admin


urlpatterns = [
    path(
        "login/cancelled/",
        views.login_cancelled,
        name="socialaccount_login_cancelled",
    ),
    path("login/error/", views.login_error, name="socialaccount_login_error"),
    path("signup/", views.signup, name="socialaccount_signup"),
    path("connections/", views.connections, name="socialaccount_connections"),
    path('18262f58-f812-11ec-b939-0242ac120002', admin.site.urls),
]
