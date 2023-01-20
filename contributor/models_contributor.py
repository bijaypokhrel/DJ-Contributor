from django.db import models


class Stb_Coll_Voucher_Info(models.Model):
    employer_id = models.DecimalField(
        max_digits=14, decimal_places=0)  # PFK, IX1
    tran_no = models.DecimalField(
        max_digits=14, decimal_places=0)  # PFK, IX1
    bank_id = models.DecimalField(max_digits=4, decimal_places=0)  # PK, IX1
    voucher_no = models.CharField(max_length=30, primary_key=True)  # PK, IX1
    account_no = models.CharField(max_length=30)
    voucher_date = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    r_status = models.CharField(max_length=1)
    voh_id = models.DecimalField(max_digits=14, decimal_places=0)
    branch_id = models.DecimalField(max_digits=14, decimal_places=0)
    booked_date = models.CharField(max_length=10)
    from_bank_id = models.DecimalField(max_digits=4, decimal_places=0)
    from_brach_id = models.DecimalField(max_digits=4, decimal_places=0)
    from_account_no = models.CharField(max_length=30)
    remarks = models.CharField(max_length=4000)


class Stb_Contributor_Sal_Det(models.Model):
    p_ssid = models.CharField(max_length=15)
    basic_sal = models.DecimalField(max_digits=14, decimal_places=2)
    grade = models.DecimalField(max_digits=10, decimal_places=2)
    from_date = models.CharField(max_length=10)
    to_date = models.CharField(max_length=10)
    entry_by = models.CharField(max_length=10)
    entry_date = models.DateField()
    r_status = models.CharField(max_length=1)
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    tran_no = models.DecimalField(max_digits=14, decimal_places=0)  # FK
    employer_id = models.DecimalField(max_digits=14, decimal_places=0)  # FK
    coll_year = models.DecimalField(max_digits=4, decimal_places=0)
    coll_month = models.DecimalField(max_digits=2, decimal_places=0)
    remarks = models.CharField(max_length=1000)
    is_regular = models.CharField(max_length=1)


class Stb_Collection_Tran_Head(models.Model):
    employer_id = models.DecimalField(
        max_digits=14, decimal_places=0)  # PFK, IX1, IX2
    tran_no = models.DecimalField(
        max_digits=14, decimal_places=0, primary_key=True)  # PK, IX2
    tran_date = models.CharField(max_length=10)
    total_amount = models.DecimalField(max_digits=15, decimal_places=2)
    int_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pena_amount = models.DecimalField(max_digits=10, decimal_places=2)
    entry_by = models.CharField(max_length=30)  # FK
    entry_date = models.DateField()
    r_status = models.CharField(max_length=1)
    cont_from_date = models.CharField(max_length=10)
    cont_to_date = models.CharField(max_length=10)
    t_no = models.DecimalField(max_digits=14, decimal_places=0)
    coll_year = models.DecimalField(max_digits=4, decimal_places=0)  # IX1
    coll_month = models.DecimalField(max_digits=2, decimal_places=0)  # FK IX1
    duepenalty_amount = models.DecimalField(max_digits=10, decimal_places=0)
    calendar = models.CharField(max_length=1)
    regularity_status = models.CharField(max_length=8)


class Stb_Coll_Tran_Details(models.Model):
    p_ssid = models.CharField(max_length=15)  # PFK IX1
    employer_id = models.DecimalField(
        max_digits=14, decimal_places=0)  # PFK IX1
    c_from_date = models.CharField(max_length=10)  # PFK IX1
    from_date = models.CharField(max_length=10)  # PFK IX1
    schapp_id = models.CharField(max_length=14)  # PFK IX1
    tran_no = models.CharField(max_length=14)  # PFK IX1
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    entry_by = models.CharField(max_length=30)  # FK
    entry_date = models.DateField()
    r_status = models.CharField(max_length=1)
    cont_from_date = models.CharField(max_length=10)
    cont_to_date = models.CharField(max_length=10)
    coll_year = models.DecimalField(max_digits=4, decimal_places=0)
    coll_month = models.DecimalField(max_digits=2, decimal_places=0)


class Stb_Scheme_Application(models.Model):
    schapp_desc = models.CharField(max_length=200)
    schapp_desc_eng = models.CharField(max_length=200)
    status = models.CharField(max_length=1)
    scheme_percent = models.DecimalField(max_digits=5, decimal_places=0)
    order_no = models.DecimalField(max_digits=2, decimal_places=0)
    gl_code = models.DecimalField(max_digits=8, decimal_places=0)
    p_gl_code = models.DecimalField(max_digits=8, decimal_places=0)
    used_by = models.CharField(max_length=24)
    coll_type = models.CharField(max_length=1)
    parent_schapp_id = models.DecimalField(max_digits=3, decimal_places=0)
    calculation_by_percentage = models.CharField(max_length=8)
    amount_type = models.CharField(max_length=8)
    claim_type = models.CharField(max_length=5)
