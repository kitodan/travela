from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView
from journey.models import Trip
from message.forms import MessageForm
from .models import Message


class CreateMessageView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['content']

    def post(self, request, receiver, product_created=None, *args, **kwargs):
        if request.method == 'POST':
            form = MessageForm(request.POST, request.FILES)
            send_by = self.request.user
            send_to = (Trip.objects.filter(id=receiver).latest('date_posted')).posted_by
            if form.is_valid():
                form.instance.send_by =send_by
                form.instance.send_to =send_to
                form.save()
                return render(request, 'journey/home.html', {'form': form})

            else:
                form = MessageForm()
            return render(request, 'journey/about.html', {
                'form': form
            })





