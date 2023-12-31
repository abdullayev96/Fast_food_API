# Generated by Django 3.2.7 on 2023-12-03 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Kategoriya_',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
                ('payment_type', models.IntegerField()),
                ('status', models.IntegerField()),
                ('address', models.CharField(max_length=250)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.customer')),
            ],
            options={
                'verbose_name': 'Haridor_',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('cost', models.IntegerField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='media/products')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.category')),
            ],
            options={
                'verbose_name': 'Mahsulot_',
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('descriptions', models.TextField()),
                ('count', models.IntegerField()),
                ('price', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.category')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.product')),
            ],
            options={
                'verbose_name': 'Haridor_tavari_',
            },
        ),
    ]
