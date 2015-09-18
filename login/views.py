from django.shortcuts import render

# Create your views here.

def index(request):
	user = None
	if request.user.is_authenticated():
		user = request.user.username
        
	template = "index.html"
	user = "amit"
	context = {user:"user"}
	return render(request,template,context)
