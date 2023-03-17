import graphene
from graphene import ObjectType, String, Decimal, Date
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

# Input Object Type


class Ctb_Special_LoanInput(graphene.InputObjectType):
    id = graphene.ID()
    p_ssid = String()
    status = String()
    loan_ref_no = String()
    loan_amount = Decimal()
    pension_amount = Decimal()
    gratuity_amount = Decimal()
    transfer_type = Decimal()
    transfer_percentage = Decimal()
    transfer_amount = Decimal()
    is_transfer_eligible = Decimal()
    is_eligible_for_loan = Decimal()
    from_date = String()
    entry_by = String()
    entry_date = Date()
    loan_start_date = String()
    loan_end_date = String()
    loan_period_in_year = Decimal()
    tran_no = Decimal()
    is_transferred = Decimal()
    transfer_tran_no = Decimal()
    payment_tran_no = Decimal()
    payment_source = String()
    cheque_no = String()
    cheque_date = String()


class Ctb_User_Tran_VerificationsInput(graphene.InputObjectType):
    id = graphene.ID()
    application_id = String()
    module_id = String()
    from_date = String()
    tran_no = Decimal()
    seq_no = Decimal()
    user_id = String()
    veri_level = Decimal()
    v_status = String()
    verify_date = String()
    verify_remarks = String()
    forwarded_to = String()
    ufrom_date = String()
    suffix_entry_date = Date()


class Dctb_SubmissionInput(graphene.InputObjectType):
    id = graphene.ID()
    submission_id = Decimal()
    user_id = String()
    password = String()
    u_name = String()
    phone_no = String()
    email = String()
    old_id = String()
    submission_for = String()
    address = String()
    submission_date = String()
    tran_no = Decimal()
    r_status = String()


class Atb_Disbursement_ProcessInput(graphene.InputObjectType):
    id = graphene.ID()
    submission_id = Decimal()
    tran_type = String()
    from_bank = Decimal()
    from_branch = Decimal()
    from_account = String()
    to_bank = Decimal()
    to_branch = Decimal()
    to_account = String()
    paid_amount = Decimal()
    voucher_amount = Decimal()
    voucher_no = String()
    voucher_date = String()
    entry_by = String()
    entry_date = String()
    status = String()
    error_log = String()
    debit_response_id = String()
    credit_response_id = String()
    debit_status = String()
    credit_status = String()
    from_account_name = String()
    to_account_name = String()
    remarks = String()
    batch_id = String()
    instruction_id = String()
    entry_date = Date()


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


class SaveCtb_Special_LoanMutation(graphene.Mutation):
    class Arguments:
        data = Ctb_Special_LoanInput()

    ctb_special_loan = graphene.Field(lambda: Ctb_Special_LoanType)

    def mutate(self, info, data):

        id = data.id
        if id:
            ctb_special_loan = Ctb_Special_Loan.objects.get(pk=id)
            for key, value in data.items():
                setattr(ctb_special_loan, key, value)
            ctb_special_loan.save()
        else:
            ctb_special_loan = Ctb_Special_Loan.objects.create(**data)
        return SaveCtb_Special_LoanMutation(ctb_special_loan=ctb_special_loan)


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


class SaveCtb_User_Tran_VerificationsMutation(graphene.Mutation):
    class Arguments:
        data = Ctb_User_Tran_VerificationsInput()

    ctb_user_tran_verifications = graphene.Field(
        lambda: Ctb_User_Tran_VerificationsType)

    def mutate(self, info, data):

        id = data.id
        if id:
            ctb_user_tran_verifications = Ctb_User_Tran_Verifications.objects.get(
                pk=id)
            for key, value in data.items():
                setattr(ctb_user_tran_verifications, key, value)
            ctb_user_tran_verifications.save()
        else:
            ctb_user_tran_verifications = Ctb_User_Tran_Verifications.objects.create(
                **data)
        return SaveCtb_User_Tran_VerificationsMutation(ctb_user_tran_verifications=ctb_user_tran_verifications)


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


class SaveDctb_SubmissionMutation(graphene.Mutation):
    class Arguments:
        data = Dctb_SubmissionInput()

    dctb_submission = graphene.Field(lambda: Dctb_SubmissionType)

    def mutate(self, info, data):

        id = data.id
        if id:
            dctb_submission = Dctb_Submission.objects.get(pk=id)
            for key, value in data.items():
                setattr(dctb_submission, key, value)
            dctb_submission.save()
        else:
            dctb_submission = Dctb_Submission.objects.create(**data)
        return SaveDctb_SubmissionMutation(dctb_submission=dctb_submission)


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


class SaveAtb_Disbursement_ProcessMutation(graphene.Mutation):
    class Arguments:
        data = Atb_Disbursement_ProcessInput()

    atb_disbursement_process = graphene.Field(
        lambda: Atb_Disbursement_ProcessType)

    def mutate(self, info, data):

        id = data.id
        if id:
            atb_disbursement_process = Atb_Disbursement_Process.objects.get(
                pk=id)
            for key, value in data.items():
                setattr(atb_disbursement_process, key, value)
            atb_disbursement_process.save()
        else:
            atb_disbursement_process = Atb_Disbursement_Process.objects.create(
                **data)
        return SaveAtb_Disbursement_ProcessMutation(atb_disbursement_process=atb_disbursement_process)




