# Generated by Django 3.1.7 on 2021-03-04 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0003_auto_20210304_1052'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_stock', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='rental',
            name='real_stock',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rent.vehiclestock'),
        ),
    ]