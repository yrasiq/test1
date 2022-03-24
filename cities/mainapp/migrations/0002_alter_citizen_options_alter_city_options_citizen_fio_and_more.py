# Generated by Django 4.0.3 on 2022-03-24 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='citizen',
            options={'verbose_name': 'гражданин', 'verbose_name_plural': 'граждане'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'город', 'verbose_name_plural': 'города'},
        ),
        migrations.AddField(
            model_name='citizen',
            name='fio',
            field=models.CharField(default='', max_length=50, verbose_name='ФИО'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='city',
            name='name',
            field=models.CharField(default='', max_length=50, verbose_name='название'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='citizen',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.city', verbose_name='город'),
        ),
    ]
