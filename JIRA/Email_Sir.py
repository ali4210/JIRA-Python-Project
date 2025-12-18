from jira import JIRA
import config
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import  encoders
from datetime import *
import time as t
user="automation52786@gmail.com"
apikey='f2Nxb496FAgCCQRJM9OC2510'
server = "https://alnafi.atlassian.net"
jira = JIRA(server,basic_auth=(user,apikey))

issue_in_project = jira.search_issues('project =IIP and issuetype = Request and created >= -5m AND assignee in (empty) and resolution = Unresolved')
total= len(issue_in_project)

tnumber=[]
uname=[]
eaddress=[]
subdetails=[]

for issues in issue_in_project:
    ticket_number = str(issues.key)
    tnumber.append(ticket_number)

    username= str(issues.fields.reporter)
    uname.append(username)

    emailadd = issues.fields.reporter.emailAddress
    eaddress.append(emailadd)

    sdetails = issues.key + ":" + issues.fields.summary
    subdetails.append(sdetails)


if total==0:
    print("JIRA not foun dfrom last 5 min ")
else:
    print("JIRA found")
    for jiraticket in range(total):
        my_mail = "automation52786@gmail.com"
        password = config.EMAIL_PASSWORD
        msg = MIMEMultipart()
        msg['Subject'] = subdetails[jiraticket]
        msg['From'] = my_mail
        msg['To'] = eaddress[jiraticket]
        msg['Cc'] = 'abdealipython@gmail.com'

        body="<p> Dear " + uname[jiraticket] +" , <br> <br> Thank you for writing us. <br> <br> This reply to acknowledgment your message. We have received your JIRA ticket number : " +tnumber[jiraticket] + " Please provide the approval from your reporting head and our team is looking into it and we will get back to you , We look forward to intrect soon. <br><br> Thank you <br> Alnafi Support team</p>"
        t.sleep(3)
        msg.attach(MIMEText(body, 'html'))
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()  # TLS transport layer security

        connection.login(user=my_mail, password=password)
        connection.send_message(msg)
        print("mail has been sent " ,uname[jiraticket] )
        connection.close()
