from jira import JIRA
import config
user="saleemali.mohammad@gmail.com"
server="https://saleemalimohammad.atlassian.net"
#password="your-password"
#jira=JIRA(server=server,basic_auth=(user,password))

apikey=config.JIRA_API_TOKEN
jira=JIRA(server=server,basic_auth=(user,apikey))

print(jira.fields())

ticket='AC-7'
issue=jira.issue(ticket)
print(type(issue))
print(issue.fields.project)
print(issue.fields.project.key)
print(issue.fields.project.name)
print(issue.fields.issue.name)
print(issue.fields.summary)
print(issue.fields.description)
print(issue.fields.assignee.displayName)
issue=jira.issue(ticket)
print(issue.fields.assignee.displayName)
print(issue.fields.status.name)
print(issue.fields.priority)
print(jira.fields())
print(issue.fields.timetracking)
print(issue.fields.timetracking.remainingEstimate)
print(issue.fields.timetracking.totalEstimate)
print(issue.fields.timetracking.timeSpent)
comments = issue.fields.comment.comments
for comment in comments:
    print(comment.body)


##This is our API Link
#https://saleemalimohammad.atlassian.net/rest/api/latest/issue/AC-7
