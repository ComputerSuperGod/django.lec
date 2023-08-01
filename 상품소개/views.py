from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import MainContent
def index(request):
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request, '상품소개/content_list.html', context)
