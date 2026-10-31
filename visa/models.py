from django.db import models
from django.contrib.auth.models import User

class Signup(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20,null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10,null=True)
    dob = models.DateField()
    address = models.CharField(max_length=50,null=True)
    def _str_(self):
        return self.user.username

class VisaRequest(models.Model):
    first_name=models.CharField(max_length=40,null=True)
    last_name=models.CharField(max_length=40,null=True)
    email=models.CharField(max_length=40,null=True)
    mobile=models.CharField(max_length=40,null=True)
    parcel_type=models.CharField(max_length=40,null=True)
    request_date=models.CharField(max_length=50,null=True)
    gov_id=models.CharField(max_length=40,null=True)
    gov_no=models.CharField(max_length=40,null=True)
    weight=models.CharField(max_length=40,null=True)
    country=models.CharField(max_length=40,null=True)
    address=models.CharField(max_length=200,null=True)
    status=models.CharField(max_length=40,null=True)
    parcel_id=models.IntegerField(max_length=50,null=True)


class Feedback(models.Model):
    feedback_name = models.CharField(max_length=20,null=True)
    feedback_contact = models.CharField(max_length=30, null=True)
    feedback_email = models.CharField(max_length=10,null=True)
    feedback_comment = models.CharField(max_length=15,null=True)

