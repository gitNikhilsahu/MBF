from django.shortcuts import render
from django.http import HttpResponseRedirect
from WebApp import forms

def EmpView(request):
    form = forms.EmpForm()
    if request.method == 'POST':
        form = forms.EmpForm(request.POST)
        if form.is_valid():
            form.save( commit = True )
            return HttpResponseRedirect('/thanks')
    else:
        form = forms.EmpForm()
    return render(request, 'WebApp/Registration.html', {'form': form})

def ThankView(request):
    return render(request, 'WebApp/Thanks.html')