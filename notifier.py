import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="ALERT!!!",
            message="Your completed your task successfully",
            timeout=10
        )
        time.sleep(3600)
