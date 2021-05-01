import time
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(
            title = "Please Drink Water",
            message ="Water makes up a large part of your joint cartilage that helps absorb shock and make bone-against-bone movements smoother. Water also can help keep gout (a painful joint condition) at bay. It helps flush toxins from your body that could inflame your joints",
            app_icon="C:\\Users\\WIndows\\Desktop\\New folder\\gallery\\icon.ico",
            timeout=2
        )
        time.sleep(6)#adjust time according to need
