from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView
from .models import News, Announcement
from django.http import HttpResponseRedirect
from .forms import CommentForm, ComplaintForm
from datetime import date

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
    template_name = "HCS_site/announcement_details.html"



class AddComment(View):

    def post(self, request, pk):
        form = CommentForm(request.POST)
        form.date_of_comment = date.today
        if form.is_valid():
            form = form.save(commit=False)
            form.news_id = pk

            form.save()
        return redirect("/")


def complaint(request):
    return render(request, 'HCS_site/complaint.html')



class AddComplaint(View):

    def post(self, request):
        form = ComplaintForm(request.POST)
        form.date_of_complaint = date.today
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
        return redirect("/")
