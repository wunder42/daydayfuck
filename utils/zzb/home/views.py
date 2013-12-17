from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, FormView

from .forms import GititemForm


def index(request):
    return HttpResponse("successful")


class TagList(ListView):

    model = ''
    template_name = ''


class GitItem(DetailView):

    # model = ''
    # template_name = ''
    context_object_name = 'gititem'

    def get_context_data(self, **kwargs):
    	context = super(GitItem, self).get_context_data(**kwargs)
    	context['text'] = 'kiss me'
    	return context

class GititemUpload(FormView):
    template_name = 'gititemupload.html'
    form_class = GititemForm

    def form_valid(self, form):
        return super(GititemUpload, self).form_valid(form)


class T(View):

	def get(self, request):
		return HttpResponse('hello')
