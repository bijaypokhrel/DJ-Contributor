import graphene
from graphene import ObjectType, String, Decimal, Date
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


# Input Object Type


class Stb_Claim_HeadInput(graphene.InputObjectType):
    id = graphene.ID()
    ssfid = String()
    schapp_id = Decimal()
    sch_id = Decimal()
    claim_app_date = String()
    anusuchi_no = Decimal()
    bank_id = Decimal()
    account_type = String()
    account_number = String()
    bank_address = String()
    recommend_by = String()
    recomm_emp_post = String()
    recomm_emp_phone = String()
    recommend_date = String()
    entry_by = String()
    entry_date = Date()
    r_status = String()
    tran_no = Decimal()
    approved_amount = Decimal()
    approved_by = String()
    approved_post = String()
    approved_date = String()
    is_death = String()
    claim_amount = Decimal()
    employer_id = Decimal()
    # approval_doc = FileField()
    remarks = String()
    p_id = String()
    h_code = String()
    claim_date = String()
    claim_id = String()
    leave_from_date = String()
    leave_to_date = String()
    bank_branch_id = Decimal()
    account_name = String()
    save_mode = String()
    is_admin_recommended = String()
    admin_recommender = String()
    admin_recommend_date = String()
    is_payment_rejected = String()
    payment_rejecter = String()
    payment_rejected_date = String()
    payment_reject_remarks = String()
    admin_recommender_post = String()
    entry_by_post = String()
    ref_no = String()
    payee_id = Decimal()
    tax_amount = Decimal()
    return_amount = Decimal()
    person_id = Decimal()


class Stb_Claim_Anusuchi6Input(graphene.InputObjectType):
    id = graphene.ID()
    p_ssid = String()
    sch_id = Decimal()
    schapp_id = Decimal()
    permanent_disability_type = String()
    permanent_disability_date = String()
    permanent_disability_reason = String()
    death_date = String()
    death_reason = String()
    dep_person_relation = String()
    no_of_children_below_18 = Decimal()
    approved_amount = Decimal()
    amount_received_by = String()
    r_status = String()
    entry_by = String()
    entry_date = Date()
    tran_no = Decimal()
    claim_app_date = String()
    dep_fname = String()
    dep_mname = String()
    dep_lname = String()
    average_basic = Decimal()
    remarks = String()
    person_id = Decimal()


class Stb_Claim_App_AmountInput(graphene.InputObjectType):
    id = graphene.ID()
    tran_no = Decimal()
    sch_app_id = Decimal()
    sch_id = Decimal()
    p_ssid = String()
    claim_amount = Decimal()
    claim_app_date = String()
    person_id = Decimal()


class Stb_Claim_DocInput(graphene.InputObjectType):
    id = graphene.ID()
    ssfid = String()
    schapp_id = Decimal()
    sch_id = Decimal()
    claim_app_date = String()
    chk_doc_id = Decimal()
    doc_path = String()
    # doc_image = ImageField()
    entry_by = String()
    entry_date = Date()
    r_status = String()
    tran_no = Decimal()


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


class UpdateStb_Claim_HeadMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        account_type = String()
        account_number = String()

    stb_claim_head = graphene.Field(lambda: Stb_Claim_HeadType)

    def mutate(self, info, id, account_type, account_number):
        stb_claim_head = Stb_Claim_Head.objects.get(pk=id)
        stb_claim_head.account_type = account_type
        stb_claim_head.account_number = account_number
        stb_claim_head.save()
        return UpdateStb_Claim_HeadMutation(stb_claim_head=stb_claim_head)


class DeleteStb_Claim_HeadMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    stb_claim_head = graphene.Field(lambda: Stb_Claim_HeadType)

    def mutate(self, info, id):
        stb_claim_head = Stb_Claim_Head.objects.get(pk=id)
        stb_claim_head.delete()
        return


class SaveStb_Claim_HeadMutation(graphene.Mutation):
    class Arguments:
        data = Stb_Claim_HeadInput()

    stb_claim_head = graphene.Field(
        lambda: Stb_Claim_HeadType)

    def mutate(self, info, data):

        id = data.id
        if id:
            stb_claim_head = Stb_Claim_Head.objects.get(
                pk=id)
            for key, value in data.items():
                setattr(stb_claim_head, key, value)
            stb_claim_head.save()
        else:
            stb_claim_head = Stb_Claim_Head.objects.create(
                **data)
        return SaveStb_Claim_HeadMutation(stb_claim_head=stb_claim_head)


class CreateStb_Claim_Anusuchi6Mutation(graphene.Mutation):
    class Arguments:
        dep_fname = String()
        dep_mname = String()

    stb_claim_anusuchi6 = graphene.Field(lambda: Stb_Claim_Anusuchi6Type)

    def mutate(self, info, dep_fname, dep_mname):
        stb_claim_anusuchi6 = Stb_Claim_Anusuchi6.objects.create(
            dep_fname=dep_fname, dep_mname=dep_mname)
        return CreateStb_Claim_Anusuchi6Mutation(stb_claim_anusuchi6=stb_claim_anusuchi6)


class UpdateStb_Claim_Anusuchi6Mutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        dep_fname = String()
        dep_mname = String()

    stb_claim_anusuchi6 = graphene.Field(lambda: Stb_Claim_Anusuchi6Type)

    def mutate(self, info, id, dep_fname, dep_mname):
        stb_claim_anusuchi6 = Stb_Claim_Anusuchi6.objects.get(pk=id)
        stb_claim_anusuchi6.dep_fname = dep_fname
        stb_claim_anusuchi6.dep_mname = dep_mname
        stb_claim_anusuchi6.save()
        return UpdateStb_Claim_Anusuchi6Mutation(stb_claim_anusuchi6=stb_claim_anusuchi6)


