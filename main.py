from plyer import notification

def send_desktop_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # The notification will automatically disappear after 10 seconds
    )

# Provide the desired title and message for the notification
title = "Notification"
message = "This is a notification message."

# Send the desktop notification
send_desktop_notification(title, message)
