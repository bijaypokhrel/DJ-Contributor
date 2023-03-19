import graphene
from graphene import ObjectType, String, Decimal, Date
from graphene_django import DjangoObjectType
from .models import *


# Query

class Stb_Coll_Voucher_InfoType(DjangoObjectType):
    class Meta:
        model = Stb_Coll_Voucher_Info


class Stb_Contributor_Sal_DetType(DjangoObjectType):
    class Meta:
        model = Stb_Contributor_Sal_Det


class Stb_Collection_Tran_HeadType(DjangoObjectType):
    class Meta:
        model = Stb_Collection_Tran_Head


class Stb_Coll_Tran_DetailsType(DjangoObjectType):
    class Meta:
        model = Stb_Coll_Tran_Details


class Stb_Scheme_ApplicationType(DjangoObjectType):
    class Meta:
        model = Stb_Scheme_Application


# Input Object Type


class Stb_Coll_Voucher_InfoInput(graphene.InputObjectType):
    id = graphene.ID()
    employer_id = Decimal()
    tran_no = Decimal()
    bank_id = Decimal()
    voucher_no = String()
    account_no = String()
    voucher_date = String()
    amount = Decimal()
    r_status = String()
    voh_id = Decimal()
    branch_id = Decimal()
    booked_date = String()
    from_bank_id = Decimal()
    from_branch_id = Decimal()
    from_account_no = String()
    remarks = String()


class Stb_Contributor_Sal_DetInput(graphene.InputObjectType):
    id = graphene.ID()
    p_ssid = String()
    basic_sal = Decimal()
    grade = Decimal()
    from_date = String()
    to_date = String()
    entry_by = String()
    entry_date = Date()
    r_status = String()
    amount = Decimal()
    tran_no = Decimal()
    employer_id = Decimal()
    coll_year = Decimal()
    coll_month = Decimal()
    remarks = String()
    is_regular = String()


class Stb_Collection_Tran_HeadInput(graphene.InputObjectType):
    id = graphene.ID()
    employer_id = Decimal()
    tran_no = Decimal()
    tran_date = String()
    total_amount = Decimal()
    int_amount = Decimal()
    pena_amount = Decimal()
    entry_by = String()
    entry_date = Date()
    r_status = String()
    cont_from_date = String()
    cont_to_date = String()
    t_no = Decimal()
    coll_year = Decimal()
    coll_month = Decimal()
    duepenalty_amount = Decimal()
    calendar = String()
    regularity_status = String()


class Stb_Coll_Tran_DetailsInput(graphene.InputObjectType):
    id = graphene.ID()
    p_ssid = String()
    employer_id = Decimal()
    c_from_date = String()
    from_date = String()
    schapp_id = String()
    tran_no = String()
    amount = Decimal()
    entry_by = String()
    entry_date = Date()
    r_status = String()
    cont_from_date = String()
    cont_to_date = String()
    coll_year = Decimal()
    coll_month = Decimal()


class Stb_Scheme_ApplicationInput(graphene.InputObjectType):
    id = graphene.ID()
    schapp_desc = String()
    schapp_desc_eng = String()
    status = String()
    scheme_percent = Decimal()
    order_no = Decimal()
    gl_code = Decimal()
    p_gl_code = Decimal()
    used_by = String()
    coll_type = String()
    parent_schapp_id = Decimal()
    calculation_by_percentage = String()
    amount_type = String()
    claim_type = String()


# Mutation


class CreateStb_Coll_Voucher_InfoMutation(graphene.Mutation):
    class Arguments:
        voucher_no = String()
        account_no = String()

    stb_coll_voucher_info = graphene.Field(lambda: Stb_Coll_Voucher_InfoType)

    def mutate(self, info, voucher_no, account_no):
        stb_coll_voucher_info = Stb_Coll_Voucher_Info.objects.create(
            voucher_no=voucher_no, account_no=account_no)
        return CreateStb_Coll_Voucher_InfoMutation(stb_coll_voucher_info=stb_coll_voucher_info)


class UpdateStb_Coll_Voucher_InfoMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        voucher_no = String()
        account_no = String()

    stb_coll_voucher_info = graphene.Field(lambda: Stb_Coll_Voucher_InfoType)

    def mutate(self, info, id, voucher_no, account_no):
        stb_coll_voucher_info = Stb_Coll_Voucher_Info.objects.get(pk=id)
        stb_coll_voucher_info.voucher_no = voucher_no
        stb_coll_voucher_info.account_no = account_no
        stb_coll_voucher_info.save()
        return UpdateStb_Coll_Voucher_InfoMutation(stb_coll_voucher_info=stb_coll_voucher_info)


class DeleteStb_Coll_Voucher_InfoMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    stb_coll_voucher_info = graphene.Field(lambda: Stb_Coll_Voucher_InfoType)

    def mutate(self, info, id):
        stb_coll_voucher_info = Stb_Coll_Voucher_Info.objects.get(pk=id)
        stb_coll_voucher_info.delete()
        return


