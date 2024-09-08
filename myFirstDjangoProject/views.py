from django.http import  HttpResponse
from django.shortcuts import render
def home(request):
    homeData={
        "title":"home page",
        "range":range(10),
        "bodyData":"this is body data",
        "student":[{"name":"joy","roll":101,"phone":123445},{"name":"mahmud","roll":102,"phone":6353635}]
    }
    return render(request,'index.html',homeData)
def aboutUs(request):
    return HttpResponse('This is about page')

def course(request,courseid):
    return HttpResponse()