from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = "index" ),
    path('about-us/', views.about, name = "about"),
    path('news/', views.NewsListView.as_view(), name = "news_list"),
    path('news/<int:pk>/', views.NewsDetails.as_view(), name = "news_deatils"),
    path('announcements/', views.AnnouncementListView.as_view(), name = "announcements_list"),
    path('announcements/<int:pk>/', views.AnnouncementDetails.as_view(), name = "announcement_details"),
    path('coment/<int:pk>/', views.AddComment.as_view(), name = 'add_comment'),
    path('complaint/', views.complaint, name = "complaint"),
    path('add_complaint/', views.AddComplaint.as_view(), name = 'add_complaint')
]
