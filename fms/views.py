from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render, redirect
from .models import TeaSubmission
from .forms import TeaSubmissionForm  # You'll need to create a form for this model

@login_required
def submit_tea(request):
    if request.method == 'POST':
        form = TeaSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page or any other page you want
    else:
        form = TeaSubmissionForm()

    return render(request, 'submit_tea.html', {'form': form})

@login_required
def success_page(request):
    return render(request, 'success_page.html')  # Create a success_page.html template

from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import Farmer  # Import your Farmer model

def generate_farmer_list_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="farmer_list.pdf"'

    # Create PDF
    p = canvas.Canvas(response)

    farmers = Farmer.objects.all()  # Get your queryset
    for farmer in farmers:
        # Customize this part based on your Farmer model fields
        p.drawString(100, 800, f"Name: {farmer.first_name} {farmer.last_name}")
        p.drawString(100, 780, f"Email: {farmer.email}")
        p.drawString(100, 760, f"Phone Number: {farmer.phone_number}")
        p.drawString(100, 740, f"Address: {farmer.address}")
        p.drawString(100, 720, "-" * 50)  # Separation line

    p.showPage()
    p.save()

    return response