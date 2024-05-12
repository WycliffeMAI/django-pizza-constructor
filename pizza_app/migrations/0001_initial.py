# Generated by Django 3.2.6 on 2022-04-28 17:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OptionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(default='', max_length=100)),
                ('customer_email', models.EmailField(default='', max_length=100)),
                ('customer_phone_number', models.CharField(default='', max_length=15)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ToppingGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('topping_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toppings', to='pizza_app.toppinggroup')),
            ],
        ),
        migrations.CreateModel(
            name='OrderTopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topping', to='pizza_app.order')),
                ('topping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza_app.topping')),
            ],
        ),
        migrations.CreateModel(
            name='OrderOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza_app.option')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option', to='pizza_app.order')),
            ],
        ),
        migrations.AddField(
            model_name='option',
            name='option_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='pizza_app.optiongroup'),
        ),
    ]