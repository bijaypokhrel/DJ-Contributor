from django.shortcuts import render, redirect
from .models import Claim_Booking
import json
from django.http import JsonResponse
import datetime
from .models_menu_views import *
from .models_bank_views import *
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

# def claim_booking_json(request):


def claim_booking_json(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        chfid = data.get('chfid')
        insureeid = data.get('insureeid')
        item_id = data.get('item_id')
        service_id = data.get('service_id')
        quantity = data.get('quantity')
        price = data.get('price')
        claimed_date = data.get('claimed_date')
        claim_id = data.get('claim_id')
        claim_amount = data.get('claim_amount')
        claim_booking = Claim_Booking(chfid=chfid, insureeid=insureeid, item_id=item_id, service_id=service_id,
                                      quantity=quantity, price=price, claimed_date=claimed_date, claim_id=claim_id, claim_amount=claim_amount)

        claim_booking.save()
        return JsonResponse({'message': 'Claim Booking successfully created'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


def claim_booking_fhir(request):
    if request.method == "POST":
        fhir_data = json.loads(request.body.decode("utf-8"))
        print(fhir_data)
        parse_fhir_claim(fhir_data)
        return JsonResponse({"message": "Claim created successfully"})
    return JsonResponse({"error": "Invalid request method"})


def parse_fhir_claim(fhir_data):
    # extract relevant data from the FHIR JSON
    chfid = fhir_data.get("id")
    patient_id = int(fhir_data["patient"]["reference"].split("/")[1])
    claims = []
    for item in fhir_data["item"]:
        service_id = int(item["service"]["reference"].split("/")[1])
        quantity = item["quantity"]["value"]
        price = item["unitPrice"]["value"]
        claimed_date = datetime.datetime.strptime(
            fhir_data["created"], '%Y-%m-%dT%H:%M:%SZ')
        claim_id = int(fhir_data["insurer"]["reference"].split("/")[1])
        claim_amount = fhir_data["total"]["value"]
        claim = Claim_Booking(chfid=chfid, insureeid=patient_id, item_id=service_id,
                              service_id=service_id, quantity=quantity, price=price,
                              claimed_date=claimed_date, claim_id=claim_id, claim_amount=claim_amount)
        claim.save()
        # claims.append(claim)
        # Claim_Booking.objects.bulk_create(claims)


def convert_to_fhir_claim(claim_booking):
    fhir_claim = {
        "resourceType": "Claim",
        "id": claim_booking.chfid,
        "patient": {
            "reference": "Patient/" + str(claim_booking.insureeid)
        },
        "item": [{
            "item_id": {
                "system": "http://hl7.org/fhir/sid/ndc",
                "code": str(claim_booking.item_id)
            },
            "service": {
                "system": "http://hl7.org/fhir/sid/ndc",
                "code": str(claim_booking.service_id)
            },
            "quantity": claim_booking.quantity,
            "unitPrice": {
                "value": claim_booking.price
            }
        }],
        "claimed_date": claim_booking.claimed_date.strftime('%Y-%m-%d'),
        "claim_id": claim_booking.claim_id,
        "claim_amount": {
            "value": claim_booking.claim_amount
        }
    }
    return fhir_claim


def get_claim(request, claim_id):
    try:
        claim_booking = Claim_Booking.objects.get(pk=claim_id)
    except Claim_Booking.DoesNotExist:
        return JsonResponse({"error": "Claim not found"})

    fhir_claim = convert_to_fhir_claim(claim_booking)
    return JsonResponse(fhir_claim, safe=False)
