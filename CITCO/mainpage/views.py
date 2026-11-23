from django.shortcuts import render,redirect
from mainpage.models import candidatemodel
from mainpage.forms import candidateform

# Create your views here.
def register(request):
    success_message=""
    if request.method=="POST":
        forms=candidateform(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            success_message="Registration Successfull!"
            forms=candidateform()
    else:
        forms=candidateform()

    return render(request,"mainpage/Registration.html",{"forms":forms,"success_message":success_message})

def Login(request):

    Error_message = ""

    if request.method == "POST":

        Email = request.POST.get("Email")
        Password = request.POST.get("Password")

        try:

            cm = candidatemodel.objects.get(
                Email=Email,
                Password=Password
            )

            request.session['Name'] = cm.Name
            request.session['Image'] = cm.Upload_Image.url

            request.session.save()

            return render(
                request,
                "mainpage/Home.html",
                {
                    "Name": request.session.get('Name'),
                    "Image": request.session.get('Images')
                }
            )

        except candidatemodel.DoesNotExist:

            Error_message = "invalid credentials"

    return render(
        request,
        "mainpage/Login.html",
        {"Error_message": Error_message}
    )


def home(request):
    user=request.session.get("Name")
    if  user is None:
        return render(request,"mainpage/Login.html",{'error_message':"session Expired,Please login again"})
    return render(request,"mainpage/Home.html",{'user':request.session.get("Name")})


def Logout(request):
    request.session.flush()
    return redirect(request,"mainpage/Login.html")