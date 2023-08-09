from django.shortcuts import render
def mainpage(request):
 return render(request, 'pages/mainpage.html')
def company(request):
 return render(request, 'pages/company_info.html')

def my_info(request):
 return render(request, 'pages/my_info.html')