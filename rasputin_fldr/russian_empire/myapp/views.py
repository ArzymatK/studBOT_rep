from django.shortcuts import render

def rqst(request):
    return render(request, 'index.html')