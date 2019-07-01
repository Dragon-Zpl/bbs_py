from worker.work import cron
from services.sendemail.send_email import *

if __name__ == '__main__':

    cron()

    # t = SMTP()
    # t.send_email_("15260826071@163.com")
