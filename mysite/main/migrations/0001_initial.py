# Generated by Django 4.2.3 on 2023-07-07 09:12

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
                ('name', models.CharField(max_length=60, verbose_name='Category name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Product name')),
                ('price', models.PositiveIntegerField(verbose_name='Product price')),
                ('img', models.ImageField(upload_to='home_images', verbose_name='Product image')),
                ('about', models.TextField(verbose_name='Product about')),
                ('slug', models.SlugField(unique=True, verbose_name='Product slug')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat_prod', to='main.category')),
            ],
        ),
    ]
