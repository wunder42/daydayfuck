from motorengine.document import Document
from motorengine import StringField

class Todo(Document):
	''''''
	content = StringField(required=True)

	def __unicode__(self):
		return self.content