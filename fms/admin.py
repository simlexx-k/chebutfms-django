from django.contrib import admin

# Register your models here.
from .models import Farmer
from django.apps import apps

admin.site.site_header = 'Chebut Tea Farmer Management System'
admin.site.site_title = 'Ukulima Bora'

from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['farmer', 'monthly_period', 'amount_paid']
    actions = ['recalculate_payments']

    def recalculate_payments(self, request, queryset):
        for payment in queryset:
            payment.save()

    recalculate_payments.short_description = "Recalculate selected payments"

admin.site.register(Payment, PaymentAdmin)


from django.contrib import admin
from .models import Farmer
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from io import BytesIO

class FarmerAdmin(admin.ModelAdmin):
    list_display = ('employee','first_name', 'last_name', 'email', 'phone_number', 'address')
    actions = ['generate_farmer_list_pdf']

    def generate_farmer_list_pdf(modeladmin, request, queryset):
    # Create the BytesIO buffer
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

            # Define style for table
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), '#77aabb'),  # Header background color
            ('TEXTCOLOR', (0, 0), (-1, 0), (1, 1, 1)),  # Header text color
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center-align all cells
            ('GRID', (0, 0), (-1, -1), 1, '#000000'),  # Add borders to all cells
            ('WORDWRAP', (0, 1), (-1, -1)),
        ])

         # Apply the style to the table
        table.setStyle(style)

        elements.append(table)

        # Build PDF
        pdf.build(elements)

        # Seek to the beginning of the BytesIO buffer
        buffer.seek(0)

        # Create the HttpResponse with PDF mime type
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="farmer_list.pdf"'

        # Write the buffer content to the response
        response.write(buffer.getvalue())

        return response

admin.site.register(Farmer, FarmerAdmin)



fms_models = apps.get_app_config('fms').get_models()

for model in fms_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass


