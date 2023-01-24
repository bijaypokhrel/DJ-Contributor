from django.db import models


class Stb_Claim_Head(models.Model):
    ssfid = models.CharField(
        max_length=15, primary_key=True, db_column="SSFID")  # PK, IX3
    schapp_id = models.DecimalField(
        max_digits=3, decimal_places=0, db_column="SCHAPP_ID")  # PK, IX3
    sch_id = models.DecimalField(
        max_digits=4, decimal_places=0, db_column="SCH_ID")  # PK, IX3
    claim_app_date = models.CharField(
        max_length=50, db_column="CLAIM_APP_DATE")  # PK, IX3
    anusuchi_no = models.DecimalField(
        max_digits=3, decimal_places=0, db_column="ANUSUCHI_NO")
    bank_id = models.DecimalField(
        max_digits=5, decimal_places=0, db_column="BANK_ID")
    account_type = models.CharField(max_length=50, db_column="ACCOUNT_TYPE")
    account_number = models.CharField(
        max_length=30, db_column="ACCOUNT_NUMBER")
    bank_address = models.CharField(max_length=100, db_column="BANK_ADDRESS")
    recommend_by = models.CharField(max_length=100, db_column="RECOMMEND_BY")
    recomm_emp_post = models.CharField(
        max_length=100, db_column="RECOMM_EMP_POST")
    recomm_emp_phone = models.CharField(
        max_length=20, db_column="RECOMM_EMP_PHONE")
    recommend_date = models.CharField(
        max_length=20, db_column="RECOMMEND_DATE")
    entry_by = models.CharField(max_length=10, db_column="ENTRY_BY")
    entry_date = models.DateField(db_column="ENTRY_DATE")
    r_status = models.CharField(max_length=1, db_column="R_STATUS")
    tran_no = models.DecimalField(
        max_digits=14, decimal_places=0, db_column="TRAN_NO")  # PK IX3
    approved_amount = models.DecimalField(
        max_digits=16, decimal_places=4, db_column="APPROVED_AMOUNT")
    approved_by = models.CharField(max_length=100, db_column="APPROVED_BY")
    approved_post = models.CharField(max_length=100, db_column="APPROVED_POST")
    approved_date = models.CharField(max_length=10, db_column="APPROVED_DATE")
    is_death = models.CharField(max_length=1, db_column="IS_DEATH")
    claim_amount = models.DecimalField(
        max_digits=16, decimal_places=4, db_column="CLAIM_AMOUNT")
    employer_id = models.DecimalField(
        max_digits=14, decimal_places=0, db_column="EMPLOYER_ID")
    approval_doc = models.FileField(
        upload_to='uploads/', db_column="APPROVAL_DOC")  # IX1
    remarks = models.CharField(max_length=1000, db_column="REMARKS")
    p_id = models.CharField(max_length=1, db_column="P_ID")
    h_code = models.CharField(max_length=20, db_column="H_CODE")
    claim_date = models.CharField(max_length=10, db_column="CLAIM_DATE")
    claim_id = models.CharField(max_length=30, db_column="CLAIM_ID")
    leave_from_date = models.CharField(
        max_length=10, db_column="LEAVE_FROM_DATE")
    leave_to_date = models.CharField(max_length=10, db_column="LEAVE_TO_DATE")
    bank_branch_id = models.DecimalField(
        max_digits=5, decimal_places=0, db_column="BANK_BRANCH_ID")
    account_name = models.CharField(max_length=200, db_column="ACCOUNT_NAME")
    save_mode = models.CharField(max_length=8, db_column="SAVE_MODE")
    is_admin_recommended = models.CharField(
        max_length=1, db_column="IS_ADMIN_RECOMMEND")
    admin_recommender = models.CharField(
        max_length=50, db_column="ADMIN_RECOMMENDER")
    admin_recommend_date = models.CharField(
        max_length=10, db_column="ADMIN_RECOMMEND_DATE")
    is_payment_rejected = models.CharField(
        max_length=1, db_column="IS_PAYMENT_REJECTED")
    payment_rejecter = models.CharField(
        max_length=50, db_column="PAYMENT_REJECTER")
    payment_rejected_date = models.CharField(
        max_length=10, db_column="PAYMENT_REJECTED_DATE")
    payment_reject_remarks = models.CharField(
        max_length=1000, db_column="PAYMENT_REJECT_REMARKS")
    admin_recommender_post = models.CharField(
        max_length=100, db_column="ADMIN_RECOMMENDER_POST")
    entry_by_post = models.CharField(max_length=100, db_column="ENTRY_BY_POST")
    ref_no = models.CharField(max_length=25, db_column="REF_NO")
    payee_id = models.DecimalField(
        max_digits=3, decimal_places=0, db_column="PAYEE_ID")
    tax_amount = models.DecimalField(
        max_digits=16, decimal_places=4, db_column="TAX_AMOUNT")
    return_amount = models.DecimalField(
        max_digits=16, decimal_places=4, db_column="RETURN_AMOUNT")
    person_id = models.DecimalField(
        max_digits=14, decimal_places=4, db_column="PERSON_ID")  # PK IX3


