from django.db import models


class Claim_Booking(models.Model):
    id = models.BigAutoField(primary_key=True, db_column="ID")
    chfid = models.CharField(max_length=15, null="True",
                             blank="True", db_column="CHFIF")
    insureeid = models.CharField(
        max_length=15, null="True", blank="True", db_column="INSUREEID")
    item_id = models.CharField(
        max_length=15, null="True", blank="True", db_column="ITEM_ID")
    service_id = models.CharField(
        max_length=15, null="True", blank="True", db_column="SERVICE_ID")
    quantity = models.DecimalField(
        max_digits=10, decimal_places=2, null="True", blank="True", db_column="QUANTITY")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null="True", blank="True", db_column="PRICE")
    claimed_date = models.DateField(
        null="True", blank="True", db_column="CLAIMED_DATE")
    claim_id = models.CharField(
        max_length=15, null="True", blank="True", db_column="CLAIM_ID")
    claim_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null="True", blank="True", db_column="CLAIM_AMOUNT")
