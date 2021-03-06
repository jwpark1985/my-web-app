# Generated by Django 2.2.12 on 2020-05-31 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_source', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='document',
            name='data_source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Source'),
        ),
    ]
