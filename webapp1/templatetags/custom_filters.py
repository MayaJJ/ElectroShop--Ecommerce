# custom_filters.py
from django import template
import requests

register = template.Library()

@register.filter
def image_exists(url):
    try:
        response = requests.head(url)
        return response.status_code == 200
    except Exception as e:
        # Log or handle exceptions as needed
        return False
