from django.db import models
from qna.models import QnaModel
from user.models import UserModel
from challenge.models import ChallengeModel
# Create your models here.
class MyPageModel(models.Model):
    class Meta:
        db_table="my_page"
    user_key = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    qna_key=models.ManyToManyField(QnaModel,blank=True,related_name='mypage_key')
    challenge_key = models.ManyToManyField(ChallengeModel, blank=True, related_name='mypage_key')

    def __str__(self):
        return str(self.user_key.username)