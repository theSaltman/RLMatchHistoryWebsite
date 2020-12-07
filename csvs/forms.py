from django import forms
from home import models
from home.models import Csv


#class CsvModelForm(forms.Form):
#	class Meta:
#		model = Csv
#		fields = ('file_name',)
		
class CsvForm(forms.Form):
	csv = forms.FileField(
		label='CSV File',
		required=True	
	)
	
	def save(self, request):
		csv_instance = models.Csv()
		csv_instance.author=request.user
		csv_instance.file_name=self.cleaned_data["csv"]
#		csv_instance.csv=self.cleaned_data["csv"]
#		csv_instance.file_name=self.csv
		csv_instance.save()
		return csv_instance