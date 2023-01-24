from django.db import models
from graphene_django import DjangoObjectType


# Create your models here.


class Ctb_Address(models.Model):
    address_id = models.BigAutoField(
        primary_key=True, db_column="ADDRESS_ID")  # PK, IX1
    district_cd = models.DecimalField(
        null=True, blank=True, max_digits=2, decimal_places=0, db_column="DISTRICT_ID")
    vdc_cd = models.DecimalField(
        null=True, blank=True, max_digits=10, decimal_places=0, db_column="VDC_CD")
    ward = models.DecimalField(
        null=True, blank=True, max_digits=2, decimal_places=0, db_column="WARD")
    tole_nep = models.CharField(
        null=True, blank=True, max_length=100, db_column="TOLE_NEP")
    tole_eng = models.CharField(
        null=True, blank=True, max_length=100, db_column="TOLE_ENG")
    house_number = models.CharField(
        null=True, blank=True, max_length=50, db_column="HOUSE_NUMBER")
    entry_by = models.CharField(
        null=True, blank=True, max_length=30, db_column="ENTRY_BY")
    entry_date = models.DateField(
        db_column="ENTRY_DATE", null=True, blank=True)
    r_status = models.CharField(
        null=True, blank=True, max_length=1, db_column="R_STATUS")
    tran_no = models.DecimalField(
        null=True, blank=True, max_digits=14, decimal_places=0, db_column="TRAN_NO")

    class Meta:
        verbose_name_plural = 'Ctb_Addresses'


class Ctb_Person(models.Model):
    # PK, IX2
    p_id = models.BigAutoField(primary_key=True, db_column='P_ID')
    fname_nep = models.CharField(
        null=True, blank=True, max_length=30, db_column="FNAME_NEP")
    mname_nep = models.CharField(
        null=True, blank=True, max_length=30, db_column="MNAME_NEP")
    lname_nep = models.CharField(
        null=True, blank=True, max_length=30, db_column="LNAME_NEP")
    fname_eng = models.CharField(
        null=True, blank=True, max_length=30, db_column="FNAME_ENG")
    mname_eng = models.CharField(
        null=True, blank=True, max_length=30, db_column="MNAME_ENG")
    lname_eng = models.CharField(
        null=True, blank=True, max_length=30, db_column="LNAME_ENG")
    dob = models.CharField(null=True, blank=True,
                           max_length=10, db_column="DOB")
    gender = models.CharField(null=True, blank=True,
                              max_length=2,  db_column="GENDER")
    ds_agency_id = models.DecimalField(
        null=True, blank=True, max_digits=3, decimal_places=0, db_column="DS_AGENCY_ID")  # FK
    ds_id_number = models.CharField(
        null=True, blank=True, max_length=20, db_column="DS_ID_NUMBER")
    p_ssid = models.CharField(
        null=True, blank=True, max_length=15, db_column="P_SSID")  # AK1, IX3
    not_understood = models.CharField(
        null=True, blank=True, max_length=2, db_column="NOT_UNDERSTOOD")  # FK
    rel_id = models.DecimalField(
        null=True, blank=True, max_digits=3, decimal_places=0, db_column="REL_ID")  # FK
    eth_id = models.DecimalField(
        null=True, blank=True, max_digits=3, decimal_places=0, db_column="ETH_ID")  # FK
    entry_by = models.CharField(
        null=True, blank=True, max_length=15, db_column="ENTRY_BY")
    entry_date = models.DateField(
        db_column="ENTRY_DATE", null=True, blank=True)
    r_status = models.CharField(
        null=True, blank=True, max_length=1, db_column="R_STATUS")
    tran_no = models.DecimalField(
        null=True, blank=True, max_digits=14, decimal_places=0, db_column="TRAN_NO")
    alert_source = models.CharField(
        null=True, blank=True, max_length=11, db_column="ALERT_SOURCE")
    alt_source_val = models.CharField(
        null=True, blank=True, max_length=100, db_column="ALERT_SOURCE_VAL")
    bloodgroup = models.CharField(
        null=True, blank=True, max_length=4, db_column="BLOODGROUP")
    image_file = models.ImageField(
        upload_to='images/', db_column="IMAGE_FILE", null=True, blank=True)  # IX1
    seq_no = models.DecimalField(
        null=True, blank=True, max_digits=5, decimal_places=0, db_column="SEQ_NO")
    is_disable = models.CharField(
        null=True, blank=True, max_length=1, db_column="IS_DISABLE")
    reaction = models.CharField(
        null=True, blank=True, max_length=1, db_column="REACTION")
    disability_percent = models.DecimalField(
        null=True, blank=True, max_digits=3, decimal_places=0, db_column="DISABILITY_PERCENT")
    bank_id = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=0, db_column="BANK_ID")
    branch_id = models.DecimalField(
        null=True, blank=True, max_digits=4, decimal_places=0, db_column="BRANCH_ID")
    bank_ac_name = models.CharField(
        null=True, blank=True, max_length=100, db_column="BANK_AC_NAME")
    bank_ac_type = models.CharField(
        null=True, blank=True, max_length=50, db_column="BANK_AC_TYPE")
    bank_ac_number = models.CharField(
        null=True, blank=True, max_length=50,  db_column="BANK_AC_NUMBER")
    grand_father_name = models.CharField(
        null=True, blank=True, max_length=100, db_column="GRAND_FATHER_NAME")
    father_name = models.CharField(
        null=True, blank=True, max_length=100, db_column="FATHER_NAME")
    mobile_no = models.CharField(
        null=True, blank=True, max_length=50, db_column="MOBILE_NO")
    parent_pssid = models.CharField(
        null=True, blank=True, max_length=10, db_column="PARENT_PSSID")


