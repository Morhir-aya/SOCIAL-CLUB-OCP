# Generated by Django 4.1 on 2022-09-07 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0012_post_id_user_resrestauration_id_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default='2022-05-16'),
        ),
        migrations.AlterField(
            model_name='resrestauration',
            name='date',
            field=models.DateField(default='2022-05-16'),
        ),
    ]
