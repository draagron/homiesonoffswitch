import time
from ..micropython_ota_updater.main.ota_updater import OTAUpdater

def run():
    # Initialize the Homie device
    print("main program starting")



    # Run
    for i in range(10) :
        print("Running ")
        time.sleep(1)

    print("main program ending")


if __name__ == "__main__":
    run()
