# Generated by Django 4.2.3 on 2024-10-22 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_subscription_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=18),
        ),
        migrations.AddField(
            model_name='user',
            name='fitness_goal',
            field=models.CharField(blank=True, choices=[('Lose Weight', 'Lose Weight'), ('Build Muscle', 'Build Muscle'), ('Stay Fit', 'Stay Fit')], max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]