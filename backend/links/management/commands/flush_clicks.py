import time 
from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.models import F
from links.models import Link
from links.clicks import get_redis_connection, PENDING, FLUSHING
import redis


class Command(BaseCommand):
  help="Redis click counters ko har N second Postgres mein flush karta hai"

  def add_arguments(self,parser):

    parser.add_argument("--interval",type=float,default=5.0)

  def handle(self,*args,**options):
    r=get_redis_connection("default")
    self.stdout.write(f"flusher started, every {options['interval']}s")
    while True:
      self.flush(r)
      time.sleep(options["interval"])

  def flush(self,r):
    if not r.exists(FLUSHING):
      try:
        r.rename(PENDING,FLUSHING)
      except redis.exceptions.ResponseError:
        return
    counts=r.hgetall(FLUSHING)

    with transaction.atomic():
      for link_id,count in counts.items():
        Link.objects.filter(pk=link_id).update(click_count=F("click_count")+int(count))

    r.delete(FLUSHING)
    total = sum(int(v) for v in counts.values())
    self.stdout.write(f"flushed {total} clicks across {len(counts)} links")