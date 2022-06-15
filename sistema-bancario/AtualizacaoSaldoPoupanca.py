import schedule
import time
from connection_sqlite import *

def job():
    print("I'm working...")
    cur.execute(f'UPDATE conta SET saldo = (saldo + 0.05) WHERE tipoConta="Poupança";')
    con_sqlite.commit()

schedule.every().day.at("00:00").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)