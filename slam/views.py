from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from models import Slam_session
from slam.forms import SlamForm, JudgesForm, PoetFormset, Poet, Slam_session

def index(request):
	return render(request, 'slam/index.html', {'slam': SlamForm(), 'poets': PoetFormset()})
	
	
def round(request):
	if request.method == 'POST':
		slam = SlamForm(request.POST)
		poet_formset = PoetFormset(request.POST, request.FILES)
		if slam.is_valid() and poet_formset.is_valid():
			instance = slam.save()
			for form in poet_formset.forms:
				my_poet = form.save(commit=False)
				my_poet.slam_details = instance
				my_poet.save()
			return render_to_response('slam/slam_round.html', {'form': JudgesForm, 'slam': instance}, context_instance=RequestContext(request))
	return render_to_response('slam/slam_round.html', {'form': JudgesForm(), 'slam': "Your Slam"}, context_instance=RequestContext(request))
	
	
def final(request):
	if request.method == 'POST':
		form = JudgesForm(request.POST)
		if form.is_valid():
			form.save()
			return render_to_response('slam/final.html', {'form': form}, context_instance=RequestContext(request))
	return render(request, 'slam/final.html')
	
	
	
	
	
	
#			slam_object = Slam_session.objects.get(slam_name=request.POST.get("slam_name", ""))
