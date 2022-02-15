from multiprocessing import context
from unicodedata import category
from django.forms import ModelChoiceField
from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from django.contrib.auth import mixins
from django.views.generic.edit import DeleteView




class IndexView(generic.ListView):
    template_name = 'news/index.html'
  

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EditStoryView(mixins.LoginRequiredMixin, generic.UpdateView):
    form_class = StoryForm
    model = NewsStory
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'


class StoryDeleteView(DeleteView):
    model = NewsStory
    success_url = reverse_lazy('news:index')



class CategoryView(generic.ListView):
    model= NewsStory
    Template_name = 'news/category.html'
    context_object_name ='stories'

    def get_queryset(self):
        self.category = self.kwargs['category']
        return NewsStory.objects.filter(category=self.category).order_by('pub_date')

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['category'] = self.category
        return context