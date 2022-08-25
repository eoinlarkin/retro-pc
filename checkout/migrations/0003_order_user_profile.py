# Generated by Django 4.0.6 on 2022-08-25 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0001_initial'),
        ('checkout', '0002_alter_order_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='user_account.userprofile'),
        ),
    ]
