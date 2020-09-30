from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('list/', views.ListView.as_view(), name="diary_list"),
    path('create/', views.CreateView.as_view(), name="diary_create"),
    path('delete/<int:pk>', views.DeleteView.as_view(), name="diary_delete"),
    path('detail/<int:pk>', views.DetailView.as_view(), name="diary_detail"),
    path('update/<int:pk>', views.UpdateView.as_view(), name="diary_update"),
]