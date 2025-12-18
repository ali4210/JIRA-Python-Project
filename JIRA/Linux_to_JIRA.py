import paramiko
from jira import JIRA
import time
import config
user="automation52786@gmail.com"
apikey=config.JIRA_API_TOKEN
server = "https://alnafi.atlassian.net"
jira = JIRA(server,basic_auth=(user,apikey))


hostname="192.168.1.6"
username="aadmin"
password="123@abd"
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname,username=username,password=password)

cmd= "free -g"
stdin , stdout, stderr = client.exec_command(cmd)

cmdout = stdout.readlines()
available_mem= cmdout[1].split()[6]

if int(available_mem) <= 1:
    print("Memory is not good")
    sum= f"Memory available {available_mem}GB and Server name is {hostname}"
    Desc = f"Hi Team, We found low memroy issue on this server {hostname}, \n {sum}"
    issue_dict = {
        'project': {'key': 'IIP'},
        'issuetype': {'name': 'Issue'},
        'description': Desc  ,
        'summary': sum ,
        'priority': {'name': 'Highest'},
        "timetracking":
            {"originalEstimate": "1h"}
    }
    new_issue = jira.create_issue(fields=issue_dict)
    time.sleep(3)
    new_issue.update(assignee={"accountId": "637b7f598fd2d2d5f12d4929"})
    print("Ticket has been created ")

else:
    print("Memory is good ")



