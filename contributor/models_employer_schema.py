import graphene
from graphene import ObjectType, String, Decimal
from graphene_django import DjangoObjectType
from .models import *


# Query

class Ctb_Emp_ContactType(DjangoObjectType):
    class Meta:
        model = Ctb_Emp_Contact


class Ctb_EmployerType(DjangoObjectType):
    class Meta:
        model = Ctb_Employer


class Ctb_Emp_DocType(DjangoObjectType):
    class Meta:
        model = Ctb_Emp_Doc


class Ctb_Emp_AddressType(DjangoObjectType):
    class Meta:
        model = Ctb_Emp_Address


class Ctb_Emp_OfficialType(DjangoObjectType):
    class Meta:
        model = Ctb_Emp_Official

# Mutation


class CreateCtb_Emp_ContactMutation(graphene.Mutation):
    class Arguments:
        from_date = String()
        to_date = String()

    ctb_emp_contact = graphene.Field(lambda: Ctb_Emp_ContactType)

    def mutate(self, info, from_date, to_date):
        ctb_emp_contact = Ctb_Emp_Contact.objects.create(
            from_date=from_date, to_date=to_date)
        return CreateCtb_Emp_ContactMutation(ctb_emp_contact=ctb_emp_contact)


class CreateCtb_EmployerMutation(graphene.Mutation):
    class Arguments:
        employer_name_nep = String()
        employer_name_eng = String()

    ctb_employer = graphene.Field(lambda: Ctb_EmployerType)

    def mutate(self, info, employer_name_nep, employer_name_eng):
        ctb_employer = Ctb_Employer.objects.create(
            employer_name_nep=employer_name_nep, employer_name_eng=employer_name_eng)
        return CreateCtb_EmployerMutation(ctb_employer=ctb_employer)


class CreateCtb_Emp_DocMutation(graphene.Mutation):
    class Arguments:
        from_date = String()
        to_date = String()

    ctb_emp_doc = graphene.Field(lambda: Ctb_Emp_DocType)

    def mutate(self, info, from_date, to_date):
        ctb_emp_doc = Ctb_Emp_Doc.objects.create(
            from_date=from_date, to_date=to_date)
        return CreateCtb_Emp_DocMutation(ctb_emp_doc=ctb_emp_doc)


class CreateCtb_Emp_AddressMutation(graphene.Mutation):
    class Arguments:
        from_date = String()
        to_date = String()

    ctb_emp_address = graphene.Field(lambda: Ctb_Emp_AddressType)

    def mutate(self, info, from_date, to_date):
        ctb_emp_address = Ctb_Emp_Address.objects.create(
            from_date=from_date, to_date=to_date)
        return CreateCtb_Emp_AddressMutation(ctb_emp_address=ctb_emp_address)


class CreateCtb_Emp_OfficialMutation(graphene.Mutation):
    class Arguments:
        from_date = String()
        to_date = String()

    ctb_emp_official = graphene.Field(lambda: Ctb_Emp_OfficialType)

    def mutate(self, info, from_date, to_date):
        ctb_emp_official = Ctb_Emp_Official.objects.create(
            from_date=from_date, to_date=to_date)
        return CreateCtb_Emp_OfficialMutation(ctb_emp_official=ctb_emp_official)
