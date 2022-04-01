from django.shortcuts import render

# Create your views here.
def home_view(request):
    context = {
        'home':'Sujan adhikari home',
    }
    return render(request, 'blog/index.html')



def login_with_google_view(request):
    return render(request, 'account/login.html')