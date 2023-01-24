import graphene
from graphene import ObjectType, String, Decimal
from graphene_django import DjangoObjectType
from .models import *


class Ctb_AddressType(DjangoObjectType):
    class Meta:
        model = Ctb_Address


class Ctb_PersonType(DjangoObjectType):
    class Meta:
        model = Ctb_Person


class Query(graphene.ObjectType):

    ctb_addresses = graphene.List(Ctb_AddressType)

    def resolve_ctb_addresses(self, info, **kwargs):
        return Ctb_Address.objects.all()

    ctb_persons = graphene.List(Ctb_PersonType)

    def resolve_ctb_persons(self, info, **kwargs):
        return Ctb_Person.objects.all()


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


class Mutation(graphene.ObjectType):
    create_ctb_address = CreateCtb_AddressMutation.Field()
    create_ctb_person = CreateCtb_PersonMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
