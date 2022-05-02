from django.core.mail import send_mail
from django.shortcuts import render ,redirect ,get_object_or_404
from .models import Comment, Subscribe, Parthners, Galeri, Slider, About, Cheff, Product, Category, Images ,SubCategory,History
from django.contrib import messages
from django.conf import settings

# Create your views here.



def index(request):
    categorys = Category.objects.all()
    otel = SubCategory.objects.filter(AltCategory__name__icontains='otel')
    endüs = SubCategory.objects.filter(AltCategory__name__icontains='endüs')
    open = SubCategory.objects.filter(AltCategory__name__icontains='açık')
    cheffs = Cheff.objects.all()
    abouts = About.objects.all()
    sliders = Slider.objects.all()
    comments = Comment.objects.all()
    if 'btnSubmit' in request.POST:
        if True:
            email = request.POST.get('email')

            scribe = Subscribe.objects.create(email=email)
            scribe.save()
            messages.success(request, "İşletme Cevabı onaya gönderildi.")
        return redirect('/')


    context = {
        'sliders':sliders,
        'comments':comments,
        'abouts':abouts,
        'cheffs':cheffs,
        'categorys':categorys,
        'otel':otel,
        'endüs':endüs,
        'open':open

    }
    return render(request,'central/index.html',context)



def about(request):
    historys = History.objects.all()
    categorys = Category.objects.all()
    otel = SubCategory.objects.filter(AltCategory__name__icontains='otel')
    endüs = SubCategory.objects.filter(AltCategory__name__icontains='endüs')
    open = SubCategory.objects.filter(AltCategory__name__icontains='açık')
    if 'btnSubmit' in request.POST:
        if True:
            email = request.POST.get('email')

            scribe = Subscribe.objects.create(email=email)
            scribe.save()
            messages.success(request, "İşletme Cevabı onaya gönderildi.")
        return redirect('/')


    context = {

        'categorys':categorys,
        'otel':otel,
        'endüs':endüs,
        'open':open,
        'historys':historys

    }
    return render(request,'central/about.html',context)


def company(request):
    categorys = Category.objects.all()
    otel = SubCategory.objects.filter(AltCategory__name__icontains='otel')
    endüs = SubCategory.objects.filter(AltCategory__name__icontains='endüs')
    open = SubCategory.objects.filter(AltCategory__name__icontains='açık')
    companys = Parthners.objects.all()
    if 'btnSubmit' in request.POST:
        if True:
            email = request.POST.get('email')

            scribe = Subscribe.objects.create(email=email)
            scribe.save()
            messages.success(request, "İşletme Cevabı onaya gönderildi.")
        return redirect('/')

    context = {
        'companys':companys,
        'categorys': categorys,
        'otel': otel,
        'endüs': endüs,
        'open': open
    }
    return render(request,'central/company.html',context)


def gallery(request):
    story = Galeri.objects.all()

    context={
        'story':story
    }
    return render(request,'central/gallery.html',context)


#def list(request):
    #products = SubCategory.objects.all()

    #return render(request,'central/list.html',{'products':products})





def Show(request,category_slug = None):
    categorys = Category.objects.all()
    otel = SubCategory.objects.filter(AltCategory__name__icontains='otel')
    endüs = SubCategory.objects.filter(AltCategory__name__icontains='endüs')
    open = SubCategory.objects.filter(AltCategory__name__icontains='açık')
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(SubCategory, slug=category_slug)
        print("category", category)
        products = products.filter(subCategory=category)

    context = {
        'products': products,
        'categorys': categorys,
        'otel': otel,
        'endüs': endüs,
        'open': open

    }
    return render(request,'central/show.html',context)

def otelShow(request,category_slug = None):
    categorys = Category.objects.all()
    otel = SubCategory.objects.filter(AltCategory__name__icontains='otel')
    endüs = SubCategory.objects.filter(AltCategory__name__icontains='endüs')
    open = SubCategory.objects.filter(AltCategory__name__icontains='açık')
    products = SubCategory.objects.filter(AltCategory__name__icontains='otel')

    context = {
        'categorys': categorys,
        'otel': otel,
        'endüs': endüs,
        'open': open,
        'products':products,

    }
    return render(request,'central/otel-show.html',context)


def enShow(request, category_slug=None):
    categorys = Category.objects.all()
    otel = SubCategory.objects.filter(AltCategory__name__icontains='otel')
    endüs = SubCategory.objects.filter(AltCategory__name__icontains='endüs')
    open = SubCategory.objects.filter(AltCategory__name__icontains='açık')
    products = SubCategory.objects.filter(AltCategory__name__icontains='endüs')

    context = {
        'categorys': categorys,
        'otel': otel,
        'endüs': endüs,
        'open': open,
        'products': products,

    }
    return render(request, 'central/en-show.html', context)

def openShow(request, category_slug=None):
    categorys = Category.objects.all()
    otel = SubCategory.objects.filter(AltCategory__name__icontains='otel')
    endüs = SubCategory.objects.filter(AltCategory__name__icontains='endüs')
    open = SubCategory.objects.filter(AltCategory__name__icontains='açık')
    products = SubCategory.objects.filter(AltCategory__name__icontains='açık')

    context = {
        'categorys': categorys,
        'otel': otel,
        'endüs': endüs,
        'open': open,
        'products': products,

    }
    return render(request, 'central/open-show.html', context)

def detail(request,slug,id):
    categorys = Category.objects.all()
    otel = SubCategory.objects.filter(AltCategory__name__icontains='otel')
    endüs = SubCategory.objects.filter(AltCategory__name__icontains='endüs')
    open = SubCategory.objects.filter(AltCategory__name__icontains='açık')
    product = get_object_or_404(Product, slug=slug, id=id)
    images = Images.objects.filter(product_id=id)


    context= {
        'product':product,
        'images':images,
        'categorys': categorys,
        'otel': otel,
        'endüs': endüs,
        'open': open

    }
    return render(request,'central/detail.html',context)


def contact(request):
    categorys = Category.objects.all()
    otel = SubCategory.objects.filter(AltCategory__name__icontains='otel')
    endüs = SubCategory.objects.filter(AltCategory__name__icontains='endüs')
    open = SubCategory.objects.filter(AltCategory__name__icontains='açık')
    if 'btnSubmit' in request.POST:
        if True:
            nerden= 'EB iletişim formu mesajı'
            name = request.POST.get('name')
            subjects = request.POST.get('subject')
            comment = request.POST.get('comment')

            subject = 'Contact Page Costumer Back'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email,"djangomarmaris@gmail.com"]
            contact_message = "\nNerden:%s\nName:%s\nSubject:%s\nMessages:%s" % (
                nerden,
                name,
            subjects,
            comment)
            send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
    context = {

        'categorys': categorys,
        'otel': otel,
        'endüs': endüs,
        'open': open,

    }
    return render(request,'central/contact.html',context)