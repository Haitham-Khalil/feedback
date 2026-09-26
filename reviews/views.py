from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import ReviewForm
# Create your views here.


def review(request):
    # if(request.method == "POST"): # If so, we might wanna extract the submitted data
    #     # which we receive on that request.

    #     entered_username = request.POST['username']

    #     print(entered_username)

    #     return HttpResponseRedirect(reverse("thank_you"))

    form = ReviewForm()

    return render(request, "reviews/review.html", {"form": form})


def thank_you(request):
    return render(request, "reviews/thank_you.html")
