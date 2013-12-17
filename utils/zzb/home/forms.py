from django import forms
from django_markdown.widgets import MarkdownWidget

class GititemForm(forms.Form):
	title = forms.CharField(label='title')
	subtitle = forms.CharField(label='subtitle')
	content = forms.CharField(widget=MarkdownWidget())
	giturl = forms.URLField(label='giturl')



