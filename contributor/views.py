from django.shortcuts import render, redirect
from .models import Claim_Booking

# Create your views here.


def home(request):
    return render(request, 'contributor/index.html')


def claim_booking(request):
    if request.method == 'POST':
        id = request.POST['id']
        chfid = request.POST['chfid']
        insureeid = request.POST['insureeid']
        item_id = request.POST['itemid']
        service_id = request.POST['serviceid']
        quantity = request.POST['quantity']
        price = request.POST['price']
        claimed_date = request.POST['claimeddate']
        claim_id = request.POST['claimid']
        claim_amount = request.POST['claimamount']
        Claim_Booking.objects.create(
            id=id, chfid=chfid, insureeid=insureeid, item_id=item_id, service_id=service_id, quantity=quantity, price=price, claimed_date=claimed_date, claim_id=claim_id, claim_amount=claim_amount)

        # my_instance = Claim_Booking.objects(
        #     id, chfid, insureeid, item_id, service_id, quantity, price, claimed_date, claim_id, claim_amount)
        # my_instance.save()
        return redirect("home")
    return render(request, 'contributor/claim_booking.html')
