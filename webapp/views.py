from django.shortcuts import render
from .models import state
# Create your views here.
def statelist(request):
    items=state.objects.all()
    return render(request,'myapp/statecapital.html',{'items':items})