class Ctb_Person_Address(models.Model):
    p_id = models.DecimalField(
        null=True, blank=True, max_digits=14, decimal_places=0, db_column="P_ID")  # PFK, IX1
    adtype_id = models.DecimalField(
        null=True, blank=True, max_digits=3, decimal_places=0, db_column="ADT_TYPE")  # PFK, IX1
    address_id = models.DecimalField(
        null=True, blank=True, max_digits=10, decimal_places=0, db_column="ADDRESS_ID")  # PFK, IX1
    from_date = models.CharField(
        max_length=10, db_column="FROM_DATE", null=True, blank=True)  # PK, IX1
    to_date = models.CharField(
        null=True, blank=True, max_length=10, db_column="TO_DATE")
    entry_by = models.CharField(
        null=True, blank=True, max_length=30, db_column="ENTRY_BY")
    entry_date = models.DateField(
        db_column="ENTRY_DATE", null=True, blank=True)
    r_status = models.CharField(
        null=True, blank=True, max_length=1, db_column="R_STATUS")
    tran_no = models.DecimalField(
        null=True, blank=True, max_digits=14, decimal_places=0, db_column="TRAN_NO")
    reaction = models.CharField(
        null=True, blank=True, max_length=1, db_column="REACTION")

    class Meta:
        verbose_name_plural = 'Ctb_Person_Addresses'


class Ctb_Person_Dependent(models.Model):
    p_id = models.DecimalField(
        null=True, blank=True, max_digits=14, decimal_places=0, db_column="P_ID")  # PFK, IX1
    reltype_id = models.DecimalField(
        null=True, blank=True, max_digits=3, decimal_places=0, db_column="RELTYPE_ID")  # PFK, IX1
    relative_id = models.DecimalField(
        null=True, blank=True, max_digits=14, decimal_places=0, db_column="RELATIVE_ID")  # FK
    entry_by = models.CharField(
        null=True, blank=True, max_length=30, db_column="ENTRY_BY")
    entry_date = models.DateField(
        name=False, db_column="ENTRY_DATE", null=True, blank=True)
    r_status = models.CharField(
        null=True, blank=True, max_length=1, db_column="R_STATUS")
    tran_no = models.DecimalField(
        null=True, blank=True, max_digits=14, decimal_places=0, db_column="TRAN_NO")
    order_no = models.AutoField(
        primary_key=True, db_column="ORDER_NO")  # PK, IX1


class Ctb_Person_Nominee(models.Model):
    p_id = models.DecimalField(
        null=True, blank=True, max_digits=14, decimal_places=0, db_column="P_ID")  # PFK, IX1
    reltype_id = models.DecimalField(
        null=True, blank=True, max_digits=3, decimal_places=0, db_column="RELTYPE_ID")  # PFK, IX1
    relative_id = models.DecimalField(
        null=True, blank=True, max_digits=14, decimal_places=0, db_column="RELATIVE_ID")
    from_date = models.CharField(
        null=True, blank=True, max_length=10, db_column="FROM_DATE")
    to_date = models.CharField(
        null=True, blank=True, max_length=10, db_column="TO_DATE")
    entry_by = models.CharField(
        null=True, blank=True, max_length=30, db_column="ENTRY_BY")
    entry_date = models.DateField(
        db_column="ENTRY_DATE", null=True, blank=True)
    r_status = models.CharField(
        null=True, blank=True, max_length=1, db_column="R_STATS")
    tran_no = models.DecimalField(
        null=True, blank=True, max_digits=14, decimal_places=0, db_column="TRAN_NO")
    order_no = models.DecimalField(
        null=True, blank=True, max_digits=2, decimal_places=0, db_column="ORDER_NO")  # PFK, IX1


