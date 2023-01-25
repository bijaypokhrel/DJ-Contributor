from django.db import models


class Atb_Gltran_Mast(models.Model):
    office_code = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=0, db_column="OFFICE_CODE")  # FK
    vch_no = models.CharField(null=True, blank=True,
                              max_length=50, db_column="VCH_NO")  # IX1
    vch_type_code = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=0, db_column="VCH_TYPE_CODE")  # FK
    cost_center_id = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=0, db_column="COST_CENTER_ID")
    tran_date = models.CharField(
        null=True, blank=True, max_length=10, db_column="TRAN_DATE")
    tran_user_id = models.CharField(
        null=True, blank=True, max_length=30, db_column="TRAN_USER_ID")
    is_approved = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=0, db_column="IS_APPROVED")
    approved_date = models.CharField(
        null=True, blank=True, max_length=10, db_column="APPROVED_DATE")
    approved_user_id = models.CharField(
        null=True, blank=True, max_length=30, db_column="APPROVED_USER_ID")
    is_reverse = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=0, db_column="IS_REVERSE")
    rev_vch_id = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=0, db_column="REV_VCH_ID")  # FK
    vch_id = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=0,  db_column="VCH_ID")  # PK IX2
    tran_number = models.CharField(
        null=True, blank=True, max_length=14, db_column="TRAN_NUMBER")
    mast_desc = models.CharField(
        null=True, blank=True, max_length=1000, db_column="MAST_DESC")
    application_id = models.CharField(
        null=True, blank=True, max_length=20, db_column="APPLICATION_ID")  # FK
    module_id = models.CharField(
        null=True, blank=True, max_length=30, db_column="MODULE_ID")  # FK
    value_date = models.CharField(
        null=True, blank=True, max_length=10, db_column="VALUE_DATE")
    is_deleted = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=0, db_column="IS_DELETED")


class Atb_Gltran_Detl(models.Model):
    gltran_detl = models.DecimalField(
        null=True, blank=True, max_digits=3, decimal_places=0,  db_column="GLTRAN_DETL")  # PK IX1
    office_code = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=0, db_column="OFFICE_CODE")  # FK
    gl_group_code = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=0, db_column="GL_GROUP_CODE")
    ac_no = models.CharField(null=True, blank=True,
                             max_length=100, db_column="AC_NO")
    gl_id = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=0, db_column="GL_ID")  # FK
    amount = models.DecimalField(
        null=True, blank=True, max_digits=18, decimal_places=2, db_column="AMOUNT")
    tran_desc = models.CharField(
        null=True, blank=True, max_length=200, db_column="TRAN_DESC")
    inst_code = models.CharField(
        null=True, blank=True, max_length=100, db_column="INST_CODE")
    inst_date = models.CharField(
        null=True, blank=True, max_length=10, db_column="INST_DATE")
    vch_id = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=0, db_column="VCH_ID")  # PFK IX1
    status = models.CharField(null=True, blank=True,
                              max_length=1, db_column="STATUS")


class Atb_Account_Ledger(models.Model):
    office_code = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=0, db_column="OFFICE_CODE")  # PK, IX1
    gl_id = models.DecimalField(
        null=True, blank=True, max_digits=10, decimal_places=0, db_column="GL_ID")  # PFK IX1 IX2
    value_date = models.CharField(
        null=True, blank=True, max_length=10, db_column="VALUE_DATE")  # PK IX1 IX2
    fiscal_year = models.CharField(
        null=True, blank=True, max_length=10, db_column="FISCAL_YEAR")  # PK IX1 IX2
    dr = models.DecimalField(
        null=True, blank=True, max_digits=20, decimal_places=2, db_column="DR")
    cr = models.DecimalField(
        null=True, blank=True, max_digits=20, decimal_places=2, db_column="CR")
    balance = models.DecimalField(
        null=True, blank=True, max_digits=22, decimal_places=2, db_column="BALANCE")
