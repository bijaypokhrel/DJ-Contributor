from django.db import models
from .emp_main import *
from .models_contributor import *
from .models_claim import *
from .models_loan import *
from .models_account import *

# Create your models here.


class Ctb_Address(models.Model):
    address_id = models.BigAutoField(primary_key=True)  # PK, IX1
    district_cd = models.DecimalField(max_digits=2, decimal_places=0)
    vdc_cd = models.DecimalField(max_digits=10, decimal_places=0)
    ward = models.DecimalField(max_digits=2, decimal_places=0)
    tole_nep = models.CharField(max_length=100)
    tole_eng = models.CharField(max_length=100)
    house_number = models.CharField(max_length=50)
    entry_by = models.CharField(max_length=30)
    entry_date = models.DateField()
    r_status = models.CharField(max_length=1)
    tran_no = models.DecimalField(max_digits=14, decimal_places=0)

    class Meta:
        verbose_name_plural = 'Ctb_Addresses'

    def __str__(self):
        return self.name


class Ctb_Person(models.Model):
    p_id = models.BigAutoField(primary_key=True)  # PK, IX2
    fname_nep = models.CharField(max_length=30)
    mname_nep = models.CharField(max_length=30)
    lname_nep = models.CharField(max_length=30)
    fname_eng = models.CharField(max_length=30)
    mname_eng = models.CharField(max_length=30)
    lname_eng = models.CharField(max_length=30)
    dob = models.CharField(max_length=10)
    gender = models.CharField(max_length=2)
    ds_agency_id = models.DecimalField(max_digits=3, decimal_places=0)  # FK
    ds_id_number = models.CharField(max_length=20)
    p_ssid = models.CharField(max_length=15)  # AK1, IX3
    not_understood = models.CharField(max_length=2)  # FK
    rel_id = models.DecimalField(max_digits=3, decimal_places=0)  # FK
    eth_id = models.DecimalField(max_digits=3, decimal_places=0)  # FK
    entry_by = models.CharField(max_length=15)
    entry_date = models.DateField()
    r_status = models.CharField(max_length=1)
    trans_no = models.DecimalField(max_digits=14, decimal_places=0)
    alert_source = models.CharField(max_length=11)
    alt_source_val = models.CharField(max_length=100)
    bloodgroup = models.CharField(max_length=4)
    image_file = models.ImageField(upload_to='images/')  # IX1
    seq_no = models.DecimalField(max_digits=5, decimal_places=0)
    is_disable = models.CharField(max_length=1)
    reaction = models.CharField(max_length=1)
    disability_percent = models.DecimalField(max_digits=3, decimal_places=0)
    bank_id = models.DecimalField(max_digits=4, decimal_places=0)
    branch_id = models.DecimalField(max_digits=4, decimal_places=0)
    bank_ac_name = models.CharField(max_length=100)
    bank_ac_type = models.CharField(max_length=50)
    bank_ac_number = models.CharField(max_length=50)
    grand_father_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=50)
    parent_pssid = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Ctb_Person_Address(models.Model):
    p_id = models.DecimalField(max_digits=14, decimal_places=0)  # PFK, IX1
    adtype_id = models.DecimalField(max_digits=3, decimal_places=0)  # PFK, IX1
    address_id = models.DecimalField(
        max_digits=10, decimal_places=0)  # PFK, IX1
    from_date = models.CharField(max_length=10, primary_key=True)  # PK, IX1
    to_date = models.CharField(max_length=10)
    entry_by = models.CharField(max_length=30)
    entry_date = models.DateField()
    r_status = models.CharField(max_length=1)
    tran_no = models.DecimalField(max_digits=14, decimal_places=0)
    reaction = models.CharField(max_length=1)

    class Meta:
        verbose_name_plural = 'Ctb_Person_Addresses'

    def __str__(self):
        return self.name


