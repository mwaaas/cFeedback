from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from customer_feedback import Form, models

__author__ = 'mwas'

def login(request):
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

def logout(request):
    return HttpResponseRedirect(reverse('home'))

def change_password(request):
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

