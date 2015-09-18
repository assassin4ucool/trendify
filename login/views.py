from django.shortcuts import render

# Create your views here.

def index(request):
	template = "index.html"
	user = "amit"
	context = {user:"user"}
	return render(request,template,context)
