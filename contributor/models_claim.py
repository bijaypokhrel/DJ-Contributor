from django.db import models


class Stb_Claim_Head(models.Model):
    ssfid = models.CharField(max_length=15, primary_key=True)  # PK, IX3
    schapp_id = models.DecimalField(max_digits=3, decimal_places=0)  # PK, IX3
    sch_id = models.DecimalField(max_digits=4, decimal_places=0)  # PK, IX3
    claim_app_date = models.CharField(max_length=50)  # PK, IX3
    anusuchi_no = models.DecimalField(max_digits=3, decimal_places=0)
    bank_id = models.DecimalField(max_digits=5, decimal_places=0)
    account_type = models.CharField(max_length=50)
    account_number = models.CharField(max_length=30)
    bank_address = models.CharField(max_length=100)
    recommend_by = models.CharField(max_length=100)
    recomm_emp_post = models.CharField(max_length=100)
    recomm_emp_phone = models.CharField(max_length=20)
    recommend_date = models.CharField(max_length=20)
    entry_by = models.CharField(max_length=10)
    entry_date = models.DateField()
    r_status = models.CharField(max_length=1)
    tran_no = models.DecimalField(max_digits=14, decimal_places=0)  # PK IX3
    approved_amount = models.DecimalField(max_digits=16, decimal_places=4)
    approved_by = models.CharField(max_length=100)
    approved_post = models.CharField(max_length=100)
    approved_date = models.CharField(max_length=10)
    is_death = models.CharField(max_length=1)
    claim_amount = models.DecimalField(max_digits=16, decimal_places=4)
    employer_id = models.DecimalField(max_digits=14, decimal_places=0)
    approval_doc = models.FileField(upload_to='uploads/')  # IX1
    remarks = models.CharField(max_length=1000)
    p_id = models.CharField(max_length=1)
    h_code = models.CharField(max_length=20)
    claim_date = models.CharField(max_length=10)
    claim_id = models.CharField(max_length=30)
    leave_from_date = models.CharField(max_length=10)
    leave_to_date = models.CharField(max_length=10)
    bank_branch_id = models.DecimalField(max_digits=5, decimal_places=0)
    account_name = models.CharField(max_length=200)
    save_mode = models.CharField(max_length=8)
    is_admin_recommended = models.CharField(max_length=1)
    admin_recommender = models.CharField(max_length=50)
    admin_recommend_date = models.CharField(max_length=10)
    is_payment_rejected = models.CharField(max_length=1)
    payment_rejecter = models.CharField(max_length=50)
    payment_rejected_date = models.CharField(max_length=10)
    payment_reject_remarks = models.CharField(max_length=1000)
    admin_recommender_post = models.CharField(max_length=100)
    entry_by_post = models.CharField(max_length=100)
    ref_no = models.CharField(max_length=25)
    ref_no = models.CharField(max_length=25)
    payee_id = models.DecimalField(max_digits=3, decimal_places=0)
    tax_amount = models.DecimalField(max_digits=16, decimal_places=4)
    return_amount = models.DecimalField(max_digits=16, decimal_places=4)
    person_id = models.DecimalField(max_digits=14, decimal_places=4)  # PK IX3


class Stb_Claim_Anusuchi6(models.Model):
    p_ssid = models.CharField(max_length=15, primary_key=True)  # PKF, IX1
    sch_id = models.DecimalField(max_digits=4, decimal_places=0)  # PKF, IX1
    schapp_id = models.DecimalField(max_digits=4, decimal_places=0)  # PKF, IX1
    permanent_disability_type = models.CharField(max_length=250)
    permanent_disability_date = models.CharField(max_length=10)
    permanent_disability_reason = models.CharField(max_length=10)
    death_date = models.CharField(max_length=10)
    death_reason = models.CharField(max_length=250)
    dep_person_relation = models.CharField(max_length=50)
    no_of_children_below_18 = models.DecimalField(
        max_digits=2, decimal_places=0)
    approved_amount = models.DecimalField(max_digits=14, decimal_places=2)
    amount_received_by = models.CharField(max_length=1000)
    r_status = models.CharField(max_length=1)
    entry_by = models.CharField(max_length=10)
    entry_date = models.DateField()
    tran_no = models.DecimalField(max_digits=14, decimal_places=0)  # PFK IX1
    claim_app_date = models.CharField(max_length=10)  # PFK IX1
    dep_fname = models.CharField(max_length=50)
    dep_mname = models.CharField(max_length=50)
    dep_lname = models.CharField(max_length=50)
    average_basic = models.DecimalField(max_digits=14, decimal_places=2)
    remarks = models.CharField(max_length=4000)
    person_id = models.DecimalField(max_digits=14, decimal_places=0)  # PFK IX1


class Stb_Claim_App_Amount(models.Model):
    tran_no = models.DecimalField(max_digits=14, decimal_places=0)
    sch_app_id = models.DecimalField(
        max_digits=3, decimal_places=0, primary_key=True)  # PK IX1
    sch_id = models.DecimalField(max_digits=4, decimal_places=0)  # PK IX1
    p_ssid = models.CharField(max_length=14)  # PK IX1
    claim_amount = models.DecimalField(max_digits=10, decimal_places=0)
    claim_app_date = models.CharField(max_length=14)  # PK IX1
    person_id = models.DecimalField(max_digits=14, decimal_places=0)  # PK IX1


class Stb_Claim_Doc(models.Model):
    ssfid = models.CharField(max_length=15, primary_key=True)  # PK, IX1
    schapp_id = models.DecimalField(max_digits=3, decimal_places=0)
    sch_id = models.DecimalField(max_digits=4, decimal_places=0)
    claim_app_date = models.CharField(max_length=10)
    chk_doc_id = models.DecimalField(
        max_digits=3, decimal_places=0)  # PK, IX1
    doc_path = models.CharField(max_length=250)
    doc_image = models.ImageField(upload_to='images/')  # IX2
    entry_by = models.CharField(max_length=10)
    entry_date = models.DateField()
    r_status = models.CharField(max_length=1)
    tran_no = models.DecimalField(max_digits=14, decimal_places=0)  # PK IX1
