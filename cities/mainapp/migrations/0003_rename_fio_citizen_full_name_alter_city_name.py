# Generated by Django 4.0.3 on 2022-03-24 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_citizen_options_alter_city_options_citizen_fio_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='citizen',
            old_name='fio',
            new_name='full_name',
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='название'),
        ),
    ]