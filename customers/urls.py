from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('account',views.show_account,name='account'),
    path('logout',views.sign_out,name='logout')
]
