# Generated by Django 5.0.4 on 2024-05-29 08:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course_image_alter_category_unique_together_outline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outline',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='outlines', to='course.category'),
        ),
    ]
