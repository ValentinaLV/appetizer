from django.shortcuts import render, redirect
from .forms import ReserveTableForm


def reserve_table(request):
    reserve_form = ReserveTableForm()
    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
            return redirect('reservation:reserve_table_url')

    return render(request, 'reservation.html', {
        'form': reserve_form
    })
