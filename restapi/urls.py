from django.urls import path

from . import views

urlpatterns = [
    path('api/mail/', views.MailConfView.as_view()),
    path('api/mail/<int:id>/', views.MailConfView.as_view()),
    path('mail/send/<int:id>/', views.SendMailView.as_view()),
]