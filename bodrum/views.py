from django.shortcuts import render ,redirect
from .models import WriteUS, SpecialArea, Comment, Subscribe, Parthners, Galeri
from django.contrib import messages
# Create your views here.



def index(request):
    writes = WriteUS.objects.all()
    specials = SpecialArea.objects.all()
    comments = Comment.objects.all()
    if 'btnSubmit' in request.POST:
        if True:
            email = request.POST.get('email')

            scribe = Subscribe.objects.create(email=email)
            scribe.save()
            messages.success(request, "İşletme Cevabı onaya gönderildi.")
        return redirect('/')


    context = {
        'writes':writes,
        'specials':specials,
        'comments':comments
    }
    return render(request,'central/index.html',context)



def about(request):
    if 'btnSubmit' in request.POST:
        if True:
            email = request.POST.get('email')

            scribe = Subscribe.objects.create(email=email)
            scribe.save()
            messages.success(request, "İşletme Cevabı onaya gönderildi.")
        return redirect('/')
    return render(request,'central/about.html')


def company(request):
    companys = Parthners.objects.all()
    if 'btnSubmit' in request.POST:
        if True:
            email = request.POST.get('email')

            scribe = Subscribe.objects.create(email=email)
            scribe.save()
            messages.success(request, "İşletme Cevabı onaya gönderildi.")
        return redirect('/')

    context = {
        'companys':companys
    }
    return render(request,'central/company.html',context)


def gallery(request):
    story = Galeri.objects.all()

    context={
        'story':story
    }
    return render(request,'central/gallery.html',context)