import graphene
from graphene import ObjectType, String, Decimal, Date
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


class Ctb_ContributorInput(graphene.InputObjectType):
    id = graphene.ID()
    p_ssid = String()
    employer_id = Decimal()
    from_date = String()
    to_date = String()
    post = String()
    emptype_id = Decimal()
    joining_date = String()
    termination_date = String()
    termination_res = String()
    entry_by = String()
    entry_date = Date()
    r_status = String()
    tran_no = Decimal()
    terminated_by = String()
    new_tran = Decimal()
    marking = String()
    group_id = Decimal()
    contributor_type = String()


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


class UpdateCtb_AddressMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        district_cd = String()
        vdc_cd = String()

    ctb_address = graphene.Field(lambda: Ctb_AddressType)

    def mutate(self, info, id, district_cd, vdc_cd):
        ctb_address = Ctb_Address.objects.get(pk=id)
        ctb_address.district_cd = district_cd
        ctb_address.vdc_cd = vdc_cd
        ctb_address.save()
        return UpdateCtb_AddressMutation(ctb_address=ctb_address)


class DeleteCtb_AddressMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    ctb_address = graphene.Field(lambda: Ctb_AddressType)

    def mutate(self, info, id):
        ctb_address = Ctb_Address.objects.get(pk=id)
        ctb_address.delete()
        return


class CreateCtb_PersonMutation(graphene.Mutation):
    class Arguments:
        fname_nep = String()
        mname_nep = String()

    ctb_person = graphene.Field(lambda: Ctb_PersonType)

    def mutate(self, info, fname_nep, mname_nep):
        ctb_person = Ctb_Person.objects.create(
            fname_nep=fname_nep, mname_nep=mname_nep)
        return CreateCtb_PersonMutation(ctb_person=ctb_person)


class UpdateCtb_PersonMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        fname_nep = String()
        mname_nep = String()

    ctb_person = graphene.Field(lambda: Ctb_PersonType)

    def mutate(self, info, id, fname_nep, mname_nep):
        ctb_person = Ctb_Person.objects.get(pk=id)
        ctb_person.fname_nep = fname_nep
        ctb_person.mname_nep = mname_nep
        ctb_person.save()
        return UpdateCtb_PersonMutation(ctb_person=ctb_person)


class DeleteCtb_PersonMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    ctb_person = graphene.Field(lambda: Ctb_PersonType)

    def mutate(self, info, id):
        ctb_person = Ctb_Person.objects.get(pk=id)
        ctb_person.delete()
        return


class CreateCtb_Person_AddressMutation(graphene.Mutation):
    class Arguments:
        from_date = String()
        to_date = String()

    ctb_person_address = graphene.Field(lambda: Ctb_Person_AddressType)

    def mutate(self, info, from_date, to_date):
        ctb_person_address = Ctb_Person_Address.objects.create(
            from_date=from_date, to_date=to_date)
        return CreateCtb_Person_AddressMutation(ctb_person_address=ctb_person_address)


class UpdateCtb_Person_AddressMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        from_date = String()
        to_date = String()

    ctb_person_address = graphene.Field(lambda: Ctb_Person_AddressType)

    def mutate(self, info, id, from_date, to_date):
        ctb_person_address = Ctb_Person_Address.objects.get(pk=id)
        ctb_person_address.from_date = from_date
        ctb_person_address.to_date = to_date
        ctb_person_address.save()
        return CreateCtb_Person_AddressMutation(ctb_person_address=ctb_person_address)


class DeleteCtb_Person_AddressMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    ctb_person_address = graphene.Field(lambda: Ctb_Person_AddressType)

    def mutate(self, info, id):
        ctb_person_address = Ctb_Person_Address.objects.get(pk=id)
        ctb_person_address.delete()
        return


class CreateCtb_Person_DependentMutation(graphene.Mutation):
    class Arguments:
        entry_by = String()
        r_status = String()

    ctb_person_dependent = graphene.Field(lambda: Ctb_Person_DependentType)

    def mutate(self, info, entry_by, r_status):
        ctb_person_dependent = Ctb_Person_Dependent.objects.create(
            entry_by=entry_by, r_status=r_status)
        return CreateCtb_Person_DependentMutation(ctb_person_dependent=ctb_person_dependent)


class UpdateCtb_Person_DependentMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        entry_by = String()
        r_status = String()

    ctb_person_dependent = graphene.Field(lambda: Ctb_Person_DependentType)

    def mutate(self, info, id, entry_by, r_status):
        ctb_person_dependent = Ctb_Person_Dependent.objects.get(pk=id)
        ctb_person_dependent.entry_by = entry_by
        ctb_person_dependent.r_status = r_status
        ctb_person_dependent.save()
        return UpdateCtb_Person_DependentMutation(ctb_person_dependent=ctb_person_dependent)


class DeleteCtb_Person_DependentMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    ctb_person_dependent = graphene.Field(lambda: Ctb_Person_DependentType)

    def mutate(self, info, id):
        ctb_person_dependent = Ctb_Person_Dependent.objects.get(pk=id)
        ctb_person_dependent.delete()
        return


class CreateCtb_Person_NomineeMutation(graphene.Mutation):
    class Arguments:
        from_date = String()
        to_date = String()

    ctb_person_nominee = graphene.Field(lambda: Ctb_Person_NomineeType)

    def mutate(self, info, from_date, to_date):
        ctb_person_nominee = Ctb_Person_Nominee.objects.create(
            from_date=from_date, to_date=to_date)
        return CreateCtb_Person_NomineeMutation(ctb_person_nominee=ctb_person_nominee)


