# Generated by Django 3.2.4 on 2021-06-02 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название формата')),
                ('code', models.CharField(max_length=100, verbose_name='Код фаормата')),
                ('desc', models.CharField(blank=True, max_length=1000, verbose_name='Описание формата')),
            ],
        ),
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('columns', models.CharField(max_length=30, verbose_name='Столбцы')),
                ('file', models.FileField(upload_to='sheets')),
                ('sheet_format', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sheets', to='sheetCheck.format', verbose_name='Формат ведомости')),
            ],
        ),
    ]
