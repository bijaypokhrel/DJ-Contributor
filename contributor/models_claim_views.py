from django.shortcuts import render


# Stb Claim Head


def stb_claim_head(request):
    return render(request, 'stb_claim_head/stb_claim_head.html')

# Stb Claim Anusuchi6


def stb_claim_anusuchi6(request):
    return render(request, 'stb_claim_anusuchi6/stb_claim_anusuchi6.html')

# Stb Claim App Amount


def stb_claim_app_amount(request):
    return render(request, 'stb_claim_app_amount/stb_claim_app_amount.html')

# Stb Claim Doc


def stb_claim_doc(request):
    return render(request, 'stb_claim_doc/stb_claim_doc.html')
