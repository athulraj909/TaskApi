# Generated by Django 5.0.6 on 2024-07-05 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_personal',
            name='Enquiry_no',
            field=models.IntegerField(auto_created=True, blank=True),
        ),
    ]