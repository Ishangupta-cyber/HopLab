from django_redis import get_redis_connection

PENDING="clicks:pending"
FLUSHING="clicks:flushing"

def record_click(link_id:int) -> None:
  """
  Record a click for a given link ID in Redis.
  
  Args:
      link_id (int): The ID of the link that was clicked.
  """
  redis_conn = get_redis_connection("default")
  redis_conn.hincrby(PENDING, link_id, 1)