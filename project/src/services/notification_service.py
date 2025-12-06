from plyer import notification
import threading

class NotificationService:
    @staticmethod
    def notify_incomplete_tasks(tasks):
        """
        Checks for incomplete tasks and sends a notification if any exist.
        This handles the logic of counting incomplete tasks.
        """
        incomplete_count = sum(1 for t in tasks if t.status.value == "pending")
        
        if incomplete_count > 0:
            message = f"You have {incomplete_count} incomplete task(s) waiting for you!"
            NotificationService.send_notification("ToDo CLI Reminder", message)

    @staticmethod
    def send_notification(title, message):
        """Sends a desktop notification."""
        try:
            notification.notify(
                title=title,
                message=message,
                app_name="ToDo CLI",
                timeout=10
            )
        except Exception as e:
            # Silently fail or log if notifications are not supported/fail
            pass
