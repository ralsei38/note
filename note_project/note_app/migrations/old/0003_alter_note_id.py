# Generated by Django 3.2.7 on 2021-10-24 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note_app', '0002_rename_text_note_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
