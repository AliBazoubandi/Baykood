from django.urls import path
from . import views
# temporary — only for testing error pages locally, remove after
from django.views.generic import TemplateView
app_name = 'core'

urlpatterns = [
    path('',         views.home,    name='home'),
    path('about/',   views.about,   name='about'),
    path('contact/', views.contact, name='contact'),
    # temporary — only for testing error pages locally, remove after
    path('test-404/', TemplateView.as_view(template_name='404.html')),
    path('test-500/', TemplateView.as_view(template_name='500.html')),
]