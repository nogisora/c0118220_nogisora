import time

start = time.time()


try:
    while True:
        time.sleep(1)
        print('processing...')
except KeyboardInterrupt:
    print('!!FINISH!!') 
