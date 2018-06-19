import time
import sys
import stomp
import smtplib
from email.mime.text import MIMEText
from email.header import Header

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        print('received a message "%s"' % message)
try:
    conn = stomp.Connection([('****',61613)])
    conn.set_listener('', MyListener())
    conn.start()
    conn.connect('admin', 'admin', wait=True)

    conn.subscribe(destination='/queue/it', id=1, ack='auto')

    conn.send(body='it for monitoring '.join(sys.argv[1:]), destination='/queue/it')

    time.sleep(2)
    conn.disconnect()

except Exception as e:

    mail_host = "smtp.qiye.163.com"  # 设置服务器
    mail_user = "*******@**.com"  # 用户名
    mail_pass = "*******"  # 口令

    sender = 'tuchengjun@idwzx.com'
    receivers = ['1875901954@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(repr(e), 'plain', 'utf-8')
    message['From'] = Header(repr(e), 'utf-8')  # 发送者
    message['To'] = Header(repr(e), 'utf-8')  # 接收者

    subject = 'activemq发生异常'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("邮件发送失败")