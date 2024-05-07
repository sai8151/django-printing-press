# marketing_user/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', RedirectView.as_view(url='/marketing-user/accounts/login/')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/profile/', views.profile, name='profile'),
    path('client-list/', views.client_list, name='client_list'),
    path('add-client/', views.add_client, name='add_client'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)