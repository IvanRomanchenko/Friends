from django.urls import path, re_path

from . import views


urlpatterns = [
    path("my_profile/", views.my_profile, name="my_profile"),

    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register_user, name="register"),
    path('terms/', views.terms, name="terms"),

    path('favicon.ico', views.favicon, name="favicon"),

    # all roads lead to the my_profile
    re_path(r'^.*\.*', views.other, name='other'),
]
