from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.utils import timezone
from django.utils.translation import ugettext
from ..models import registration
from ..forms import  PostForm


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'





def home(request):
     template_name = 'classroom/Introduction.html'
     return render(request, template_name)


def post_new(request):
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'classroom/post_edit.html', {'form': form})