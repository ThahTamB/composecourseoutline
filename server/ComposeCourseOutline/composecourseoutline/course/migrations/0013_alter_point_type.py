# Generated by Django 5.0.4 on 2024-06-01 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_point_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='type',
            field=models.CharField(default='Enter the grade type here', max_length=100),
        ),
    ]
