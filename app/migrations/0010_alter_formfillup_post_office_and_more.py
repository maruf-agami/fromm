# Generated by Django 4.1.3 on 2022-11-07 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_formfillup_religion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formfillup',
            name='post_office',
            field=models.CharField(default='', max_length=200, verbose_name='Post_office'),
        ),
        migrations.AlterField(
            model_name='formfillup',
            name='upazila',
            field=models.CharField(default='', max_length=200, verbose_name='upazila'),
        ),
        migrations.AlterField(
            model_name='formfillup',
            name='village',
            field=models.CharField(default='', max_length=200, verbose_name='village'),
        ),
    ]