class SaveStb_Coll_Voucher_InfoMutation(graphene.Mutation):
    class Arguments:
        data = Stb_Coll_Voucher_InfoInput()

    stb_coll_voucher_info = graphene.Field(
        lambda: Stb_Coll_Voucher_InfoType)

    def mutate(self, info, data):

        id = data.id
        if id:
            stb_coll_voucher_info = Stb_Coll_Voucher_Info.objects.get(
                pk=id)
            for key, value in data.items():
                setattr(stb_coll_voucher_info, key, value)
            stb_coll_voucher_info.save()
        else:
            stb_coll_voucher_info = Stb_Coll_Voucher_Info.objects.create(
                **data)
        return SaveStb_Coll_Voucher_InfoMutation(stb_coll_voucher_info=stb_coll_voucher_info)


class CreateStb_Contributor_Sal_DetMutation(graphene.Mutation):
    class Arguments:
        from_date = String()
        to_date = String()

    stb_contributor_sal_det = graphene.Field(
        lambda: Stb_Contributor_Sal_DetType)

    def mutate(self, info, from_date, to_date):
        stb_contributor_sal_det = Stb_Contributor_Sal_Det.objects.create(
            from_date=from_date, to_date=to_date)
        return CreateStb_Contributor_Sal_DetMutation(stb_contributor_sal_det=stb_contributor_sal_det)


class UpdateStb_Contributor_Sal_DetMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        from_date = String()
        to_date = String()

    stb_contributor_sal_det = graphene.Field(
        lambda: Stb_Contributor_Sal_DetType)

    def mutate(self, info, id, from_date, to_date):
        stb_contributor_sal_det = Stb_Contributor_Sal_Det.objects.get(pk=id)
        stb_contributor_sal_det.from_date = from_date
        stb_contributor_sal_det.to_date = to_date
        stb_contributor_sal_det.save()
        return UpdateStb_Contributor_Sal_DetMutation(stb_contributor_sal_det=stb_contributor_sal_det)


class DeleteStb_Contributor_Sal_DetMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    stb_contributor_sal_det = graphene.Field(
        lambda: Stb_Contributor_Sal_DetType)

    def mutate(self, info, id):
        stb_contributor_sal_det = Stb_Contributor_Sal_Det.objects.get(pk=id)
        stb_contributor_sal_det.delete()
        return


class SaveStb_Contributor_Sal_DetMutation(graphene.Mutation):
    class Arguments:
        data = Stb_Contributor_Sal_DetInput()

    stb_contributor_sal_det = graphene.Field(
        lambda: Stb_Contributor_Sal_DetType)

    def mutate(self, info, data):

        id = data.id
        if id:
            stb_contributor_sal_det = Stb_Contributor_Sal_Det.objects.get(
                pk=id)
            for key, value in data.items():
                setattr(stb_contributor_sal_det, key, value)
            stb_contributor_sal_det.save()
        else:
            stb_contributor_sal_det = Stb_Contributor_Sal_Det.objects.create(
                **data)
        return SaveStb_Contributor_Sal_DetMutation(stb_contributor_sal_det=stb_contributor_sal_det)


class CreateStb_Collection_Tran_HeadMutation(graphene.Mutation):
    class Arguments:
        entry_by = String()
        r_status = String()

    stb_collection_tran_head = graphene.Field(
        lambda: Stb_Collection_Tran_HeadType)

    def mutate(self, info, entry_by, r_status):
        stb_collection_tran_head = Stb_Collection_Tran_Head.objects.create(
            entry_by=entry_by, r_status=r_status)
        return CreateStb_Collection_Tran_HeadMutation(stb_collection_tran_head=stb_collection_tran_head)


class UpdateStb_Collection_Tran_HeadMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        entry_by = String()
        r_status = String()

    stb_collection_tran_head = graphene.Field(
        lambda: Stb_Collection_Tran_HeadType)

    def mutate(self, info, id, entry_by, r_status):
        stb_collection_tran_head = Stb_Collection_Tran_Head.objects.get(pk=id)
        stb_collection_tran_head.entry_by = entry_by
        stb_collection_tran_head.r_status = r_status
        stb_collection_tran_head.save()
        return UpdateStb_Collection_Tran_HeadMutation(stb_collection_tran_head=stb_collection_tran_head)


class DeleteStb_Collection_Tran_HeadMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    stb_collection_tran_head = graphene.Field(
        lambda: Stb_Collection_Tran_HeadType)

    def mutate(self, info, id):
        stb_collection_tran_head = Stb_Collection_Tran_Head.objects.get(pk=id)
        stb_collection_tran_head.delete()
        return


