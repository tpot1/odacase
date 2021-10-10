from django.shortcuts import render
from .utils import crawl, scrape
import csv
from django.http import HttpResponse

def productscraper(request, template='productscraper.html'):
    context = {}
    context['hasSearched'] = False
    if request.method == 'GET':
        return render(request, template, context)
    if request.method == 'POST':
        # Retrieve form attributes
        base_url = request.POST.get("base_url", "")
        whitelist = request.POST.get("whitelist", "")
        product_identifier = request.POST.get("product_identifier", "")
        name_identifier = request.POST.get("name_identifier", "")
        unit_price_identifier = request.POST.get("unit_price_identifier", "")

        # Crawl from base url to find other pages on site, filtered by whitelist
        links = crawl(base_url, whitelist)

        # Scrape products from each page found
        products = []
        for link in links:
            print('Scraping: ' + link)
            newProducts = scrape(link, product_identifier, name_identifier, unit_price_identifier)
            products = products + newProducts
            print(len(products))
        
        # Create a CSV response object
        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="products.csv"'},
        )

        writer = csv.writer(response)
        writer.writerow(['Link', 'Product Name', 'Product Unit Price'])
        for product in products:
            writer.writerow([product.url, product.name, product.price])
        
        return response
