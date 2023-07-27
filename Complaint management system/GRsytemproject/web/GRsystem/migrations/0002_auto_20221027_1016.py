# Generated by Django 3.2.2 on 2022-10-27 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRsystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Branch',
            field=models.CharField(choices=[('ComputerScience', 'ComputerScience'), ('InformationScience', 'InformationScience'), ('Electronics and Communication', 'Electronics and Communication')], default='ComputerScience', max_length=29),
        ),
        migrations.AlterField(
            model_name='profile',
            name='collegename',
            field=models.CharField(choices=[('K.C College of Engineering', 'K.C College of Engineering'), ('K.B College', 'K.B College')], max_length=29),
        ),
    ]
