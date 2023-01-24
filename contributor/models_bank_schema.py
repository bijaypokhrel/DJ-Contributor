import graphene
from graphene import ObjectType, String, Decimal
from graphene_django import DjangoObjectType
from .models import *


class BankType(DjangoObjectType):
    class Meta:
        model = Bank
        fields = ("name", "capital")


class Query(graphene.ObjectType):
    banks = graphene.List(BankType)

    def resolve_banks(self, info, **kwargs):
        return Bank.objects.all()


class CreateBankMutation(graphene.Mutation):
    class Arguments:
        name = String()
        capital = Decimal()

    bank = graphene.Field(lambda: BankType)

    def mutate(self, info, name, capital):
        bank = Bank.objects.create(name=name, capital=capital)
        return CreateBankMutation(bank=bank)


class Mutation(graphene.ObjectType):
    create_bank = CreateBankMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
