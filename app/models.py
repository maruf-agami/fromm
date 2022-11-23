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
    # -----------------------------------------------

    student_id = models.CharField(max_length=200, verbose_name='student_id',)

    semester = models.CharField(max_length=50, verbose_name='semester', default='')

    session = models.CharField(max_length=50, verbose_name='session',)

    hall = models.CharField(max_length=200, verbose_name='hall', default='')

    department = models.CharField(max_length=200, verbose_name='department', default='')

    exam_year = models.CharField(max_length=50, verbose_name='exam_year', default='')

    exam_starting_date = models.DateField(verbose_name='exam_starting_date', default=None, blank=True, null=True)

    # ----------COURSE CODES-------
    code1 = models.CharField(max_length=50, verbose_name='code1', default='')
    code2 = models.CharField(max_length=50, verbose_name='code2', default='')
    code3 = models.CharField(max_length=50, verbose_name='code3', default='')
    code4 = models.CharField(max_length=50, verbose_name='code4', default='')
    code5 = models.CharField(max_length=50, verbose_name='code5', default='')
    code6 = models.CharField(max_length=50, verbose_name='code6', default='')
    code7 = models.CharField(max_length=50, verbose_name='code7', default='')
    code8 = models.CharField(max_length=50, verbose_name='code8', default='')
    code9 = models.CharField(max_length=50, verbose_name='code9', default='')

    last_semester = models.CharField(max_length=50, verbose_name='last_semester', default='')

    passing_year = models.CharField(max_length=50, verbose_name='passing_year', default='')

    result = models.CharField(max_length=50, verbose_name='result', default='')

    name = models.CharField(max_length=200, verbose_name='Name', )

    father = models.CharField(max_length=200, verbose_name='father', default='',)

    mother = models.CharField(max_length=200, verbose_name='mother', default='')

    guardian = models.CharField(max_length=200, verbose_name='guardian', default='')

    phone = models.CharField(max_length=50, verbose_name='phone', default=' ')

    birth_date = models.DateField(verbose_name='birth_date', default=None, blank=True, null=True)

    nationality = models.CharField(max_length=200, verbose_name='nationality', default='')

    religion = models.CharField(max_length=200, verbose_name='religion', default='')

    village = models.CharField(max_length=200, verbose_name='village', default='')

    post_office = models.CharField(max_length=200, verbose_name='Post_office', default='',)

    upazila = models.CharField(max_length=200, verbose_name='upazila', default='')

    district = models.CharField(max_length=200, verbose_name='district', default='')

    # TODO: ekhan theke aro add kor field ja ja lagbe..
