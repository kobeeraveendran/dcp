import time

def job_scheduler(f, n):
    time.sleep(n / 1000)
    f()

def f():
    print('output')

job_scheduler(f, 5000)