from django.db import models


class Ctb_Special_Loan(models.Model):
    p_ssid = models.CharField(max_length=15)  # Fk, AK2, IX3
    status = models.CharField(max_length=1)
    loan_ref_no = models.CharField(max_length=30)  # AK2, IX3
    loan_amount = models.DecimalField(max_digits=14, decimal_places=2)
    pension_amount = models.DecimalField(max_digits=14, decimal_places=2)
    gratuity_amount = models.DecimalField(max_digits=14, decimal_places=2)
    transfer_type = models.DecimalField(max_digits=3, decimal_places=0)
    transfer_percentage = models.DecimalField(max_digits=3, decimal_places=0)
    transfer_amount = models.DecimalField(max_digits=14, decimal_places=2)
    is_transfer_eligible = models.DecimalField(max_digits=1, decimal_places=0)
    is_eligible_for_loan = models.DecimalField(max_digits=1, decimal_places=0)
    from_date = models.CharField(max_length=10)
    entry_by = models.CharField(max_length=50)
    entry_date = models.DateField()
    loan_start_date = models.CharField(max_length=10)
    loan_end_date = models.CharField(max_length=10)
    loan_period_in_year = models.DecimalField(max_digits=2, decimal_places=0)
    tran_no = models.DecimalField(
        max_digits=14, decimal_places=0, primary_key=True)  # PK IX2
    is_transferred = models.DecimalField(max_digits=1, decimal_places=0)
    transfer_tran_no = models.DecimalField(max_digits=14, decimal_places=0)
    payment_tran_no = models.DecimalField(
        max_digits=14, decimal_places=0)  # AK0, IX1
    pay_source = models.CharField(max_length=2)
    cheque_no = models.CharField(max_length=100)
    cheque_date = models.CharField(max_length=10)


class Ctb_User_Tran_Verifications(models.Model):
    application_id = models.CharField(max_length=20)  # PFK, IX1, IX3
    module_id = models.CharField(max_length=50)  # PFK, IX1, IX3
    from_date = models.CharField(max_length=10)  # PFK, IX1, IX3
    tran_no = models.DecimalField(
        max_digits=14, decimal_places=0, primary_key=True)  # PK IX1, IX3
    seq_no = models.DecimalField(max_digits=2, decimal_places=0)  # PK IX1, IX3
    user_id = models.CharField(max_length=30)  # IX2
    veri_level = models.DecimalField(max_digits=3, decimal_places=0)  # IX2
    v_status = models.CharField(max_length=1)
    verify_date = models.CharField(max_length=10)
    verify_remarks = models.CharField(max_length=400)
    forwarded_to = models.CharField(max_length=30)
    ufrom_date = models.CharField(max_length=10)  # IX2
    suffix_entry_date = models.DateField()


class Dctb_Submission(models.Model):
    submission_id = models.DecimalField(
        max_digits=14, decimal_places=0, primary_key=True)  # IX1
    user_id = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    u_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    old_id = models.CharField(max_length=30)
    submission_for = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    submission_date = models.CharField(max_length=10)
    submission_date = models.CharField(max_length=10)
    tran_no = models.DecimalField(max_digits=14, decimal_places=0)
    r_status = models.CharField(max_length=1)


class Atb_Disbursement_Process(models.Model):
    submission_id = models.DecimalField(
        max_digits=14, decimal_places=0, primary_key=True)  # IX1
    tran_type = models.CharField(max_length=20)
    from_bank = models.DecimalField(max_digits=5, decimal_places=0)
    from_branch = models.DecimalField(max_digits=5, decimal_places=0)
    from_account = models.CharField(max_length=30)
    to_bank = models.DecimalField(max_digits=5, decimal_places=0)
    to_branch = models.DecimalField(max_digits=5, decimal_places=0)
    to_account = models.CharField(max_length=30)
    paid_amount = models.DecimalField(max_digits=14, decimal_places=4)
    voucher_amount = models.DecimalField(max_digits=14, decimal_places=4)
    voucher_no = models.CharField(max_length=20)
    voucher_date = models.CharField(max_length=10)
    entry_by = models.CharField(max_length=20)
    entry_date = models.CharField(max_length=10)
    status = models.CharField(max_length=1)
    error_log = models.CharField(max_length=500)
    debit_response_id = models.CharField(max_length=10)
    credit_response_id = models.CharField(max_length=10)
    debit_status = models.CharField(max_length=5)
    credit_status = models.CharField(max_length=5)
    from_account_name = models.CharField(max_length=60)
    to_account_name = models.CharField(max_length=60)
    remarks = models.CharField(max_length=100)
    batch_id = models.CharField(max_length=20)
    instruction_id = models.CharField(max_length=20)
    entry_date = models.DateField()
