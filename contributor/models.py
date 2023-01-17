from django.db import models

# Create your models here.


class Ctb_Address(models.Model):
    address_id = models.BigAutoField(primary_key=True)
    district_cd = models.SmallIntegerField(null=False)
    vdc_cd = models.BigIntegerField(null=False)
    ward = models.SmallIntegerField(null=False)
    tole_nep = models.CharField(max_length=100, null=False, blank=False)
    tole_eng = models.CharField(max_length=100)
    house_number = models.CharField(max_length=50)
    entry_by = models.CharField(max_length=30, null=False, blank=False)
    entry_date = models.DateField(null=False, blank=False)
    r_status = models.CharField(max_length=1, null=False, blank=False)
    tran_no = models.DecimalField(max_digits=14, decimal_places=0)

    class Meta:
        verbose_name_plural = 'Ctb_Addresses'

    def __str__(self):
        return self.name


class Ctb_Person(models.Model):
    p_id = models.BigAutoField(primary_key=True)
    fname_nep = models.CharField(max_length=30, null=False, blank=False)
    mname_nep = models.CharField(max_length=30)
    lname_nep = models.CharField(max_length=30, null=False, blank=False)
    fname_eng = models.CharField(max_length=30)
    mname_eng = models.CharField(max_length=30)
    lname_eng = models.CharField(max_length=30)
    dob = models.CharField(max_length=10)
    gender = models.CharField(max_length=2)
    # ds_agency_id =  FK LATER
    ds_id_number = models.CharField(max_length=20)
    p_ssid = models.CharField(max_length=15)
    # not_understood = FK LATER
    # rel_id = FK Later
    # eth_id = FK Later
    entry_by = models.CharField(max_length=15, null=False, blank=False)
    entry_date = models.DateField(null=False, blank=False)
    r_status = models.CharField(max_length=1, null=False, blank=False)
    trans_no = models.DecimalField(max_digits=14, decimal_places=0)
    alert_source = models.CharField(max_length=11)
    alt_source_val = models.CharField(max_length=100)
    bloodgroup = models.CharField(max_length=4)
    image_file = models.ImageField(upload_to='images/')
    seq_no = models.IntegerField()
    is_disable = models.CharField(max_length=1)
    reaction = models.CharField(max_length=1)
    disability_percent = models.SmallIntegerField()
    bank_id = models.SmallIntegerField()
    branch_id = models.SmallIntegerField()
    bank_ac_name = models.CharField(max_length=100)
    bank_ac_type = models.CharField(max_length=50)
    bank_ac_number = models.CharField(max_length=50)
    grand_father_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mobile_no = models.CharField()
    parent_pssid = models.CharField()

    def __str__(self):
        return self.name


class Ctb_Person_Address(models.Model):
    # p_id = PFK LATER
    # adtype_id = PFK LATER
    # address_id = PFK LATER
    from_date = models.CharField(
        max_length=10, primary_key=True, null=False, blank=False)
    to_date = models.CharField(max_length=10)
    entry_by = models.CharField(max_length=30, null=False, blank=False)
    entry_date = models.DateField(null=False, blank=False)
    r_status = models.CharField(max_length=1, null=False, blank=False)
    tran_no = models.DecimalField(max_digits=14, decimal_places=0)
    reaction = models.CharField(max_length=1)

    class Meta:
        verbose_name_plural = 'Ctb_Person_Addresses'

    def __str__(self):
        return self.name


class Ctb_Person_Dependent(models.Model):
    # p_id = PFK LATER
    # reltype_id = PFK LATER
    # relative_id = FK LATER
    entry_by = models.CharField(max_length=30, null=False, blank=False)
    entry_date = models.DateField(name=False, blank=False)
    r_status = models.CharField(max_length=1, null=False, blank=False)
    tran_no = models.DecimalField(max_digits=14, decimal_places=0)
    order_no = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


class Ctb_Person_Nominee(models.Model):
    # p_id = PFK LATER
    # reltype_id = PFK LATER
    relative_id = models.DecimalField(max_digits=14, decimal_places=0)
    from_date = models.CharField(max_length=10)
    to_date = models.CharField(max_length=10)
    entry_by = models.CharField(max_length=30, null=False, blank=False)
    entry_date = models.DateField(null=False, blank=False)
    r_status = models.CharField(max_length=1, null=False, blank=False)
    tran_no = models.DecimalField(max_digits=14, decimal_places=0)
    # order_no = PFK LATER

    def __str__(self):
        return self.name


class Ctb_Person_Contact(models.Model):
    # p_id = PFK LATER
    # ctype_id = PFK LATER
    from_date = models.CharField(
        max_length=10, primary_key=True, null=False, blank=False)
    c_value = models.CharField(max_length=100, null=False, blank=False)
    to_date = models.CharField(max_length=10)
    entry_by = models.CharField(max_length=30, null=False, blank=False)
    entry_date = models.DateField(null=False, blank=False)
    r_status = models.CharField(max_length=1, null=False, blank=False)
    tran_no = models.DecimalField(max_digits=14, decimal_places=0)

    def __str__(self):
        return self.name


class Ctb_Person_Doc(models.Model):
    # p_id = PFK LATER
    # doc_id = PFK LATER
    from_date = models.CharField(
        max_length=10, null=False, blank=False, primary_key=True)
    to_date = models.CharField(max_length=10)
    issue_no = models.CharField(max_length=60, null=False, blank=False)
    issue_date = models.CharField(max_length=11)
    issue_place = models.CharField(max_length=100)
    entry_by = models.CharField(max_length=30, null=False, blank=False)
    entry_date = models.DateField(null=False, blank=False)
    r_status = models.CharField(max_length=1, null=False, blank=False)
    tran_no = models.DecimalField(max_digits=14, decimal_places=0)
    docfile = file = models.FileField(upload_to='uploads/')


class Ctb_Contributor(models.Model):
    # p_ssid = PFK LATER
    # employer_id = PFK LATER
    from_date = models.CharField(
        max_length=10, null=False, blank=False, primary_key=True)
    to_date = models.CharField(max_length=10)
    post = models.CharField(max_length=300, null=False, blank=False)
    # emptype_id = FK LATER
    joining_date = models.CharField(max_length=11, null=False, blank=False)
    termination_date = models.CharField(max_length=10)
    termination_res = models.CharField(max_length=300)
    entry_by = models.CharField(max_length=30, null=False, blank=False)
    entry_date = models.DateField(null=False, blank=False)
    r_status = models.CharField(max_length=1, null=False, blank=False)
    tran_no = models.DecimalField(max_digits=14, decimal_places=0)
    terminated_by = models.CharField(max_length=30)
    new_tran = models.DecimalField(max_digits=14, decimal_places=0)
    marking = models.CharField(max_length=1)
    # group_id = FK LATER
    contributor_type = models.CharField(max_length=1)
