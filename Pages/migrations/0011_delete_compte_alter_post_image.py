# Generated by Django 4.1 on 2022-08-27 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0010_resrestauration_status_ressport_status_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Compte',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='./img/posts'),
        ),
    ]
