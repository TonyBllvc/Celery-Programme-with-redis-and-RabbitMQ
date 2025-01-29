from celery import shared_task

@shared_task
def add(x, y):
    for i in range(10):
        if i == 5:
            print("Hello")
            break
    return x + y



