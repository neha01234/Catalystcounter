from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  # Import User model
from io import TextIOWrapper
from django.contrib import messages


from .models import Companydata
from .forms import UploadFileForm, QueryForm
import csv
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    def get_success_url(self):
        return '/accounts/login/' 

def home(request):
    return render(request, 'main/home.html')


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES['file'])
                messages.success(request, 'File uploded')
                return redirect('home')
            except ValueError as e:
                form.add_error(None, f"Error processing file: {e}")
    else:
        form = UploadFileForm()
    return render(request, 'main/upload.html', {'form': form})

def handle_uploaded_file(f):
    file = TextIOWrapper(f, encoding='utf-8-sig')
    reader = csv.reader(file)

    # Skip the header row
    next(reader, None)

    for row in reader:
        if len(row) >= 10:  # Ensure there are enough columns
            try:
                com = row[0].strip()
                if not com:
                    raise ValueError("The 'com' field is empty.")
                com = int(com)  # Convert com to integer

                name = row[1].strip()
                domain = row[2].strip()
                year_founded = row[3].strip()
                if not year_founded.isdigit():
                    raise ValueError(f"The 'year_founded' field is not a number: {year_founded}")
                year_founded = int(year_founded)

                industry = row[5].strip()
                locality = row[6].strip()
                country = row[7].strip()
                linkedin_url = row[8].strip()

                # Convert employee estimates to integers
                current_employee_estimate = row[9].strip()
                if not current_employee_estimate:
                    raise ValueError("The 'current_employee_estimate' field is empty.")
                current_employee_estimate = int(current_employee_estimate)

                total_employee_estimate = row[10].strip()
                if not total_employee_estimate:
                    raise ValueError("The 'total_employee_estimate' field is empty.")
                total_employee_estimate = int(total_employee_estimate)

                Companydata.objects.create(
                    com=com,
                    name=name,
                    domain=domain,
                    year_founded=year_founded,
                    industry=industry,
                    locality=locality,
                    country=country,
                    linkedin_url=linkedin_url,
                    current_employee_estimate=current_employee_estimate,
                    total_employee_estimate=total_employee_estimate
                )
            except ValueError as e:
                raise ValueError(f"Invalid data in CSV file: {e}")
        else:
            raise ValueError("CSV row does not contain enough columns.")
from django.db.models import Q
@login_required
def query_builder(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            industry = form.cleaned_data['industry']
            year_founded =form.cleaned_data['year_founded']
            country =form.cleaned_data['country']
            domain =form.cleaned_data['domain']
            count = Companydata.objects.filter(Q(name=name) | 
                    Q(industry=industry) | 
                    Q(year_founded=year_founded) | 
                    Q(country=country) | 
                    Q(domain=domain)
                ).count()
            return render(request, 'main/query_result.html', {'count': count})
    else:
        form = QueryForm()
    dropdown = {}
    dropdown['name'] = Companydata.objects.values_list('name',flat=True).distinct()
    dropdown['industry'] = Companydata.objects.values_list('industry',flat=True).distinct()
    dropdown['year_founded'] = Companydata.objects.values_list('year_founded',flat=True).distinct()
    dropdown['country'] = Companydata.objects.values_list('country',flat=True).distinct()
    dropdown['domain'] = Companydata.objects.values_list('domain',flat=True).distinct()
    print(dropdown)
    return render(request, 'main/query.html', {'form':form,'dropdown':dropdown})

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'main/users.html', {'users': users})


def drop(request):
    dropdown = {}
    dropdown['name'] = Companydata.objects.values_list('name',flat=True).distinct()
    