# -*- coding:utf-8 -*-
from django import forms

class SignupForm(forms.Form):
	name = forms.CharField(label="姓名")
	college = forms.CharField(label="学校")
	phone = forms.CharField(label="电话")
	qq = forms.CharField(label="QQ")
	mail = forms.EmailField(label="邮箱")
	course = forms.ChoiceField(label="课程", choices=[(1, '室内A班'), (2, '室内B班'), (3, '室内C班')])

class LiuyanForm(forms.Form):
	name = forms.CharField(label="大名")
	mail = forms.EmailField(label="邮箱")
	content = forms.CharField(label="内容", widget=forms.Textarea, max_length=200)