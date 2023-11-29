from django.db import models

# Create your models here.

class Employee(models.Model):
    empid = models.CharField(max_length=10, unique=True)
    # Add other fields related to employees

    def __str__(self):
        return self.empid
    
from .models import Employee  # Import the Employee model

class Farmer(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.employee.empid}"
    
from .models import Farmer  # Import the Farmer model
from django.contrib.auth.models import User
from django.db import models

class SalaryDeduction(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    deduction_date = models.DateField()

    def __str__(self):
        return f"Salary Deduction for {self.farmer} on {self.deduction_date}"

    
class TeaSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #field_manager = models.ForeignKey(User, on_delete=models.CASCADE)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    amount_in_kgs = models.DecimalField(max_digits=10, decimal_places=2)
    submission_date = models.DateField(auto_now=True)
    # Add other fields as needed

    def __str__(self):
        return f"{self.user} - {self.farmer} - {self.amount_in_kgs}"
    
class SalaryAdvance(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    amount_taken = models.DecimalField(max_digits=10, decimal_places=2)
    date_taken = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Salary Advance for {self.farmer} - {self.amount_taken} KES"
    
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Sum
from django.utils import timezone
from .models import Farmer, TeaSubmission, SalaryAdvance

class Payment(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    rate_per_kg = models.DecimalField(max_digits=10, decimal_places=2, default=50)
    nhif_rate = models.DecimalField(max_digits=5, decimal_places=2, default=200)
    nssf_rate = models.DecimalField(max_digits=5, decimal_places=2, default=500)
    max_salary_advance = models.DecimalField(max_digits=10, decimal_places=2, default=7000.00)
    monthly_period = models.DateField(default=timezone.now)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    deduction_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, editable=False)
    
    def save(self, *args, **kwargs):
        # Calculate the total amount_in_kgs for the farmer within the monthly period
        total_kgs = TeaSubmission.objects.filter(
            farmer=self.farmer,
            submission_date__year=self.monthly_period.year,
            submission_date__month=self.monthly_period.month
        ).aggregate(Sum('amount_in_kgs'))['amount_in_kgs__sum']

        # Calculate the amount_paid based on the total_kgs and rate per kg
        if total_kgs:
            self.amount_paid = total_kgs * self.rate_per_kg

        # Calculate deductions for NHIF, NSSF, and salary advance
        self.deduction_amount = (self.nhif_rate) + (self.nssf_rate)

        # Ensure salary advance does not exceed the maximum allowed
        salary_advance = SalaryAdvance.objects.filter(farmer=self.farmer).aggregate(Sum('amount_taken'))['amount_taken__sum'] or 0
        if salary_advance > self.max_salary_advance:
            salary_advance = self.max_salary_advance

        # Subtract the deduction_amount and salary_advance from the amount_paid
        self.amount_paid -= (self.deduction_amount + salary_advance)

        super().save(*args, **kwargs)


    def __str__(self):
        return f"Payment for {self.farmer} - {self.monthly_period.strftime('%B %Y')}"
    

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from io import BytesIO

def generate_farmer_list_pdf(queryset):
    buffer = BytesIO()

    # Create the PDF object, using BytesIO as its "file."
    pdf = SimpleDocTemplate(buffer, pagesize=letter)

    # Our container for 'Flowable' objects
    elements = []

    # Create the table header
    table_data = [['First Name', 'Last Name', 'Email', 'Phone Number', 'Address']]

    # Populate the table data from the queryset
    for farmer in queryset:
        table_data.append([farmer.first_name, farmer.last_name, farmer.email, farmer.phone_number, farmer.address])

    # Create the table
    table = Table(table_data, colWidths=[120, 120, 120, 120, 120])
    elements.append(table)

    # Build PDF
    pdf.build(elements)

    # Seek to the beginning of the BytesIO buffer
    buffer.seek(0)

    return buffer
