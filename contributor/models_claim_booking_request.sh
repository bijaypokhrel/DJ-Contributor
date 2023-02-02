curl --location --request POST 'http://127.0.0.1:8000/claimbookingfhir' \
--header 'Content-Type: application/json' \
--data-raw '{
  "resourceType": "Claim",
  "id": "60",
  "patient": {
	"reference": "Patient/1"
  },
 
  "created": "2023-01-31T12:00:00Z",
  "enterer": {
	"reference": "Practitioner/3"
  },
  "insurer": {
	"reference": "Organization/4"
  },
  "item": [
	{
  	"sequence": 1,
  	"careTeamLinkId": [
    	1
  	],
  	"service": {
    	"reference": "Procedure/5"
  	},
  	"quantity": {
    	"value": 10.0
  	},
  	"unitPrice": {
    	"value": 20.0,
    	"currency": "USD"
  	}
	},
    {
  	"sequence": 2,
  	"careTeamLinkId": [
    	1
  	],
  	"service": {
    	"reference": "Procedure/5"
  	},
  	"quantity": {
    	"value": 10.0
  	},
  	"unitPrice": {
    	"value": 20.0,
    	"currency": "USD"
  	}
	}
  ],
  "total": {
	"value": 200.0,
	"currency": "USD"
  }
}
'


# Booking from database

curl --location --request GET 'http://127.0.0.1:8000/fhirbookingclaim/17' \
--data-raw ''

# Response

{"resourceType": "Claim", "id": "60", "patient": {"reference": "Patient/1"}, "item": [{"item_id": {"system": "http://hl7.org/fhir/sid/ndc", "code": "5"}, "service": {"system": "http://hl7.org/fhir/sid/ndc", "code": "5"}, "quantity": "10.00", "unitPrice": {"value": "20.00"}}], "claimed_date": "2023-01-31", "claim_id": "4", "claim_amount": {"value": "200.00"}}