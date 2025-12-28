# 🚀 JIRA Python Automation - Quick Reference Card

**Author:** Saleem Ali | **Course:** AIOps @ Al-Nafi International College  
**Version:** 1.0 | **Last Updated:** January 2025

> **Quick access guide for common JIRA automation tasks. Keep this handy for daily operations!**

---

## 📑 Table of Contents

1. [Quick Setup](#-quick-setup)
2. [Essential Commands](#-essential-commands)
3. [Common Patterns](#-common-patterns)
4. [JQL Cheat Sheet](#-jql-cheat-sheet)
5. [Error Quick Fixes](#-error-quick-fixes)
6. [Code Snippets](#-code-snippets)
7. [Time Format Reference](#-time-format-reference)
8. [Date Format Reference](#-date-format-reference)

---

## ⚡ Quick Setup

### Installation (One-Time)

```bash
# Install dependencies
pip install jira paramiko

# Verify installation
python -c "import jira; import paramiko; print('✅ Ready!')"
```

### Environment Variables (Copy & Customize)

```bash
# Windows PowerShell
$env:JIRA_SERVER="https://your-domain.atlassian.net"
$env:JIRA_USER="your-email@gmail.com"
$env:JIRA_API_KEY="your-api-key"
$env:EMAIL_USER="your-email@gmail.com"
$env:EMAIL_PASSWORD="your-app-password"

# Linux/Mac
export JIRA_SERVER="https://your-domain.atlassian.net"
export JIRA_USER="your-email@gmail.com"
export JIRA_API_KEY="your-api-key"
export EMAIL_USER="your-email@gmail.com"
export EMAIL_PASSWORD="your-app-password"
```

### Basic Connection Template

```python
from jira import JIRA
import os

# Load credentials
server = os.getenv('JIRA_SERVER')
user = os.getenv('JIRA_USER')
apikey = os.getenv('JIRA_API_KEY')

# Connect
jira = JIRA(server, basic_auth=(user, apikey))
print("✅ Connected!")
```

---

## 🎯 Essential Commands

### Issue Operations

```python
# GET ISSUE
issue = jira.issue('ST-4')

# CREATE ISSUE
new_issue = jira.create_issue(
    project='ST',
    summary='Issue title',
    description='Issue details',
    issuetype={'name': 'Task'},
    priority={'name': 'High'}
)

# UPDATE ISSUE
issue.update(summary='New title', description='New description')

# DELETE ISSUE (Use with caution!)
issue.delete()

# ASSIGN ISSUE
issue.update(assignee={'accountId': 'user-account-id'})

# UNASSIGN ISSUE
issue.update(assignee=None)
```

### Search & Query

```python
# BASIC SEARCH
issues = jira.search_issues('project = ST')

# ADVANCED SEARCH
issues = jira.search_issues(
    'project = ST AND status = "To Do" AND priority = High',
    maxResults=50
)

# GET COUNT
total = len(issues)

# ITERATE RESULTS
for issue in issues:
    print(f"{issue.key}: {issue.fields.summary}")
```

### Comments

```python
# GET ALL COMMENTS
comments = issue.fields.comment.comments

# ADD COMMENT
jira.add_comment(issue, 'This is a comment')

# GET SPECIFIC COMMENT
comment = jira.comment(issue, comment_id)

# UPDATE COMMENT
comment.update(body='Updated text')

# DELETE COMMENT
comment.delete()

# LATEST COMMENT
latest = comments[-1] if comments else None
```

### Attachments

```python
# ADD ATTACHMENT
with open('file.jpg', 'rb') as f:
    jira.add_attachment(issue='ST-4', attachment=f)

# MULTIPLE ATTACHMENTS
files = ['file1.pdf', 'file2.jpg', 'file3.txt']
for filepath in files:
    with open(filepath, 'rb') as f:
        jira.add_attachment(issue='ST-4', attachment=f)

# GET ATTACHMENTS
attachments = issue.fields.attachment
for att in attachments:
    print(f"{att.filename} ({att.size} bytes)")
```

### Worklogs

```python
# ADD WORKLOG
jira.add_worklog(issue='ST-4', timeSpent='2h')

# WORKLOG WITH COMMENT
jira.add_worklog(
    issue='ST-4',
    timeSpent='2h',
    comment='Fixed the bug'
)

# GET ALL WORKLOGS
worklogs = jira.worklogs(issue)
for log in worklogs:
    print(f"{log.author}: {log.timeSpent}")
```

---

## 🔄 Common Patterns

### Pattern 1: Create Ticket with Everything

```python
# Complete ticket creation
new_issue = jira.create_issue(
    project='ST',
    summary='Complete ticket example',
    description='Detailed description here',
    issuetype={'name': 'Task'},
    priority={'name': 'High'},
    timetracking={'originalEstimate': '4h'},
    assignee={'accountId': 'user-id'}
)

# Add comment
jira.add_comment(new_issue, 'Auto-created by script')

# Add attachment
with open('report.pdf', 'rb') as f:
    jira.add_attachment(new_issue.key, f)

# Log work
jira.add_worklog(new_issue, timeSpent='1h', comment='Initial setup')

print(f"✅ Created: {new_issue.key}")
```

### Pattern 2: Find & Process Unassigned Tickets

```python
# Search unassigned tickets
issues = jira.search_issues(
    'project = ST AND assignee = EMPTY AND resolution = Unresolved'
)

# Process each
for issue in issues:
    print(f"Processing: {issue.key}")
    
    # Add comment
    jira.add_comment(issue, 'Auto-processed by system')
    
    # Assign to default user
    issue.update(assignee={'accountId': 'default-user-id'})
    
    print(f"✅ Assigned: {issue.key}")
```

### Pattern 3: Email Notification Loop

```python
import smtplib
from email.message import EmailMessage

# Find issues
issues = jira.search_issues('created >= -30m AND assignee = EMPTY')

# Connect to SMTP (once!)
connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls()
connection.login(email_user, email_password)

# Send email for each
for issue in issues:
    msg = EmailMessage()
    msg['Subject'] = f'Ticket {issue.key} Received'
    msg['From'] = email_user
    msg['To'] = issue.fields.reporter.emailAddress
    msg.set_content(f'Your ticket {issue.key} has been received.')
    
    connection.send_message(msg)
    print(f"✅ Email sent for {issue.key}")

# Close connection (after all emails!)
connection.close()
```

### Pattern 4: Server Monitoring → JIRA

```python
import paramiko

# Connect to server
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.1.6', username='admin', password='pass')

# Check memory
stdin, stdout, stderr = client.exec_command('free -g')
output = stdout.readlines()
available_mem = int(output[1].split()[6])

# Create ticket if low
if available_mem <= 1:
    issue = jira.create_issue(
        project='IIP',
        summary=f'Low Memory: {available_mem}GB available',
        description=f'Server 192.168.1.6 has low memory',
        issuetype={'name': 'Issue'},
        priority={'name': 'Highest'}
    )
    print(f"⚠️ Alert created: {issue.key}")

client.close()
```

### Pattern 5: Safe Data Extraction

```python
# Search issues
issues = jira.search_issues('project = ST')

# Extract data safely
data = []
for issue in issues:
    ticket_data = {
        'key': issue.key,
        'summary': issue.fields.summary,
        'status': issue.fields.status.name,
        # Safe extraction with fallback
        'assignee': (
            issue.fields.assignee.displayName 
            if issue.fields.assignee 
            else 'Unassigned'
        ),
        'reporter': (
            issue.fields.reporter.displayName 
            if issue.fields.reporter 
            else 'Unknown'
        ),
        'created': issue.fields.created
    }
    data.append(ticket_data)

# Now process data
for item in data:
    print(f"{item['key']}: {item['summary']}")
```

---

## 🔍 JQL Cheat Sheet

### Basic Syntax

```
field operator value
```

### Common Fields

| Field | Example | Description |
|-------|---------|-------------|
| `project` | `project = "ST"` | Project key |
| `issuetype` | `issuetype = Task` | Issue type |
| `status` | `status = "To Do"` | Current status |
| `priority` | `priority = High` | Priority level |
| `assignee` | `assignee = currentUser()` | Assigned person |
| `reporter` | `reporter = "john@email.com"` | Who created it |
| `created` | `created >= -7d` | Creation date |
| `updated` | `updated <= -1h` | Last update |
| `resolution` | `resolution = Unresolved` | Resolution status |
| `duedate` | `duedate < now()` | Due date |

### Common Operators

| Operator | Example | Meaning |
|----------|---------|---------|
| `=` | `status = "Done"` | Equals |
| `!=` | `priority != Low` | Not equals |
| `>` | `created > -7d` | Greater than |
| `<` | `priority < High` | Less than |
| `>=` | `created >= startOfDay()` | Greater or equal |
| `<=` | `duedate <= endOfWeek()` | Less or equal |
| `IN` | `status IN ("To Do", "In Progress")` | In list |
| `NOT IN` | `priority NOT IN (Low, Lowest)` | Not in list |
| `IS` | `assignee IS EMPTY` | Is (for null) |
| `IS NOT` | `resolution IS NOT EMPTY` | Is not |
| `~` | `summary ~ "account"` | Contains text |
| `AND` | `project = ST AND status = Done` | Logical AND |
| `OR` | `priority = High OR priority = Highest` | Logical OR |

### Time Ranges

```jql
created >= -5m          # Last 5 minutes
created >= -2h          # Last 2 hours
created >= -1d          # Last 1 day
created >= -1w          # Last 1 week
created >= -30d         # Last 30 days
created >= startOfDay() # Today
created >= startOfWeek() # This week
```

### Useful JQL Queries

```jql
# Unassigned tickets
project = ST AND assignee = EMPTY AND resolution = Unresolved

# High priority open tickets
project = ST AND priority = High AND status != Done

# My tickets
assignee = currentUser() AND resolution = Unresolved

# Recent tickets
created >= -24h AND project = ST

# Overdue tickets
duedate < now() AND resolution = Unresolved

# Tickets without comments
project = ST AND comment is EMPTY

# Tickets created by specific user
reporter = "john@email.com" AND created >= -7d

# Multiple conditions
project = ST AND 
status IN ("To Do", "In Progress") AND 
priority IN (High, Highest) AND 
created >= -7d
```

---

## 🐛 Error Quick Fixes

### Error: 401 Unauthorized

**Problem:** Wrong credentials

```python
# Fix: Verify credentials
print(f"Server: {server}")
print(f"User: {user}")
print(f"API Key: {apikey[:10]}...")  # Only show first 10 chars

# Generate new API token if needed
# https://id.atlassian.com/manage-profile/security/api-tokens
```

### Error: 404 Not Found

**Problem:** Issue doesn't exist

```python
# Fix: Check issue key
try:
    issue = jira.issue('ST-999')
except JIRAError as e:
    if e.status_code == 404:
        print("Issue not found! Check the ticket number.")
```

### Error: AttributeError 'NoneType'

**Problem:** Accessing None object

```python
# ❌ BAD
assignee = issue.fields.assignee.displayName  # Crashes if None!

# ✅ GOOD
if issue.fields.assignee:
    assignee = issue.fields.assignee.displayName
else:
    assignee = "Unassigned"

# ✅ BETTER (One-liner)
assignee = issue.fields.assignee.displayName if issue.fields.assignee else "Unassigned"
```

### Error: Empty Attachment

**Problem:** File closed before upload

```python
# ❌ BAD
f = open('file.jpg', 'rb')
jira.add_attachment(issue, f)

# ✅ GOOD
with open('file.jpg', 'rb') as f:
    jira.add_attachment(issue, f)
```

### Error: SMTPAuthenticationError

**Problem:** Wrong email password

```python
# Fix: Use App Password, not regular password!
# 1. Enable 2FA in Gmail
# 2. Generate App Password (16 chars: xxxx xxxx xxxx xxxx)
# 3. Use that password in script
```

---

## 💾 Code Snippets

### Complete Script Template

```python
#!/usr/bin/env python3
"""
JIRA Automation Script Template
"""
from jira import JIRA
from jira.exceptions import JIRAError
import sys
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """Main function"""
    try:
        # Connect
        jira = JIRA(server, basic_auth=(user, apikey))
        logger.info("✅ Connected to JIRA")
        
        # Your logic here
        issues = jira.search_issues('project = ST')
        logger.info(f"Found {len(issues)} issues")
        
        return 0
        
    except JIRAError as e:
        logger.error(f"JIRA Error: {e.text}")
        return 1
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

### Read Issue Fields

```python
issue = jira.issue('ST-4')

# Basic info
print(f"Key: {issue.key}")
print(f"ID: {issue.id}")
print(f"Summary: {issue.fields.summary}")
print(f"Description: {issue.fields.description}")

# Status & Type
print(f"Status: {issue.fields.status.name}")
print(f"Type: {issue.fields.issuetype.name}")
print(f"Priority: {issue.fields.priority.name}")

# People
print(f"Assignee: {issue.fields.assignee.displayName if issue.fields.assignee else 'None'}")
print(f"Reporter: {issue.fields.reporter.displayName}")

# Dates
print(f"Created: {issue.fields.created}")
print(f"Updated: {issue.fields.updated}")

# Time tracking
print(f"Original: {issue.fields.timetracking.originalEstimate}")
print(f"Remaining: {issue.fields.timetracking.remainingEstimate}")
print(f"Spent: {issue.fields.timetracking.timeSpent}")

# Project
print(f"Project: {issue.fields.project.key} - {issue.fields.project.name}")
```

### Batch Processing

```python
# Get all issues efficiently
all_issues = []
start = 0
batch_size = 50

while True:
    issues = jira.search_issues(
        'project = ST',
        startAt=start,
        maxResults=batch_size
    )
    all_issues.extend(issues)
    
    if len(issues) < batch_size:
        break
    start += batch_size

print(f"Total: {len(all_issues)} issues")
```

### Error Handling Template

```python
from jira.exceptions import JIRAError

try:
    issue = jira.issue('ST-4')
    print(f"✅ Found: {issue.key}")
    
except JIRAError as e:
    if e.status_code == 401:
        print("❌ Authentication failed")
    elif e.status_code == 404:
        print("❌ Issue not found")
    elif e.status_code == 403:
        print("❌ Permission denied")
    else:
        print(f"❌ JIRA Error {e.status_code}: {e.text}")
        
except Exception as e:
    print(f"❌ Unexpected error: {str(e)}")
```

---

## ⏰ Time Format Reference

### For Time Tracking

```python
# Formats accepted by JIRA
'30m'      # 30 minutes
'1h'       # 1 hour
'2h 30m'   # 2 hours 30 minutes
'1d'       # 1 day (usually 8 hours)
'2d 4h'    # 2 days 4 hours
'1w'       # 1 week (usually 40 hours)
'1w 2d'    # 1 week 2 days
'1w 2d 3h' # 1 week 2 days 3 hours
```

### Usage Examples

```python
# Set estimate
jira.create_issue(
    project='ST',
    summary='Task',
    issuetype={'name': 'Task'},
    timetracking={'originalEstimate': '2h 30m'}
)

# Log work
jira.add_worklog(issue='ST-4', timeSpent='1h 45m')
```

---

## 📅 Date Format Reference

### Python datetime Formats

```python
import datetime

# Format codes
%Y  # Year (4 digits): 2025
%m  # Month (2 digits): 01
%d  # Day (2 digits): 15
%H  # Hour (24-hour): 14
%M  # Minute: 30
%S  # Second: 22
%f  # Microsecond: 840000
%z  # Timezone: +0600
```

### JIRA Timestamp Parsing

```python
# JIRA format: "2025-11-21T14:30:22.840+0600"
jiratime = comment.created

# Parse to datetime object
dt = datetime.datetime.strptime(
    jiratime,
    "%Y-%m-%dT%H:%M:%S.%f%z"
)

# Format to custom string
date_only = dt.strftime("%Y-%m-%d")          # "2025-11-21"
time_only = dt.strftime("%H:%M:%S")          # "14:30:22"
readable = dt.strftime("%B %d, %Y")          # "November 21, 2025"
full = dt.strftime("%Y-%m-%d %H:%M:%S")      # "2025-11-21 14:30:22"
```

### Current Date/Time

```python
from datetime import datetime, timedelta

# Now
now = datetime.now()

# Today (date only)
today = datetime.now().date()

# Calculations
tomorrow = datetime.now() + timedelta(days=1)
last_week = datetime.now() - timedelta(days=7)
two_hours_ago = datetime.now() - timedelta(hours=2)

# Format current time
current = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

---

## 🎯 Best Practices

### ✅ DO

```python
# Use environment variables for credentials
import os
apikey = os.getenv('JIRA_API_KEY')

# Use context managers for files
with open('file.jpg', 'rb') as f:
    jira.add_attachment(issue, f)

# Check for None before accessing
if issue.fields.assignee:
    name = issue.fields.assignee.displayName

# Use try-except for error handling
try:
    issue = jira.issue('ST-4')
except JIRAError as e:
    print(f"Error: {e.text}")

# Reuse connections
connection = smtplib.SMTP('smtp.gmail.com', 587)
for email in emails:
    connection.send_message(email)
connection.close()
```

### ❌ DON'T

```python
# DON'T hardcode credentials
apikey = "ATATT3xFfGF0..."  # ❌ Bad!

# DON'T open files without context manager
f = open('file.jpg', 'rb')  # ❌ Might not close!

# DON'T assume attributes exist
name = issue.fields.assignee.displayName  # ❌ Crashes if None!

# DON'T skip error handling
issue = jira.issue('ST-999')  # ❌ No error handling!

# DON'T reconnect for each operation
for email in emails:
    connection = smtplib.SMTP(...)  # ❌ Slow!
    connection.send_message(email)
    connection.close()
```

---

## 📞 Quick Help

### Generate API Token
https://id.atlassian.com/manage-profile/security/api-tokens

### JIRA REST API Docs
https://developer.atlassian.com/cloud/jira/platform/rest/v3/

### jira-python Library Docs
https://jira.readthedocs.io/

### Get Help
- **Email:** saleemali.mohammad@gmail.com
- **LinkedIn:** [linkedin.com/in/saleem-ali-189719325](https://www.linkedin.com/in/saleem-ali-189719325/)
- **GitHub:** [@ali4210](https://github.com/ali4210)

---

## 🖨️ Print-Friendly Version

```
To print this reference:
1. Save as PDF from browser
2. Print double-sided
3. Laminate for durability
4. Keep near your workstation
```

---

<div align="center">

**🎯 Quick Reference Card - JIRA Python Automation**

**Made by Saleem Ali | AIOps @ Al-Nafi International College**

**⭐ Star the project: [github.com/ali4210](https://github.com/ali4210)**

</div>
