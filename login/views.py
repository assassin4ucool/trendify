from django.shortcuts import render

# Create your views here.

def index(request):
	user = None
	if request.user.is_authenticated():
		user = request.user.username.title
        
	template = "index.html"
	context = {user:"user"}
	return render(request,template,context)
