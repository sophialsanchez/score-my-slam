from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from models import Slam_session
from slam.forms import SlamForm, JudgesForm, PoetFormset

def index(request):
	return render(request, 'slam/index.html', {'slam': SlamForm(), 'poets': PoetFormset})
	
def round(request):
	if request.method == 'POST':
		slam = SlamForm(request.POST)
		poet_formset = PoetFormset(request.POST, request.FILES)
		if slam.is_valid() and poet_formset.is_valid():
			slam.save()
			for form in poet_formset.forms:
				#poet = form.save(commit=False)
				print(form)
				form.save()
				
				#poet.slam_details = slam_form.instance
				return render_to_response('slam/slam_round.html', {'form': JudgesForm, 'slam': "space"}, context_instance=RequestContext(request))
			else:
				print("slam is not valiiid???")
	return render_to_response('slam/slam_round.html', {'form': JudgesForm()}, context_instance=RequestContext(request))
	
def final(request):
	if request.method == 'POST':
		form = JudgesForm(request.POST)
		if form.is_valid():
			form.save()
			return render_to_response('slam/final.html', {'form': form}, context_instance=RequestContext(request))
	return render(request, 'slam/final.html')