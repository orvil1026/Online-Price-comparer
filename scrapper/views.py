from django.shortcuts import render, redirect
from django.views import View
from .scrapper import FlipkartScrapper, Scrapper
from .models import *

class HomeView(View):

    template_name = 'homepage.html'

    def get(self, request):
        Product.objects.all().delete()
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        search = request.POST.get('search')
        print(search)

        return redirect('scrapper:search', product_name=search)


class SearchView(View):

    template_name = 'products.html'

    def get(self, request, product_name):

        scrap = Scrapper()
        links = scrap.get_links(product_name)

        amazon_object_list = scrap.get_object_list(links)
        
        f_scrap = FlipkartScrapper()
        flip_links = f_scrap.get_links(product_name)
        flipkart_object_list = f_scrap.get_object_list(flip_links)


        object_list = amazon_object_list + flipkart_object_list
        # request.session['object_list']
        for object in object_list:
            product = Product(name=product_name,title=object.title,price=object.price, rating=object.star,image_url=object.image_url,url=object.url,website=object.website)
            product.save()
            for review in object.reviews_list:
                r = Review(product=product, text=review)
                r.save()
        object_list = Product.objects.filter(name=product_name)
        context = {
            'product_name': product_name,
            'object_list': object_list
        }
        return render(request, self.template_name, context)


class DetailView(View):

    template_name = 'reviews.html'

    def get(self, request, id, *args, **kwargs):

        object = Product.objects.get(id=id)
        review_list = object.review_set.all()
        
        context = {
            'object':object,
            'review_list':review_list
            
            }

        return render(request, self.template_name, context)
