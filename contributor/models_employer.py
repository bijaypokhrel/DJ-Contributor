from django.db import models


class Ctb_Emp_Contact(models.Model):
    employer_id = models.DecimalField(
        null=True, blank=True, max_digits=14, decimal_places=0, db_column="EMPLOYER_ID")  # PFK, IX1
    adtype_id = models.DecimalField(
        null=True, blank=True, max_digits=3, decimal_places=0, db_column="ADTYPE_ID")  # PFK, IX1
    address_id = models.DecimalField(
        null=True, blank=True, max_digits=10, decimal_places=0, db_column="ADDRESS_ID")  # PFK, IX1
    a_from_date = models.CharField(
        null=True, blank=True, max_length=10, db_column="A_FROM_DATE")  # PFK, IX1
    ctype_id = models.DecimalField(
        null=True, blank=True, max_digits=3, decimal_places=0, db_column="CTYPE_ID")  # PFK, IX1
    from_date = models.CharField(
        null=True, blank=True, max_length=10, db_column="FROM_DATE")  # PK, IX1
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


class Ctb_Employer(models.Model):
    employer_id = models.BigAutoField(
        primary_key=True, db_column="EMPLOYER_ID")  # PK, IX1
    employer_name_nep = models.CharField(
        null=True, blank=True, max_length=150, db_column="EMPLOYER_NAME_NEP")
    employer_name_eng = models.CharField(
        null=True, blank=True, max_length=150, db_column="EMPLOYER_NAME_ENG")
    etype_id = models.DecimalField(
        null=True, blank=True, max_digits=3, decimal_places=0, db_column="ETYPE_ID")  # FK
    stype_id = models.DecimalField(
        null=True, blank=True, max_digits=3, decimal_places=0, db_column="STYPE_ID")  # FK
    e_ssid = models.CharField(null=True, blank=True,
                              max_length=25, db_column="E_SSID")
    entry_by = models.CharField(
        null=True, blank=True, max_length=30, db_column="ENTRY_BY")
    entry_date = models.DateField(
        db_column="ENTRY_DATE", null=True, blank=True)
    r_status = models.CharField(
        null=True, blank=True, max_length=1, db_column="R_STATUS")
    tran_no = models.DecimalField(
        null=True, blank=True, max_digits=14, decimal_places=0, db_column="TRAN_NO")
    alert_source = models.CharField(
        null=True, blank=True, max_length=11, db_column="ALERT_SOURCE")
    alt_source_val = models.CharField(
        null=True, blank=True, max_length=100, db_column="ALT_SOURCE_VAL")
    short_menu = models.CharField(
        null=True, blank=True, max_length=1, db_column="SHORT_MENU")
    calendar = models.CharField(
        null=True, blank=True, max_length=1, db_column="CALENDAR")
    group_applied = models.CharField(
        null=True, blank=True, max_length=1, db_column="GROUP_APPLIED")


class Ctb_Emp_Doc(models.Model):
    employer_id = models.DecimalField(
        null=True, blank=True, max_digits=14, decimal_places=0, db_column="EMPLOYER_ID")  # PFK, IX1
    doc_id = models.DecimalField(
        null=True, blank=True, max_digits=3, decimal_places=0, db_column="DOC_ID")  # PK, AK1, IX1, IX2
    from_date = models.CharField(
        null=True, blank=True, max_length=10, db_column="FROM_DATE")  # PK, IX1
    to_date = models.CharField(
        null=True, blank=True, max_length=10, db_column="TO_DATE")
    issue_no = models.CharField(
        null=True, blank=True, max_length=60, db_column="ISSUE_NO")  # AK1, IX2
    issue_date = models.CharField(
        null=True, blank=True, max_length=10, db_column="ISSUE_DATE")
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
        upload_to='uploads/', db_column="DOCFILE")  # IX3


# class Ctb_Address(models.Model):
#     address_id = models.BigAutoField(primary_key=True)  # PK, IX1
#     district_cd = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0)
#     vdc_cd = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=0)
#     ward = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0)
#     tole_nep = models.CharField(null=True, blank=True, max_length=100)
#     tole_eng = models.CharField(null=True, blank=True, max_length=100)
#     house_number = models.CharField(null=True, blank=True, max_length=50)
#     entry_by = models.CharField(null=True, blank=True, max_length=30)
#     entry_date = models.DateField()
#     r_status = models.CharField(null=True, blank=True, max_length=1)
#     tran_no = models.DecimalField(null=True, blank=True, max_digits=14, decimal_places=0)

#     class Meta:
#         verbose_name_plural = 'Ctb_Addresses'

#     def __str__(self):
#         return self.name


class Ctb_Emp_Address(models.Model):
    employer_id = models.DecimalField(
        null=True, blank=True, max_digits=14, decimal_places=0, db_column="EMPLOYER_ID")  # PFK, IX1
    adtype_id = models.DecimalField(
        null=True, blank=True, max_digits=3, decimal_places=0, db_column="ADTYPE_ID")  # PFK, IX1
    address_id = models.DecimalField(
        null=True, blank=True, max_digits=10, decimal_places=0, db_column="ADDRESS_ID")  # PFK, IX1
    from_date = models.CharField(
        null=True, blank=True, max_length=10, db_column="FROM_DATE")  # PK, IX1
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

    class Meta:
        verbose_name_plural = 'Ctb_Emp_Addresses'


class Ctb_Emp_Official(models.Model):
    employer_id = models.DecimalField(
        null=True, blank=True, max_digits=14, decimal_places=0, db_column="EMPLOYER_ID")  # PFK, IX1
    e_id = models.DecimalField(
        null=True, blank=True, max_digits=14, decimal_places=0, db_column="E_ID")  # PFK, IX1
    post_id = models.DecimalField(
        null=True, blank=True, max_digits=10, decimal_places=0, db_column="POST_ID")
    from_date = models.CharField(
        null=True, blank=True, max_length=10, db_column="FROM_DATE")
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
