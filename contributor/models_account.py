from django.db import models


class Atb_Gltran_Mast(models.Model):
    office_code = models.DecimalField(max_digits=4, decimal_places=0)  # FK
    vch_no = models.CharField(max_length=50)  # IX1
    vch_type_code = models.DecimalField(max_digits=4, decimal_places=0)  # FK
    cost_center_id = models.DecimalField(max_digits=4, decimal_places=0)
    tran_date = models.CharField(max_length=10)
    tran_user_id = models.CharField(max_length=30)
    is_approved = models.DecimalField(max_digits=4, decimal_places=0)
    approved_date = models.CharField(max_length=10)
    approved_user_id = models.CharField(max_length=30)
    is_reverse = models.DecimalField(max_digits=4, decimal_places=0)
    rev_vch_id = models.DecimalField(max_digits=4, decimal_places=0)  # FK
    vch_id = models.DecimalField(
        max_digits=4, decimal_places=0, primary_key=True)  # PK IX2
    tran_number = models.CharField(max_length=14)
    mast_desc = models.CharField(max_length=1000)
    application_id = models.CharField(max_length=20)  # FK
    module_id = models.CharField(max_length=30)  # FK
    value_date = models.CharField(max_length=10)
    is_deleted = models.DecimalField(max_digits=4, decimal_places=0)


class Atb_Gltran_Detl(models.Model):
    gltran_detl = models.DecimalField(
        max_digits=3, decimal_places=0, primary_key=True)  # PK IX1
    office_code = models.DecimalField(max_digits=4, decimal_places=0)  # FK
    gl_group_code = models.DecimalField(max_digits=4, decimal_places=0)
    ac_no = models.CharField(max_length=100)
    gl_id = models.DecimalField(max_digits=4, decimal_places=0)  # FK
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    tran_desc = models.CharField(max_length=200)
    inst_code = models.CharField(max_length=100)
    inst_date = models.CharField(max_length=10)
    vch_id = models.DecimalField(max_digits=4, decimal_places=0)  # PFK IX1
    status = models.CharField(max_length=1)


class Atb_Account_Ledger(models.Model):
    office_code = models.DecimalField(
        max_digits=4, decimal_places=0, primary_key=True)  # PK, IX1
    gl_id = models.DecimalField(max_digits=10, decimal_places=0)  # PFK IX1 IX2
    value_date = models.CharField(max_length=10)  # PK IX1 IX2
    fiscal_year = models.CharField(max_length=10)  # PK IX1 IX2
    dr = models.DecimalField(max_digits=20, decimal_places=2)
    cr = models.DecimalField(max_digits=20, decimal_places=2)
    balance = models.DecimalField(max_digits=22, decimal_places=2)
