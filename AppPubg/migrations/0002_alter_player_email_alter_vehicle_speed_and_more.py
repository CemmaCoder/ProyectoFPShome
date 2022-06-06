# Generated by Django 4.0.4 on 2022-06-06 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPubg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='email',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='speed',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='bullets',
            field=models.IntegerField(),
        ),
    ]
