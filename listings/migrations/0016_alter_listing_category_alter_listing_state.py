# Generated by Django 4.2.1 on 2023-05-26 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0015_alter_listing_category_alter_listing_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Bikes', 'Bikes'), ('Property', 'Property'), ('Cars', 'Cars'), ('Electronics', 'Electronics'), ('Jobs', 'Jobs'), ('Furniture', 'Furniture'), ('Mobiles', 'Mobiles'), ('Books&Sports', 'Books&Sports'), ('Fashion', 'Fashion')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(choices=[('OD', 'Odisha'), ('UP', 'Uttar Pradesh'), ('CG', 'Chhattisgarh'), ('UK', 'Uttarakhand'), ('HP', 'Haryana'), ('MN', 'Manipur'), ('AS', 'Assam'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('WB', 'West Bengal'), ('GJ', 'Gujarat'), ('TN', 'Tamil Nadu'), ('BR', 'Bihar'), ('GA', 'Goa'), ('AP', 'Andhra Pradesh'), ('PB', 'Punjab'), ('KL', 'Kerala'), ('TS', 'Telangana'), ('TR', 'Tripura'), ('JH', 'Jharkhand'), ('AR', 'Arunachal Pradesh'), ('MI', 'Sikkim'), ('KA', 'Karnataka'), ('NL', 'Nagaland'), ('RJ', 'Rajasthan')], max_length=100),
        ),
    ]
