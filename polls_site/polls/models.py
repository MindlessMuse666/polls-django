from django.db.models import (Model, ForeignKey, CASCADE,
                              CharField, DateTimeField, IntegerField)
from django.utils.timezone import now, timedelta


class Question(Model):
  question_text = CharField(max_length=255)
  publish_datetime = DateTimeField('date published')

  
  def __str__(self):
    return self.question_text
  
  
  def was_published_recently(self):
    return self.publish_datetime >= now() - timedelta(days=1)


class Choice(Model):
  question = ForeignKey(
    Question,
    on_delete=CASCADE
  )
  choice_text = CharField(max_length=255)
  votes = IntegerField(default=0)
  
  
  def __str__(self):
      return self.choice_text