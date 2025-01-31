from celery import shared_task

@shared_task(name='add_test')
def add(x, y):
    for i in range(10):
        if i == 5:
            # print("Hello")
            break
    return x + y

@shared_task(name='multiply_test')
def multiply(x=3, y=3):
    print('Periodic task')
    return x * y


