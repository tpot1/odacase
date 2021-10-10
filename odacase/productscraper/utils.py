import requests
import lxml.html
from .product import Product
import re

def scrape(url, product_identifier, name_identifier, unit_price_identifier):
    products = []
    # Use lxml to parse the url into an html tree
    html = requests.get(url)
    doc = lxml.html.document_fromstring(html.content)
    
    # Use given xpaths to identify products in lxml tree
    products_html = doc.xpath(product_identifier)

    # Loop over products and extract their metadata
    for product_html in products_html:
        name = product_html.xpath(name_identifier)[0].text
        unit_price = product_html.xpath(unit_price_identifier)[0].text
        products.append(Product(name=name, price=unit_price))

    return products

def crawl(base_url, whitelist):
    # Use lxml to parse the url into an html tree
    html = requests.get(base_url)
    doc = lxml.html.document_fromstring(html.content)
    # find additional links from base url
    links = doc.xpath('*//a/@href')
    # Filter out links not in whitelist
    valid_links = [base_url]
    for l in links:
        if re.search("^"+whitelist, l):
            valid_links.append(base_url + l)
    
    return valid_links
