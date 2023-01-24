import graphene
from graphene import ObjectType, String, Decimal
from graphene_django import DjangoObjectType
from .models import *

# Query


class Stb_Claim_HeadType(DjangoObjectType):
    class Meta:
        model = Stb_Claim_Head


class Stb_Claim_Anusuchi6Type(DjangoObjectType):
    class Meta:
        model = Stb_Claim_Anusuchi6


class Stb_Claim_App_AmountType(DjangoObjectType):
    class Meta:
        model = Stb_Claim_App_Amount


class Stb_Claim_DocType(DjangoObjectType):
    class Meta:
        model = Stb_Claim_Doc


# Mutation
class CreateStb_Claim_HeadMutation(graphene.Mutation):
    class Arguments:
        account_type = String()
        account_number = String()

    stb_claim_head = graphene.Field(lambda: Stb_Claim_HeadType)

    def mutate(self, info, account_type, account_number):
        stb_claim_head = Stb_Claim_Head.objects.create(
            account_type=account_type, account_number=account_number)
        return CreateStb_Claim_HeadMutation(stb_claim_head=stb_claim_head)


class CreateStb_Claim_Anusuchi6Mutation(graphene.Mutation):
    class Arguments:
        dep_fname = String()
        dep_mname = String()

    stb_claim_anusuchi6 = graphene.Field(lambda: Stb_Claim_Anusuchi6Type)

    def mutate(self, info, dep_fname, dep_mname):
        stb_claim_anusuchi6 = Stb_Claim_Anusuchi6.objects.create(
            dep_fname=dep_fname, dep_mname=dep_mname)
        return CreateStb_Claim_Anusuchi6Mutation(stb_claim_anusuchi6=stb_claim_anusuchi6)


class CreateStb_Claim_App_AmountMutation(graphene.Mutation):
    class Arguments:
        p_ssid = String()
        claim_app_date = String()

    stb_claim_app_amount = graphene.Field(lambda: Stb_Claim_App_AmountType)

    def mutate(self, info, p_ssid, claim_app_date):
        stb_claim_app_amount = Stb_Claim_App_Amount.objects.create(
            p_ssid=p_ssid, claim_app_date=claim_app_date)
        return CreateStb_Claim_App_AmountMutation(stb_claim_app_amount=stb_claim_app_amount)


class CreateStb_Claim_DocMutation(graphene.Mutation):
    class Arguments:
        doc_path = String()
        entry_by = String()

    stb_claim_doc = graphene.Field(lambda: Stb_Claim_DocType)

    def mutate(self, info, doc_path, entry_by):
        stb_claim_doc = Stb_Claim_Doc.objects.create(
            doc_path=doc_path, entry_by=entry_by)
        return CreateStb_Claim_DocMutation(stb_claim_doc=stb_claim_doc)
