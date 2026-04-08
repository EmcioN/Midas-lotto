from django.shortcuts import get_object_or_404, render
from .models import Draw


def draw_list(request):
    draws = Draw.objects.select_related('monthly_summary').all()
    return render(request, 'lotto/draw_list.html', {'draws': draws})


def draw_detail(request, draw_id):
    draw = get_object_or_404(Draw, id=draw_id)
    return render(request, 'lotto/draw_detail.html', {'draw': draw})