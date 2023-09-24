from django.shortcuts import render

# Create your views here.
def DealiciousView(request):
    return render(request, "Dealicious.html")