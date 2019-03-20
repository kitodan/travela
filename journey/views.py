from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView, CreateView, UpdateView,DeleteView
from . models import Trip
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin





def home(request):
    context = {
        'journies': Journey.objects.all()
    }
    return render(request, 'journey/home.html',context)

class TripListView(ListView):
    model = Trip
    template_name = 'journey/home.html'
    context_object_name = 'journies'
    ordering = ['-date_posted']
    paginate_by = 3

class AllTripsListView(LoginRequiredMixin,ListView):
    model = Trip
    template_name = 'journey/alltrips.html'
    context_object_name = 'journies'
    ordering = ['-date_posted']
    paginate_by = 6
 
class TripDetailView(LoginRequiredMixin,DetailView):
    model = Trip 

class TripCreateView(LoginRequiredMixin,CreateView):
    model = Trip
    fields = ['depature', 'destination','date_travel', 'time_travel','seats','amount','ride_detail']
    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)
    
class TripUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Trip
    fields = ['depature', 'destination', 'time_travel','amount','date_travel','ride_detail']
    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)
    def test_func(self):
        Journey = self.get_object()
        if self.request.user == Journey.posted_by:
            return True
        return False

class TripDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Trip 
    success_url = '/'
    def test_func(self):
        Journey = self.get_object()
        if self.request.user == Journey.posted_by:
            return True
        return False


def about(request):
    return render(request, 'journey/about.html')