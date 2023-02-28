from .models_bank_schema import *
from .models_registration_schema import *
from .models_claim_schema import *
from .models_employer_schema import *
from .models_contributor_schema import *
from .models_loan_schema import *
from .models_account_schema import *


class Query(graphene.ObjectType):

    # Bank
    banks = graphene.List(BankType)

    def resolve_banks(self, info, **kwargs):
        return Bank.objects.all()

    # Registration
    ctb_addresses = graphene.List(Ctb_AddressType)

    def resolve_ctb_addresses(self, info, **kwargs):
        return Ctb_Address.objects.all()

    ctb_persons = graphene.List(Ctb_PersonType)

    def resolve_ctb_persons(self, info, **kwargs):
        return Ctb_Person.objects.all()

    ctb_person_addresses = graphene.List(Ctb_Person_AddressType)

    def resolve_ctb_person_addresses(self, info, **kwargs):
        return Ctb_Person_Address.objects.all()

    ctb_person_dependents = graphene.List(Ctb_Person_DependentType)

    def resolve_ctb_person_dependents(self, info, **kwargs):
        return Ctb_Person_Dependent.objects.all()

    ctb_person_nominees = graphene.List(Ctb_Person_NomineeType)

    def resolve_ctb_person_nominees(self, info, **kwargs):
        return Ctb_Person_Nominee.objects.all()

    ctb_person_contacts = graphene.List(Ctb_Person_ContactType)

    def resolve_ctb_person_contacts(self, info, **kwargs):
        return Ctb_Person_Contact.objects.all()

    ctb_person_docs = graphene.List(Ctb_Person_DocType)

    def resolve_ctb_person_docs(self, info, **kwargs):
        return Ctb_Person_Doc.objects.all()

    ctb_contributors = graphene.List(Ctb_ContributorType)

    def resolve_ctb_contributors(self, info, **kwargs):
        return Ctb_Contributor.objects.all()

    # Claim
    stb_claim_heads = graphene.List(Stb_Claim_HeadType)

    def resolve_stb_claim_heads(self, info, **kwargs):
        return Stb_Claim_Head.objects.all()

    stb_claim_anusuchi6s = graphene.List(Stb_Claim_Anusuchi6Type)

    def resolve_stb_claim_anusuchi6s(self, info, **kwargs):
        return Stb_Claim_Anusuchi6.objects.all()

    stb_claim_app_amounts = graphene.List(Stb_Claim_App_AmountType)

    def resolve_stb_claim_app_amounts(self, info, **kwargs):
        return Stb_Claim_App_Amount.objects.all()

    stb_claim_docs = graphene.List(Stb_Claim_DocType)

    def resolve_stb_claim_docs(self, info, **kwargs):
        return Stb_Claim_Doc.objects.all()

    # Employer

    ctb_emp_contacts = graphene.List(Ctb_Emp_ContactType)

    def resolve_ctb_emp_contacts(self, info, **kwargs):
        return Ctb_Emp_Contact.objects.all()

    ctb_employers = graphene.List(Ctb_EmployerType)

    def resolve_ctb_employers(self, info, **kwargs):
        return Ctb_Employer.objects.all()

    ctb_emp_docs = graphene.List(Ctb_Emp_DocType)

    def resolve_ctb_emp_docs(self, info, **kwargs):
        return Ctb_Emp_Doc.objects.all()

    ctb_emp_addresses = graphene.List(Ctb_Emp_AddressType)

    def resolve_ctb_emp_addresses(self, info, **kwargs):
        return Ctb_Emp_Address.objects.all()

    ctb_emp_officials = graphene.List(Ctb_Emp_OfficialType)

    def resolve_ctb_emp_officials(self, info, **kwargs):
        return Ctb_Emp_Official.objects.all()

    # Contributor

    stb_coll_voucher_infos = graphene.List(Stb_Coll_Voucher_InfoType)

    def resolve_stb_coll_voucher_infos(self, info, **kwargs):
        return Stb_Coll_Voucher_Info.objects.all()

    stb_contributor_sal_dets = graphene.List(Stb_Contributor_Sal_DetType)

    def resolve_stb_contributor_sal_dets(self, info, **kwargs):
        return Stb_Contributor_Sal_Det.objects.all()

    stb_collection_tran_heads = graphene.List(Stb_Collection_Tran_HeadType)

    def resolve_stb_collection_tran_heads(self, info, **kwargs):
        return Stb_Collection_Tran_Head.objects.all()

    stb_coll_tran_details = graphene.List(Stb_Coll_Tran_DetailsType)

    def resolve_stb_coll_tran_details(self, info, **kwargs):
        return Stb_Coll_Tran_Details.objects.all()

    stb_scheme_applications = graphene.List(Stb_Scheme_ApplicationType)

    def resolve_stb_scheme_applications(self, info, **kwargs):
        return Stb_Scheme_Application.objects.all()

    # Loan

    ctb_special_loans = graphene.List(Ctb_Special_LoanType)

    def resolve_ctb_special_loans(self, info, **kwargs):
        return Ctb_Special_Loan.objects.all()

    ctb_user_tran_verifications = graphene.List(
        Ctb_User_Tran_VerificationsType)

    def resolve_ctb_user_tran_verifications(self, info, **kwargs):
        return Ctb_User_Tran_Verifications.objects.all()

    dctb_submissions = graphene.List(Dctb_SubmissionType)

    def resolve_dctb_submissions(self, info, **kwargs):
        return Dctb_Submission.objects.all()

    atb_disbursement_processes = graphene.List(Atb_Disbursement_ProcessType)

    def resolve_atb_disbursement_processes(self, info, **kwargs):
        return Atb_Disbursement_Process.objects.all()

    # Account

    atb_gltran_masts = graphene.List(Atb_Gltran_MastType)

    def resolve_atb_gltran_masts(self, info, **kwargs):
        return Atb_Gltran_Mast.objects.all()

    atb_gltran_detls = graphene.List(Atb_Gltran_DetlType)

    def resolve_atb_gltran_detls(self, info, **kwargs):
        return Atb_Gltran_Detl.objects.all()

    atb_account_ledgers = graphene.List(Atb_Account_LedgerType)

    def resolve_atb_account_ledgers(self, info, **kwargs):
        return Atb_Account_Ledger.objects.all()


