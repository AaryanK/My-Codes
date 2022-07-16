from winotify import Notification,audio


toast = Notification(app_id="DragonZpyder",title="Water Time",msg="Please Drink water",duration="long",icon=r"C:\My Codes\Python\Spotify\dragon.png")
toast.add_actions(label="Fine")
toast.show()