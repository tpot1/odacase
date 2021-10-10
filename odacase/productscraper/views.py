from django.shortcuts import render
from .utils import crawl, scrape

def productscraper(request, template='productscraper.html'):
    context = {}
    context['products'] = []
    context['hasSearched'] = False
    if request.method == 'POST':
        # Set hasSearched to True to display table of contents on page
        context['hasSearched'] = True

        # Retrieve form attributes
        base_url = request.POST.get("base_url", "")
        whitelist = request.POST.get("whitelist", "")
        product_identifier = request.POST.get("product_identifier", "")
        name_identifier = request.POST.get("name_identifier", "")
        unit_price_identifier = request.POST.get("unit_price_identifier", "")

        # Crawl from base url to find other pages on site, filtered by whitelist
        links = crawl(base_url, whitelist)

        # Scrape products from each page found
        for link in links:
            print('Scraping: ' + link)
            newProducts = scrape(link, product_identifier, name_identifier, unit_price_identifier)
            context['products'] = context['products'] + newProducts
            print(len(context['products']))
        
    return render(request, template, context)