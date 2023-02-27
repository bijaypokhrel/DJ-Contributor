from django.shortcuts import render

# Stb Coll Voucher info


def stb_coll_voucher_info_add_dynamic(request):
    return render(request, 'stb_coll_voucher_info/stb_coll_voucher_info_add_dynamic.html')


def stb_coll_voucher_info_edit_and_delete(request):
    return render(request, 'stb_coll_voucher_info/stb_coll_voucher_info_edit_and_delete.html')

# Stb Contributor Sal Det


def stb_contributor_sal_det_add_dynamic(request):
    return render(request, 'stb_contributor_sal_det/stb_contributor_sal_det_add_dynamic.html')


def stb_contributor_sal_det_edit_and_delete(request):
    return render(request, 'stb_contributor_sal_det/stb_contributor_sal_det_edit_and_delete.html')


# Stb Collection Tran Head


def stb_collection_tran_head(request):
    return render(request, 'stb_collection_tran_head/stb_collection_tran_head.html')

# Stb Collection Tran Head


def stb_coll_tran_details(request):
    return render(request, 'stb_coll_tran_details/stb_coll_tran_details.html')

# Stb Scheme Application


def stb_scheme_application(request):
    return render(request, 'stb_scheme_application/stb_scheme_application.html')
