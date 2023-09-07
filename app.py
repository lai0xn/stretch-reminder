from notif import Notification
import time

notification = Notification("Go stretch")
notification.set_sound("Glass")

while True:
    notification.notify()
    time.sleep(3600)
    

    
