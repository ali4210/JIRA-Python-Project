from jira import JIRA
import config


user="saleemali.mohammad@gmail.com"
apikey=config.JIRA_API_TOKEN

server="https://saleemalimohammad.atlassian.net"
#password="your-password"
#jira=JIRA(server=server,basic_auth=(user,password))

jira=JIRA(server=server,basic_auth=(user,apikey))

ticket='AC-7'
issue=jira.issue(ticket)

comment=issue.fields.comment.comments
for comment in comment:
    print("My comment is:" ,comment.body)
    print("Comment Auther is:",comment.author)
    print("Comment time is :",comment.created)
    print("-------------------------------------------------")


##This is our API Link
#https://saleemalimohammad.atlassian.net/rest/api/latest/issue/ST-3