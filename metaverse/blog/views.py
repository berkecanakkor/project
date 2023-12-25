from django.shortcuts import render
from django.http import HttpResponseRedirect
from blog.forms import ContactForm

# Create your views here.

def index(request):
    
    context = {}
    url = request.META.get('HTTP_REFERER')
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return HttpResponseRedirect(url)
    else:
        context['form'] = ContactForm() 
    
    
    return render(request, 'blog/index.html', context)

