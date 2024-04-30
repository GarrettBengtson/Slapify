from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def create_account(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/slapify')
    else:
        form = CustomUserCreationForm()

    args = {'form': form}
    return render(request, './registration/create_account.html', args)