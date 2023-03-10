import graphene
from graphene import ObjectType, String, Decimal
from graphene_django import DjangoObjectType
from .models import *

# Query


class Atb_Gltran_MastType(DjangoObjectType):
    class Meta:
        model = Atb_Gltran_Mast


class Atb_Gltran_DetlType(DjangoObjectType):
    class Meta:
        model = Atb_Gltran_Detl


class Atb_Account_LedgerType(DjangoObjectType):
    class Meta:
        model = Atb_Account_Ledger


# Mutation


class CreateAtb_Gltran_MastMutation(graphene.Mutation):
    class Arguments:
        tran_date = String()
        tran_user_id = String()

    atb_gltran_mast = graphene.Field(lambda: Atb_Gltran_MastType)

    def mutate(self, info, tran_date, tran_user_id):
        atb_gltran_mast = Atb_Gltran_Mast.objects.create(
            tran_date=tran_date, tran_user_id=tran_user_id)
        return CreateAtb_Gltran_MastMutation(atb_gltran_mast=atb_gltran_mast)


class CreateAtb_Gltran_DetlMutation(graphene.Mutation):
    class Arguments:
        inst_code = String()
        inst_date = String()

    atb_gltran_detl = graphene.Field(lambda: Atb_Gltran_DetlType)

    def mutate(self, info, inst_code, inst_date):
        atb_gltran_detl = Atb_Gltran_Detl.objects.create(
            inst_code=inst_code, inst_date=inst_date)
        return CreateAtb_Gltran_DetlMutation(atb_gltran_detl=atb_gltran_detl)


class CreateAtb_Account_LedgerMutation(graphene.Mutation):
    class Arguments:
        value_date = String()
        fiscal_year = String()

    atb_account_ledger = graphene.Field(lambda: Atb_Account_LedgerType)

    def mutate(self, info, value_date, fiscal_year):
        atb_account_ledger = Atb_Account_Ledger.objects.create(
            value_date=value_date, fiscal_year=fiscal_year)
        return CreateAtb_Account_LedgerMutation(atb_account_ledger=atb_account_ledger)
