# Create your views here.
from django.core.urlresolvers import reverse
from django.http import HttpRequest,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View
from customer_feedback import models
from customer_feedback import Form

def home(request):
    companies = models.Company.objects.all()
    return render_to_response('home.html',{'companies':companies}, context_instance=RequestContext(request))

def admin_login(request):
    adminLoginForm = Form.admin_login_form()
    if request.method == 'GET':
        return render_to_response('adminLogin.html',
                           {'adminLoginForm':adminLoginForm},
                           context_instance=RequestContext(request),

                           )
    if request.method == 'POST':
        adminLoginForm = Form.admin_login_form(request.POST)

        #this validates and check if the password is valid
        if adminLoginForm.is_valid():
            return render_to_response('manage.html',{},
                                   context_instance=RequestContext(request))

    return render_to_response('adminLogin.html',
                           {'adminLoginForm':adminLoginForm},
                           context_instance=RequestContext(request),

                           )

def manage_employee(request):
    all_employees = models.Employee.objects.all()
    return render_to_response('employees.html',
                              {'all_employees':all_employees},
                              context_instance=RequestContext(request)
                              )

def add_employee(request):
    add_employee_form = Form.AddEmployeeForm()
    if request.method == 'POST':
        add_employee_form = Form.AddEmployeeForm(request.POST)
        if add_employee_form.is_valid():
            add_employee_form.save()
            return HttpResponseRedirect(reverse('manage_employee'))
    return render_to_response('addEmployee.html',
                              {'add_employee_form':add_employee_form},
                              context_instance=RequestContext(request)
                              )

def delete_employee(request, pk):
    models.Employee.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('manage_employee'))

def edit_employee(request, pk):
    edit_employee_form = Form.AddEmployeeForm()
    employee = models.Employee.objects.get(pk=pk)
    if request.method ==  'GET':
        edit_employee_form = Form.AddEmployeeForm(instance=employee)
    else:
        edit_employee_form = Form.AddEmployeeForm(request.POST, instance=employee)
        if edit_employee_form.is_valid():
            edit_employee_form.save()
            return HttpResponseRedirect(reverse('manage_employee'))

    return render_to_response('editEmployee.html',
                                  {'edit_employee_form':edit_employee_form, 'employeeId':pk},
                                  context_instance=RequestContext(request)
                                  )

def company(request):
    all_companies = models.Company.objects.all()
    return render_to_response('company.html',
                              {'all_companies':all_companies},
                              context_instance=RequestContext(request)
                              )


def add_company(request):
    add_company_form = Form.AddCompanyForm()
    if request.method == 'POST':
        add_company_form = Form.AddCompanyForm(request.POST)
        if add_company_form.is_valid():
            add_company_form.save()
            return HttpResponseRedirect(reverse('home'))
    return render_to_response('addCompany.html', {'add_company_form':add_company_form},
                              context_instance = RequestContext(request)
                              )

def edit_company(request, pk):
    company = models.Company.objects.get(pk=pk)
    edit_company_form = Form.AddCompanyForm(instance=company)
    if request.method == 'POST':
        edit_company_form = Form.AddCompanyForm(request.POST,instance=company)
        if edit_company_form.is_valid():
            edit_company_form.save()
            return HttpResponseRedirect(reverse('company'))
    return render_to_response('editCompany.html',
                              {'edit_company_form':edit_company_form, 'companyId':pk},
                              context_instance = RequestContext(request)
                              )

def assign_company(request, pk):
    companyName = models.Company.objects.get(pk=pk).companyName
    assign_form = Form.AssignEmployee({'companyName':companyName})
    if request.method == 'POST':
        assign_form = Form.AssignEmployee(request.POST)

        if assign_form.is_valid():
            company_instance=models.Company.objects.get(pk=pk)
            employee_instance=models.Employee.objects.get(pk=request.POST['choose_employee'])
            models.Assigned(companyName=company_instance, employee=employee_instance).save()

            return HttpResponseRedirect(reverse('company'))
    return render_to_response('assignCompany.html', {'assign_form':assign_form,
                                                     'companyId':pk},
                              context_instance=RequestContext(request)
                              )

def delete_company(request, pk):
    models.Company.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('company'))

def admin_logout(request):
    return HttpResponseRedirect(reverse('home'))

def change_admin_password(request):
    change_admin_password_form = Form.change_password_form()

    if request.method == 'POST':
        change_admin_password_form = Form.change_password_form(request.POST)
        if change_admin_password_form.is_valid():
            #save the new password
            admin_password = models.Admin.objects.get(admin_name='admin_name')
            admin_password.password = request.POST['new_password']
            admin_password.save()

            return HttpResponseRedirect(reverse('admin_login'))

    return render_to_response('change_password.html',
                           {'change_admin_password_form':change_admin_password_form},
                           context_instance=RequestContext(request))


def employee_login(request):
    pass



