from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUser

# Create your models here.


class Formfillup(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    step = models.PositiveSmallIntegerField(default=1, blank=True, null=True)
    dept_signature = models.ImageField(
        null=True, blank=True, upload_to='uploads/%Y-%m-%d')
    provost_signature = models.ImageField(
        null=True, blank=True, upload_to='uploads/%Y-%m-%d')
    register_signature = models.ImageField(
        null=True, blank=True, upload_to='uploads/%Y-%m-%d')
    payable_amount = models.IntegerField(blank=True, null=True)

    name = models.CharField(max_length=200, verbose_name='Name', )
    phone = models.CharField(max_length=50, verbose_name='Phone', default=' ')

    father = models.CharField(
        max_length=200, verbose_name='Father/Husband', default='',)

    mother = models.CharField(
        max_length=200, verbose_name='Mother', default='')
    guardian = models.CharField(
        max_length=200, verbose_name='Guardian', default='')
    village = models.CharField(
        max_length=200, verbose_name='Village', default='')
    post_office = models.CharField(
        max_length=200, verbose_name='Post office', default='',)
    upazila = models.CharField(
        max_length=200, verbose_name='Upazila', default='')
    district = models.CharField(
        max_length=200, verbose_name='district', default='')
    birth_date = models.DateField(
        verbose_name='Birth Date', default=None, blank=True, null=True)

    student_id = models.CharField(max_length=200, verbose_name='Student ID',)

    session = models.CharField(max_length=50, verbose_name='session',)

    semester = models.CharField(
        max_length=50, verbose_name='semester', default='')

    hall = models.CharField(max_length=200, verbose_name='hall', default='')

    # TODO: ekhan theke aro add kor field ja ja lagbe..
