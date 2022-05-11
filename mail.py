import datetime
import dy
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase  # 表示任意对象
from email import encoders  # 邮箱编码器

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "654396051@qq.com"
mail_pass = "dcmhicembzfzbeid"  # 口令
sender = '654396051@qq.com'
receivers = ['654396051@qq.com',"3209726671@qq.com","18051299485@qq.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱


# 邮件信息
date=datetime.date.today()
message=MIMEMultipart()#生成对象
message['From'] = Header("654396051@qq.com", 'utf-8')
message['To'] = Header("", 'utf-8')
subject = '今日电影推送'
message['Subject'] = Header(subject, 'utf-8')



#文本附件
cottents = "{0} 今日更新电影请查收\n国内电影:\n{1}\n日韩电影:\n{2}\n欧美电影:\n{3}".format(date,list(dy.dict1new.keys()),list(dy.dict2new.keys()),list(dy.dict3new.keys()))
att=MIMEText(cottents,"plain","utf-8")
message.attach(att)
#邮箱附件
att=MIMEBase("application", "octet-stream")
att.set_payload(open(r"今日更新电影.txt", "rb").read())
#附件编码
att.add_header("Content-Disposition", "attachment", filename=Header("{}.txt".format(date), "utf-8").encode())
encoders.encode_base64(att)
message.attach(att)


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")