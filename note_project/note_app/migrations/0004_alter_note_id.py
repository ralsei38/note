# Generated by Django 3.2.7 on 2021-10-24 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note_app', '0003_alter_note_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
