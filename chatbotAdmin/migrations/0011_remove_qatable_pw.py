# Generated by Django 4.1 on 2023-12-07 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbotAdmin', '0010_qatable_pw'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qatable',
            name='pw',
        ),
    ]
