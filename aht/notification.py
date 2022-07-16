from pynotifier import Notification

def notify(message):
    

    notification =Notification(
        title='AHT',
        description=message
        # icon_path='/absolute/path/to/image/icon.png', # On Windows .ico is required, on Linux - .png
        # duration=5,                                   # Duration in seconds
        # urgency='normal'
    )

    notification.send()
   
    

