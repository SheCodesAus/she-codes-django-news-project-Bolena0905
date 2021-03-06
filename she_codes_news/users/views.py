from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic

from news.models import NewsStory
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm



class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class ProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'users/userpage.html'
    context_object_name = 'author'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_stories'] = NewsStory.objects.filter(author=self.request.user.id).order_by('-pub_date')
        return context
    def get_object(self):
        return self.request.user


class AuthorView(generic.DetailView):
    model = CustomUser
    template_name = 'users/userpage.html'
    context_object_name = 'author'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_stories'] = NewsStory.objects.filter(author=self.kwargs['pk']).order_by('-pub_date')
        return context