class DeleteStb_Claim_Anusuchi6Mutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    stb_claim_anusuchi6 = graphene.Field(lambda: Stb_Claim_Anusuchi6Type)

    def mutate(self, info, id):
        stb_claim_anusuchi6 = Stb_Claim_Anusuchi6.objects.get(pk=id)
        stb_claim_anusuchi6.delete()
        return


class SaveStb_Claim_Anusuchi6Mutation(graphene.Mutation):
    class Arguments:
        data = Stb_Claim_Anusuchi6Input()

    stb_claim_anusuchi6 = graphene.Field(
        lambda: Stb_Claim_Anusuchi6Type)

    def mutate(self, info, data):

        id = data.id
        if id:
            stb_claim_anusuchi6 = Stb_Claim_Anusuchi6.objects.get(
                pk=id)
            for key, value in data.items():
                setattr(stb_claim_anusuchi6, key, value)
            stb_claim_anusuchi6.save()
        else:
            stb_claim_anusuchi6 = Stb_Claim_Anusuchi6.objects.create(
                **data)
        return SaveStb_Claim_Anusuchi6Mutation(stb_claim_anusuchi6=stb_claim_anusuchi6)


class CreateStb_Claim_App_AmountMutation(graphene.Mutation):
    class Arguments:
        p_ssid = String()
        claim_app_date = String()

    stb_claim_app_amount = graphene.Field(lambda: Stb_Claim_App_AmountType)

    def mutate(self, info, p_ssid, claim_app_date):
        stb_claim_app_amount = Stb_Claim_App_Amount.objects.create(
            p_ssid=p_ssid, claim_app_date=claim_app_date)
        return CreateStb_Claim_App_AmountMutation(stb_claim_app_amount=stb_claim_app_amount)


class UpdateStb_Claim_App_AmountMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        p_ssid = String()
        claim_app_date = String()

    stb_claim_app_amount = graphene.Field(lambda: Stb_Claim_App_AmountType)

    def mutate(self, info, id, p_ssid, claim_app_date):
        stb_claim_app_amount = Stb_Claim_App_Amount.objects.get(pk=id)
        stb_claim_app_amount.p_ssid = p_ssid
        stb_claim_app_amount.claim_app_date = claim_app_date
        stb_claim_app_amount.save()
        return UpdateStb_Claim_App_AmountMutation(stb_claim_app_amount=stb_claim_app_amount)


class DeleteStb_Claim_App_AmountMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    stb_claim_app_amount = graphene.Field(lambda: Stb_Claim_App_AmountType)

    def mutate(self, info, id):
        stb_claim_app_amount = Stb_Claim_App_Amount.objects.get(pk=id)
        stb_claim_app_amount.delete()
        return


class SaveStb_Claim_App_AmountMutation(graphene.Mutation):
    class Arguments:
        data = Stb_Claim_App_AmountInput()

    stb_claim_app_amount = graphene.Field(
        lambda: Stb_Claim_App_AmountType)

    def mutate(self, info, data):

        id = data.id
        if id:
            stb_claim_app_amount = Stb_Claim_App_Amount.objects.get(
                pk=id)
            for key, value in data.items():
                setattr(stb_claim_app_amount, key, value)
            stb_claim_app_amount.save()
        else:
            stb_claim_app_amount = Stb_Claim_App_Amount.objects.create(
                **data)
        return SaveStb_Claim_App_AmountMutation(stb_claim_app_amount=stb_claim_app_amount)


class CreateStb_Claim_DocMutation(graphene.Mutation):
    class Arguments:
        doc_path = String()
        entry_by = String()

    stb_claim_doc = graphene.Field(lambda: Stb_Claim_DocType)

    def mutate(self, info, doc_path, entry_by):
        stb_claim_doc = Stb_Claim_Doc.objects.create(
            doc_path=doc_path, entry_by=entry_by)
        return CreateStb_Claim_DocMutation(stb_claim_doc=stb_claim_doc)


class UpdateStb_Claim_DocMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        doc_path = String()
        entry_by = String()

    stb_claim_doc = graphene.Field(lambda: Stb_Claim_DocType)

    def mutate(self, info, id, doc_path, entry_by):
        stb_claim_doc = Stb_Claim_Doc.objects.get(pk=id)
        stb_claim_doc.doc_path = doc_path
        stb_claim_doc.entry_by = entry_by
        stb_claim_doc.save()
        return UpdateStb_Claim_DocMutation(stb_claim_doc=stb_claim_doc)


class DeleteStb_Claim_DocMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    stb_claim_doc = graphene.Field(lambda: Stb_Claim_DocType)

    def mutate(self, info, id):
        stb_claim_doc = Stb_Claim_Doc.objects.get(pk=id)
        stb_claim_doc.delete()
        return


class SaveStb_Claim_DocMutation(graphene.Mutation):
    class Arguments:
        data = Stb_Claim_DocInput()

    stb_claim_doc = graphene.Field(
        lambda: Stb_Claim_DocType)

    def mutate(self, info, data):

        id = data.id
        if id:
            stb_claim_doc = Stb_Claim_Doc.objects.get(
                pk=id)
            for key, value in data.items():
                setattr(stb_claim_doc, key, value)
            stb_claim_doc.save()
        else:
            stb_claim_doc = Stb_Claim_Doc.objects.create(
                **data)
        return SaveStb_Claim_DocMutation(stb_claim_doc=stb_claim_doc)
