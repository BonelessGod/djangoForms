from django.shortcuts import render, redirect
from Forms.forms import InscriptionsForm
from Forms.models import Inscriptions


# Create your views here.

def forms(request):

    inscription = Inscriptions()

    if request.method == 'POST':

        form = InscriptionsForm(request.POST)

        if form.is_valid():

            inscription = form.save()
            return redirect('https://unionskateboard.fr/')

    else:

        inscription = InscriptionsForm()

    form = InscriptionsForm()

    return render(request, 
                'Forms/forms.html',
                {'form': form})