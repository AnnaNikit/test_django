# Generated by Django 2.0.3 on 2018-04-02 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('grade', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]
