from django.urls import path
from . import views

pages_patterns = ([
    path('', views.PagesListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', views.PageDetailView.as_view(), name='page'),
    path('created/', views.PageCreateView.as_view(), name='created')
], 'pages')