# Generated by Django 5.1.7 on 2025-03-26 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_location', models.CharField(max_length=30)),
                ('user_age', models.IntegerField()),
                ('user_gender', models.CharField(max_length=10)),
                ('recipient_relationship', models.CharField(max_length=30)),
                ('recipient_age', models.IntegerField()),
                ('recipient_gender', models.CharField(max_length=30)),
                ('recipient_interests', models.CharField(max_length=30)),
                ('special_occasion', models.CharField(max_length=30)),
                ('budget_preference', models.CharField(max_length=30)),
                ('gift_name', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('brand', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('description', models.CharField(max_length=30)),
                ('gift_rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
    ]
