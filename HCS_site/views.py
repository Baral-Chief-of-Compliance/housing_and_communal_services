from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView
from .models import News, Announcement

# Create your views here.


def index(request):
    return render(request, 'HCS_site/home.html')


def about(request):
    return render(request, 'HCS_site/about.html')


class NewsListView(ListView):
    model = News
    queryset = News.objects.all()
    template_name = 'HCS_site/news_list.html'


class NewsDetails(DetailView):
    model = News
    template_name = "HCS_site/news_deatils.html"

class AnnouncementListView(ListView):
    model = Announcement
    queryset = Announcement.objects.all()
    template_name = 'HCS_site/announcement_list.html'


class AnnouncementDetails(DetailView):
    model = Announcement
    template_name = "HCs_site/announcement_details.html"


class AddComment(View):
    def post(self, request, pk):
        print(request.POST)
        return redirect("/")
