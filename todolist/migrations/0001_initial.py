# Generated by Django 3.1.6 on 2021-02-03 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.TextField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description_category', models.TextField(null=True, verbose_name='description category')),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_todo', models.TextField(verbose_name='name')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('deadline_date', models.DateTimeField(verbose_name='date of deadline')),
                ('description_todo', models.TextField(null=True, verbose_name='description todo')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='todo', to='todolist.category')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]
