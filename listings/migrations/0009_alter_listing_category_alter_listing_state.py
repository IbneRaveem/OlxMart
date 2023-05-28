# Generated by Django 4.2.1 on 2023-05-22 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_alter_listing_category_alter_listing_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Property', 'Property'), ('Furniture', 'Furniture'), ('Fashion', 'Fashion'), ('Jobs', 'Jobs'), ('Electronics', 'Electronics'), ('Cars', 'Cars'), ('Bikes', 'Bikes'), ('Mobiles', 'Mobiles'), ('Books&Sports', 'Books&Sports')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(choices=[('TN', 'Tamil Nadu'), ('GA', 'Goa'), ('MN', 'Manipur'), ('TS', 'Telegana'), ('AP', 'Andhra Pradesh'), ('KL', 'Kerala'), ('OD', 'Odisha'), ('NL', 'Nagaland'), ('KA', 'Karnataka'), ('BR', 'Bihar'), ('ML', 'Meghalaya'), ('MH', 'Maharashtra'), ('AR', 'Arunachal Pradesh'), ('GJ', 'Gujarat'), ('MP', 'Madhya Pradesh'), ('JH', 'Jharkhand'), ('CG', 'Chhattisgarh'), ('MI', 'Sikkim'), ('WB', 'West Bengal'), ('MZ', 'Mizoram'), ('HP', 'Haryana'), ('RJ', 'Rajasthan'), ('UK', 'Uttarakhand'), ('AS', 'Assam'), ('UP', 'Uttar Pradesh'), ('PB', 'Punjab'), ('TR', 'Tripura')], max_length=100),
        ),
    ]