class SaveStb_Collection_Tran_HeadMutation(graphene.Mutation):
    class Arguments:
        data = Stb_Collection_Tran_HeadInput()

    stb_collection_tran_head = graphene.Field(
        lambda: Stb_Collection_Tran_HeadType)

    def mutate(self, info, data):

        id = data.id
        if id:
            stb_collection_tran_head = Stb_Collection_Tran_Head.objects.get(
                pk=id)
            for key, value in data.items():
                setattr(stb_collection_tran_head, key, value)
            stb_collection_tran_head.save()
        else:
            stb_collection_tran_head = Stb_Collection_Tran_Head.objects.create(
                **data)
        return SaveStb_Collection_Tran_HeadMutation(stb_collection_tran_head=stb_collection_tran_head)


class CreateStb_Coll_Tran_DetailsMutation(graphene.Mutation):
    class Arguments:
        entry_by = String()
        r_status = String()

    stb_coll_tran_detail = graphene.Field(
        lambda: Stb_Coll_Tran_DetailsType)

    def mutate(self, info, entry_by, r_status):
        stb_coll_tran_detail = Stb_Coll_Tran_Details.objects.create(
            entry_by=entry_by, r_status=r_status)
        return CreateStb_Coll_Tran_DetailsMutation(stb_coll_tran_detail=stb_coll_tran_detail)


class UpdateStb_Coll_Tran_DetailsMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        entry_by = String()
        r_status = String()

    stb_coll_tran_detail = graphene.Field(
        lambda: Stb_Coll_Tran_DetailsType)

    def mutate(self, info, id, entry_by, r_status):
        stb_coll_tran_detail = Stb_Coll_Tran_Details.objects.get(pk=id)
        stb_coll_tran_detail.entry_by = entry_by
        stb_coll_tran_detail.r_status = r_status
        stb_coll_tran_detail.save()
        return UpdateStb_Coll_Tran_DetailsMutation(stb_coll_tran_detail=stb_coll_tran_detail)


class DeleteStb_Coll_Tran_DetailsMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    stb_coll_tran_detail = graphene.Field(
        lambda: Stb_Coll_Tran_DetailsType)

    def mutate(self, info, id):
        stb_coll_tran_detail = Stb_Coll_Tran_Details.objects.get(pk=id)
        stb_coll_tran_detail.delete()
        return


class SaveStb_Coll_Tran_DetailsMutation(graphene.Mutation):
    class Arguments:
        data = Stb_Coll_Tran_DetailsInput()

    stb_coll_tran_details = graphene.Field(
        lambda: Stb_Coll_Tran_DetailsType)

    def mutate(self, info, data):

        id = data.id
        if id:
            stb_coll_tran_details = Stb_Coll_Tran_Details.objects.get(
                pk=id)
            for key, value in data.items():
                setattr(stb_coll_tran_details, key, value)
            stb_coll_tran_details.save()
        else:
            stb_coll_tran_details = Stb_Coll_Tran_Details.objects.create(
                **data)
        return SaveStb_Coll_Tran_DetailsMutation(stb_coll_tran_details=stb_coll_tran_details)


class CreateStb_Scheme_ApplicationMutation(graphene.Mutation):
    class Arguments:
        used_by = String()
        coll_type = String()

    stb_scheme_application = graphene.Field(
        lambda: Stb_Scheme_ApplicationType)

    def mutate(self, info, used_by, coll_type):
        stb_scheme_application = Stb_Scheme_Application.objects.create(
            used_by=used_by, coll_type=coll_type)
        return CreateStb_Scheme_ApplicationMutation(stb_scheme_application=stb_scheme_application)


class UpdateStb_Scheme_ApplicationMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        used_by = String()
        coll_type = String()

    stb_scheme_application = graphene.Field(
        lambda: Stb_Scheme_ApplicationType)

    def mutate(self, info, id, used_by, coll_type):
        stb_scheme_application = Stb_Scheme_Application.objects.get(pk=id)
        stb_scheme_application.used_by = used_by
        stb_scheme_application.coll_type = coll_type
        stb_scheme_application.save()
        return UpdateStb_Scheme_ApplicationMutation(stb_scheme_application=stb_scheme_application)


class DeleteStb_Scheme_ApplicationMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    stb_scheme_application = graphene.Field(
        lambda: Stb_Scheme_ApplicationType)

    def mutate(self, info, id):
        stb_scheme_application = Stb_Scheme_Application.objects.get(pk=id)
        stb_scheme_application.delete()
        return UpdateStb_Scheme_ApplicationMutation(stb_scheme_application=stb_scheme_application)


class SaveStb_Scheme_ApplicationMutation(graphene.Mutation):
    class Arguments:
        data = Stb_Scheme_ApplicationInput()

    stb_scheme_application = graphene.Field(
        lambda: Stb_Scheme_ApplicationType)

    def mutate(self, info, data):

        id = data.id
        if id:
            stb_scheme_application = Stb_Scheme_Application.objects.get(
                pk=id)
            for key, value in data.items():
                setattr(stb_scheme_application, key, value)
            stb_scheme_application.save()
        else:
            stb_scheme_application = Stb_Scheme_Application.objects.create(
                **data)
        return SaveStb_Scheme_ApplicationMutation(stb_scheme_application=stb_scheme_application)
