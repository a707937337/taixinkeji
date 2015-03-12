#-*- coding: utf8 -*-
import smtplib 
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
HOST = "mail.ronglian.com"
SUBJECT = u"官网数据流量报表"
TO = "jjyan@ronglian.com"
FROM = "jjyan@ronglian.com"

#添加图片
def addimage(src,imageid):
	fp = open(src, 'rb')
	msgimage = MIMEImage(fp.read())
	fp.close()
	msgimage.add_header('Content-ID',imageid)
	return msgimage

#邮件内嵌形式
msg = MIMEMultipart('related')

#邮件支持附件
attach = MIMEText(open("c:\ip.xls","rb").read(), "base64", "utf-8")
attach["Content-Type"] = "application/octet-stream"
attach["Content-Disposition"] = "attachment; filename=\"业务报表.xls\"".decode("utf-8").encode("gb18030")

MSG = MIMEText("""
		<table width="800" border="0" cellspacing="0" cellpadding="4">
		<tr>
			<td bgcolor="#CECFAD" height="20" style="font-size:14px">官网数据 <a href="monitor.ronglian.com">更多>></a></td>
			</tr>
			<tr>
			<td bgcolor="#EFEBDE" height="100" style="font-size:13px">
			1)日访问量:</br>
			2）状态码信息:</br>
			3）访问浏览器信息:</td></tr></br>
			<tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
			<td>
			<img src="cid:mem"></td></br><td>
			<img src="cid:cpu">
			</td></tr></table>""",                                                                                                                                                                                         
			"html","utf-8")
msg.attach(attach)
msg.attach(MSG)
msg.attach(addimage("c:\mingxing0306.jpg","mem"))
msg.attach(addimage("c:\qiche0306.jpg","cpu"))
msg["subject"]=SUBJECT
msg["FROM"]=FROM
msg["TO"]=TO
try:
	server = smtplib.SMTP()
	server.connect(HOST,"25")
	server.starttls()
	server.login("jjyan@ronglian.com","Rl123!#%yfQa")
	server.sendmail(FROM,TO,msg.as_string())
	server.quit()
	print u"邮件发送成功"
except Exception, e:
	print u"失败:"+str(e)
