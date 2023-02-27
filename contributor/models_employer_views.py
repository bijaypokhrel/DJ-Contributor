from django.shortcuts import render


# Ctb Emp Contact


def ctb_emp_contact_add_dynamic(request):
    return render(request, 'ctb_emp_contact/ctb_emp_contact_add_dynamic.html')


def ctb_emp_contact_edit_and_delete(request):
    return render(request, 'ctb_emp_contact/ctb_emp_contact_edit_and_delete.html')

# Ctb Employer


def ctb_employer_add_dynamic(request):
    return render(request, 'ctb_employer/ctb_employer_add_dynamic.html')


def ctb_employer_edit_and_delete(request):
    return render(request, 'ctb_employer/ctb_employer_edit_and_delete.html')

# Ctb Emp Doc


def ctb_emp_doc_add_dynamic(request):
    return render(request, 'ctb_emp_doc/ctb_emp_doc_add_dynamic.html')


def ctb_emp_doc_edit_and_delete(request):
    return render(request, 'ctb_emp_doc/ctb_emp_doc_edit_and_delete.html')

# Ctb Emp Address


def ctb_emp_address_add_dynamic(request):
    return render(request, 'ctb_emp_address/ctb_emp_address_add_dynamic.html')


def ctb_emp_address_edit_and_delete(request):
    return render(request, 'ctb_emp_address/ctb_emp_address_edit_and_delete.html')

# Ctb Emp Official


def ctb_emp_official_add_dynamic(request):
    return render(request, 'ctb_emp_official/ctb_emp_official_add_dynamic.html')


def ctb_emp_official_edit_and_delete(request):
    return render(request, 'ctb_emp_official/ctb_emp_official_edit_and_delete.html')


