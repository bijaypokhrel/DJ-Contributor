from django.db import models


class Stb_Coll_Voucher_Info(models.Model):
    employer_id = models.DecimalField(
        max_digits=14, decimal_places=0, db_column="EMPLOYER_ID")  # PFK, IX1
    tran_no = models.DecimalField(
        max_digits=14, decimal_places=0, db_column="TRAN_NO")  # PFK, IX1
    bank_id = models.DecimalField(
        max_digits=4, decimal_places=0, db_column="BANK_ID")  # PK, IX1
    voucher_no = models.CharField(
        max_length=30, primary_key=True, db_column="VOUCHER_NO")  # PK, IX1
    account_no = models.CharField(max_length=30, db_column="ACCOUNT_NO")
    voucher_date = models.CharField(max_length=10, db_column="VOUCHER_DATE")
    amount = models.DecimalField(
        max_digits=15, decimal_places=2, db_column="AMOUNT")
    r_status = models.CharField(max_length=1, db_column="R_STATUS")
    voh_id = models.DecimalField(
        max_digits=14, decimal_places=0, db_column="VOH_ID")
    branch_id = models.DecimalField(
        max_digits=14, decimal_places=0, db_column="BRANCH_ID")
    booked_date = models.CharField(max_length=10, db_column="BOOKED_DATE")
    from_bank_id = models.DecimalField(
        max_digits=4, decimal_places=0, db_column="FROM_BANK_ID")
    from_brach_id = models.DecimalField(
        max_digits=4, decimal_places=0, db_column="FROM_BRANCH_ID")
    from_account_no = models.CharField(
        max_length=30, db_column="FROM_ACCOUNT_NO")
    remarks = models.CharField(max_length=4000, db_column="REMARKS")


class Stb_Contributor_Sal_Det(models.Model):
    p_ssid = models.CharField(max_length=15, db_column="P_SSID")
    basic_sal = models.DecimalField(
        max_digits=14, decimal_places=2, db_column="BASIC_SAL")
    grade = models.DecimalField(
        max_digits=10, decimal_places=2, db_column="GRADE")
    from_date = models.CharField(max_length=10, db_column="FROM_DATE")
    to_date = models.CharField(max_length=10, db_column="TO_DATE")
    entry_by = models.CharField(max_length=10, db_column="ENTRY_BY")
    entry_date = models.DateField(db_column="ENTRY_DATE")
    r_status = models.CharField(max_length=1, db_column="R_STATUS")
    amount = models.DecimalField(
        max_digits=14, decimal_places=2, db_column="AMOUNT")
    tran_no = models.DecimalField(
        max_digits=14, decimal_places=0, db_column="TRAN_NO")  # FK
    employer_id = models.DecimalField(
        max_digits=14, decimal_places=0, db_column="EMPLOYER_ID")  # FK
    coll_year = models.DecimalField(
        max_digits=4, decimal_places=0, db_column="COLL_YEAR")
    coll_month = models.DecimalField(
        max_digits=2, decimal_places=0, db_column="COLL_MONTH")
    remarks = models.CharField(max_length=1000, db_column="REMARKS")
    is_regular = models.CharField(max_length=1, db_column="IS_REGULAR")


