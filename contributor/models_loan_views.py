from django.shortcuts import render


# Ctb Special Loan


def ctb_special_loan_add_dynamic(request):
    return render(request, 'ctb_special_loan/ctb_special_loan_add_dynamic.html')


def ctb_special_loan_edit_and_delete(request):
    return render(request, 'ctb_special_loan/ctb_special_loan_edit_and_delete.html')


# Ctb User Tran Verifications


def ctb_user_tran_verifications_add_dynamic(request):
    return render(request, 'ctb_user_tran_verifications/ctb_user_tran_verifications_add_dynamic.html')


def ctb_user_tran_verifications_edit_and_delete(request):
    return render(request, 'ctb_user_tran_verifications/ctb_user_tran_verifications_edit_and_delete.html')

# DCtb Submission


def dctb_submission_add_dynamic(request):
    return render(request, 'dctb_submission/dctb_submission_add_dynamic.html')


def dctb_submission_edit_and_delete(request):
    return render(request, 'dctb_submission/dctb_submission_edit_and_delete.html')

# Atb Disbursement Process


def atb_disbursement_process_add_dynamic(request):
    return render(request, 'atb_disbursement_process/atb_disbursement_process_add_dynamic.html')


def atb_disbursement_process_edit_and_delete(request):
    return render(request, 'atb_disbursement_process/atb_disbursement_process_edit_and_delete.html')
