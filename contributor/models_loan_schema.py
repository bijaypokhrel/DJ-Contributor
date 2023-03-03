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


class UpdateCtb_Special_LoanMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        cheque_no = String()
        cheque_date = String()

    ctb_special_loan = graphene.Field(lambda: Ctb_Special_LoanType)

    def mutate(self, info, id, cheque_no, cheque_date):
        ctb_special_loan = Ctb_Special_Loan.objects.get(pk=id)
        ctb_special_loan.cheque_no = cheque_no
        ctb_special_loan.cheque_date = cheque_date
        ctb_special_loan.save()
        return UpdateCtb_Special_LoanMutation(ctb_special_loan=ctb_special_loan)


class DeleteCtb_Special_LoanMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    ctb_special_loan = graphene.Field(lambda: Ctb_Special_LoanType)

    def mutate(self, info, id):
        ctb_special_loan = Ctb_Special_Loan.objects.get(pk=id)
        ctb_special_loan.delete()
        return


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


class UpdateCtb_User_Tran_VerificationsMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        v_status = String()
        verify_date = String()

    ctb_user_tran_verification = graphene.Field(
        lambda: Ctb_User_Tran_VerificationsType)

    def mutate(self, info, id, v_status, verify_date):
        ctb_user_tran_verification = Ctb_User_Tran_Verifications.objects.get(
            pk=id)
        ctb_user_tran_verification.v_status = v_status
        ctb_user_tran_verification.verify_date = verify_date
        ctb_user_tran_verification.save()
        return UpdateCtb_User_Tran_VerificationsMutation(ctb_user_tran_verification=ctb_user_tran_verification)


class DeleteCtb_User_Tran_VerificationsMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    ctb_user_tran_verification = graphene.Field(
        lambda: Ctb_User_Tran_VerificationsType)

    def mutate(self, info, id):
        ctb_user_tran_verification = Ctb_User_Tran_Verifications.objects.get(
            pk=id)
        ctb_user_tran_verification.delete()
        return


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


class UpdateDctb_SubmissionMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        phone_no = String()
        email = String()

    dctb_submission = graphene.Field(
        lambda: Dctb_SubmissionType)

    def mutate(self, info, id, phone_no, email):
        dctb_submission = Dctb_Submission.objects.get(pk=id)
        dctb_submission.phone_no = phone_no
        dctb_submission.email = email
        dctb_submission.save()
        return UpdateDctb_SubmissionMutation(dctb_submission=dctb_submission)


class DeleteDctb_SubmissionMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    dctb_submission = graphene.Field(
        lambda: Dctb_SubmissionType)

    def mutate(self, info, id):
        dctb_submission = Dctb_Submission.objects.get(pk=id)
        dctb_submission.delete()
        return


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


class UpdateAtb_Disbursement_ProcessMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        from_account = String()
        to_account = String()

    atb_disbursement_process = graphene.Field(
        lambda: Atb_Disbursement_ProcessType)

    def mutate(self, info, id, from_account, to_account):
        atb_disbursement_process = Atb_Disbursement_Process.objects.get(pk=id)
        atb_disbursement_process.from_account = from_account
        atb_disbursement_process.to_account = to_account
        atb_disbursement_process.save()
        return UpdateAtb_Disbursement_ProcessMutation(atb_disbursement_process=atb_disbursement_process)


class DeleteAtb_Disbursement_ProcessMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    atb_disbursement_process = graphene.Field(
        lambda: Atb_Disbursement_ProcessType)

    def mutate(self, info, id):
        atb_disbursement_process = Atb_Disbursement_Process.objects.get(pk=id)
        atb_disbursement_process.delete()
        return
