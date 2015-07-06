from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from models import Slam_session
from slam.forms import SlamForm, JudgesForm

def index(request):
	return render(request, 'slam/index.html', {'form': SlamForm()})
	
def round(request):
	if request.method == 'POST':
		slam = SlamForm(request.POST)
		if slam.is_valid(): # if form is completely filled out - should return errors if not!
			slam.save()
			return render_to_response('slam/slam_round.html', {'form': JudgesForm, 'slam': slam}, context_instance=RequestContext(request))
	return render_to_response('slam/slam_round.html', {'form': JudgesForm()}, context_instance=RequestContext(request))
	
def final(request):
	if request.method == 'POST':
		form = JudgesForm(request.POST)
		if form.is_valid():
			form.save()
			return render_to_response('slam/final.html', {'form': form}, context_instance=RequestContext(request))
	return render(request, 'slam/final.html')