# Generated by Django 4.2.7 on 2024-04-19 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skola', '0004_student_obec_student_psc_student_ulica'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='narodenie',
            field=models.DateField(blank=True, null=True),
        ),
    ]
