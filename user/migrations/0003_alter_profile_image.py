# Generated by Django 5.2 on 2025-05-05 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_profile_staff_profile_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='avatar.jpg', upload_to='Profile_Images'),
        ),
    ]
