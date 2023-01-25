import graphene
from graphene import ObjectType, String, Decimal
from graphene_django import DjangoObjectType
from .models import *


# Query

class Ctb_Special_LoanType(DjangoObjectType):
    class Meta:
        model = Ctb_Special_Loan


class Ctb_User_Tran_VerificationsType(DjangoObjectType):
    class Meta:
        model = Ctb_User_Tran_Verifications


class Dctb_SubmissionType(DjangoObjectType):
    class Meta:
        model = Dctb_Submission


class Atb_Disbursement_ProcessType(DjangoObjectType):
    class Meta:
        model = Atb_Disbursement_Process

# Mutation


class CreateCtb_Special_LoanMutation(graphene.Mutation):
    class Arguments:
        cheque_no = String()
        cheque_date = String()

    ctb_special_loan = graphene.Field(lambda: Ctb_Special_LoanType)

    def mutate(self, info, cheque_no, cheque_date):
        ctb_special_loan = Ctb_Special_Loan.objects.create(
            cheque_no=cheque_no, cheque_date=cheque_date)
        return CreateCtb_Special_LoanMutation(ctb_special_loan=ctb_special_loan)


class CreateCtb_User_Tran_VerificationsMutation(graphene.Mutation):
    class Arguments:
        v_status = String()
        verify_date = String()

    ctb_user_tran_verification = graphene.Field(
        lambda: Ctb_User_Tran_VerificationsType)

    def mutate(self, info, v_status, verify_date):
        ctb_user_tran_verification = Ctb_User_Tran_Verifications.objects.create(
            v_status=v_status, verify_date=verify_date)
        return CreateCtb_User_Tran_VerificationsMutation(ctb_user_tran_verification=ctb_user_tran_verification)


class CreateDctb_SubmissionMutation(graphene.Mutation):
    class Arguments:
        phone_no = String()
        email = String()

    dctb_submission = graphene.Field(
        lambda: Dctb_SubmissionType)

    def mutate(self, info, phone_no, email):
        dctb_submission = Dctb_Submission.objects.create(
            phone_no=phone_no, email=email)
        return CreateDctb_SubmissionMutation(dctb_submission=dctb_submission)


class CreateAtb_Disbursement_ProcessMutation(graphene.Mutation):
    class Arguments:
        from_account = String()
        to_account = String()

    atb_disbursement_process = graphene.Field(
        lambda: Atb_Disbursement_ProcessType)

    def mutate(self, info, from_account, to_account):
        atb_disbursement_process = Atb_Disbursement_Process.objects.create(
            from_account=from_account, to_account=to_account)
        return CreateAtb_Disbursement_ProcessMutation(atb_disbursement_process=atb_disbursement_process)
