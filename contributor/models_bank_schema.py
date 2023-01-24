import graphene
from graphene import ObjectType, String, Decimal
from graphene_django import DjangoObjectType
from .models import *


# Query

class BankType(DjangoObjectType):
    class Meta:
        model = Bank

# Mutation


class CreateBankMutation(graphene.Mutation):
    class Arguments:
        name = String()
        capital = Decimal()

    bank = graphene.Field(lambda: BankType)

    def mutate(self, info, name, capital):
        bank = Bank.objects.create(name=name, capital=capital)
        return CreateBankMutation(bank=bank)
