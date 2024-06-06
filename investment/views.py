from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Investment, Customer, ProductMaster
from .forms import InvestmentForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required



@login_required
def investment_list(request):
    investments = Investment.objects.all()
    return render(request, 'investment/investment_list.html', {'investments': investments})

@login_required
def investment_create(request):
    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('investment_list')
    else:
        form = InvestmentForm()
    return render(request, 'investment/investment_form.html', {'form': form})

@login_required
@csrf_exempt
@require_POST
def investment_update(request, pk):
    investment = get_object_or_404(Investment, pk=pk)
    if request.is_ajax():
        new_amount = request.POST.get('investment_amount')
        if new_amount:
            investment.investment_amount = new_amount
            investment.save()
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@login_required
def investment_delete(request, pk):
    investment = get_object_or_404(Investment, pk=pk)
    investment.delete()
    return redirect('investment_list')
