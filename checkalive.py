import requests
# import aiosmtplib
# from email.message import EmailMessage
# import asyncio
# from aiosmtplib import SMTP
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# url = 'http://10.244.12.50:9223/#/'
urls = ['http://10.244.12.50:9223/#/',
        'http://10.244.12.21:8081/',
        'http://10.244.12.21:8080/',
        'http://10.244.12.21:8088/',
        'http://10.244.12.21:8089/']
urls_failed = []
url_failed_num = 0
# headers = {'Accept':'application/vnd.github.v3+json'}
for url in urls:
    try:
        r = requests.get(url)
    except Exception:
    # except ConnectionRefusedError:
        print(f"失败(无法访问) {url}")
        urls_failed.append(url)
        url_failed_num = + 1
        continue
    #200成功以及403无权限访问均表示该网站没有挂
    if r.status_code == 200 or r.status_code == 403:
        print(f"成功 该url为：{url}")
    else:
        print(f"失败 该url为：{url}")
        url_failed_num = + 1
        urls_failed.append(url)

print(f"一共失败了{url_failed_num}个")
print(f"失败的url如下:{urls_failed}")

# message = EmailMessage()
# message["From"] = "root@localhost"
# message["To"] = "chengdegang@ezxr.com"
# message["Subject"] = "Hello World!"
# message.set_content("Sent via aiosmtplib")
# loop = asyncio.get_event_loop()
# loop.run_until_complete(aiosmtplib.send(message, hostname="127.0.0.1", port=25))
# def sent_email(mail_body):
#     sender = '***********'
#     receiver = '**********'
#     smtpServer = 'smtp.163.com'
#     username = '*******'
#     password = '*******'
#     mail_title = '今日通知'
#     mail_body = mail_body
#
#     message = MIMEText(mail_body, 'plain', 'utf-8')
#     message["Accept-Language"] = "zh-CN"
#     message["Accept-Charset"] = "ISO-8859-1,utf-8"
#     message['From'] = sender
#     message['To'] = receiver
#     message['Subject'] = Header(mail_title, 'utf-8')
#
#     try:
#         smtp = smtplib.SMTP()
#         smtp.connect(smtpServer)
#         smtp.login(username, password)
#         smtp.sendmail(sender, receiver, message.as_string())
#         print('邮件发送成功')
#         smtp.quit()
#     except smtplib.SMTPException:
#         print("邮件发送失败！！！")


# print(f"Status code: {r.status_code}")
