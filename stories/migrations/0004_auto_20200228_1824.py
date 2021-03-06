# Generated by Django 2.2.7 on 2020-02-28 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='adresse',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='country',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.EmailField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='firs_name',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='last_name',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='phone_number',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='school',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='zip_code',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
