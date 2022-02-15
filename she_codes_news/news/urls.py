from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('<int:pk>/delete', views.StoryDeleteView.as_view(), name='delete'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    
    

]