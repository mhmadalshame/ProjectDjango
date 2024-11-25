# Generated by Django 4.2.1 on 2024-01-01 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='rolee',
            field=models.CharField(choices=[('company_manager', 'مدير الشركة'), ('warehouse_keeper', 'أمين المستودع'), ('customer', 'الزبون')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=1, max_length=150, unique=True),
            preserve_default=False,
        ),
    ]
