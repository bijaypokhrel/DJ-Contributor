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


# Input Object Type

class Atb_Gltran_MastInput(graphene.InputObjectType):
    id = graphene.ID()
    office_code = Decimal()
    vch_no = String()
    vch_type_code = Decimal()
    cost_center_id = Decimal()
    tran_date = String()
    tran_user_id = String()
    is_approved = Decimal()
    approved_date = String()
    approved_user_id = String()
    is_reverse = Decimal()
    rev_vch_id = Decimal()
    vch_id = Decimal()
    tran_number = String()
    mast_desc = String()
    application_id = String()
    module_id = String()
    value_date = String()
    is_deleted = Decimal()


class Atb_Gltran_DetlInput(graphene.InputObjectType):
    id = graphene.ID()
    gltran_detl = Decimal()
    office_code = Decimal()
    gl_group_code = Decimal()
    ac_no = String()
    gl_id = Decimal()
    amount = Decimal()
    tran_desc = String()
    inst_code = String()
    inst_date = String()
    vch_id = Decimal()
    status = String()


class Atb_Account_LedgerInput(graphene.InputObjectType):
    id = graphene.ID()
    office_code = Decimal()
    gl_id = Decimal()
    value_date = String()
    fiscal_year = String()
    dr = Decimal()
    cr = Decimal()
    balance = Decimal()


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


class UpdateAtb_Gltran_MastMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        tran_date = String()
        tran_user_id = String()

    atb_gltran_mast = graphene.Field(lambda: Atb_Gltran_MastType)

    def mutate(self, info, id, tran_date, tran_user_id):
        atb_gltran_mast = Atb_Gltran_Mast.objects.get(pk=id)
        atb_gltran_mast.tran_date = tran_date
        atb_gltran_mast.tran_user_id = tran_user_id
        atb_gltran_mast.save()
        return UpdateAtb_Gltran_MastMutation(atb_gltran_mast=atb_gltran_mast)


class DeleteAtb_Gltran_MastMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    atb_gltran_mast = graphene.Field(lambda: Atb_Gltran_MastType)

    def mutate(self, info, id):
        atb_gltran_mast = Atb_Gltran_Mast.objects.get(pk=id)
        atb_gltran_mast.delete()
        return


class SaveAtb_Gltran_MastMutation(graphene.Mutation):
    class Arguments:
        data = Atb_Gltran_MastInput()

    atb_gltran_mast = graphene.Field(
        lambda: Atb_Gltran_MastType)

    def mutate(self, info, data):

        id = data.id
        if id:
            atb_gltran_mast = Atb_Gltran_Mast.objects.get(
                pk=id)
            for key, value in data.items():
                setattr(atb_gltran_mast, key, value)
            atb_gltran_mast.save()
        else:
            atb_gltran_mast = Atb_Gltran_Mast.objects.create(
                **data)
        return SaveAtb_Gltran_MastMutation(atb_gltran_mast=atb_gltran_mast)


class CreateAtb_Gltran_DetlMutation(graphene.Mutation):
    class Arguments:
        inst_code = String()
        inst_date = String()

    atb_gltran_detl = graphene.Field(lambda: Atb_Gltran_DetlType)

    def mutate(self, info, inst_code, inst_date):
        atb_gltran_detl = Atb_Gltran_Detl.objects.create(
            inst_code=inst_code, inst_date=inst_date)
        return CreateAtb_Gltran_DetlMutation(atb_gltran_detl=atb_gltran_detl)


class UpdateAtb_Gltran_DetlMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        inst_code = String()
        inst_date = String()

    atb_gltran_detl = graphene.Field(lambda: Atb_Gltran_DetlType)

    def mutate(self, info, id, inst_code, inst_date):
        atb_gltran_detl = Atb_Gltran_Detl.objects.get(pk=id)
        atb_gltran_detl.inst_code = inst_code
        atb_gltran_detl.inst_date = inst_date
        atb_gltran_detl.save()
        return UpdateAtb_Gltran_DetlMutation(atb_gltran_detl=atb_gltran_detl)


class DeleteAtb_Gltran_DetlMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    atb_gltran_detl = graphene.Field(lambda: Atb_Gltran_DetlType)

    def mutate(self, info, id):
        atb_gltran_detl = Atb_Gltran_Detl.objects.get(pk=id)
        atb_gltran_detl.delete()
        return


class SaveAtb_Gltran_DetlMutation(graphene.Mutation):
    class Arguments:
        data = Atb_Gltran_DetlInput()

    atb_gltran_detl = graphene.Field(
        lambda: Atb_Gltran_DetlType)

    def mutate(self, info, data):

        id = data.id
        if id:
            atb_gltran_detl = Atb_Gltran_Detl.objects.get(
                pk=id)
            for key, value in data.items():
                setattr(atb_gltran_detl, key, value)
            atb_gltran_detl.save()
        else:
            atb_gltran_detl = Atb_Gltran_Detl.objects.create(
                **data)
        return SaveAtb_Gltran_DetlMutation(atb_gltran_detl=atb_gltran_detl)


class CreateAtb_Account_LedgerMutation(graphene.Mutation):
    class Arguments:
        value_date = String()
        fiscal_year = String()

    atb_account_ledger = graphene.Field(lambda: Atb_Account_LedgerType)

    def mutate(self, info, value_date, fiscal_year):
        atb_account_ledger = Atb_Account_Ledger.objects.create(
            value_date=value_date, fiscal_year=fiscal_year)
        return CreateAtb_Account_LedgerMutation(atb_account_ledger=atb_account_ledger)


class UpdateAtb_Account_LedgerMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        value_date = String()
        fiscal_year = String()

    atb_account_ledger = graphene.Field(lambda: Atb_Account_LedgerType)

    def mutate(self, info, id, value_date, fiscal_year):
        atb_account_ledger = Atb_Account_Ledger.objects.get(pk=id)
        atb_account_ledger.value_date = value_date
        atb_account_ledger.fiscal_year = fiscal_year
        atb_account_ledger.save()
        return UpdateAtb_Account_LedgerMutation(atb_account_ledger=atb_account_ledger)


class DeleteAtb_Account_LedgerMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    atb_account_ledger = graphene.Field(lambda: Atb_Account_LedgerType)

    def mutate(self, info, id):
        atb_account_ledger = Atb_Account_Ledger.objects.get(pk=id)
        atb_account_ledger.delete()
        return


class SaveAtb_Account_LedgerMutation(graphene.Mutation):
    class Arguments:
        data = Atb_Account_LedgerInput()

    atb_account_ledger = graphene.Field(
        lambda: Atb_Account_LedgerType)

    def mutate(self, info, data):

        id = data.id
        if id:
            atb_account_ledger = Atb_Account_Ledger.objects.get(
                pk=id)
            for key, value in data.items():
                setattr(atb_account_ledger, key, value)
            atb_account_ledger.save()
        else:
            atb_account_ledger = Atb_Account_Ledger.objects.create(
                **data)
        return SaveAtb_Account_LedgerMutation(atb_account_ledger=atb_account_ledger)
