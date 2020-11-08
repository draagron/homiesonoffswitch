import time
import sys
import gc

sys.path.append('../')
try:
    from micropython_ota_updater.main.ota_updater import OTAUpdater
except ImportError:
    print('IMPORT ERROR')
    print('Sys.path: ' + sys.path )
    print('CurDir  : ' + os.getcwd())
    raise 


gc.collect()

def download_updates_if_available():
    token = '56d67abdb6236b591652e275520387d4d94dce1b'
    ota_updater = OTAUpdater('https://github.com/draagron/homie-sonoff-switch', headers={'Authorization': 'token {}'.format(token)}, main_dir='custom',)
    ota_updater.download_updates_if_available()
    gc.collect()

def run():
    # Initialize the Homie device
    print("NEW main program starting")



    # Run
    for i in range(10) :
        print("Running ")
        time.sleep(1)

    print("main program ending")
    download_updates_if_available()   

if __name__ == "__main__":
    run()
