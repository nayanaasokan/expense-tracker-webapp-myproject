# Generated by Django 5.0.1 on 2024-02-19 07:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('expenses', 'expenses'), ('income', 'income')], default='expenses', max_length=200)),
                ('category', models.CharField(choices=[('food', 'food'), ('fuel', 'fuel'), ('entertainment', 'entertainment'), ('emi', 'emi'), ('bills', 'bills'), ('rent', 'rent'), ('miscellaneous', 'miscellaneous')], default='miscellaneous', max_length=200)),
                ('amount', models.PositiveIntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
