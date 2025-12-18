from jira import JIRA
import datetime
import config

user="saleemali.mohammad@gmail.com"
apikey=config.JIRA_API_TOKEN
server="https://saleemalimohammad.atlassian.net"
#password="your-password"
#jira=JIRA(server=server,basic_auth=(user,password))

jira=JIRA(server=server,basic_auth=(user,apikey))

ticket='AC-7'
issue=jira.issue(ticket)

comments=issue.fields.comment.comments
commentID=str(0)
mycomment=[]

for comment in comments:
    #print(comment.body)
    #print(comment.id)
    if comment.id > commentID:
        commentID=comment.id
        print (comment.id)
        #print(jira.comment(issue,comment.id).body)
#Recent Comment finding
print(jira.comment(issue,comment.id).body)

print("------------------------------------------------------------")

#             OR

for comment in comments:
    if comment in comments:
        latestcomment=comment.body
        #print(latestcomment)
print(latestcomment)

print("------------------------------------------------------------")

for comment in comments:
    if comment in comments:
        latestcomment=comment.body
        mycomment.append(latestcomment)
print(latestcomment)
print(mycomment[0])

print("------------------------------------------------------------")

for comment in comments:
    eng=comment.author.displayName
    #print(eng)
    if eng == "sameenaAndroid@":
        print(comment.body)

print("------------------------------------------------------------")

for comment in comments:
    jiratime=comment.created
    # print(jiratime)
    # The original format: "%Y-%m-%dT%H:%M:%S.%f"
    # The FIXED format:    "%Y-%m-%dT%H:%M:%S.%f%z"  <-- The '%z' handles the +0600
    datetimeobject = datetime.datetime.strptime(jiratime, "%Y-%m-%dT%H:%M:%S.%f%z")

    #print(datetimeobject)

    mycustom = datetimeobject.strftime("%Y-%m-%d")
    #print(mycustom)

    if mycustom == "2025-11-21":
        print(comment.body)





##This is our API Link
#https://saleemalimohammad.atlassian.net/rest/api/latest/issue/ST-3