# Generated by Django 2.1 on 2022-06-11 21:55

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
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('phoneId', models.AutoField(primary_key=True, serialize=False)),
                ('phoneName', models.CharField(max_length=255)),
                ('phonePrice', models.FloatField()),
                ('phoneDescription', models.TextField()),
                ('image_url', models.CharField(max_length=2083)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
            ],
        ),
        migrations.AddField(
            model_name='cartitem',
            name='phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Phone'),
        ),
        migrations.AddField(
            model_name='cart',
            name='itemlist',
            field=models.ManyToManyField(to='products.CartItem'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
