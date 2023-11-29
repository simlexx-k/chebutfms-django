from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render, redirect
from .models import TeaSubmission


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

# views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('tea_submission')  # Redirect to a success page or home page
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})

    return render(request, 'login.html')


# views.py


# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TeaSubmission
from .forms import TeaSubmissionForm

@login_required
def tea_submission_view(request):
    if request.method == 'POST':
        form = TeaSubmissionForm(request.POST)

        if form.is_valid():
            tea_submission = form.save(commit=False)
            tea_submission.user = request.user
            tea_submission.save()
            # Redirect to a success page or home page
            return redirect('dashboard')  # Replace 'home' with the actual URL name for your home page
    else:
        form = TeaSubmissionForm()

    return render(request, 'tea_submission.html', {'form': form})


# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import TeaSubmission
from django.contrib.auth.models import User


@login_required
def dashboard_view(request):
    tea_records = TeaSubmission.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'tea_records': tea_records})

def landing_view(request):
    return render(request, 'landing.html')
