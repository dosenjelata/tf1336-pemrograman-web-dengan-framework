from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:pk>/vote/', views.vote, name='vote'),
    # path('question/add/', views.QuestionCreate.as_view(), name='question-add'),
    path('question/add/', views.buat_soal, name='question-add'),
]