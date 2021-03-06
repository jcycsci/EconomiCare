from django.views import generic
from django.shortcuts import render
from hospital.models import Item

def what(request):
	return render(request, 'whatis/what.html')

def diagnosis(request):
	return render(request, 'diagnose/diagnosis.html')

def presley(request):
	return render(request, 'about-pj/presley.html')
	
def amina(request):
	return render(request, 'about-ab/amina.html')

def jeffrey(request):
	return render(request, 'about-jy/jeffrey.html')

def asif(request):
	return render(request, 'about-ac/asif.html')

def result(request):
	all_chest_pain = Item.objects.filter(diagnosis_related_group='Chest Pain')
	return render(request, 'results/result.html',{'all_chest_pain' : all_chest_pain})

def stroke(request): 
	all_stroke = Item.objects.filter(diagnosis_related_group='Stroke')
	return render(request, 'res-str/stroke.html',{'all_stroke' : all_stroke})

def broken_limb(request): 
	all_broken_limb = Item.objects.filter(diagnosis_related_group='Broken limbs')
	return render(request, 'res-brl/broken_limb.html',{'all_broken_limb' : all_broken_limb})

def poison(request):
	all_poison = Item.objects.filter(diagnosis_related_group='Poisons')
	return render(request, 'res-poi/poison.html',{'all_poison' : all_poison})

def cardiac(request):
	all_cardiac = Item.objects.filter(diagnosis_related_group='Cardiac Arrhythmia & Conduction Disorders')
	return render(request, 'res-cac/cardiac.html',{'all_cardiac' : all_cardiac})

def chest_pain(request):
	all_chest_pain = Item.objects.filter(diagnosis_related_group='Chest Pain')
	return render(request, 'res-chp/chest_pain.html',{'all_chest_pain' : all_chest_pain})


def respiratory(request):
	all_respiratory = Item.objects.filter(diagnosis_related_group='Respiratory Infections & Inflammations')
	return render(request, 'res-rii/respiratory.html',{'all_respiratory' : all_respiratory})



def index(request):
	return render(request, 'homepage/home.html')

#def result(request):
	#all_chest_pain = Item.objects.filter(diagnosis_related_group='Broken Limbs')
	#return render(request, 'broken_limbs/broken_limb_result.html',{'all_broken_limbs' : all_broken_limbs)


def about(request):
	return render(request, 'aboutus/about.html')

class IndexView(generic.ListView):
	template_name = 'hospital/index.html'
	context_object_name = 'all_items'

	def get_queryset(self):
		return Item.objects.all()


class DetailView(generic.DetailView):
	model = Item
	template_name = 'hospital/detail.html'


	
	
		