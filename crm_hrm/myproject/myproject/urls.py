#myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.views.generic import TemplateView

urlpatterns = [
    path('', RedirectView.as_view(url='/index.html/')),  # Redirect empty path to index.html
    path('index.html/', TemplateView.as_view(template_name='index.html'), name='index'),
    path('admin/', admin.site.urls),
    path('user-management/', include('user_management.urls')),
    path('marketing-user/', include('marketing_user.urls')), 
    path('accounts/profile/', RedirectView.as_view(url='/marketing-user/accounts/profile/')),
]