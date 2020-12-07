from django.shortcuts import render
from home.models import Csv, User
from .forms import CsvForm
from . import forms
import csv

def upload_file_view(request):
	form = CsvForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save(request)
		return render(request, 'users/profile.html', {'form': form, 'title': 'Profile'})
		
	return render(request, 'csvs/upload.html', {'form': form, 'title': 'Upload'})