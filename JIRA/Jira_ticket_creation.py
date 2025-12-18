import os
import config

from jira import JIRA
from matplotlib.pyplot import summer

user="saleemali.mohammad@gmail.com"
apikey=config.JIRA_API_TOKEN

server="https://saleemalimohammad.atlassian.net"
#password="your-password"
#jira=JIRA(server=server,basic_auth=(user,password))

jira=JIRA(server=server,basic_auth=(user,apikey))

# issue_dict = {
#     'project': {'key': 'ST'},
#     'issuetype': {'name': 'Issue'},
#     'description': 'Account got Locked Seriously',
#     'summary': 'Account got Locked Seriously',
#     'priority': {'name': 'Highest'},
#     'timetracking':
#         { "originalEstimate": "1h"},
#     'assignee': {'accountId': '712020:fd4e96d4-fe75-4c8d-b754-301be21eafd9'},
#
# }
#
# new_issue = jira.create_issue(fields=issue_dict)
# print(new_issue)
#
# jira.add_worklog(new_issue,timeSpent="30m") # For Adding WorkLog TimeSpent

#                            OR

# new_issue = jira.create_issue(project='ST',summary='Account got Locked Seriously', description='Account got Locked Seriously',issuetype={'name': 'Issue'})
# print(new_issue)

new_issue = jira.create_issue(project='ST',summary='Testing JIRA',description='Testing JIRA',issuetype={'name':'Request'},priority={'name':'Highest'},timetracking={'originalEstimate':'10h'}, reporter={'accountId':'712020:fd4e96d4-fe75-4c8d-b754-301be21eafd9'})
print(new_issue)

jira.add_comment(new_issue.key, 'Testing JIRA, This is Automated Comment')
#f=open('C:\\Users\\User\\Downloads\\yes.jpg','rb')
#jira.add_attachment(issue=new_issue.key,attachment=f)



# ---------------------------------------------------------------------
# === FIX: Use a List of File Paths and Iterate with 'with open' ===
# ---------------------------------------------------------------------

attachment_files = [
    'C:\\Users\\User\\Downloads\\yes.jpg',
    'C:\\Users\\User\\Downloads\\my.txt'
]

for file_path in attachment_files:
    if os.path.exists(file_path):
        # The 'with open' ensures the file is available for reading
        # and is automatically closed, preventing the "empty attachment" error.
        with open(file_path, 'rb') as f:
            jira.add_attachment(issue=new_issue.key, attachment=f)
            print(f"✅ Attachment added: {os.path.basename(file_path)}")
    else:
        print(f"⚠️ Warning: File not found at path: {file_path}")

# Add comment after attachments
jira.add_comment(new_issue.key, 'Testing JIRA, This is Automated Comment')
print("✅ Comment Added.")



### For Adding Attachment into an individual Tickets
jira.add_comment('ST-8','Learning JIRA, This an Automated Comment')
f=open('C:\\Users\\User\\Downloads\\yes.jpg','rb')
jira.add_attachment('ST-8',attachment=f)




##This is our API Link
#https://saleemalimohammad.atlassian.net/rest/api/latest/issue/ST-4


