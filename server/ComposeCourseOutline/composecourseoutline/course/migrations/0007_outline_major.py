# Generated by Django 5.0.4 on 2024-05-29 09:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_course_major_alter_course_image_alter_outline_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='outline',
            name='major',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.major'),
        ),
    ]
