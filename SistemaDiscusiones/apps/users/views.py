from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import View

from .forms import ExtraDataForm

class ExtraDataView(View):

	def get(self, request, *args, **kwargs):
		if request.user.status:
			return redirect('/')
		else:
			return render(request, 'users/extra_data.html')

	def post(self, request, *args, **kwargs):
		form = ExtraDataForm(request.POST)
		if form.is_valid():
			request.user.username = request.POST['username']
			request.user.email = request.POST['email']
			request.user.status = True
			request.user.save()
			return redirect('/')
		else:
			error_username = form['username'].errors.as_text()
			error_email = form['email'].errors.as_text()
			ctx = {'error_username':error_username, 'error_email':error_email}
			return render(request, 'users/extra_data.html', ctx)

def LogOut(request):
	logout(request)
	return redirect('/')
