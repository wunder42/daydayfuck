from django import forms
from pagedown.widgets import PagedownWidget

class TForm(forms.Form):
	title = forms.CharField(widget=PagedownWidget())