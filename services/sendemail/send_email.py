import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from conf.conf import EMAIL_MSG


class SMTP(object):
    def __init__(self):
        """

        :param sender:xxxxxx@qq.com
        :param receivers:email of receivers
        :param host:"smtp.qq.com"
        :param user:xxxxxx@qq.com
        :param password:
        """

        self.sender = EMAIL_MSG['sender']
        self.host = EMAIL_MSG['host']
        self.user = EMAIL_MSG['user']
        self.password = EMAIL_MSG['password']

    def send_email_(self, email, file_path):
        try:
            self.message = MIMEMultipart()
            self.message["Form"] = Header(EMAIL_MSG['from'], "utf-8")
            self.message["Subject"] = Header(EMAIL_MSG['subject'], "utf-8")
            self.receivers = [email]

            self.att1 = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
            self.att1["Content-Type"] = 'application/octet-stream'
            self.att1["Content-Disposition"] = 'attachment; filename="test.zip"'
            self.message.attach(self.att1)
            smtp_obj = smtplib.SMTP()
            smtp_obj.connect(self.host, 25)
            smtp_obj.login(self.user, self.password)
            smtp_obj.sendmail(self.sender, self.receivers, self.message.as_string())
            print("Email send success")
            return True
        except smtplib.SMTPException:
            print("Email send error")
            return False
