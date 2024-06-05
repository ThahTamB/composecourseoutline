# Generated by Django 5.0.4 on 2024-05-28 16:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_major_category_major'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default=None, upload_to='outline/%Y/%m'),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('name', 'major')},
        ),
        migrations.CreateModel(
            name='Outline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=None, upload_to='outline/%Y/%m')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('content', models.TextField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.category')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.course')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
