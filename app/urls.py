from django.urls import URLPattern, path
from knox import views as know_views
from . import views

urlpatterns = [
    path('login/',views.login_api),
    path('user/',views.get_user_data),
    path('register/',views.register_api),
    path('logout/', know_views.LogoutView.as_view()),
    path('logoutall' , know_views.LogoutAllView.as_view()),

]