class Stb_Collection_Tran_Head(models.Model):
    employer_id = models.DecimalField(
        max_digits=14, decimal_places=0, db_column="EMPLOYER_ID")  # PFK, IX1, IX2
    tran_no = models.DecimalField(
        max_digits=14, decimal_places=0, primary_key=True, db_column="TRAN_NO")  # PK, IX2
    tran_date = models.CharField(max_length=10, db_column="TRAN_DATE")
    total_amount = models.DecimalField(
        max_digits=15, decimal_places=2, db_column="TOTAL_AMOUNT")
    int_amount = models.DecimalField(
        max_digits=10, decimal_places=2, db_column="INT_AMOUNT")
    pena_amount = models.DecimalField(
        max_digits=10, decimal_places=2, db_column="PENA_AMOUNT")
    entry_by = models.CharField(max_length=30, db_column="ENTRY_BY")  # FK
    entry_date = models.DateField(db_column="ENTRY_DATE")
    r_status = models.CharField(max_length=1, db_column="R_STATUS")
    cont_from_date = models.CharField(
        max_length=10, db_column="CONT_FROM_DATE")
    cont_to_date = models.CharField(max_length=10, db_column="CONT_TO_DATE")
    t_no = models.DecimalField(
        max_digits=14, decimal_places=0, db_column="T_NO")
    coll_year = models.DecimalField(
        max_digits=4, decimal_places=0, db_column="COLL_YEAR")  # IX1
    coll_month = models.DecimalField(
        max_digits=2, decimal_places=0, db_column="COLL_MONTH")  # FK IX1
    duepenalty_amount = models.DecimalField(
        max_digits=10, decimal_places=0, db_column="DUEPENALTY_AMOUNT")
    calendar = models.CharField(max_length=1, db_column="CALENDAR")
    regularity_status = models.CharField(
        max_length=8, db_column="REGULARITY_STATUS")


class Stb_Coll_Tran_Details(models.Model):
    p_ssid = models.CharField(max_length=15, db_column="P_SSID")  # PFK IX1
    employer_id = models.DecimalField(
        max_digits=14, decimal_places=0, db_column="EMPLOYER_ID")  # PFK IX1
    c_from_date = models.CharField(
        max_length=10, db_column="C_FROM_DATE")  # PFK IX1
    from_date = models.CharField(
        max_length=10, db_column="FROM_DATE")  # PFK IX1
    schapp_id = models.CharField(
        max_length=14, db_column="SCHAPP_ID")  # PFK IX1
    tran_no = models.CharField(max_length=14, db_column="TRAN_NO")  # PFK IX1
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, db_column="AMOUNT")
    entry_by = models.CharField(max_length=30, db_column="ENTRY_BY")  # FK
    entry_date = models.DateField(db_column="ENTRY_DATE")
    r_status = models.CharField(max_length=1, db_column="R_STATUS")
    cont_from_date = models.CharField(
        max_length=10, db_column="CONT_FROM_DATE")
    cont_to_date = models.CharField(max_length=10, db_column="CONT_TO_DATE")
    coll_year = models.DecimalField(
        max_digits=4, decimal_places=0, db_column="COLL_YEAR")
    coll_month = models.DecimalField(
        max_digits=2, decimal_places=0, db_column="COLL_MONTH")


class Stb_Scheme_Application(models.Model):
    schapp_desc = models.CharField(max_length=200, db_column="SCHAPP_DESC")
    schapp_desc_eng = models.CharField(
        max_length=200, db_column="SCHAPP_DESC_ENG")
    status = models.CharField(max_length=1, db_column="STATUS")
    scheme_percent = models.DecimalField(
        max_digits=5, decimal_places=0, db_column="SCHEME_PERCENT")
    order_no = models.DecimalField(
        max_digits=2, decimal_places=0, db_column="ORDER_NO")
    gl_code = models.DecimalField(
        max_digits=8, decimal_places=0, db_column="GL_CODE")
    p_gl_code = models.DecimalField(
        max_digits=8, decimal_places=0, db_column="P_GL_CODE")
    used_by = models.CharField(max_length=24, db_column="USED_BY")
    coll_type = models.CharField(max_length=1, db_column="COLL_TYPE")
    parent_schapp_id = models.DecimalField(
        max_digits=3, decimal_places=0, db_column="PARENT_SCHAPP_ID")
    calculation_by_percentage = models.CharField(
        max_length=8, db_column="CALCULATION_BY_PERCENTAGE")
    amount_type = models.CharField(max_length=8, db_column="AMOUNT_TYPE")
    claim_type = models.CharField(max_length=5, db_column="CLAIM_TYPE")
