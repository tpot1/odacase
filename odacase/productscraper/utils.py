import requests
import lxml.html
import re

def scrape(url, product_identifier, attributes):
    products = []
    # Use lxml to parse the url into an html tree
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36', "Upgrade-Insecure-Requests": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8","Accept-Encoding": "gzip, deflate, br"}
    html = requests.get(url, headers=headers)
    doc = lxml.html.document_fromstring(html.content)
    
    # Use given xpaths to identify products in lxml tree
    products_html = doc.xpath(product_identifier)

    # Loop over products and extract their metadata
    for product_html in products_html:
        product = {}
        product['url'] = url
        for attribute in attributes:
            try:
                product[attribute.attribute_name] = product_html.xpath(attribute.attribute_xpath)[0].text
            except IndexError:
                product[attribute.attribute_name] = ''
        products.append(product)

    return products

def crawl(base_url, whitelist):
    valid_links = [base_url]
    # If whitelist is none then no crawling is necessary
    if whitelist is None:
        return valid_links
    # Use lxml to parse the url into an html tree
    html = requests.get(base_url)
    doc = lxml.html.document_fromstring(html.content)
    # find additional links from base url
    links = doc.xpath('*//a/@href')
    # Filter out links not in whitelist
    whitelist_items = whitelist.split(',')
    for l in links:
        for w in whitelist_items:
            if re.search("^"+w, l):
                valid_links.append(base_url + l)
    print(valid_links)
    return valid_links
