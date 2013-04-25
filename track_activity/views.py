# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from track_activity.forms import ActivityForm
from track_activity.models import Activity, TimeTrack
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


@login_required
def list_activity(request):

    activity_list = Activity.objects.filter(user = request.user)
    return render_to_response('list_activity.html',{'activity_list':activity_list},context_instance=RequestContext(request))


@login_required
def save_activity(request):

    form = ActivityForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save(request)
        return HttpResponseRedirect(reverse('list'))

    return render_to_response('new_activity.html',{'form':form},context_instance=RequestContext(request))


@login_required
def activity_detail(request,activity_id):

    activity_detail = TimeTrack.objects.filter(activity = activity_id)
    return render_to_response('activity_detail.html',{'activity_detail':activity_detail},context_instance=RequestContext(request))
    

    
        
    
