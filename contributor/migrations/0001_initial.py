# Generated by Django 4.1.5 on 2023-01-20 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ctb_Address',
            fields=[
                ('address_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('district_cd', models.DecimalField(decimal_places=0, max_digits=2)),
                ('vdc_cd', models.DecimalField(decimal_places=0, max_digits=10)),
                ('ward', models.DecimalField(decimal_places=0, max_digits=2)),
                ('tole_nep', models.CharField(max_length=100)),
                ('tole_eng', models.CharField(max_length=100)),
                ('house_number', models.CharField(max_length=50)),
                ('entry_by', models.CharField(max_length=30)),
                ('entry_date', models.DateField()),
                ('r_status', models.CharField(max_length=1)),
                ('tran_no', models.DecimalField(decimal_places=0, max_digits=14)),
            ],
            options={
                'verbose_name_plural': 'Ctb_Addresses',
            },
        ),
        migrations.CreateModel(
            name='Ctb_Contributor',
            fields=[
                ('p_ssid', models.CharField(max_length=15)),
                ('employer_id', models.DecimalField(decimal_places=0, max_digits=14)),
                ('from_date', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('to_date', models.CharField(max_length=10)),
                ('post', models.CharField(max_length=300)),
                ('emptype_id', models.DecimalField(decimal_places=0, max_digits=3)),
                ('joining_date', models.CharField(max_length=11)),
                ('termination_date', models.CharField(max_length=10)),
                ('termination_res', models.CharField(max_length=300)),
                ('entry_by', models.CharField(max_length=30)),
                ('entry_date', models.DateField()),
                ('r_status', models.CharField(max_length=1)),
                ('tran_no', models.DecimalField(decimal_places=0, max_digits=14)),
                ('terminated_by', models.CharField(max_length=30)),
                ('new_tran', models.DecimalField(decimal_places=0, max_digits=14)),
                ('marking', models.CharField(max_length=1)),
                ('group_id', models.DecimalField(decimal_places=0, max_digits=3)),
                ('contributor_type', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Ctb_Emp_Address',
            fields=[
                ('employer_id', models.DecimalField(decimal_places=0, max_digits=14)),
                ('adtype_id', models.DecimalField(decimal_places=0, max_digits=3)),
                ('address_id', models.DecimalField(decimal_places=0, max_digits=10)),
                ('from_date', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('to_date', models.CharField(max_length=10)),
                ('entry_by', models.CharField(max_length=30)),
                ('entry_date', models.DateField()),
                ('r_status', models.CharField(max_length=1)),
                ('tran_no', models.DecimalField(decimal_places=0, max_digits=14)),
            ],
            options={
                'verbose_name_plural': 'Ctb_Person_Addresses',
            },
        ),
        migrations.CreateModel(
            name='Ctb_Emp_Contact',
            fields=[
                ('employer_id', models.DecimalField(decimal_places=0, max_digits=14)),
                ('adtype_id', models.DecimalField(decimal_places=0, max_digits=3)),
                ('address_id', models.DecimalField(decimal_places=0, max_digits=10)),
                ('a_from_date', models.CharField(max_length=10)),
                ('ctype_id', models.DecimalField(decimal_places=0, max_digits=3)),
                ('from_date', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('c_value', models.CharField(max_length=100)),
                ('to_date', models.CharField(max_length=10)),
                ('entry_by', models.CharField(max_length=30)),
                ('entry_date', models.DateField()),
                ('r_status', models.CharField(max_length=1)),
                ('tran_no', models.DecimalField(decimal_places=0, max_digits=14)),
            ],
        ),
        migrations.CreateModel(
            name='Ctb_Emp_Doc',
            fields=[
                ('employer_id', models.DecimalField(decimal_places=0, max_digits=14)),
                ('doc_id', models.DecimalField(decimal_places=0, max_digits=3)),
                ('from_date', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('to_date', models.CharField(max_length=10)),
                ('issue_no', models.CharField(max_length=60)),
                ('issue_date', models.CharField(max_length=10)),
                ('issue_place', models.CharField(max_length=100)),
                ('entry_by', models.CharField(max_length=30)),
                ('entry_date', models.DateField()),
                ('r_status', models.CharField(max_length=1)),
                ('tran_no', models.DecimalField(decimal_places=0, max_digits=14)),
                ('docfile', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Ctb_Emp_Official',
            fields=[
                ('employer_id', models.DecimalField(decimal_places=0, max_digits=14)),
                ('e_id', models.DecimalField(decimal_places=0, max_digits=14)),
                ('post_id', models.DecimalField(decimal_places=0, max_digits=10)),
                ('from_date', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('to_date', models.CharField(max_length=10)),
                ('entry_by', models.CharField(max_length=30)),
                ('entry_date', models.DateField()),
                ('r_status', models.CharField(max_length=1)),
                ('tran_no', models.DecimalField(decimal_places=0, max_digits=14)),
            ],
        ),
        migrations.CreateModel(
            name='Ctb_Employer',
            fields=[
                ('employer_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('employer_name_nep', models.CharField(max_length=150)),
                ('employer_name_eng', models.CharField(max_length=150)),
                ('etype_id', models.DecimalField(decimal_places=0, max_digits=3)),
                ('stype_id', models.DecimalField(decimal_places=0, max_digits=3)),
                ('e_ssid', models.CharField(max_length=25)),
                ('entry_by', models.CharField(max_length=30)),
                ('entry_date', models.DateField()),
                ('r_status', models.CharField(max_length=1)),
                ('tran_no', models.DecimalField(decimal_places=0, max_digits=14)),
                ('alert_source', models.CharField(max_length=11)),
                ('alt_source_val', models.CharField(max_length=100)),
                ('short_menu', models.CharField(max_length=1)),
                ('calendar', models.CharField(max_length=1)),
                ('group_applied', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Ctb_Person',
            fields=[
                ('p_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('fname_nep', models.CharField(max_length=30)),
                ('mname_nep', models.CharField(max_length=30)),
                ('lname_nep', models.CharField(max_length=30)),
                ('fname_eng', models.CharField(max_length=30)),
                ('mname_eng', models.CharField(max_length=30)),
                ('lname_eng', models.CharField(max_length=30)),
                ('dob', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=2)),
                ('ds_agency_id', models.DecimalField(decimal_places=0, max_digits=3)),
                ('ds_id_number', models.CharField(max_length=20)),
                ('p_ssid', models.CharField(max_length=15)),
                ('not_understood', models.CharField(max_length=2)),
                ('rel_id', models.DecimalField(decimal_places=0, max_digits=3)),
                ('eth_id', models.DecimalField(decimal_places=0, max_digits=3)),
                ('entry_by', models.CharField(max_length=15)),
                ('entry_date', models.DateField()),
                ('r_status', models.CharField(max_length=1)),
                ('trans_no', models.DecimalField(decimal_places=0, max_digits=14)),
                ('alert_source', models.CharField(max_length=11)),
                ('alt_source_val', models.CharField(max_length=100)),
                ('bloodgroup', models.CharField(max_length=4)),
                ('image_file', models.ImageField(upload_to='images/')),
                ('seq_no', models.DecimalField(decimal_places=0, max_digits=5)),
                ('is_disable', models.CharField(max_length=1)),
                ('reaction', models.CharField(max_length=1)),
                ('disability_percent', models.DecimalField(decimal_places=0, max_digits=3)),
                ('bank_id', models.DecimalField(decimal_places=0, max_digits=4)),
                ('branch_id', models.DecimalField(decimal_places=0, max_digits=4)),
                ('bank_ac_name', models.CharField(max_length=100)),
                ('bank_ac_type', models.CharField(max_length=50)),
                ('bank_ac_number', models.CharField(max_length=50)),
                ('grand_father_name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=50)),
                ('parent_pssid', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ctb_Person_Address',
            fields=[
                ('p_id', models.DecimalField(decimal_places=0, max_digits=14)),
                ('adtype_id', models.DecimalField(decimal_places=0, max_digits=3)),
                ('address_id', models.DecimalField(decimal_places=0, max_digits=10)),
                ('from_date', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('to_date', models.CharField(max_length=10)),
                ('entry_by', models.CharField(max_length=30)),
                ('entry_date', models.DateField()),
                ('r_status', models.CharField(max_length=1)),
                ('tran_no', models.DecimalField(decimal_places=0, max_digits=14)),
                ('reaction', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name_plural': 'Ctb_Person_Addresses',
            },
        ),
        migrations.CreateModel(
            name='Ctb_Person_Contact',
            fields=[
                ('p_id', models.DecimalField(decimal_places=0, max_digits=14)),
                ('ctype_id', models.DecimalField(decimal_places=0, max_digits=3)),
                ('from_date', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('c_value', models.CharField(max_length=100)),
                ('to_date', models.CharField(max_length=10)),
                ('entry_by', models.CharField(max_length=30)),
                ('entry_date', models.DateField()),
                ('r_status', models.CharField(max_length=1)),
                ('tran_no', models.DecimalField(decimal_places=0, max_digits=14)),
            ],
        ),
        migrations.CreateModel(
            name='Ctb_Person_Dependent',
            fields=[
                ('p_id', models.DecimalField(decimal_places=0, max_digits=14)),
                ('reltype_id', models.DecimalField(decimal_places=0, max_digits=3)),
                ('relative_id', models.DecimalField(decimal_places=0, max_digits=14)),
                ('entry_by', models.CharField(max_length=30)),
                ('entry_date', models.DateField()),
                ('r_status', models.CharField(max_length=1)),
                ('tran_no', models.DecimalField(decimal_places=0, max_digits=14)),
                ('order_no', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ctb_Person_Doc',
            fields=[
                ('p_id', models.DecimalField(decimal_places=0, max_digits=14)),
                ('doc_id', models.DecimalField(decimal_places=0, max_digits=3)),
                ('from_date', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('to_date', models.CharField(max_length=10)),
                ('issue_no', models.CharField(max_length=60)),
                ('issue_date', models.CharField(max_length=11)),
                ('issue_place', models.CharField(max_length=100)),
                ('entry_by', models.CharField(max_length=30)),
                ('entry_date', models.DateField()),
                ('r_status', models.CharField(max_length=1)),
                ('tran_no', models.DecimalField(decimal_places=0, max_digits=14)),
                ('docfile', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Ctb_Person_Nominee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.DecimalField(decimal_places=0, max_digits=14)),
                ('reltype_id', models.DecimalField(decimal_places=0, max_digits=3)),
                ('relative_id', models.DecimalField(decimal_places=0, max_digits=14)),
                ('from_date', models.CharField(max_length=10)),
                ('to_date', models.CharField(max_length=10)),
                ('entry_by', models.CharField(max_length=30)),
                ('entry_date', models.DateField()),
                ('r_status', models.CharField(max_length=1)),
                ('tran_no', models.DecimalField(decimal_places=0, max_digits=14)),
                ('order_no', models.DecimalField(decimal_places=0, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Stb_Coll_Tran_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_ssid', models.CharField(max_length=15)),
                ('employer_id', models.DecimalField(decimal_places=0, max_digits=14)),
                ('c_from_date', models.CharField(max_length=10)),
                ('from_date', models.CharField(max_length=10)),
                ('schapp_id', models.CharField(max_length=14)),
                ('tran_no', models.CharField(max_length=14)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('entry_by', models.CharField(max_length=30)),
                ('entry_date', models.DateField()),
                ('r_status', models.CharField(max_length=1)),
                ('cont_from_date', models.CharField(max_length=10)),
                ('cont_to_date', models.CharField(max_length=10)),
                ('coll_year', models.DecimalField(decimal_places=0, max_digits=4)),
                ('coll_month', models.DecimalField(decimal_places=0, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Stb_Coll_Voucher_Info',
            fields=[
                ('employer_id', models.DecimalField(decimal_places=0, max_digits=14)),
                ('tran_no', models.DecimalField(decimal_places=0, max_digits=14)),
                ('bank_id', models.DecimalField(decimal_places=0, max_digits=4)),
                ('voucher_no', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('account_no', models.CharField(max_length=30)),
                ('voucher_date', models.CharField(max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('r_status', models.CharField(max_length=1)),
                ('voh_id', models.DecimalField(decimal_places=0, max_digits=14)),
                ('branch_id', models.DecimalField(decimal_places=0, max_digits=14)),
                ('booked_date', models.CharField(max_length=10)),
                ('from_bank_id', models.DecimalField(decimal_places=0, max_digits=4)),
                ('from_brach_id', models.DecimalField(decimal_places=0, max_digits=4)),
                ('from_account_no', models.CharField(max_length=30)),
                ('remarks', models.CharField(max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='Stb_Collection_Tran_Head',
            fields=[
                ('employer_id', models.DecimalField(decimal_places=0, max_digits=14)),
                ('tran_no', models.DecimalField(decimal_places=0, max_digits=14, primary_key=True, serialize=False)),
                ('tran_date', models.CharField(max_length=10)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('int_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pena_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('entry_by', models.CharField(max_length=30)),
                ('entry_date', models.DateField()),
                ('r_status', models.CharField(max_length=1)),
                ('cont_from_date', models.CharField(max_length=10)),
                ('cont_to_date', models.CharField(max_length=10)),
                ('t_no', models.DecimalField(decimal_places=0, max_digits=14)),
                ('coll_year', models.DecimalField(decimal_places=0, max_digits=4)),
                ('coll_month', models.DecimalField(decimal_places=0, max_digits=2)),
                ('duepenalty_amount', models.DecimalField(decimal_places=0, max_digits=10)),
                ('calendar', models.CharField(max_length=1)),
                ('regularity_status', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Stb_Contributor_Sal_Det',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_ssid', models.CharField(max_length=15)),
                ('basic_sal', models.DecimalField(decimal_places=2, max_digits=14)),
                ('grade', models.DecimalField(decimal_places=2, max_digits=10)),
                ('from_date', models.CharField(max_length=10)),
                ('to_date', models.CharField(max_length=10)),
                ('entry_by', models.CharField(max_length=10)),
                ('entry_date', models.DateField()),
                ('r_status', models.CharField(max_length=1)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=14)),
                ('tran_no', models.DecimalField(decimal_places=0, max_digits=14)),
                ('employer_id', models.DecimalField(decimal_places=0, max_digits=14)),
                ('coll_year', models.DecimalField(decimal_places=0, max_digits=4)),
                ('coll_month', models.DecimalField(decimal_places=0, max_digits=2)),
                ('remarks', models.CharField(max_length=1000)),
                ('is_regular', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Stb_Scheme_Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schapp_desc', models.CharField(max_length=200)),
                ('schapp_desc_eng', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=1)),
                ('scheme_percent', models.DecimalField(decimal_places=0, max_digits=5)),
                ('order_no', models.DecimalField(decimal_places=0, max_digits=2)),
                ('gl_code', models.DecimalField(decimal_places=0, max_digits=8)),
                ('p_gl_code', models.DecimalField(decimal_places=0, max_digits=8)),
                ('used_by', models.CharField(max_length=24)),
                ('coll_type', models.CharField(max_length=1)),
                ('parent_schapp_id', models.DecimalField(decimal_places=0, max_digits=3)),
                ('calculation_by_percentage', models.CharField(max_length=8)),
                ('amount_type', models.CharField(max_length=8)),
                ('claim_type', models.CharField(max_length=5)),
            ],
        ),
    ]
