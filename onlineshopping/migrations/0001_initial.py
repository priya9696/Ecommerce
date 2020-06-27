# Generated by Django 3.0.2 on 2020-05-20 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('Cname', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=15, unique=True)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pname', models.CharField(max_length=30)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Description', models.TextField(max_length=300)),
                ('pimage', models.ImageField(default='', upload_to='shop/images')),
                ('Cname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineshopping.Category')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
        migrations.CreateModel(
            name='MyOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subt', models.IntegerField()),
                ('Price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineshopping.Product')),
                ('qty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineshopping.Cart')),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment', models.TextField(max_length=300)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineshopping.User')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlineshopping.User'),
        ),
        migrations.AddField(
            model_name='cart',
            name='pid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='onlineshopping.Product'),
        ),
    ]
