# Generated by Django 4.2.4 on 2024-04-08 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_alter_client_commentary_alter_client_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Наименование'),
        ),
    ]
