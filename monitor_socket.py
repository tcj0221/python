import socket
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import paramiko
import os
import sys
HOST = '****'
PORT = 19999

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    #while True:
    #    s.sendall()
    data = s.recv(1024)
 #   print(data)
    s.close()
    sys.exit()
except Exception as e:

    mail_host = "smtp.qiye.163.com"  # 设置服务器
    mail_user = "******@*****.com"  # 用户名
    mail_pass = "*******"  # 口令

    sender = 'tuchengjun@idwzx.com'
    receivers = ['1875901954@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(repr(e), 'plain', 'utf-8')
    message['From'] = Header(repr(e), 'utf-8')  # 发送者
    message['To'] = Header(repr(e), 'utf-8')  # 接收者

    subject = 'gateway发生异常'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")

    except smtplib.SMTPException:
        print("邮件发送失败")


    def sshclient_execmd(hostname, port, username, password, execmd):
        paramiko.util.log_to_file("paramiko.log")

        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        s.connect(hostname=hostname, port=port, username=username, password=password)
        stdin, stdout, stderr = s.exec_command(execmd)
        stdin.write("Y")  # 第一次连接主机时输入
        stdout.read()
        s.close()
        return

    sshclient_execmd('*****', 22, '*******', '*******[',"sh start_gateway.sh> /dev/null &")

