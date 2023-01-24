from django.db import models


class Ctb_Special_Loan(models.Model):
    p_ssid = models.CharField(
        max_length=15, db_column="P_SSID")  # Fk, AK2, IX3
    status = models.CharField(max_length=1, db_column="STATUS")
    loan_ref_no = models.CharField(
        max_length=30, db_column="LOAN_REF_NO")  # AK2, IX3
    loan_amount = models.DecimalField(
        max_digits=14, decimal_places=2, db_column="LOAN_AMOUNT")
    pension_amount = models.DecimalField(
        max_digits=14, decimal_places=2, db_column="PENSION_AMOUNT")
    gratuity_amount = models.DecimalField(
        max_digits=14, decimal_places=2, db_column="GRATUITY_AMOUNT")
    transfer_type = models.DecimalField(
        max_digits=3, decimal_places=0, db_column="TRANSFER_TYPE")
    transfer_percentage = models.DecimalField(
        max_digits=3, decimal_places=0, db_column="TRANSFER_PERCENTAGE")
    transfer_amount = models.DecimalField(
        max_digits=14, decimal_places=2, db_column="TRANSFER_AMOUNT")
    is_transfer_eligible = models.DecimalField(
        max_digits=1, decimal_places=0, db_column="IS_TRANSFER_ELIGIBLE")
    is_eligible_for_loan = models.DecimalField(
        max_digits=1, decimal_places=0, db_column="IS_ELIGIBLE_FOR_LOAN")
    from_date = models.CharField(max_length=10, db_column="FROM_DATE")
    entry_by = models.CharField(max_length=50, db_column="ENTRY_BY")
    entry_date = models.DateField(db_column="ENTRY_DATE")
    loan_start_date = models.CharField(
        max_length=10, db_column="LOAN_START_DATE")
    loan_end_date = models.CharField(max_length=10, db_column="LOAN_END_DATE")
    loan_period_in_year = models.DecimalField(
        max_digits=2, decimal_places=0, db_column="LOAN_PERIOD_IN_YEAR")
    tran_no = models.DecimalField(
        max_digits=14, decimal_places=0, primary_key=True, db_column="TRAN_NO")  # PK IX2
    is_transferred = models.DecimalField(
        max_digits=1, decimal_places=0, db_column="IS_TRANSFERRED")
    transfer_tran_no = models.DecimalField(
        max_digits=14, decimal_places=0, db_column="TRANSFER_TRAN_NO")
    payment_tran_no = models.DecimalField(
        max_digits=14, decimal_places=0, db_column="PAYMENT_TRAN_NO")  # AK0, IX1
    pay_source = models.CharField(max_length=2, db_column="PAY_SOURCE")
    cheque_no = models.CharField(max_length=100, db_column="CHEQUE_NO")
    cheque_date = models.CharField(max_length=10, db_column="CHEQUE_DATE")



class Ctb_User_Tran_Verifications(models.Model):
    application_id = models.CharField(
        max_length=20, db_column="APPLICATION_ID")  # PFK, IX1, IX3
    module_id = models.CharField(
        max_length=50, db_column="MODULE_ID")  # PFK, IX1, IX3
    from_date = models.CharField(
        max_length=10, db_column="FROM_DATE")  # PFK, IX1, IX3
    tran_no = models.DecimalField(
        max_digits=14, decimal_places=0, primary_key=True, db_column="TRAN_NO")  # PK IX1, IX3
    seq_no = models.DecimalField(
        max_digits=2, decimal_places=0, db_column="SEQ_NO")  # PK IX1, IX3
    user_id = models.CharField(max_length=30, db_column="USER_ID")  # IX2
    veri_level = models.DecimalField(
        max_digits=3, decimal_places=0, db_column="VERI_LEVEL")  # IX2
    v_status = models.CharField(max_length=1, db_column="V_STATUS")
    verify_date = models.CharField(max_length=10, db_column="VERIFY_DATE")
    verify_remarks = models.CharField(
        max_length=400, db_column="VERIFY_REMARKS")
    forwarded_to = models.CharField(max_length=30, db_column="FORWARDED_TO")
    ufrom_date = models.CharField(max_length=10, db_column="UFROM_DATE")  # IX2
    suffix_entry_date = models.DateField(db_column="SUFFIX_ENTRY_DATE")



