# Generated by Django 4.2.6 on 2023-10-27 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_customfield_historicalcustomfield_customfieldvalue_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='customfieldvalue',
            unique_together={('custom_field', 'object_id')},
        ),
        migrations.RemoveField(
            model_name='customfieldvalue',
            name='content_type',
        ),
    ]
