# This is a sample Python script.
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header

#设置smtplib所需的参数
#下面的发件人，收件人是用于邮件传输的。
smtpserver = 'smtp.exmail.qq.com'
username = '1093637306@qq.com'
password='glgfdpxlnhiogaji'
sender='18868890069@163.com'
#收件人为多个收件人
# receiver=['XXX@126.com']

subject = 'Python email test'

msg = MIMEMultipart('mixed')
msg['Subject'] = subject
msg['From'] = '1093637306@qq.com <1093637306@qq.com>'
msg['To'] = '18868890069@163.com'
#收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
# msg['To'] = ";".join(receiver)

text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.baidu.com"
text_plain = MIMEText(text,'plain', 'utf-8')
msg.attach(text_plain)

smtp = smtplib.SMTP()
smtp.connect(smtpserver,'465')
#我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
#smtp.set_debuglevel(1)
smtp.login(username, password)
smtp.sendmail(sender, msg.as_string())
smtp.quit()

# def sendMail(message,Subject,sender_show,recipient_show,to_addrs,cc_show=''):
#     '''
#     :param message: str 邮件内容
#     :param Subject: str 邮件主题描述
#     :param sender_show: str 发件人显示，不起实际作用如："xxx"
#     :param recipient_show: str 收件人显示，不起实际作用 多个收件人用','隔开如："xxx,xxxx"
#     :param to_addrs: str 实际收件人
#     :param cc_show: str 抄送人显示，不起实际作用，多个抄送人用','隔开如："xxx,xxxx"
#     '''
#     # 填写真实的发邮件服务器用户名、密码
#     user = '1093637306@qq.com'
#     password = 'Chengdegang01'
#     # 邮件内容
#     msg = MIMEText(message, 'plain', _charset="utf-8")
#     # 邮件主题描述
#     msg["Subject"] = Subject
#     # 发件人显示，不起实际作用
#     msg["from"] = sender_show
#     # 收件人显示，不起实际作用
#     msg["to"] = recipient_show
#     # 抄送人显示，不起实际作用
#     msg["Cc"] = cc_show
#     with SMTP_SSL(host="smtp.exmail.qq.com",port=25) as smtp:
#         # 登录发邮件服务器
#         smtp.login(user = user, password = password)
#         # 实际发送、接收邮件配置
#         smtp.sendmail(from_addr = user, to_addrs=to_addrs.split(','), msg=msg.as_string())
#         print("success")
#
# if __name__ =='__main':
#     message = 'Python 测试邮件...'
#     Subject = 'ces'
#     # 显示发送人
#     sender_show = 'ctest'
#     # 显示收件人
#     recipient_show = 'c'
#     # 实际发给的收件人
#     to_addrs = '18868890069@163.com'
#     sendMail(message,Subject,sender_show,recipient_show,to_addrs)

# smtpObj = smtplib.SMTP( [host='smtp.exmail.qq.com' [, port=465 [, local_hostname]]] )
