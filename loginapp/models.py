from django.db import models
class User(models.Model):
    user=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    def __str__(self):
    	return self.user +','+ self.password