class UpdateCtb_Person_NomineeMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        from_date = String()
        to_date = String()

    ctb_person_nominee = graphene.Field(lambda: Ctb_Person_NomineeType)

    def mutate(self, info, id, from_date, to_date):
        ctb_person_nominee = Ctb_Person_Nominee.objects.get(pk=id)
        ctb_person_nominee.from_date = from_date
        ctb_person_nominee.to_date = to_date
        ctb_person_nominee.save()
        return UpdateCtb_Person_NomineeMutation(ctb_person_nominee=ctb_person_nominee)


class DeleteCtb_Person_NomineeMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    ctb_person_nominee = graphene.Field(lambda: Ctb_Person_NomineeType)

    def mutate(self, info, id):
        ctb_person_nominee = Ctb_Person_Nominee.objects.get(pk=id)
        ctb_person_nominee.delete()
        return


class CreateCtb_Person_ContactMutation(graphene.Mutation):
    class Arguments:
        from_date = String()
        to_date = String()

    ctb_person_contact = graphene.Field(lambda: Ctb_Person_ContactType)

    def mutate(self, info, from_date, to_date):
        ctb_person_contact = Ctb_Person_Contact.objects.create(
            from_date=from_date, to_date=to_date)
        return CreateCtb_Person_ContactMutation(ctb_person_contact=ctb_person_contact)


class UpdateCtb_Person_ContactMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        from_date = String()
        to_date = String()

    ctb_person_contact = graphene.Field(lambda: Ctb_Person_ContactType)

    def mutate(self, info, id, from_date, to_date):
        ctb_person_contact = Ctb_Person_Contact.objects.get(pk=id)
        ctb_person_contact.from_date = from_date
        ctb_person_contact.to_date = to_date
        ctb_person_contact.save()
        return UpdateCtb_Person_ContactMutation(ctb_person_contact=ctb_person_contact)


class DeleteCtb_Person_ContactMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    ctb_person_contact = graphene.Field(lambda: Ctb_Person_ContactType)

    def mutate(self, info, id):
        ctb_person_contact = Ctb_Person_Contact.objects.get(pk=id)
        ctb_person_contact.delete()
        return


class CreateCtb_Person_DocMutation(graphene.Mutation):
    class Arguments:
        from_date = String()
        to_date = String()

    ctb_person_doc = graphene.Field(lambda: Ctb_Person_DocType)

    def mutate(self, info, from_date, to_date):
        ctb_person_doc = Ctb_Person_Doc.objects.create(
            from_date=from_date, to_date=to_date)
        return CreateCtb_Person_DocMutation(ctb_person_doc=ctb_person_doc)


class UpdateCtb_Person_DocMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        from_date = String()
        to_date = String()

    ctb_person_doc = graphene.Field(lambda: Ctb_Person_DocType)

    def mutate(self, info, id, from_date, to_date):
        ctb_person_doc = Ctb_Person_Doc.objects.get(pk=id)
        ctb_person_doc.from_date = from_date
        ctb_person_doc.to_date = to_date
        ctb_person_doc.save()
        return UpdateCtb_Person_DocMutation(ctb_person_doc=ctb_person_doc)


class DeleteCtb_Person_DocMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    ctb_person_doc = graphene.Field(lambda: Ctb_Person_DocType)

    def mutate(self, info, id):
        ctb_person_doc = Ctb_Person_Doc.objects.get(pk=id)
        ctb_person_doc.delete()
        return


class CreateCtb_ContributorMutation(graphene.Mutation):
    class Arguments:
        from_date = String()
        to_date = String()

    ctb_contributor = graphene.Field(lambda: Ctb_ContributorType)

    def mutate(self, info, from_date, to_date):
        ctb_contributor = Ctb_Contributor.objects.create(
            from_date=from_date, to_date=to_date)
        return CreateCtb_ContributorMutation(ctb_contributor=ctb_contributor)


class UpdateCtb_ContributorMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        from_date = String()
        to_date = String()

    ctb_contributor = graphene.Field(lambda: Ctb_ContributorType)

    def mutate(self, info, id, from_date, to_date):
        ctb_contributor = Ctb_Contributor.objects.get(pk=id)
        ctb_contributor.from_date = from_date
        ctb_contributor.to_date = to_date
        ctb_contributor.save()
        return UpdateCtb_ContributorMutation(ctb_contributor=ctb_contributor)


class DeleteCtb_ContributorMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    ctb_contributor = graphene.Field(lambda: Ctb_ContributorType)

    def mutate(self, info, id):
        ctb_contributor = Ctb_Contributor.objects.get(pk=id)
        ctb_contributor.delete()
        return


class SaveCtb_ContributorMutation(graphene.Mutation):
    class Arguments:
        data = Ctb_ContributorInput()

    ctb_contributor = graphene.Field(lambda: Ctb_ContributorType)

    def mutate(self, info, data):

        id = data.id
        if id:
            ctb_contributor = Ctb_Contributor.objects.get(pk=id)
            ctb_contributor.from_date = data.from_date
            ctb_contributor.to_date = data.to_date
            ctb_contributor.save()
        else:
            ctb_contributor = Ctb_Contributor.objects.create(**data)
        return CreateCtb_ContributorMutation(ctb_contributor=ctb_contributor)
