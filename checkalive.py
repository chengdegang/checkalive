import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
        url_failed_num = url_failed_num + 1
        continue
    #200成功以及403无权限访问均表示该网站没有挂
    if r.status_code == 200 or r.status_code == 403:
        print(f"成功 该url为：{url}")
    else:
        print(f"失败 该url为：{url}")
        url_failed_num += 1
        urls_failed.append(url)

msg_text = f"今天一共失败了{url_failed_num}个"
print(f"一共失败了{url_failed_num}个")
print(f"失败的url如下:{urls_failed}")

#设置smtplib所需的参数
#下面的发件人，收件人是用于邮件传输的。
smtpserver = 'smtp.qq.com'
username = 'chengdgccc@qq.com'
password='glgfdpxlnhiogaji'
sender='1093637306@qq.com'
receivers = ['chengdegang@ezxr.com']
#收件人为多个收件人
# receiver=['XXX@126.com']

subject = 'Service check reminder'

msg = MIMEMultipart('mixed')
msg['Subject'] = subject
msg['From'] = '1093637306@qq.com <1093637306@qq.com>'
msg['To'] = '18868890069@163.com'
#收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
# msg['To'] = ";".join(receiver)

text = f"Hi!\n{msg_text}\nHere is the link you wanted:\n{urls_failed}"
text_plain = MIMEText(text,'plain', 'utf-8')
msg.attach(text_plain)

smtp = smtplib.SMTP_SSL(smtpserver)
smtp.connect(smtpserver,'465')
#我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
#smtp.set_debuglevel(1)
smtp.login(username, password)
smtp.sendmail(sender,receivers, msg.as_string())
print("send success")
smtp.quit()
