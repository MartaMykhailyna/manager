# Generated by Django 5.0.4 on 2024-05-29 13:19

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id_shoes', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('sh_name', models.CharField(max_length=255)),
                ('sh_model', models.CharField(max_length=255)),
                ('sh_size', models.IntegerField(default=38)),
                ('sh_color', models.CharField(max_length=255)),
                ('sh_manufacturer', models.CharField(blank=True, max_length=255, null=True)),
                ('sh_count', models.IntegerField(default=1)),
                ('sh_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sh_image', models.ImageField(upload_to='images/')),
            ],
            options={
                'db_table': 'shoes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id_user', models.IntegerField(primary_key=True, serialize=False)),
                ('u_username', models.CharField(max_length=255)),
                ('u_name', models.CharField(max_length=255)),
                ('u_surname', models.CharField(max_length=255)),
                ('u_email', models.CharField(blank=True, max_length=255, null=True)),
                ('u_phone', models.CharField(max_length=13)),
                ('u_status', models.BooleanField(default=False)),
                ('u_role', models.CharField(choices=[('administartor', 'administartor'), ('user', 'user')], default='user', max_length=45)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id_reservation', models.AutoField(primary_key=True, serialize=False)),
                ('r_count', models.IntegerField(default=1)),
                ('r_start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('r_end_date', models.DateTimeField(default=datetime.datetime(2024, 5, 29, 16, 19, 47, 402823, tzinfo=datetime.timezone.utc))),
                ('r_shoes', models.ForeignKey(db_column='r_shoes', on_delete=django.db.models.deletion.CASCADE, to='manager_app.shoes')),
                ('r_user', models.ForeignKey(db_column='r_user', on_delete=django.db.models.deletion.CASCADE, to='manager_app.users')),
            ],
            options={
                'db_table': 'reservations',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id_order', models.AutoField(primary_key=True, serialize=False)),
                ('o_count', models.IntegerField(default=1)),
                ('o_sum', models.DecimalField(decimal_places=2, max_digits=10)),
                ('o_recipient', models.CharField(default='Name,Surname', max_length=45)),
                ('o_address', models.CharField(default='Address', max_length=100)),
                ('o_comment', models.CharField(max_length=100, null=True)),
                ('o_status', models.CharField(choices=[('accepted', 'accepted'), ('paid', 'paid'), ('in processing', 'in_processing'), ('shipped', 'shipped'), ('delivered', 'delivered'), ('paid to dropper', 'paid_to_dropper')], default='accepted', max_length=45)),
                ('o_date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('o_shoes', models.ForeignKey(db_column='o_shoes', on_delete=django.db.models.deletion.CASCADE, to='manager_app.shoes')),
                ('o_user', models.ForeignKey(db_column='o_user', null=True, on_delete=django.db.models.deletion.CASCADE, to='manager_app.users')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]
