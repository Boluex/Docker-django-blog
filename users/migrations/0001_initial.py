# Generated by Django 4.2 on 2023-12-15 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='images')),
                ('location', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('about', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('business_info', models.CharField(blank=True, default='', max_length=2000, null=True)),
                ('business_link', models.URLField(blank=True, default='', null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
