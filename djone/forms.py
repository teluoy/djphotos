from django.forms import ModelForm
from .models import One

class OneForm(ModelForm):
	class Meta:
		model = One
