# Generated by Django 4.1.5 on 2023-01-20 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributor', '0003_atb_disbursement_process_ctb_special_loan_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atb_Account_Ledger',
            fields=[
                ('office_code', models.DecimalField(decimal_places=0, max_digits=4, primary_key=True, serialize=False)),
                ('gl_id', models.DecimalField(decimal_places=0, max_digits=10)),
                ('value_date', models.CharField(max_length=10)),
                ('fiscal_year', models.CharField(max_length=10)),
                ('dr', models.DecimalField(decimal_places=2, max_digits=20)),
                ('cr', models.DecimalField(decimal_places=2, max_digits=20)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=22)),
            ],
        ),
        migrations.CreateModel(
            name='Atb_Gltran_Detl',
            fields=[
                ('gltran_detl', models.DecimalField(decimal_places=0, max_digits=3, primary_key=True, serialize=False)),
                ('office_code', models.DecimalField(decimal_places=0, max_digits=4)),
                ('gl_group_code', models.DecimalField(decimal_places=0, max_digits=4)),
                ('ac_no', models.CharField(max_length=100)),
                ('gl_id', models.DecimalField(decimal_places=0, max_digits=4)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=18)),
                ('tran_desc', models.CharField(max_length=200)),
                ('inst_code', models.CharField(max_length=100)),
                ('inst_date', models.CharField(max_length=10)),
                ('vch_id', models.DecimalField(decimal_places=0, max_digits=4)),
                ('status', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Atb_Gltran_Mast',
            fields=[
                ('office_code', models.DecimalField(decimal_places=0, max_digits=4)),
                ('vch_no', models.CharField(max_length=50)),
                ('vch_type_code', models.DecimalField(decimal_places=0, max_digits=4)),
                ('cost_center_id', models.DecimalField(decimal_places=0, max_digits=4)),
                ('tran_date', models.CharField(max_length=10)),
                ('tran_user_id', models.CharField(max_length=30)),
                ('is_approved', models.DecimalField(decimal_places=0, max_digits=4)),
                ('approved_date', models.CharField(max_length=10)),
                ('approved_user_id', models.CharField(max_length=30)),
                ('is_reverse', models.DecimalField(decimal_places=0, max_digits=4)),
                ('rev_vch_id', models.DecimalField(decimal_places=0, max_digits=4)),
                ('vch_id', models.DecimalField(decimal_places=0, max_digits=4, primary_key=True, serialize=False)),
                ('tran_number', models.CharField(max_length=14)),
                ('mast_desc', models.CharField(max_length=1000)),
                ('application_id', models.CharField(max_length=20)),
                ('module_id', models.CharField(max_length=30)),
                ('value_date', models.CharField(max_length=10)),
                ('is_deleted', models.DecimalField(decimal_places=0, max_digits=4)),
            ],
        ),
    ]