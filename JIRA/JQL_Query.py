from jira import JIRA
import config
import smtplib
from email.message import EmailMessage


my_mail="saleemali.mohammad211126@gmail.com"
my_password=config.GMAIL_APP_PASSWORD
connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls()
connection.login(user=my_mail, password=my_password)


user="saleemali.mohammad@gmail.com"
apikey=config.JIRA_API_TOKEN

server="https://saleemalimohammad.atlassian.net"
#password="your-password"
#jira=JIRA(server=server,basic_auth=(user,password))

jira=JIRA(server=server,basic_auth=(user,apikey))

# issue_in_project= jira.search_issues('project = "ST" and issuetype = Issue AND status in ("To Do",Building,Done)')
#
# print(issue_in_project)
# print(len(issue_in_project))
#
# for issue in issue_in_project:
#     print(f"Ticket Number: {issue.key}\n Ticket Summary:\n {issue.fields.summary}")


issue_in_project= jira.search_issues('created >= -120m AND project =Saleem_T AND assignee = EMPTY AND resolution = Unresolved')
total=len(issue_in_project)

t_number=[]
uname=[]
e_address=[]

for issue in issue_in_project:
    ticket_number = str(issue.key)
    t_number.append(ticket_number)

    username = str(issue.fields.reporter)
    uname.append(username)

    emailAdd = issue.fields.reporter.emailAddress
    e_address.append(emailAdd)



if total==0:
    print("No issues found in JIRA")
else:
    print("There are {} issues found in JIRA".format(total))
    for jiraticket in range(total):
        print(t_number[jiraticket])
        print(uname[jiraticket])
        print(e_address[jiraticket])

       