class Dctb_Submission(models.Model):
    submission_id = models.DecimalField(
        max_digits=14, decimal_places=0, primary_key=True, db_column="SUBMISSION_ID")  # IX1
    user_id = models.CharField(max_length=50, db_column="USER_ID")
    password = models.CharField(max_length=30, db_column="PASSWORD")
    u_name = models.CharField(max_length=100, db_column="U_NAME")
    phone_no = models.CharField(max_length=30, db_column="PHONE_NO")
    email = models.CharField(max_length=50, db_column="EMAIL")
    old_id = models.CharField(max_length=30, db_column="OLD_ID")
    submission_for = models.CharField(
        max_length=20, db_column="SUBMISSION_FOR")
    address = models.CharField(max_length=200, db_column="ADDRESS")
    submission_date = models.CharField(
        max_length=10, db_column="SUBMISSION_DATE")
    tran_no = models.DecimalField(
        max_digits=14, decimal_places=0, db_column="TRAN_NO")
    r_status = models.CharField(max_length=1, db_column="R_STATUS")



class Atb_Disbursement_Process(models.Model):
    submission_id = models.DecimalField(
        max_digits=14, decimal_places=0, primary_key=True, db_column="SUBMISSION_ID")  # IX1
    tran_type = models.CharField(max_length=20, db_column="TRAN_TYPE")
    from_bank = models.DecimalField(
        max_digits=5, decimal_places=0, db_column="FROM_BANK")
    from_branch = models.DecimalField(
        max_digits=5, decimal_places=0, db_column="FROM_BRANCH")
    from_account = models.CharField(max_length=30, db_column="FROM_ACCOUNT")
    to_bank = models.DecimalField(
        max_digits=5, decimal_places=0, db_column="TO_BANK")
    to_branch = models.DecimalField(
        max_digits=5, decimal_places=0, db_column="TO_BRANCH")
    to_account = models.CharField(max_length=30, db_column="TO_ACCOUNT")
    paid_amount = models.DecimalField(
        max_digits=14, decimal_places=4, db_column="PAID_AMOUNT")
    voucher_amount = models.DecimalField(
        max_digits=14, decimal_places=4, db_column="VOUCHER_AMOUNT")
    voucher_no = models.CharField(max_length=20, db_column="VOUCHER_NO")
    voucher_date = models.CharField(max_length=10, db_column="VOUCHER_DATE")
    entry_by = models.CharField(max_length=20, db_column="ENTRY_BY")
    entry_date = models.CharField(max_length=10, db_column="ENTRY_DATE")
    status = models.CharField(max_length=1, db_column="STATUS")
    error_log = models.CharField(max_length=500, db_column="ERROR_LOG")
    debit_response_id = models.CharField(
        max_length=10, db_column="DEBIT_RESPONSE_ID")
    credit_response_id = models.CharField(
        max_length=10, db_column="CREDIT_RESPONSE_ID")
    debit_status = models.CharField(max_length=5, db_column="DEBIT_STATUS")
    credit_status = models.CharField(max_length=5, db_column="CREDIT_STATUS")
    from_account_name = models.CharField(
        max_length=60, db_column="FROM_ACCOUNT_NAME")
    to_account_name = models.CharField(
        max_length=60, db_column="TO_ACCOUNT_NAME")
    remarks = models.CharField(max_length=100, db_column="REMARKS")
    batch_id = models.CharField(max_length=20, db_column="BATCH_ID")
    instruction_id = models.CharField(
        max_length=20, db_column="INSTRUCTION_ID")
    entry_date = models.DateField(db_column="ENTRY_DATE")