class Ctb_Person_Contact(models.Model):
    p_id = models.DecimalField(
        null=True, blank=True, max_digits=14, decimal_places=0, db_column="P_ID")  # PFK, IX1
    ctype_id = models.DecimalField(
        null=True, blank=True, max_digits=3, decimal_places=0, db_column="CTYPE_ID")  # PFK, IX1
    from_date = models.CharField(
        max_length=10, db_column="FROM_DATE", null=True, blank=True)  # PK, IX1
    c_value = models.CharField(
        null=True, blank=True, max_length=100, db_column="C_VALUE")
    to_date = models.CharField(
        null=True, blank=True, max_length=10, db_column="TO_DATE")
    entry_by = models.CharField(
        null=True, blank=True, max_length=30, db_column="ENTRY_BY")
    entry_date = models.DateField(
        db_column="ENTRY_DATE", null=True, blank=True)
    r_status = models.CharField(
        null=True, blank=True, max_length=1, db_column="R_STATUS")
    tran_no = models.DecimalField(
        null=True, blank=True, max_digits=14, decimal_places=0, db_column="TRAN_NO")


class Ctb_Person_Doc(models.Model):
    p_id = models.DecimalField(
        null=True, blank=True, max_digits=14, decimal_places=0, db_column="P_ID")  # PFK, IX1
    doc_id = models.DecimalField(
        null=True, blank=True, max_digits=3, decimal_places=0, db_column="DOC_ID")  # PFK, IX1
    from_date = models.CharField(
        max_length=10, db_column="FROM_DATE", null=True, blank=True)  # PK, IX1
    to_date = models.CharField(
        null=True, blank=True, max_length=10, db_column="TO_DATE")
    issue_no = models.CharField(
        null=True, blank=True, max_length=60, db_column="ISSUE_NO")
    issue_date = models.CharField(
        null=True, blank=True, max_length=11, db_column="ISSUE_DATE")
    issue_place = models.CharField(
        null=True, blank=True, max_length=100, db_column="ISSUE_PLACE")
    entry_by = models.CharField(
        null=True, blank=True, max_length=30, db_column="ENTRY_BY")
    entry_date = models.DateField(
        db_column="ENTRY_DATE", null=True, blank=True)
    r_status = models.CharField(
        null=True, blank=True, max_length=1, db_column="R_STATUS")
    tran_no = models.DecimalField(
        null=True, blank=True, max_digits=14, decimal_places=0, db_column="TRAN_NO")
    docfile = models.FileField(
        upload_to='uploads/', db_column="DOCFILE", null=True, blank=True)  # IX2


class Ctb_Contributor(models.Model):
    p_ssid = models.CharField(
        null=True, blank=True, max_length=15, db_column="P_SSID")  # PFK, IX1
    employer_id = models.DecimalField(
        null=True, blank=True, max_digits=14, decimal_places=0, db_column="EMPLOYER_ID")  # PFK, IX1
    from_date = models.CharField(
        max_length=10, db_column="FROM_DATE", null=True, blank=True)  # PK, IX1
    to_date = models.CharField(
        null=True, blank=True, max_length=10, db_column="TO_DATE")
    post = models.CharField(null=True, blank=True,
                            max_length=300, db_column="POST")
    emptype_id = models.DecimalField(
        null=True, blank=True, max_digits=3, decimal_places=0, db_column="EMPTYPE_ID")  # FK
    joining_date = models.CharField(
        null=True, blank=True, max_length=11, db_column="JOINING_DATE")
    termination_date = models.CharField(
        null=True, blank=True, max_length=10, db_column="TERMINATION_DATE")
    termination_res = models.CharField(
        null=True, blank=True, max_length=300, db_column="TERMINATION_RES")
    entry_by = models.CharField(
        null=True, blank=True, max_length=30, db_column="ENTRY_BY")
    entry_date = models.DateField(
        db_column="ENTRY_DATE", null=True, blank=True)
    r_status = models.CharField(
        null=True, blank=True, max_length=1, db_column="R_STATUS")
    tran_no = models.DecimalField(
        null=True, blank=True, max_digits=14, decimal_places=0, db_column="TRAN_NO")
    terminated_by = models.CharField(
        null=True, blank=True, max_length=30, db_column="TERMINATED_BY")
    new_tran = models.DecimalField(
        null=True, blank=True, max_digits=14, decimal_places=0, db_column="NEW_TRAN")
    marking = models.CharField(
        null=True, blank=True, max_length=1, db_column="MARKING")
    group_id = models.DecimalField(
        null=True, blank=True, max_digits=3, decimal_places=0, db_column="GROUP_ID")  # FK
    contributor_type = models.CharField(
        null=True, blank=True, max_length=1, db_column="CONTRIBUTOR_TYPE")
