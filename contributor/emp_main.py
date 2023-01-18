from django.db import models


class Ctb_Emp_Contact(models.Model):
    employer_id = models.DecimalField(max_digits=14, decimal_places=0)
    adtype_id = models.DecimalField(max_digits=3, decimal_places=0)
    address_id = models.DecimalField(max_digits=10, decimal_places=0)
    a_from_date = models.CharField(max_length=10)
    ctype_id = models.DecimalField(max_digits=3, decimal_places=0)
    from_date = models.CharField(max_length=10, primary_key=True)
    c_value = models.CharField(max_length=100)
    to_date = models.CharField(max_length=10)
    entry_by = models.CharField(max_length=30)
    entry_date = models.DateField()
    r_status = models.CharField(max_length=1)
    tran_no = models.DecimalField(max_digits=14, decimal_places=0)

    def __str__(self):
        return self.name


class Ctb_Employer(models.Model):
    employer_id = models.BigAutoField(primary_key=True)
    employer_name_nep = models.CharField(
        max_length=150)
    employer_name_eng = models.CharField(max_length=150)
    # etype_id = FK LATER
    # stype_id = FK LATER
    e_ssid = models.CharField(max_length=25)
    entry_by = models.CharField(max_length=30)
    entry_date = models.DateField()
    r_status = models.CharField(max_length=1)
    tran_no = models.DecimalField(max_digits=14, decimal_places=0)
    alert_source = models.CharField(max_length=11)
    alt_source_val = models.CharField(max_length=100)
    short_menu = models.CharField(max_length=1)
    calendar = models.CharField(max_length=1)
    group_applied = models.CharField(max_length=1)

    def __str__(self):
        return self.name


class Ctb_Emp_Doc(models.Model):
    employer_id = models.DecimalField(max_digits=14, decimal_places=0)
    doc_id = models.DecimalField(max_digits=3, decimal_places=0)
    from_date = models.CharField(max_length=10, primary_key=True)
    to_date = models.CharField(max_length=10)
    issue_no = models.CharField(max_length=60)
    issue_date = models.CharField(max_length=10)
    issue_place = models.CharField(max_length=100)
    entry_by = models.CharField(max_length=30)
    entry_date = models.DateField()
    r_status = models.CharField(max_length=1)
    tran_no = models.DecimalField(max_digits=14, decimal_places=0)
    docfile = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name


# class Ctb_Address(models.Model):
#     address_id = models.BigAutoField(primary_key=True)
#     district_cd = models.DecimalField(max_digits=2, decimal_places=0)
#     vdc_cd = models.DecimalField(max_digits=10, decimal_places=0)
#     ward = models.DecimalField(max_digits=2, decimal_places=0)
#     tole_nep = models.CharField(max_length=100)
#     tole_eng = models.CharField(max_length=100)
#     house_number = models.CharField(max_length=50)
#     entry_by = models.CharField(max_length=30)
#     entry_date = models.DateField()
#     r_status = models.CharField(max_length=1)
#     tran_no = models.DecimalField(max_digits=14, decimal_places=0)

#     class Meta:
#         verbose_name_plural = 'Ctb_Addresses'

#     def __str__(self):
#         return self.name


class Ctb_Emp_Address(models.Model):
    employer_id = models.DecimalField(max_digits=14, decimal_places=0)
    adtype_id = models.DecimalField(max_digits=3, decimal_places=0)
    address_id = models.DecimalField(max_digits=10, decimal_places=0)
    from_date = models.CharField(
        max_length=10, primary_key=True)
    to_date = models.CharField(max_length=10)
    entry_by = models.CharField(max_length=30)
    entry_date = models.DateField()
    r_status = models.CharField(max_length=1)
    tran_no = models.DecimalField(max_digits=14, decimal_places=0)

    class Meta:
        verbose_name_plural = 'Ctb_Person_Addresses'

    def __str__(self):
        return self.name


class Ctb_Emp_Official(models.Model):
    employer_id = models.DecimalField(max_digits=14, decimal_places=0)
    e_id = models.DecimalField(max_digits=14, decimal_places=0)
    post_id = models.DecimalField(max_digits=10, decimal_places=0)
    from_date = models.CharField(
        max_length=10, primary_key=True)
    to_date = models.CharField(max_length=10)
    entry_by = models.CharField(max_length=30)
    entry_date = models.DateField()
    r_status = models.CharField(max_length=1)
    tran_no = models.DecimalField(max_digits=14, decimal_places=0)

    def __str__(self):
        return self.name
