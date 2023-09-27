from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )
from django.urls import reverse_lazy
from .models import Jeki

class BlogListView(ListView):
    model = Jeki
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Jeki
    template_name = 'jek_detail.html'

class BlogCreateView(CreateView):
    model = Jeki
    template_name = 'jek_new.html'
    fields = ['title','author','body']

class BlogUpdateView(UpdateView):
    model = Jeki
    template_name = 'jek_edit.html'
    fields = ['title','body']

class BlogDeleteView(DeleteView):
    model = Jeki
    template_name = 'jek_delete.html'
    success_url = reverse_lazy('home')