# Generated by Django 2.0.4 on 2018-06-07 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tnt', '0020_changelog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='floor',
            old_name='display_text',
            new_name='name_text',
        ),
        migrations.AddField(
            model_name='floor',
            name='info_text',
            field=models.CharField(default='', max_length=200),
        ),
    ]