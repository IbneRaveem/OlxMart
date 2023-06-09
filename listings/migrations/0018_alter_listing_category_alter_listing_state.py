# Generated by Django 4.2.1 on 2023-05-28 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0017_alter_listing_category_alter_listing_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Fashion', 'Fashion'), ('Property', 'Property'), ('Jobs', 'Jobs'), ('Electronics', 'Electronics'), ('Cars', 'Cars'), ('Mobiles', 'Mobiles'), ('Books&Sports', 'Books&Sports'), ('Furniture', 'Furniture'), ('Bikes', 'Bikes')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(choices=[('MN', 'Manipur'), ('WB', 'West Bengal'), ('RJ', 'Rajasthan'), ('UP', 'Uttar Pradesh'), ('AS', 'Assam'), ('AR', 'Arunachal Pradesh'), ('UK', 'Uttarakhand'), ('TS', 'Telangana'), ('ML', 'Meghalaya'), ('TR', 'Tripura'), ('MP', 'Madhya Pradesh'), ('BR', 'Bihar'), ('JH', 'Jharkhand'), ('OD', 'Odisha'), ('MI', 'Sikkim'), ('TN', 'Tamil Nadu'), ('CG', 'Chhattisgarh'), ('HP', 'Haryana'), ('MZ', 'Mizoram'), ('KL', 'Kerala'), ('PB', 'Punjab'), ('GJ', 'Gujarat'), ('NL', 'Nagaland'), ('AP', 'Andhra Pradesh'), ('KA', 'Karnataka'), ('GA', 'Goa'), ('MH', 'Maharashtra')], max_length=100),
        ),
    ]
