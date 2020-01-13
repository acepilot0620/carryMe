from django.db import models
from login.models import Account

# Create your models here.



class Question(models.Model):
    title = models.TextField(max_length="50")
    content = models.TextField(max_length="500")
    username = models.TextField(null = True)

    # coment = models.OneToManyField('Answer') 이게 나을까 혹은 views에서 함수를 적용 시키는게 나을까?
    created_at = models.DateTimeField( auto_now_add = True )

    updated_at = models.DateTimeField( auto_now = True)

    # 엔서 객채를 받아서 여기의 엔서를 받아야 함......................

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE)

    #다대 일 관계 = foreignkey 이다아아아아
    username = models.TextField(null = True)
    content = models.TextField(null = True)