from django.views.generic import CreateView, ListView

from .models import UserProfile

# Create your views here.

# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {"form": form})

#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES) # Passing the submitted non-file data and ALSO FILES
#         if submitted_form.is_valid():
#             # store_file(request.FILES["image"])
#             profile = UserProfile(image=request.FILES["user_image"])
#             profile.save()
#             return HttpResponseRedirect("/profiles/")
#         return render(request, "profiles/create_profile.html", {"form": submitted_form})


class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles/"


class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"

    
  
    
    
        
