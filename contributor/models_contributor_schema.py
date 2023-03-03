import graphene
from graphene import ObjectType, String, Decimal
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
