# encoding:utf-8
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
import os

NOW_PHASE = 1
# Create your models here.
# 新闻，教程，开班信息
class DyNews(models.Model):
	title = models.CharField(max_length=100, verbose_name="新闻标题")
	author = models.ForeignKey(User, verbose_name="发布人", default="dianyi")
	publication_date = models.DateTimeField(verbose_name="发表日期/时间")
	hot_dot = models.IntegerField(verbose_name="新闻热度[请保持默认值]",default=0)
	top = models.BooleanField(verbose_name="是否置顶[请保持默认值]", default=False)
	tag = models.ManyToManyField('Tag', verbose_name="标签", blank=True)
	content = tinymce_models.HTMLField(blank=True, max_length=2000, verbose_name="新闻内容")
	class Meta:
		verbose_name = u"新闻"
		verbose_name_plural = u'点艺新闻列表'
	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-id']

# 课程类别列表
class DyCourse(models.Model):
	name = models.CharField(max_length=100, verbose_name="课程类别", unique=True)
	def __unicode__(self):
		return self.name

# 课程开班
class DyCourseClass(models.Model):
	title = models.CharField(max_length=100, verbose_name="班级", unique=True)
	name = models.ForeignKey(DyCourse, verbose_name="选择课程类别")
	content = tinymce_models.HTMLField(null=True, max_length=3000, verbose_name="课程班级介绍、设置")
	def __unicode__(self):
		return self.title

# 最新教程列表
class DyCourseNews(models.Model):
	title = models.CharField(max_length=100, verbose_name="教程标题")
	author = models.ForeignKey(User, verbose_name="发布人", default="dianyi")
	course_category = models.ForeignKey(DyCourse, verbose_name="教程类别")
	publication_date = models.DateTimeField(verbose_name="发表日期/时间")
	hot_dot = models.IntegerField(verbose_name="教程热度[请保持默认值]",default=0)
	top = models.BooleanField(verbose_name="是否置顶[请保持默认值]", default=False)
	tag = models.ManyToManyField('Tag', verbose_name="标签", blank=True)
	image = models.ImageField(upload_to='static/images/courses', max_length=150, null=True, verbose_name="图片")
	content = tinymce_models.HTMLField(blank=True, max_length=2000, verbose_name="详细信息")
	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-id']

# 开班信息
class DyClass(models.Model):
	title = models.CharField(max_length=100, verbose_name="开班信息")
	class_date = models.DateField(verbose_name="开班时间")
	publication_date = models.DateField(verbose_name="发表日期/时间")
	content = tinymce_models.HTMLField(blank=True, max_length=2000, verbose_name="详细信息")
	def __unicode__(self):
		return self.title

# 学生信息
class DyStu(models.Model):
	name = models.CharField(max_length=30, verbose_name="姓名")
	sex = models.CharField(max_length=1, choices=(('M', '男'), ('F', '女')), default='男', verbose_name="性别")
	college = models.ForeignKey('College', verbose_name="学校")
	phase = models.IntegerField(default=NOW_PHASE, verbose_name="第几期学员")
	course_class = models.ManyToManyField(DyCourseClass, verbose_name="选择课程")
	phone_num = models.CharField(max_length=50, verbose_name="电话号码")
	qq_num = models.CharField(max_length=50, verbose_name="QQ号码")
	publication_date = models.DateField(verbose_name="添加日期")

	def __unicode__(self):
		return self.name

# 就业信息
class DyJobInfo(models.Model):
	company = models.CharField(max_length=30, verbose_name="公司名称")
	publication_date = models.DateField(verbose_name="添加日期")
	name = models.ForeignKey(DyStu, verbose_name="姓名")

	def __unicode__(self):
		return self.company

	class Meta:
		ordering = ['-id']

# 广而告知
class DyAdInfo(models.Model):
	title = models.CharField(max_length=100, verbose_name="标题")
	sub_title = models.CharField(max_length=100, blank=True, verbose_name="子标题")
	publication_date = models.DateField(verbose_name="添加日期")
	image = models.ImageField(upload_to='static/images/navs', max_length=150, verbose_name="图片")
	content = tinymce_models.HTMLField(blank=True, max_length=2000, verbose_name="文章详情")
	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-id']

# 作品信息
class DyStuOpusInfo(models.Model):
	author = models.ForeignKey('DyStu', verbose_name="作品作者")
	course_category = models.ForeignKey(DyCourseClass, verbose_name="课程类别")
	title = models.CharField(max_length=30, verbose_name="作品标题")
	sub_title = models.CharField(max_length=100, blank=True, verbose_name="作品子标题")
	content = models.CharField(max_length=100, null=True, verbose_name="作品内容")
	publication_date = models.DateTimeField(verbose_name="添加日期")
	hot_dot = models.IntegerField(verbose_name="教程热度[请保持默认值]",default=0)
	top = models.BooleanField(verbose_name="是否置顶[请保持默认值]", default=False)
	tag = models.ManyToManyField('Tag', verbose_name="标签", blank=True)
	image = models.ImageField(upload_to='static/images/opus', max_length=150, verbose_name="图片位置")	

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-id']

class Tag(models.Model):
	name = models.CharField(max_length=100, unique=True, verbose_name="标签名称")

	def __unicode__(self):
		return self.name

class College(models.Model):
	name = models.CharField(max_length=100, unique=True, verbose_name="学校名称")
	def __unicode__(self):
		return self.name

class Tiny(models.Model):
	body = tinymce_models.HTMLField(verbose_name="正文输入")

class Liuyan(models.Model):
	course_id = models.ForeignKey(DyCourseNews, verbose_name="课程ID")
	liuyan_id = models.IntegerField(null=True, verbose_name="回复留言")
	author = models.CharField(max_length=30, verbose_name="作者")
	mail = models.EmailField(verbose_name="邮箱")
	content = models.TextField(max_length=240, verbose_name="评论内容")
	display = models.BooleanField(default=True, verbose_name="是否显示")
	publication_date = models.DateTimeField(blank=True, verbose_name="评论日期")

	class Meta:
		ordering = ['id']
		verbose_name = u"留言"
		verbose_name_plural = u'留言列表'

	def __unicode__(self):
		return self.author

admin.site.register([Tiny, DyCourseNews,DyStu, DyNews, DyCourse, DyClass, DyAdInfo, DyJobInfo, DyStuOpusInfo, Tag, DyCourseClass, College, Liuyan])

# admin.site.register(DyCourse)

