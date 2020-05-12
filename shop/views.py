from django.shortcuts import render, get_object_or_404
from .models import Product, Contact
from math import ceil

# Create your views here.
from django.http import HttpResponse

def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)


def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query)<4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html', params)

def productView(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/prodView.html', {'product':product[0]})



def about(request):
    return render(request, 'shop/about.html')

# def contact(request):
#     # return HttpResponse('hello')
#     return render(request, 'shop/index.html.html')

def contact(request):
    thank = False
    if request.method=="POST":
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        query = request.POST.get('query', '')
        contact = Contact(username=username, email=email, phone=phone, query=query)
        contact.save()
        thank = True
    return render(request, 'shop/contact.html', {'thank': thank})

# def contact(request):
#     if request.method == 'POST':
#         if request.POST['username'] and request.POST['email'] and request.POST['phone'] and request.POST['query']:
#                 prod = Contact()
#                 prod.username = request.POST['username']
#                 prod.email = request.POST['email']
#                 prod.phone = request.POST['phone']
#                 prod.query = request.POST['query']
#                 prod.save()
#                 return render(request, 'shop/index.html')
#
#         else:
#             return render(request, 'shop/contact.html', {'error' : 'All fields are required'})
#     else:
#         return render(request, 'shop/contact.html')



#
# def contact(request):
#     if request.method == 'POST':
#         if request.POST['username'] and request.POST['email'] and request.POST['phone'] and request.POST['query']:
#             cont = Contact()
#             cont.username = request.get.POST['username']
#             cont.email= request.get.POST['email']
#             cont.phone = request.get.POST['phone']
#             cont.query = request.get.POST['query']
#             cont.save()
#             return render(request, 'shop/index.html')
#         else:
#             return render(request, 'shop/contact.html', {'error' : 'All fields are required'})
#     else:
#         return render(request, 'shop/contact.html')
