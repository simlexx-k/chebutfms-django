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