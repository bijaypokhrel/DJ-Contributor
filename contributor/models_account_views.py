from django.shortcuts import render


# Atb Gltran Mast


def atb_gltran_mast(request):
    return render(request, 'atb_gltran_mast/atb_gltran_mast.html')


# Atb Gltran Detl


def atb_gltran_detl(request):
    return render(request, 'atb_gltran_detl/atb_gltran_detl.html')

# Atb Account Ledger


def atb_account_ledger(request):
    return render(request, 'atb_account_ledger/atb_account_ledger.html')
