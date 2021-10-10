import requests
import lxml.html
from .product import Product
import re

def scrape(url, product_identifier, attributes):
    products = []
    # Use lxml to parse the url into an html tree
    html = requests.get(url)
    doc = lxml.html.document_fromstring(html.content)
    
    # Use given xpaths to identify products in lxml tree
    products_html = doc.xpath(product_identifier)

    # Loop over products and extract their metadata
    for product_html in products_html:
        product = {}
        for attribute in attributes:
            product['url'] = url
            product[attribute.attribute_name] = product_html.xpath(attribute.attribute_xpath)[0].text
            products.append(product)

    return products

def crawl(base_url, whitelist):
    # Use lxml to parse the url into an html tree
    html = requests.get(base_url)
    doc = lxml.html.document_fromstring(html.content)
    # find additional links from base url
    links = doc.xpath('*//a/@href')
    # Filter out links not in whitelist
    whitelist_items = whitelist.split(',')
    valid_links = [base_url]
    for l in links:
        for w in whitelist_items:
            if re.search("^"+w, l):
                valid_links.append(base_url + l)
    print(valid_links)
    return valid_links
