from django.db import transaction

from .base62 import encode
from .models import Link

ID_OFFSET=1000000  # Offset to avoid short codes that are too short

@transaction.atomic
def create_short_link(original_url:str)->str:
  #Create a new link object in the db without a short code
  link=Link.objects.create(original_url=original_url)
  #Generate a short code based on the link's id
  short_code=encode(link.id+ID_OFFSET)
  #Update the link object with the generated short code
  link.short_code=short_code
  link.save(update_fields=['short_code'])
  return link