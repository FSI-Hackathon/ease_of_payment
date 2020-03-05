from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect


class Home(View):
	def get(self, request):
		context = {}
		return render(request,'accounts/base.html',context)