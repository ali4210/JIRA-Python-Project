
# Jira Automation & DevOps Integration Portfolio
**Author:** Saleem Ali
**Focus:** ITSM Automation, System Monitoring, & API Integration
**Tech Stack:** Python 3.x, Jira REST API, Paramiko (SSH), SMTP, JQL

---

## ==>> 1. Comprehensive File Index
*Use this table to find the specific automation logic you need.*

| Module | File Name | Automation Skill |
| :--- | :--- | :--- |
| **Core Jira** | `Jira_ticket_creation.py` | **CRUD Operations:** Create Ticket, Add Comment, Attach Files |
| | `JQL_Query.py` | **Search:** Fetching issues using JQL (Jira Query Language) |
| | `Python_JIRA.py` | **Inspection:** analyzing issue fields & metadata |
| | `Comments.py` | Extracting & filtering comments |
| | `last_comment.py` | Logic to find the *most recent* update |
| **DevOps** | `Linux_to_JIRA.py` | **Server Monitoring:** SSH into Linux -> Check RAM -> Create Alert Ticket |
| **Communication** | `JQL_Query+EMAIL.py` | **Auto-Response:** Fetch Ticket -> Email Reporter automatically |
| | `Email_Sir.py` | HTML Email formatting & SMTP logic |

---

## ==>> Module 1: Core Jira Operations
*Scripts used to interact with the Jira Cloud instance.*

### => Connection Setup
**Concept:** Connecting to Jira Cloud using an API Token (Basic Auth).
```python
from jira import JIRA

user = "your_email@gmail.com"
apikey = "YOUR_ATLASSIAN_API_TOKEN"
server = "[https://your-domain.atlassian.net](https://your-domain.atlassian.net)"

# Establish Connection
jira = JIRA(server=server, basic_auth=(user, apikey))

```

### => Creating Tickets & Attachments (`Jira_ticket_creation.py`)

**Concept:** Programmatically reporting issues and uploading evidence.

```python
# 1. Define Fields
issue_dict = {
    'project': {'key': 'ST'},
    'summary': 'Automated Ticket via Python',
    'description': 'Created by script',
    'issuetype': {'name': 'Task'},
}

# 2. Create Issue
new_issue = jira.create_issue(fields=issue_dict)

# 3. Add Attachment (Using 'with open' for safety)
with open('C:\\error_log.txt', 'rb') as f:
    jira.add_attachment(issue=new_issue.key, attachment=f)

```

### => Advanced Searching (JQL) (`JQL_Query.py`)

**Concept:** Finding specific tickets (e.g., "Unresolved tickets created in the last 30 minutes").

```python
# JQL: Created in last 30m AND Unassigned
query = 'created >= -30m AND assignee = EMPTY AND resolution = Unresolved'
issues = jira.search_issues(query)

for issue in issues:
    print(f"Ticket: {issue.key}, Reporter: {issue.fields.reporter.displayName}")

```

---

## ==>> Module 2: DevOps Integration (Linux -> Jira)

*The most advanced part of your portfolio. It connects Infrastructure to Ticketing.*

### => Server Health Check & Alerting (`Linux_to_JIRA.py`)

**Concept:** SSH into a remote server, check RAM usage, and auto-create a Jira ticket if memory is low.

**1. SSH Connection (Paramiko):**

```python
import paramiko
client = paramiko.SSHClient()
client.connect(hostname="192.168.1.6", username="admin", password="password")

```

**2. Check Memory:**

```python
# Run Linux command
stdin, stdout, stderr = client.exec_command("free -g")
# Parse output to get available GB
available_mem = int(stdout.readlines()[1].split()[6])

```

**3. Conditional Logic:**

```python
if available_mem <= 1:
    # Trigger Jira Incident
    summary = f"CRITICAL: Low Memory on {hostname}"
    jira.create_issue(project='IIP', summary=summary, issuetype={'name': 'Incident'})

```

---

## ==>> Module 3: Automated Communication (SMTP)

*Closing the loop by notifying users via email.*

### => The Auto-Responder (`JQL_Query+EMAIL.py`)

**Concept:** Detect new tickets and immediately send an HTML acknowledgment email to the reporter.

**1. Logic Flow:**

* Fetch new issues via JQL.
* Extract `reporter.emailAddress`.
* Generate HTML Body (`test.html`).
* Send via Gmail SMTP.

**2. SMTP Configuration:**

```python
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = f"We received your ticket {ticket_key}"
msg['To'] = recipient_email
msg.set_content(html_body, subtype='html')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(my_email, my_password)
    smtp.send_message(msg)

```

---

**Status:** Validated
**Dependencies:** `jira`, `paramiko`, `secure-smtplib`

```

