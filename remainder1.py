import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title="Medicine eat",
            message=" Eat paracetamol 500mg 1 tablet "
                    "Body massage twice",
            timeout=10
        )
        time.sleep(10)
#