# Generated by Django 4.2.1 on 2023-06-04 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_evallect_author'),
        ('accounts', '0007_rename_mylect_lectlist_mylects_alter_lectlist_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='eval',
            field=models.ManyToManyField(to='board.evallect'),
        ),
    ]