from Foundation import NSUserNotification,NSUserNotificationCenter,NSURL
from AppKit import NSImage

class Notification:
    def __init__(self,title):
        self.notification = NSUserNotification.alloc().init()
        self.notification.setTitle_(str(title))
        self.notification_center = NSUserNotificationCenter.defaultUserNotificationCenter()

    
    def set_sub_title(self,subtitle):
        self.notification.setSubtitle_(str(subtitle))

    def set_sound(self,sound):
        self.notification.setSoundName_(str(sound))

    def set_text(self,text):
        self.notification.setInformativeText_(str(text))

    def set_content_image(self,url):
        URLObject = NSURL.URLWithString_(url)
        image = NSImage.alloc().initByReferencingURL_(URLObject)
        
        notification.notification.setContentImage_(image) 

    def notify(self):
        self.notification_center.deliverNotification_(self.notification)




    
