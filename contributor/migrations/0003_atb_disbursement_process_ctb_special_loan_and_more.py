# Generated by Django 4.1.5 on 2023-01-20 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributor', '0002_stb_claim_anusuchi6_stb_claim_app_amount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atb_Disbursement_Process',
            fields=[
                ('submission_id', models.DecimalField(decimal_places=0, max_digits=14, primary_key=True, serialize=False)),
                ('tran_type', models.CharField(max_length=20)),
                ('from_bank', models.DecimalField(decimal_places=0, max_digits=5)),
                ('from_branch', models.DecimalField(decimal_places=0, max_digits=5)),
                ('from_account', models.CharField(max_length=30)),
                ('to_bank', models.DecimalField(decimal_places=0, max_digits=5)),
                ('to_branch', models.DecimalField(decimal_places=0, max_digits=5)),
                ('to_account', models.CharField(max_length=30)),
                ('paid_amount', models.DecimalField(decimal_places=4, max_digits=14)),
                ('voucher_amount', models.DecimalField(decimal_places=4, max_digits=14)),
                ('voucher_no', models.CharField(max_length=20)),
                ('voucher_date', models.CharField(max_length=10)),
                ('entry_by', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=1)),
                ('error_log', models.CharField(max_length=500)),
                ('debit_response_id', models.CharField(max_length=10)),
                ('credit_response_id', models.CharField(max_length=10)),
                ('debit_status', models.CharField(max_length=5)),
                ('credit_status', models.CharField(max_length=5)),
                ('from_account_name', models.CharField(max_length=60)),
                ('to_account_name', models.CharField(max_length=60)),
                ('remarks', models.CharField(max_length=100)),
                ('batch_id', models.CharField(max_length=20)),
                ('instruction_id', models.CharField(max_length=20)),
                ('entry_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ctb_Special_Loan',
            fields=[
                ('p_ssid', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=1)),
                ('loan_ref_no', models.CharField(max_length=30)),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=14)),
                ('pension_amount', models.DecimalField(decimal_places=2, max_digits=14)),
                ('gratuity_amount', models.DecimalField(decimal_places=2, max_digits=14)),
                ('transfer_type', models.DecimalField(decimal_places=0, max_digits=3)),
                ('transfer_percentage', models.DecimalField(decimal_places=0, max_digits=3)),
                ('transfer_amount', models.DecimalField(decimal_places=2, max_digits=14)),
                ('is_transfer_eligible', models.DecimalField(decimal_places=0, max_digits=1)),
                ('is_eligible_for_loan', models.DecimalField(decimal_places=0, max_digits=1)),
                ('from_date', models.CharField(max_length=10)),
                ('entry_by', models.CharField(max_length=50)),
                ('entry_date', models.DateField()),
                ('loan_start_date', models.CharField(max_length=10)),
                ('loan_end_date', models.CharField(max_length=10)),
                ('loan_period_in_year', models.DecimalField(decimal_places=0, max_digits=2)),
                ('tran_no', models.DecimalField(decimal_places=0, max_digits=14, primary_key=True, serialize=False)),
                ('is_transferred', models.DecimalField(decimal_places=0, max_digits=1)),
                ('transfer_tran_no', models.DecimalField(decimal_places=0, max_digits=14)),
                ('payment_tran_no', models.DecimalField(decimal_places=0, max_digits=14)),
                ('pay_source', models.CharField(max_length=2)),
                ('cheque_no', models.CharField(max_length=100)),
                ('cheque_date', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ctb_User_Tran_Verifications',
            fields=[
                ('application_id', models.CharField(max_length=20)),
                ('module_id', models.CharField(max_length=50)),
                ('from_date', models.CharField(max_length=10)),
                ('tran_no', models.DecimalField(decimal_places=0, max_digits=14, primary_key=True, serialize=False)),
                ('seq_no', models.DecimalField(decimal_places=0, max_digits=2)),
                ('user_id', models.CharField(max_length=30)),
                ('veri_level', models.DecimalField(decimal_places=0, max_digits=3)),
                ('v_status', models.CharField(max_length=1)),
                ('verify_date', models.CharField(max_length=10)),
                ('verify_remarks', models.CharField(max_length=400)),
                ('forwarded_to', models.CharField(max_length=30)),
                ('ufrom_date', models.CharField(max_length=10)),
                ('suffix_entry_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Dctb_Submission',
            fields=[
                ('submission_id', models.DecimalField(decimal_places=0, max_digits=14, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('u_name', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('old_id', models.CharField(max_length=30)),
                ('submission_for', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('submission_date', models.CharField(max_length=10)),
                ('tran_no', models.DecimalField(decimal_places=0, max_digits=14)),
                ('r_status', models.CharField(max_length=1)),
            ],
        ),
    ]