# Generated by Django 4.1.5 on 2023-01-20 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stb_Claim_Anusuchi6',
            fields=[
                ('p_ssid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('sch_id', models.DecimalField(decimal_places=0, max_digits=4)),
                ('schapp_id', models.DecimalField(decimal_places=0, max_digits=4)),
                ('permanent_disability_type', models.CharField(max_length=250)),
                ('permanent_disability_date', models.CharField(max_length=10)),
                ('permanent_disability_reason', models.CharField(max_length=10)),
                ('death_date', models.CharField(max_length=10)),
                ('death_reason', models.CharField(max_length=250)),
                ('dep_person_relation', models.CharField(max_length=50)),
                ('no_of_children_below_18', models.DecimalField(decimal_places=0, max_digits=2)),
                ('approved_amount', models.DecimalField(decimal_places=2, max_digits=14)),
                ('amount_received_by', models.CharField(max_length=1000)),
                ('r_status', models.CharField(max_length=1)),
                ('entry_by', models.CharField(max_length=10)),
                ('entry_date', models.DateField()),
                ('tran_no', models.DecimalField(decimal_places=0, max_digits=14)),
                ('claim_app_date', models.CharField(max_length=10)),
                ('dep_fname', models.CharField(max_length=50)),
                ('dep_mname', models.CharField(max_length=50)),
                ('dep_lname', models.CharField(max_length=50)),
                ('average_basic', models.DecimalField(decimal_places=2, max_digits=14)),
                ('remarks', models.CharField(max_length=4000)),
                ('person_id', models.DecimalField(decimal_places=0, max_digits=14)),
            ],
        ),
        migrations.CreateModel(
            name='Stb_Claim_App_Amount',
            fields=[
                ('tran_no', models.DecimalField(decimal_places=0, max_digits=14)),
                ('sch_app_id', models.DecimalField(decimal_places=0, max_digits=3, primary_key=True, serialize=False)),
                ('sch_id', models.DecimalField(decimal_places=0, max_digits=4)),
                ('p_ssid', models.CharField(max_length=14)),
                ('claim_amount', models.DecimalField(decimal_places=0, max_digits=10)),
                ('claim_app_date', models.CharField(max_length=14)),
                ('person_id', models.DecimalField(decimal_places=0, max_digits=14)),
            ],
        ),
        migrations.CreateModel(
            name='Stb_Claim_Doc',
            fields=[
                ('ssfid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('schapp_id', models.DecimalField(decimal_places=0, max_digits=3)),
                ('sch_id', models.DecimalField(decimal_places=0, max_digits=4)),
                ('claim_app_date', models.CharField(max_length=10)),
                ('chk_doc_id', models.DecimalField(decimal_places=0, max_digits=3)),
                ('doc_path', models.CharField(max_length=250)),
                ('doc_image', models.ImageField(upload_to='images/')),
                ('entry_by', models.CharField(max_length=10)),
                ('entry_date', models.DateField()),
                ('r_status', models.CharField(max_length=1)),
                ('tran_no', models.DecimalField(decimal_places=0, max_digits=14)),
            ],
        ),
        migrations.CreateModel(
            name='Stb_Claim_Head',
            fields=[
                ('ssfid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('schapp_id', models.DecimalField(decimal_places=0, max_digits=3)),
                ('sch_id', models.DecimalField(decimal_places=0, max_digits=4)),
                ('claim_app_date', models.CharField(max_length=50)),
                ('anusuchi_no', models.DecimalField(decimal_places=0, max_digits=3)),
                ('bank_id', models.DecimalField(decimal_places=0, max_digits=5)),
                ('account_type', models.CharField(max_length=50)),
                ('account_number', models.CharField(max_length=30)),
                ('bank_address', models.CharField(max_length=100)),
                ('recommend_by', models.CharField(max_length=100)),
                ('recomm_emp_post', models.CharField(max_length=100)),
                ('recomm_emp_phone', models.CharField(max_length=20)),
                ('recommend_date', models.CharField(max_length=20)),
                ('entry_by', models.CharField(max_length=10)),
                ('entry_date', models.DateField()),
                ('r_status', models.CharField(max_length=1)),
                ('tran_no', models.DecimalField(decimal_places=0, max_digits=14)),
                ('approved_amount', models.DecimalField(decimal_places=4, max_digits=16)),
                ('approved_by', models.CharField(max_length=100)),
                ('approved_post', models.CharField(max_length=100)),
                ('approved_date', models.CharField(max_length=10)),
                ('is_death', models.CharField(max_length=1)),
                ('claim_amount', models.DecimalField(decimal_places=4, max_digits=16)),
                ('employer_id', models.DecimalField(decimal_places=0, max_digits=14)),
                ('approval_doc', models.FileField(upload_to='uploads/')),
                ('remarks', models.CharField(max_length=1000)),
                ('p_id', models.CharField(max_length=1)),
                ('h_code', models.CharField(max_length=20)),
                ('claim_date', models.CharField(max_length=10)),
                ('claim_id', models.CharField(max_length=30)),
                ('leave_from_date', models.CharField(max_length=10)),
                ('leave_to_date', models.CharField(max_length=10)),
                ('bank_branch_id', models.DecimalField(decimal_places=0, max_digits=5)),
                ('account_name', models.CharField(max_length=200)),
                ('save_mode', models.CharField(max_length=8)),
                ('is_admin_recommended', models.CharField(max_length=1)),
                ('admin_recommender', models.CharField(max_length=50)),
                ('admin_recommend_date', models.CharField(max_length=10)),
                ('is_payment_rejected', models.CharField(max_length=1)),
                ('payment_rejecter', models.CharField(max_length=50)),
                ('payment_rejected_date', models.CharField(max_length=10)),
                ('payment_reject_remarks', models.CharField(max_length=1000)),
                ('admin_recommender_post', models.CharField(max_length=100)),
                ('entry_by_post', models.CharField(max_length=100)),
                ('ref_no', models.CharField(max_length=25)),
                ('payee_id', models.DecimalField(decimal_places=0, max_digits=3)),
                ('tax_amount', models.DecimalField(decimal_places=4, max_digits=16)),
                ('return_amount', models.DecimalField(decimal_places=4, max_digits=16)),
                ('person_id', models.DecimalField(decimal_places=4, max_digits=14)),
            ],
        ),
    ]