from .models_bank_schema import *
from .models_registration_schema import *
from .models_claim_schema import *
from .models_employer_schema import *


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


class Mutation(graphene.ObjectType):
    # Bank
    create_bank = CreateBankMutation.Field()
    # Registration
    create_ctb_address = CreateCtb_AddressMutation.Field()
    create_ctb_person = CreateCtb_PersonMutation.Field()
    create_ctb_person_address = CreateCtb_Person_AddressMutation.Field()
    create_ctb_person_dependent = CreateCtb_Person_DependentMutation.Field()
    create_ctb_person_nominee = CreateCtb_Person_NomineeMutation.Field()
    create_ctb_person_contact = CreateCtb_Person_ContactMutation.Field()
    create_ctb_person_doc = CreateCtb_Person_DocMutation.Field()
    create_ctb_contributor = CreateCtb_ContributorMutation.Field()
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


schema = graphene.Schema(query=Query, mutation=Mutation)
