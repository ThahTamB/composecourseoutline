# Generated by Django 5.0.4 on 2024-06-02 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0015_rename_score_point_percent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outline',
            name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='outlines',
            field=models.ManyToManyField(blank=True, null=True, to='course.outline'),
        ),
    ]
