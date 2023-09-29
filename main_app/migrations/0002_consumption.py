# Generated by Django 4.2.5 on 2023-09-29 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.CharField(choices=[('AM', 'Before Noon'), ('PM', 'After Noon')], default='AM', max_length=2)),
                ('soda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.soda')),
            ],
        ),
    ]
