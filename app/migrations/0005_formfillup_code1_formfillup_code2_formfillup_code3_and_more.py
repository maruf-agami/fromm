# Generated by Django 4.1.3 on 2022-11-07 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_formfillup_exam_starting_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='formfillup',
            name='code1',
            field=models.CharField(default='', max_length=50, verbose_name='code1'),
        ),
        migrations.AddField(
            model_name='formfillup',
            name='code2',
            field=models.CharField(default='', max_length=50, verbose_name='code2'),
        ),
        migrations.AddField(
            model_name='formfillup',
            name='code3',
            field=models.CharField(default='', max_length=50, verbose_name='code3'),
        ),
        migrations.AddField(
            model_name='formfillup',
            name='code4',
            field=models.CharField(default='', max_length=50, verbose_name='code4'),
        ),
        migrations.AddField(
            model_name='formfillup',
            name='code5',
            field=models.CharField(default='', max_length=50, verbose_name='code5'),
        ),
        migrations.AddField(
            model_name='formfillup',
            name='code6',
            field=models.CharField(default='', max_length=50, verbose_name='code6'),
        ),
        migrations.AddField(
            model_name='formfillup',
            name='code7',
            field=models.CharField(default='', max_length=50, verbose_name='code7'),
        ),
        migrations.AddField(
            model_name='formfillup',
            name='code8',
            field=models.CharField(default='', max_length=50, verbose_name='code8'),
        ),
        migrations.AddField(
            model_name='formfillup',
            name='code9',
            field=models.CharField(default='', max_length=50, verbose_name='code9'),
        ),
        migrations.AlterField(
            model_name='formfillup',
            name='exam_starting_date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='exam_starting_date'),
        ),
    ]
