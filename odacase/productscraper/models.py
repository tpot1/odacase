from django.db import models

# Product Scraper Config object, for storing the base config of a search
class PSConfig(models.Model):
    base_url = models.CharField(max_length=200)
    whitelist = models.CharField(max_length=200)
    product_xpath = models.CharField(max_length=200)

# Product Scraper Attribute associates many product attributes to one config object
class PSAttribute(models.Model):
    ps_config = models.ForeignKey('PSConfig', on_delete=models.CASCADE)
    attribute_name = models.CharField(max_length=200)
    attribute_xpath = models.CharField(max_length=200)
