import csv
from rest_framework import viewsets

from django.shortcuts import render
from django.forms import inlineformset_factory
from django.http import HttpResponse

from .utils import crawl, scrape
from .models import PSAttribute, PSConfig
from .forms import PSConfigForm, PSAttributeForm
from .serializers import PSConfigSerializer, PSAttributeSerializer


def home(request, template='home.html'):
    context = {
        'configs' : PSConfig.objects.all()
    }
    return render(request, template, context)

def new(request, template='new.html'):
    config_form_set = inlineformset_factory(PSConfig, PSAttribute, exclude=())
    if request.method == 'POST':
        config_form = config_form_set(request.POST)
        if config_form.is_valid:
            config = config_form.save()
            formset = config_form_set(instance=config)
    else:
        config = PSConfigForm
        formset = config_form_set(instance=config)
    context = {
        'form': formset,
    }
    return render(request, template, context)

class psconfigView(viewsets.ModelViewSet):
    serializer_class = PSConfigSerializer
    queryset = PSConfig.objects.all()

class psattributeView(viewsets.ModelViewSet):
    serializer_class = PSAttributeSerializer
    queryset = PSAttribute.objects.all()

def productscraper(request, configId, template='productscraper.html'):
    context = {}
    config = PSConfig.objects.get(pk=configId)
    if request.method == 'GET':
        context['base_url'] = config.base_url
        context['whitelist'] = config.whitelist
        context['product_xpath'] = config.product_xpath
        context['attributes'] = []
        for attribute in config.psattribute_set.all():
            context['attributes'].append(attribute)
        return render(request, template, context)
    if request.method == 'POST':
        # Retrieve form attributes
        base_url = config.base_url
        whitelist = config.whitelist
        product_identifier = config.product_xpath
        attributes = config.psattribute_set.all()

        # Crawl from base url to find other pages on site, filtered by whitelist
        links = crawl(base_url, whitelist)

        # Scrape products from each page found
        products = []
        for link in links:
            print('Scraping: ' + link)
            newProducts = scrape(link, product_identifier, attributes)
            products = products + newProducts
            print(len(products))
        
        # Create a CSV response object
        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="products.csv"'},
        )

        writer = csv.writer(response)
        # Write the headings
        column_headings = ['Link']
        for attribute in config.psattribute_set.all():
            column_headings.append(attribute.attribute_name)
        writer.writerow(column_headings)
        # Write the data
        for product in products:
            row = [product['url']]
            for attribute in config.psattribute_set.all():
                row.append(product[attribute.attribute_name])
            writer.writerow(row)
        
        return response