class Mutation(graphene.ObjectType):
    # Bank
    create_bank = CreateBankMutation.Field()
    # Registration
    create_ctb_address = CreateCtb_AddressMutation.Field()
    update_ctb_address = UpdateCtb_AddressMutation.Field()
    delete_ctb_address = DeleteCtb_AddressMutation.Field()

    create_ctb_person = CreateCtb_PersonMutation.Field()
    update_ctb_person = UpdateCtb_PersonMutation.Field()
    delete_ctb_person = DeleteCtb_PersonMutation.Field()

    create_ctb_person_address = CreateCtb_Person_AddressMutation.Field()
    update_ctb_person_address = UpdateCtb_Person_AddressMutation.Field()
    delete_ctb_person_address = DeleteCtb_Person_AddressMutation.Field()

    create_ctb_person_dependent = CreateCtb_Person_DependentMutation.Field()
    update_ctb_person_dependent = UpdateCtb_Person_DependentMutation.Field()
    delete_ctb_person_dependent = DeleteCtb_Person_DependentMutation.Field()

    create_ctb_person_nominee = CreateCtb_Person_NomineeMutation.Field()
    update_ctb_person_nominee = UpdateCtb_Person_NomineeMutation.Field()
    delete_ctb_person_nominee = DeleteCtb_Person_NomineeMutation.Field()

    create_ctb_person_contact = CreateCtb_Person_ContactMutation.Field()
    update_ctb_person_contact = UpdateCtb_Person_ContactMutation.Field()
    delete_ctb_person_contact = DeleteCtb_Person_ContactMutation.Field()

    create_ctb_person_doc = CreateCtb_Person_DocMutation.Field()
    update_ctb_person_doc = UpdateCtb_Person_DocMutation.Field()
    delete_ctb_person_doc = DeleteCtb_Person_DocMutation.Field()

    create_ctb_contributor = CreateCtb_ContributorMutation.Field()
    update_ctb_contributor = UpdateCtb_ContributorMutation.Field()
    delete_ctb_contributor = DeleteCtb_ContributorMutation.Field()

    # Claim
    create_stb_claim_head = CreateStb_Claim_HeadMutation.Field()
    create_stb_claim_anusuchi6 = CreateStb_Claim_Anusuchi6Mutation.Field()
    create_stb_claim_app_amount = CreateStb_Claim_App_AmountMutation.Field()
    create_stb_claim_doc = CreateStb_Claim_DocMutation.Field()
    # Employer
    create_ctb_emp_contact = CreateCtb_Emp_ContactMutation.Field()
    create_ctb_employer = CreateCtb_EmployerMutation.Field()
    create_ctb_emp_doc = CreateCtb_Emp_DocMutation.Field()
    create_ctb_emp_address = CreateCtb_Emp_AddressMutation.Field()
    create_ctb_emp_official = CreateCtb_Emp_OfficialMutation.Field()
    # Contributor
    create_stb_coll_voucher_info = CreateStb_Coll_Voucher_InfoMutation.Field()
    create_stb_contributor_sal_det = CreateStb_Contributor_Sal_DetMutation.Field()
    create_stb_collection_tran_head = CreateStb_Collection_Tran_HeadMutation.Field()
    create_stb_coll_tran_detail = CreateStb_Coll_Tran_DetailsMutation.Field()
    create_stb_scheme_application = CreateStb_Scheme_ApplicationMutation.Field()

    # Loan
    create_ctb_special_loan = CreateCtb_Special_LoanMutation.Field()
    update_ctb_special_loan = UpdateCtb_Special_LoanMutation.Field()
    delete_ctb_special_loan = DeleteCtb_Special_LoanMutation.Field()

    create_ctb_user_tran_verification = CreateCtb_User_Tran_VerificationsMutation.Field()
    update_ctb_user_tran_verification = UpdateCtb_User_Tran_VerificationsMutation.Field()
    delete_ctb_user_tran_verification = DeleteCtb_User_Tran_VerificationsMutation.Field()

    create_dctb_submission = CreateDctb_SubmissionMutation.Field()
    update_dctb_submission = UpdateDctb_SubmissionMutation.Field()
    delete_dctb_submission = DeleteDctb_SubmissionMutation.Field()

    create_atb_disbursement_process = CreateAtb_Disbursement_ProcessMutation.Field()

    # Account
    create_atb_gltran_mast = CreateAtb_Gltran_MastMutation.Field()
    update_atb_gltran_mast = UpdateAtb_Gltran_MastMutation.Field()
    create_atb_gltran_detl = CreateAtb_Gltran_DetlMutation.Field()
    create_atb_account_ledger = CreateAtb_Account_LedgerMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
