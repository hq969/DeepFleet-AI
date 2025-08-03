import schedule
import time

def job():
    print("Running fleet optimization...")

schedule.every(10).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
