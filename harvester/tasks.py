

from datetime import datetime

from celery import shared_task


@shared_task
def test_harvester(*args, **kwargs):
    print("*args:"+str(args))
    print("**kwar:"+str(kwargs))
    now = datetime.now()
    result = {
        "datetime": now,
        "message": "test_harvester"
    }
    print(result)
    return result
