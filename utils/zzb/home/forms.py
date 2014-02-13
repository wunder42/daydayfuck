from django import forms
from django_markdown.widgets import MarkdownWidget
from pagedown.widgets import AdminPagedownWidget

class GititemForm(forms.Form):
	title = forms.CharField(label='title')
	subtitle = forms.CharField(label='subtitle')
	content = forms.CharField(widget=AdminPagedownWidget())
	giturl = forms.URLField(label='giturl')



