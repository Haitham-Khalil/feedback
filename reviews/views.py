from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.


def review(request):
    if(request.method == "POST"): # If so, we might wanna extract the submitted data 
        # which we receive on that request.

        entered_username = request.POST['username'] 
        
        print(entered_username) 
        
        return HttpResponseRedirect(reverse("thank_you"))

    return render(request, "reviews/review.html")


def thank_you(request):
    return render(request, "reviews/thank_you.html")