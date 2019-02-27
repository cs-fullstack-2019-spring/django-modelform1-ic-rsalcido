from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewUserForm


# Create your views here.
# This view handles the landing page
def index(request):
    return render(request, 'm_f_app/index.html')


# this page will provide a form to add users
def users(request):
    new_form = NewUserForm()

    if request.method == 'POST':
        print('Got posted data')
        new_form = NewUserForm(request.POST)
        if new_form.is_valid():
            new_form.save(commit= True)
            return index(request)
        else:
            print('Error Not Valid')
    return render(request, 'm_f_app/users.html', {'form': new_form})
