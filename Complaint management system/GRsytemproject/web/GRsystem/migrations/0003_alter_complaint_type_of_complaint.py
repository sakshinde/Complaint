# Generated by Django 3.2.2 on 2022-10-27 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRsystem', '0002_auto_20221027_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='Type_of_complaint',
            field=models.CharField(choices=[('Academic Grievance', 'Academic Grievance'), ('Infrastructure related Complaint', 'Infrastructure related Complaint'), ('Unfair Treatment', 'Unfair Treatment'), ('Financial Complaint', 'Financial Complaint'), ('Inequality', 'Inequality'), ('Other', 'Other')], max_length=200, null=True),
        ),
    ]
