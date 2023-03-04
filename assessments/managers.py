from django.db import models


class ScoreModelManager(models.Manager):
    def create_score(self,stdnt_user,quiz,score):
        score = self.create(
            stdnt_user=stdnt_user, quiz = quiz, score=score,
        )
        return score
