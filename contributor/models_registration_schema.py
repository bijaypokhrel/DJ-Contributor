import graphene
from graphene import ObjectType, String, Decimal
from graphene_django import DjangoObjectType
from .models import *

# Query


class Ctb_AddressType(DjangoObjectType):
    class Meta:
        model = Ctb_Address


class Ctb_PersonType(DjangoObjectType):
    class Meta:
        model = Ctb_Person


class Ctb_Person_AddressType(DjangoObjectType):
    class Meta:
        model = Ctb_Person_Address


class Ctb_Person_DependentType(DjangoObjectType):
    class Meta:
        model = Ctb_Person_Dependent


class Ctb_Person_NomineeType(DjangoObjectType):
    class Meta:
        model = Ctb_Person_Nominee


class Ctb_Person_ContactType(DjangoObjectType):
    class Meta:
        model = Ctb_Person_Contact


class Ctb_Person_DocType(DjangoObjectType):
    class Meta:
        model = Ctb_Person_Doc


class Ctb_ContributorType(DjangoObjectType):
    class Meta:
        model = Ctb_Contributor


# Mutations
class CreateCtb_AddressMutation(graphene.Mutation):
    class Arguments:
        district_cd = String()
        vdc_cd = String()

    ctb_address = graphene.Field(lambda: Ctb_AddressType)

    def mutate(self, info, district_cd, vdc_cd):
        ctb_address = Ctb_Address.objects.create(
            district_cd=district_cd, vdc_cd=vdc_cd)
        return CreateCtb_AddressMutation(ctb_address=ctb_address)


class CreateCtb_PersonMutation(graphene.Mutation):
    class Arguments:
        fname_nep = String()
        mname_nep = String()

    ctb_person = graphene.Field(lambda: Ctb_PersonType)

    def mutate(self, info, fname_nep, mname_nep):
        ctb_person = Ctb_Person.objects.create(
            fname_nep=fname_nep, mname_nep=mname_nep)
        return CreateCtb_PersonMutation(ctb_person=ctb_person)


class CreateCtb_Person_AddressMutation(graphene.Mutation):
    class Arguments:
        from_date = String()
        to_date = String()

    ctb_person_address = graphene.Field(lambda: Ctb_Person_AddressType)

    def mutate(self, info, from_date, to_date):
        ctb_person_address = Ctb_Person_Address.objects.create(
            from_date=from_date, to_date=to_date)
        return CreateCtb_Person_AddressMutation(ctb_person_address=ctb_person_address)


class CreateCtb_Person_DependentMutation(graphene.Mutation):
    class Arguments:
        entry_by = String()
        r_status = String()

    ctb_person_dependent = graphene.Field(lambda: Ctb_Person_DependentType)

    def mutate(self, info, entry_by, r_status):
        ctb_person_dependent = Ctb_Person_Dependent.objects.create(
            entry_by=entry_by, r_status=r_status)
        return CreateCtb_Person_DependentMutation(ctb_person_dependent=ctb_person_dependent)


class CreateCtb_Person_NomineeMutation(graphene.Mutation):
    class Arguments:
        from_date = String()
        to_date = String()

    ctb_person_nominee = graphene.Field(lambda: Ctb_Person_NomineeType)

    def mutate(self, info, from_date, to_date):
        ctb_person_nominee = Ctb_Person_Nominee.objects.create(
            from_date=from_date, to_date=to_date)
        return CreateCtb_Person_NomineeMutation(ctb_person_nominee=ctb_person_nominee)


class CreateCtb_Person_ContactMutation(graphene.Mutation):
    class Arguments:
        from_date = String()
        to_date = String()

    ctb_person_contact = graphene.Field(lambda: Ctb_Person_ContactType)

    def mutate(self, info, from_date, to_date):
        ctb_person_contact = Ctb_Person_Contact.objects.create(
            from_date=from_date, to_date=to_date)
        return CreateCtb_Person_ContactMutation(ctb_person_contact=ctb_person_contact)


class CreateCtb_Person_DocMutation(graphene.Mutation):
    class Arguments:
        from_date = String()
        to_date = String()

    ctb_person_doc = graphene.Field(lambda: Ctb_Person_DocType)

    def mutate(self, info, from_date, to_date):
        ctb_person_doc = Ctb_Person_Doc.objects.create(
            from_date=from_date, to_date=to_date)
        return CreateCtb_Person_DocMutation(ctb_person_doc=ctb_person_doc)


class CreateCtb_ContributorMutation(graphene.Mutation):
    class Arguments:
        from_date = String()
        to_date = String()

    ctb_contributor = graphene.Field(lambda: Ctb_ContributorType)

    def mutate(self, info, from_date, to_date):
        ctb_contributor = Ctb_Contributor.objects.create(
            from_date=from_date, to_date=to_date)
        return CreateCtb_ContributorMutation(ctb_contributor=ctb_contributor)
