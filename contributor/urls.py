from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from . import views


urlpatterns = [

    path('links', views.links, name="links"),

    #     path('', views.home, name="home"),
    path('', views.links, name="home"),
    path('claimbooking', views.claim_booking, name="claimbooking"),
    path('claimbookingjson', csrf_exempt(views.claim_booking_json),
         name="claimbookingjson"),
    path('claimbookingfhir', csrf_exempt(views.claim_booking_fhir),
         name="claimbookingfhir"),
    path('fhirbookingclaim/<int:claim_id>', csrf_exempt(views.get_claim),
         name="fhirbookingclaim"),

    # Menu
    path('menu', views.menu, name="menu"),
    path('app-menus', csrf_exempt(views.app_menus),
         name="app-menus"),
    path('app_menus/<int:menu_id>', csrf_exempt(views.app_menus)),
    path('menu_add', csrf_exempt(views.menu_add),
         name="menu_add"),
    path('menu_edit', csrf_exempt(views.menu_edit),
         name="menu_edit"),
    path('menu_delete', csrf_exempt(views.menu_delete),
         name="menu_delete"),

    path('menu_list', views.menu_list, name="menu_list"),
    path('menu_list_edit', views.menu_list_edit, name="menu_list_edit"),

    # Bank
    path('bank', views.bank, name="bank"),
    path('app-banks', csrf_exempt(views.app_banks),
         name="app-banks"),
    path('app-banks/<int:bank_id>', csrf_exempt(views.app_banks)),
    path('bank_add', csrf_exempt(views.bank_add),
         name="bank_add"),
    path('bank_edit', csrf_exempt(views.bank_edit),
         name="bank_edit"),
    path('bank_delete', csrf_exempt(views.bank_delete),
         name="bank_delete"),

    # Graphql
    # Bank and Link
    path('bank_graphql', views.bank_graphql, name="bank_graphql"),
    path('links', views.links, name="links"),
    # Ctb Address

    path('ctb_address', views.ctb_address,
         name="ctb_address"),
    #     path('ctb_address_graphql', views.ctb_address_graphql,
    #          name="ctb_address_graphql"),

    #     path('ctb_address_add', views.ctb_address_add,
    #          name="ctb_address_add"),

    #     path('ctb_address_add_static', views.ctb_address_add_static,
    #          name="ctb_address_add_static"),

    #     path('ctb_address_add_dynamic', views.ctb_address_add_dynamic,
    #          name="ctb_address_add_dynamic"),


    #     path('ctb_address_list_only', views.ctb_address_list_only,
    #          name="ctb_address_list_only"),

    #     path('ctb_address_list_edit', views.ctb_address_list_edit,
    #          name="ctb_address_list_edit"),

    #     path('ctb_address_edit', views.ctb_address_edit,
    #          name="ctb_address_edit"),

    #     path('ctb_address_delete', views.ctb_address_delete,
    #          name="ctb_address_delete"),

    #     Ctb Person

    path('ctb_person_add_static', views.ctb_person_add_static,
         name="ctb_person_add_static"),

    path('ctb_person_add_dynamic', views.ctb_person_add_dynamic,
         name="ctb_person_add_dynamic"),

    path('ctb_person_list_only', views.ctb_person_list_only,
         name="ctb_person_list_only"),

    path('ctb_person_list_edit', views.ctb_person_list_edit,
         name="ctb_person_list_edit"),

    path('ctb_person_edit', views.ctb_person_edit,
         name="ctb_person_edit"),

    path('ctb_person_delete', views.ctb_person_delete,
         name="ctb_person_delete"),


    #     Ctb Person Address

    path('ctb_person_address_add_static', views.ctb_person_address_add_static,
         name="ctb_person_address_add_static"),

    path('ctb_person_address_add_dynamic', views.ctb_person_address_add_dynamic,
         name="ctb_person_address_add_dynamic"),

    path('ctb_person_address_list_only', views.ctb_person_address_list_only,
         name="ctb_person_address_list_only"),

    path('ctb_person_address_list_edit', views.ctb_person_address_list_edit,
         name="ctb_person_address_list_edit"),

    path('ctb_person_address_edit', views.ctb_person_address_edit,
         name="ctb_person_address_edit"),
    path('ctb_person_address_delete', views.ctb_person_address_delete,
         name="ctb_person_address_delete"),

    #     Ctb Person Dependent

    path('ctb_person_dependent_add_static', views.ctb_person_dependent_add_static,
         name="ctb_person_dependent_add_static"),

    path('ctb_person_dependent_add_dynamic', views.ctb_person_dependent_add_dynamic,
         name="ctb_person_dependent_add_dynamic"),

    path('ctb_person_dependent_list_only', views.ctb_person_dependent_list_only,
         name="ctb_person_dependent_list_only"),

    path('ctb_person_dependent_list_edit', views.ctb_person_dependent_list_edit,
         name="ctb_person_dependent_list_edit"),

    path('ctb_person_dependent_edit', views.ctb_person_dependent_edit,
         name="ctb_person_dependent_edit"),

    path('ctb_person_dependent_delete', views.ctb_person_dependent_delete,
         name="ctb_person_dependent_delete"),

    #     Ctb Person Nominee

    path('ctb_person_nominee_add_static', views.ctb_person_nominee_add_static,
         name="ctb_person_nominee_add_static"),

    path('ctb_person_nominee_add_dynamic', views.ctb_person_nominee_add_dynamic,
         name="ctb_person_nominee_add_dynamic"),

    path('ctb_person_nominee_list_only', views.ctb_person_nominee_list_only,
         name="ctb_person_nominee_list_only"),

    path('ctb_person_nominee_list_edit', views.ctb_person_nominee_list_edit,
         name="ctb_person_nominee_list_edit"),

    path('ctb_person_nominee_edit', views.ctb_person_nominee_edit,
         name="ctb_person_nominee_edit"),

    path('ctb_person_nominee_delete', views.ctb_person_nominee_delete,
         name="ctb_person_nominee_delete"),

    #     Ctb Person Contact

    path('ctb_person_contact_add_dynamic', views.ctb_person_contact_add_dynamic,
         name="ctb_person_contact_add_dynamic"),

    path('ctb_person_contact_list_only', views.ctb_person_contact_list_only,
         name="ctb_person_contact_list_only"),

    path('ctb_person_contact_list_edit', views.ctb_person_contact_list_edit,
         name="ctb_person_contact_list_edit"),

    path('ctb_person_contact_edit', views.ctb_person_contact_edit,
         name="ctb_person_contact_edit"),

    path('ctb_person_contact_delete', views.ctb_person_contact_delete,
         name="ctb_person_contact_delete"),

    #     Ctb Person Doc

    path('ctb_person_doc_add_dynamic', views.ctb_person_doc_add_dynamic,
         name="ctb_person_doc_add_dynamic"),

    path('ctb_person_doc_list_only', views.ctb_person_doc_list_only,
         name="ctb_person_doc_list_only"),

    path('ctb_person_doc_list_edit', views.ctb_person_doc_list_edit,
         name="ctb_person_doc_list_edit"),

    path('ctb_person_doc_edit', views.ctb_person_doc_edit,
         name="ctb_person_doc_edit"),

    path('ctb_person_doc_delete', views.ctb_person_doc_delete,
         name="ctb_person_doc_delete"),

    #     Ctb Contributor

    path('ctb_contributor_add_dynamic', views.ctb_contributor_add_dynamic,
         name="ctb_contributor_add_dynamic"),

    path('ctb_contributor_list_only', views.ctb_contributor_list_only,
         name="ctb_contributor_list_only"),

    path('ctb_contributor_list_edit', views.ctb_contributor_list_edit,
         name="ctb_contributor_list_edit"),

    path('ctb_contributor_edit', views.ctb_contributor_edit,
         name="ctb_contributor_edit"),

    path('ctb_contributor_delete', views.ctb_contributor_delete,
         name="ctb_contributor_delete"),

    #     Ctb Special Loan

    path('ctb_special_loan_add_dynamic', views.ctb_special_loan_add_dynamic,
         name="ctb_special_loan_add_dynamic"),

    path('ctb_special_loan_edit_and_delete', views.ctb_special_loan_edit_and_delete,
         name="ctb_special_loan_edit_and_delete"),

    #     Ctb User Tran Verifications

    path('ctb_user_tran_verifications_add_dynamic', views.ctb_user_tran_verifications_add_dynamic,
         name="ctb_user_tran_verifications_add_dynamic"),

    path('ctb_user_tran_verifications_edit_and_delete', views.ctb_user_tran_verifications_edit_and_delete,
         name="ctb_user_tran_verifications_edit_and_delete"),

    #     DCtb Submission

    path('dctb_submission_add_dynamic', views.dctb_submission_add_dynamic,
         name="dctb_submission_add_dynamic"),

    path('dctb_submission_edit_and_delete', views.dctb_submission_edit_and_delete,
         name="dctb_submission_edit_and_delete"),

    #     Atb disbursement Process

    path('atb_disbursement_process_add_dynamic', views.atb_disbursement_process_add_dynamic,
         name="atb_disbursement_process_add_dynamic"),

    path('atb_disbursement_process_edit_and_delete', views.atb_disbursement_process_edit_and_delete,
         name="atb_disbursement_process_edit_and_delete"),

    # Ctb Emp Contact

    path('ctb_emp_contact_add_dynamic', views.ctb_emp_contact_add_dynamic,
         name="ctb_emp_contact_add_dynamic"),

    path('ctb_emp_contact_edit_and_delete', views.ctb_emp_contact_edit_and_delete,
         name="ctb_emp_contact_edit_and_delete"),


    # Ctb Employer

    path('ctb_employer_add_dynamic', views.ctb_employer_add_dynamic,
         name="ctb_employer_add_dynamic"),

    path('ctb_employer_edit_and_delete', views.ctb_employer_edit_and_delete,
         name="ctb_employer_edit_and_delete"),

    # Ctb Emp Doc

    path('ctb_emp_doc_add_dynamic', views.ctb_emp_doc_add_dynamic,
         name="ctb_emp_doc_add_dynamic"),

    path('ctb_emp_doc_edit_and_delete', views.ctb_emp_doc_edit_and_delete,
         name="ctb_emp_doc_edit_and_delete"),

    # Ctb Emp Address

    path('ctb_emp_address_add_dynamic', views.ctb_emp_address_add_dynamic,
         name="ctb_emp_address_add_dynamic"),

    path('ctb_emp_address_edit_and_delete', views.ctb_emp_address_edit_and_delete,
         name="ctb_emp_address_edit_and_delete"),

    # Ctb Emp Official

    path('ctb_emp_official_add_dynamic', views.ctb_emp_official_add_dynamic,
         name="ctb_emp_official_add_dynamic"),

    path('ctb_emp_official_edit_and_delete', views.ctb_emp_official_edit_and_delete,
         name="ctb_emp_official_edit_and_delete"),

    # Stb Coll Voucher Info

    path('stb_coll_voucher_info_add_dynamic', views.stb_coll_voucher_info_add_dynamic,
         name="stb_coll_voucher_info_add_dynamic"),

    path('stb_coll_voucher_info_edit_and_delete', views.stb_coll_voucher_info_edit_and_delete,
         name="stb_coll_voucher_info_edit_and_delete"),

    # Stb Contributor Sal Det

    path('stb_contributor_sal_det_add_dynamic', views.stb_contributor_sal_det_add_dynamic,
         name="stb_contributor_sal_det_add_dynamic"),
    path('stb_contributor_sal_det_edit_and_delete', views.stb_contributor_sal_det_edit_and_delete,
         name="stb_contributor_sal_det_edit_and_delete"),

    # Stb Collection Tran Head

    path('stb_collection_tran_head', views.stb_collection_tran_head,
         name="stb_collection_tran_head"),

    # Stb Coll Tran Details

    path('stb_coll_tran_details', views.stb_coll_tran_details,
         name="stb_coll_tran_details"),

    # Stb Scheme Application

    path('stb_scheme_application', views.stb_scheme_application,
         name="stb_scheme_application"),

    # Stb Claim Head

    path('stb_claim_head', views.stb_claim_head,
         name="stb_claim_head"),

    # Stb Claim Anusuchi6

    path('stb_claim_anusuchi6', views.stb_claim_anusuchi6,
         name="stb_claim_anusuchi6"),

    # Stb Claim App Amount

    path('stb_claim_app_amount', views.stb_claim_app_amount,
         name="stb_claim_app_amount"),

    # Stb Claim Doc

    path('stb_claim_doc', views.stb_claim_doc,
         name="stb_claim_doc"),

    # Atb Gltran Mast

    path('atb_gltran_mast', views.atb_gltran_mast,
         name="atb_gltran_mast"),

    # Atb Gltran Detl

    path('atb_gltran_detl', views.atb_gltran_detl,
         name="atb_gltran_detl"),

    # Atb Account Ledger

    path('atb_account_ledger', views.atb_account_ledger,
         name="atb_account_ledger"),


]
