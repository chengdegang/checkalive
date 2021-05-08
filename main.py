from smtplib import SMTP_SSL
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header

# #设置smtplib所需的参数
# #下面的发件人，收件人是用于邮件传输的。
# smtpserver = 'smtp.qq.com'
# username = 'chengdgccc@qq.com'
# password='glgfdpxlnhiogaji'
# sender='chengdgccc@qq.com'
# receivers = ['chengdegang@ezxr.com']
#
# subject = 'Service check reminder'
#
# msg = MIMEMultipart('mixed')
# msg['Subject'] = subject
# msg['From'] = '1093637306@qq.com <1093637306@qq.com>'
# msg['To'] = 'qaccc'
# #收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
# # msg['To'] = ";".join(receiver)
#
# text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.baidu.com"
# text_plain = MIMEText(text,'plain', 'utf-8')
# msg.attach(text_plain)
#
# smtp = smtplib.SMTP_SSL(smtpserver)
# smtp.connect(smtpserver,'465')
# #我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
# #smtp.set_debuglevel(1)
# smtp.login(username, password)
# smtp.sendmail(sender,receivers, msg.as_string())
# print("send success")
# smtp.quit()

urls = ['http://10.244.12.50:9223/#/',
        'http://10.244.12.21:8081/',
        'http://10.244.12.21:8080/',
        'http://10.244.12.21:8088/',
        'http://10.244.12.21:8089/']

def result(urls):
    for url in urls:
        # print(url)
        return url

print(result())


