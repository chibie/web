# Generated by Django 2.2.4 on 2020-11-19 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0094_grant_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grantclr',
            name='contribution_multiplier',
            field=models.DecimalField(decimal_places=4, default=1.0, help_text='This contribution multipler is applied to each contribution before running CLR calculations. In order to increase the saturation, please increase this value first, before modifying the thresholds.', max_digits=10),
        ),
        migrations.AlterField(
            model_name='grantclr',
            name='total_pot',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Total CLR Pot', max_digits=10),
        ),
        migrations.AlterField(
            model_name='grantclr',
            name='unverified_threshold',
            field=models.DecimalField(decimal_places=2, default=5.0, help_text='This is the unverified CLR threshold. The relationship with the CLR match is the same as the verified threshold. If you would like to increase the saturation of round / increase the CLR match, increase this value, but please use the contribution multiplier first.', max_digits=5),
        ),
        migrations.AlterField(
            model_name='grantclr',
            name='verified_threshold',
            field=models.DecimalField(decimal_places=2, default=25.0, help_text='This is the verfied CLR threshold. You can generally increase the saturation of the round / increase the CLR match by increasing this value, as it has a proportional relationship. However, depending on the pair totals by grant, it may reduce certain matches. In any case, please use the contribution multiplier first.', max_digits=5),
        ),
    ]