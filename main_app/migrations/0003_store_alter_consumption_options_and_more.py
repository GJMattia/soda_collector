# Generated by Django 4.2.5 on 2023-10-02 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_consumption'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='consumption',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='consumption',
            name='date',
            field=models.DateField(verbose_name='Consumption Date'),
        ),
    ]