# Generated by Django 5.1.4 on 2025-01-17 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_note_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
