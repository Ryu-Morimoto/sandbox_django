from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from .models import Diary

from .forms import InquiryForm,DiaryForm
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        return super().form_valid(form)

class CreateView(LoginRequiredMixin, generic.CreateView):
    model = Diary
    form_class = DiaryForm
    template_name = "diary_create.html"

class ListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = "diary_list.html"

class DeleteView(generic.DeleteView):
    model = Diary
    template_name = "diary_delete.html"
    success_url = reverse_lazy('diary:diary_list')


class DetailView(generic.DetailView):
    model = Diary
    form_class = DiaryForm
    template_name = "diary_detail.html"

class UpdateView(generic.UpdateView):
    model = Diary
    form_class = DiaryForm
    template_name = "diary_update.html"