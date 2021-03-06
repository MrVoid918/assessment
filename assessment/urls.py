"""assessment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from claims import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('claims-admin/', admin.site.urls, name="admin"),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('claims', views.claim_view, name="claims_view"),
    path('claims/view/<str:id>', views.indv_claim_view, name="indv_claims_view"),
    path('claims/edit/<str:id>', views.indv_claim_edit, name="indv_claims_edit"),
    path('claims/delete/<str:id>', views.indv_claim_delete,
         name="indv_claims_delete"),
    path('claims/submit', views.claim_form_view, name="Claims"),
    path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/', include("accounts.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
