from django.db import models

# Create your models here.
class NewClientModel(models.Model):
    client_id = models.IntegerField(null=True)
    client_name = models.CharField(max_length=300)
    phone_number = models.IntegerField(null=True)

class CPFTrackerCompanyModel(models.Model):
    monthly_update = models.JSONField(null=True)
    hr_info = models.JSONField(null=True)

class CompanyReviewModel(models.Model):
    status_date = models.DateField(null=True)
    status = models.CharField(max_length=300, null=True)
    quota_date = models.DateField(null=True)
    size = models.IntegerField(null=True)
    spass_sp = models.IntegerField(null=True)
    spass_ex = models.IntegerField(null=True)
    spass_add = models.IntegerField(null=True)
    ep = models.IntegerField(null=True)
    new_sp = models.CharField(max_length=300, null=True)
    new_wp = models.CharField(max_length=300, null=True)
    new_prc = models.CharField(max_length=300, null=True)
    new_ind = models.CharField(max_length=300, null=True)
    new_sfa = models.CharField(max_length=300, null=True)
    note = models.TextField(null=True)
    local_col = models.CharField(max_length=300, null=True)
    date_of_incorp = models.CharField(max_length=300, null=True)
    finance_year_end = models.CharField(max_length=300, null=True)

class AddCompanyModel(models.Model):
    client = models.ForeignKey(NewClientModel, on_delete=models.CASCADE)
    company_id = models.CharField(max_length=500)
    company_name = models.CharField(max_length=500)
    roc = models.CharField(max_length=300, null=True)
    email = models.CharField(max_length=300, null=True)
    contact_person = models.CharField(max_length=300, null=True)
    contact_number = models.IntegerField(null=True)
    singpass_id = models.CharField(max_length=300, null=True)
    singpass_password = models.CharField(max_length=300, null=True)
    qr_code = models.BooleanField(default=False)
    director_name = models.CharField(max_length=300, null=True)
    company_review = models.ForeignKey(CompanyReviewModel, on_delete=models.SET_NULL, null=True)
    cpf_tracker = models.ForeignKey(CPFTrackerCompanyModel, on_delete=models.SET_NULL, null=True)

class CreateOrderModel(models.Model):
    order_date = models.DateField(auto_now_add=True)
    ref_id = models.CharField(max_length=300)
    company = models.ForeignKey(AddCompanyModel, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True)
    pass_type = models.CharField(max_length=300, null=True)
    no_of_vacancies = models.IntegerField(null=True)
    voice_record = models.FileField(upload_to='CreateOrder/', null=True)
    application_id = models.CharField(max_length=300, null=True)
    result = models.CharField(max_length=300, null=True)
    dropbox_url = models.CharField(max_length=500, null=True)
    tiny_url = models.CharField(max_length=300, null=True)
    require_date = models.DateField(null=True)

class BuyingSellingAttachmentsModel(models.Model):
    attachments = models.FileField(upload_to='BuyingSelling/', null=True)

class BuyingSellingModel(models.Model):
    submit_date = models.DateField()
    employeer = models.ForeignKey(NewClientModel, on_delete=models.SET_NULL, null=True)
    business_type = models.CharField(max_length=500, null=True)
    address = models.TextField(null=True)
    rental_deposite = models.CharField(max_length=500, null=True)
    sales_details = models.TextField(null=True)
    staff_needed = models.IntegerField(null=True)
    company_details = models.TextField(null=True)
    take_over_fee = models.CharField(max_length=500, null=True)
    recommended_buyers = models.TextField(null=True)
    remarks = models.TextField(null=True)
    status = models.CharField(max_length=500, null=True)
    video = models.FileField(upload_to='BuyingSellingVideo/', null=True)
    attachments = models.ManyToManyField(BuyingSellingAttachmentsModel)

class PaySlipModel(models.Model):
    from mom_application.models import AfterApprovalTEPModel
    payslip_date_from = models.DateField(null=True)
    payslip_date_to = models.DateField(null=True)
    after_approved_tep = models.ForeignKey(AfterApprovalTEPModel, on_delete=models.SET_NULL, null=True)
    basic_pay = models.IntegerField(null=True)
    total_allowance = models.IntegerField(null=True)
    advance = models.IntegerField(null=True)
    employee_cpf_deduction = models.IntegerField(null=True)
    payment_date = models.DateField(null=True)
    mode_of_payment = models.CharField(max_length=300, null=True)
    overtime_payment_period = models.IntegerField(null=True)
    overtime_work_hours = models.IntegerField(null=True)
    other_additional = models.IntegerField(null=True)
    employee_cpf_contribution = models.IntegerField(null=True)
    net_pay = models.IntegerField(null=True)
    total_deduction = models.IntegerField(null=True)

class BuyerFormModel(models.Model):
    employeer = models.ForeignKey(NewClientModel, on_delete=models.SET_NULL, null=True)
    contact_number = models.IntegerField(null=True)
    whatsapp_number = models.IntegerField(null=True)
    requirement = models.TextField(null=True)