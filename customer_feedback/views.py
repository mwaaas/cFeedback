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















