# Generated by Django 5.0.4 on 2024-06-02 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0021_remove_outline_course_outline_courses_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseOutline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.course')),
                ('outline', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.outline')),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='outlines',
            field=models.ManyToManyField(blank=True, related_name='courses_included', through='course.CourseOutline', to='course.outline'),
        ),
        migrations.AlterField(
            model_name='outline',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='outline_set', through='course.CourseOutline', to='course.course'),
        ),
    ]
