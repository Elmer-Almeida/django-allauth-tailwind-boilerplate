from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('allauth.urls')),

    path('', views.Landing.as_view(), name='landing'),
    path('about/', views.About.as_view(), name='about'),

    path('contact/', include('contact.urls', namespace='contact')),
]
