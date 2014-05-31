from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from customer_feedback import models, Form

__author__ = 'mwas'

def view(request):
    all_employees = models.Employee.objects.all()
    return render_to_response('employees.html',
                              {'all_employees':all_employees},
                              context_instance=RequestContext(request)
                              )

def add(request):
    add_employee_form = Form.AddEmployeeForm()
    if request.method == 'POST':
        add_employee_form = Form.AddEmployeeForm(request.POST)
        if add_employee_form.is_valid():
            add_employee_form.save()
            return HttpResponseRedirect(reverse('view_employee'))
    return render_to_response('addEmployee.html',
                              {'add_employee_form':add_employee_form},
                              context_instance=RequestContext(request)
                              )

def delete(request, pk):
    models.Employee.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('view_employee'))

def edit(request, pk):
    edit_employee_form = Form.AddEmployeeForm()
    employee = models.Employee.objects.get(pk=pk)
    if request.method ==  'GET':
        edit_employee_form = Form.AddEmployeeForm(instance=employee)
    else:
        edit_employee_form = Form.AddEmployeeForm(request.POST, instance=employee)
        if edit_employee_form.is_valid():
            edit_employee_form.save()
            return HttpResponseRedirect(reverse('view_employee'))

    return render_to_response('editEmployee.html',
                                  {'edit_employee_form':edit_employee_form, 'employeeId':pk},
                                  context_instance=RequestContext(request)
                                  )

def login(request):
    pass