class Ctb_Person_Dependent(models.Model):
    p_id = models.DecimalField(max_digits=14, decimal_places=0)  # PFK, IX1
    reltype_id = models.DecimalField(
        max_digits=3, decimal_places=0)  # PFK, IX1
    relative_id = models.DecimalField(max_digits=14, decimal_places=0)  # FK
    entry_by = models.CharField(max_length=30)
    entry_date = models.DateField(name=False)
    r_status = models.CharField(max_length=1)
    tran_no = models.DecimalField(max_digits=14, decimal_places=0)
    order_no = models.AutoField(primary_key=True)  # PK, IX1

    def __str__(self):
        return self.name


class Ctb_Person_Nominee(models.Model):
    p_id = models.DecimalField(max_digits=14, decimal_places=0)  # PFK, IX1
    reltype_id = models.DecimalField(
        max_digits=3, decimal_places=0)  # PFK, IX1
    relative_id = models.DecimalField(max_digits=14, decimal_places=0)
    from_date = models.CharField(max_length=10)
    to_date = models.CharField(max_length=10)
    entry_by = models.CharField(max_length=30)
    entry_date = models.DateField()
    r_status = models.CharField(max_length=1)
    tran_no = models.DecimalField(max_digits=14, decimal_places=0)
    order_no = models.DecimalField(max_digits=2, decimal_places=0)  # PFK, IX1

    def __str__(self):
        return self.name


class Ctb_Person_Contact(models.Model):
    p_id = models.DecimalField(max_digits=14, decimal_places=0)  # PFK, IX1
    ctype_id = models.DecimalField(max_digits=3, decimal_places=0)  # PFK, IX1
    from_date = models.CharField(max_length=10, primary_key=True)  # PK, IX1
    c_value = models.CharField(max_length=100)
    to_date = models.CharField(max_length=10)
    entry_by = models.CharField(max_length=30)
    entry_date = models.DateField()
    r_status = models.CharField(max_length=1)
    tran_no = models.DecimalField(max_digits=14, decimal_places=0)

    def __str__(self):
        return self.name


class Ctb_Person_Doc(models.Model):
    p_id = models.DecimalField(max_digits=14, decimal_places=0)  # PFK, IX1
    doc_id = models.DecimalField(max_digits=3, decimal_places=0)  # PFK, IX1
    from_date = models.CharField(
        max_length=10, primary_key=True)  # PK, IX1
    to_date = models.CharField(max_length=10)
    issue_no = models.CharField(max_length=60)
    issue_date = models.CharField(max_length=11)
    issue_place = models.CharField(max_length=100)
    entry_by = models.CharField(max_length=30)
    entry_date = models.DateField()
    r_status = models.CharField(max_length=1)
    tran_no = models.DecimalField(max_digits=14, decimal_places=0)
    docfile = models.FileField(upload_to='uploads/')  # IX2

    def __str__(self):
        return self.name


class Ctb_Contributor(models.Model):
    p_ssid = models.CharField(max_length=15)  # PFK, IX1
    employer_id = models.DecimalField(
        max_digits=14, decimal_places=0)  # PFK, IX1
    from_date = models.CharField(
        max_length=10, primary_key=True)  # PK, IX1
    to_date = models.CharField(max_length=10)
    post = models.CharField(max_length=300)
    emptype_id = models.DecimalField(max_digits=3, decimal_places=0)  # FK
    joining_date = models.CharField(max_length=11)
    termination_date = models.CharField(max_length=10)
    termination_res = models.CharField(max_length=300)
    entry_by = models.CharField(max_length=30)
    entry_date = models.DateField()
    r_status = models.CharField(max_length=1)
    tran_no = models.DecimalField(max_digits=14, decimal_places=0)
    terminated_by = models.CharField(max_length=30)
    new_tran = models.DecimalField(max_digits=14, decimal_places=0)
    marking = models.CharField(max_length=1)
    group_id = models.DecimalField(max_digits=3, decimal_places=0)  # FK
    contributor_type = models.CharField(max_length=1)

    def __str__(self):
        return self.name
