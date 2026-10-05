from typing import ClassVar

from django.urls import reverse
from django.views.generic import DetailView, CreateView, ListView, TemplateView

from .forms import ReviewForm
from .models import Review
# Create your views here.


# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html", {"form": form})

#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("thank_you"))
#         return render(request, "reviews/review.html", {"form": form})


# class ReviewView(FormView):
#     template_name = "reviews/review.html"
#     form_class = ReviewForm
#     success_url = "/thank-you"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Empty dictionary
        context["message"] = "This works!"  # Filling the dictionary
        return context


# class ReviewsListView(TemplateView):
#     template_name = "reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context


# class SingleReviewView(TemplateView):
#     template_name = "reviews/single_review.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_review = Review.objects.get(id=review_id)
#         context["review"] = selected_review
#         return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    context_object_name = "review"


class ReviewView(CreateView):
    template_name = "reviews/review.html"
    model = Review
    form_class = ReviewForm
    success_url = "/thank-you"