class Stb_Claim_Anusuchi6(models.Model):
    p_ssid = models.CharField(
        max_length=15, primary_key=True, db_column="P_SSID")  # PKF, IX1
    sch_id = models.DecimalField(
        max_digits=4, decimal_places=0, db_column="SCH_ID")  # PKF, IX1
    schapp_id = models.DecimalField(
        max_digits=4, decimal_places=0, db_column="SCHAPP_ID")  # PKF, IX1
    permanent_disability_type = models.CharField(
        max_length=250, db_column="PERMANENT_DISABILITY_TYPE")
    permanent_disability_date = models.CharField(
        max_length=10, db_column="PERMANENT_DISABILITY_DATE")
    permanent_disability_reason = models.CharField(
        max_length=10, db_column="PERMANENT_DISABILITY_REASON")
    death_date = models.CharField(max_length=10, db_column="DEATH_DATE")
    death_reason = models.CharField(max_length=250, db_column="DEATH_REASON")
    dep_person_relation = models.CharField(
        max_length=50, db_column="DEP_PERSON_RELATION")
    no_of_children_below_18 = models.DecimalField(
        max_digits=2, decimal_places=0, db_column="NO_OF_CHILDREN_BELOW_18")
    approved_amount = models.DecimalField(
        max_digits=14, decimal_places=2, db_column="APPROVED_AMOUNT")
    amount_received_by = models.CharField(
        max_length=1000, db_column="AMOUNT_RECEIVED_BY")
    r_status = models.CharField(max_length=1, db_column="R_STATUS")
    entry_by = models.CharField(max_length=10, db_column="ENTRY_BY")
    entry_date = models.DateField(db_column="ENTRY_DATE")
    tran_no = models.DecimalField(
        max_digits=14, decimal_places=0, db_column="TRAN_NO")  # PFK IX1
    claim_app_date = models.CharField(
        max_length=10, db_column="CLAIM_APP_DATE")  # PFK IX1
    dep_fname = models.CharField(max_length=50, db_column="DEP_FNAME")
    dep_mname = models.CharField(max_length=50, db_column="DEP_MNAME")
    dep_lname = models.CharField(max_length=50, db_column="DEP_LNAME")
    average_basic = models.DecimalField(
        max_digits=14, decimal_places=2, db_column="AVERAGE_BASIC")
    remarks = models.CharField(max_length=4000, db_column="REMARKS")
    person_id = models.DecimalField(
        max_digits=14, decimal_places=0, db_column="PERSON_ID")  # PFK IX1


class Stb_Claim_App_Amount(models.Model):
    tran_no = models.DecimalField(
        max_digits=14, decimal_places=0, db_column="TRAN_NO")
    sch_app_id = models.DecimalField(
        max_digits=3, decimal_places=0, primary_key=True, db_column="SCH_APP_ID")  # PK IX1
    sch_id = models.DecimalField(
        max_digits=4, decimal_places=0, db_column="SCH_ID")  # PK IX1
    p_ssid = models.CharField(max_length=14, db_column="P_SSID")  # PK IX1
    claim_amount = models.DecimalField(
        max_digits=10, decimal_places=0, db_column="CLAIM_AMOUNT")
    claim_app_date = models.CharField(
        max_length=14, db_column="CLAIM_APP_DATE")  # PK IX1
    person_id = models.DecimalField(
        max_digits=14, decimal_places=0, db_column="PERSON_ID")  # PK IX1


class Stb_Claim_Doc(models.Model):
    ssfid = models.CharField(
        max_length=15, primary_key=True, db_column="SSFID")  # PK, IX1
    schapp_id = models.DecimalField(
        max_digits=3, decimal_places=0, db_column="SCHAPP_ID")
    sch_id = models.DecimalField(
        max_digits=4, decimal_places=0, db_column="SCH_ID")
    claim_app_date = models.CharField(
        max_length=10, db_column="CLAIM_APP_DATE")
    chk_doc_id = models.DecimalField(
        max_digits=3, decimal_places=0, db_column="CHK_DOC_ID")  # PK, IX1
    doc_path = models.CharField(max_length=250, db_column="DOC_PATH")
    doc_image = models.ImageField(
        upload_to='images/', db_column="DOC_IMAGE")  # IX2
    entry_by = models.CharField(max_length=10, db_column="ENTRY_BY")
    entry_date = models.DateField(db_column="ENTRY_DATE")
    r_status = models.CharField(max_length=1, db_column="R_STATUS")
    tran_no = models.DecimalField(
        max_digits=14, decimal_places=0, db_column="TRAN_NO")  # PK IX1
