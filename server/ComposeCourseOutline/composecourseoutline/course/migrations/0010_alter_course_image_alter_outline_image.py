# Generated by Django 5.0.4 on 2024-05-31 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_remove_course_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default=None, upload_to='course/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='outline',
            name='image',
            field=models.ImageField(default=None, upload_to='course/%Y/%m'),
        ),
    ]
