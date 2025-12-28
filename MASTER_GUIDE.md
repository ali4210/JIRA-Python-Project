# 🎯 JIRA with Python Automation - Complete Master Guide

**Version:** 1.0  
**Author:** Saleem Ali  
**Course:** AIOps (AI Operations)  
**Institution:** Al-Nafi International College  
**Last Updated:** December 2024

---

## 📑 Table of Contents

### Part 1: Foundation & Setup
1. [Introduction to JIRA Automation](#1-introduction-to-jira-automation)
2. [Understanding JIRA Architecture](#2-understanding-jira-architecture)
3. [Project Overview](#3-project-overview)
4. [Prerequisites & Environment Setup](#4-prerequisites--environment-setup)
5. [Authentication Methods](#5-authentication-methods)

### Part 2: Core Concepts
6. [JIRA REST API Fundamentals](#6-jira-rest-api-fundamentals)
7. [Python JIRA Library Deep Dive](#7-python-jira-library-deep-dive)
8. [Working with Issues & Tickets](#8-working-with-issues--tickets)
9. [JQL (JIRA Query Language)](#9-jql-jira-query-language)
10. [Comment Management](#10-comment-management)

### Part 3: Advanced Features
11. [Email Integration with SMTP](#11-email-integration-with-smtp)
12. [Attachment Handling](#12-attachment-handling)
13. [Time Tracking & Worklogs](#13-time-tracking--worklogs)
14. [Linux Server Monitoring Integration](#14-linux-server-monitoring-integration)
15. [Date & Time Operations](#15-date--time-operations)

### Part 4: Real-World Applications
16. [Auto-Acknowledgment Email System](#16-auto-acknowledgment-email-system)
17. [Unassigned Ticket Monitoring](#17-unassigned-ticket-monitoring)
18. [Server Health Monitoring](#18-server-health-monitoring)
19. [Comment Analysis & Filtering](#19-comment-analysis--filtering)

### Part 5: Best Practices & Security
20. [Security Best Practices](#20-security-best-practices)
21. [Error Handling & Debugging](#21-error-handling--debugging)
22. [Performance Optimization](#22-performance-optimization)
23. [Production Deployment](#23-production-deployment)

### Part 6: Appendices
24. [Complete Code Reference](#24-complete-code-reference)
25. [Troubleshooting Guide](#25-troubleshooting-guide)
26. [API Reference](#26-api-reference)
27. [Resources & Further Learning](#27-resources--further-learning)

---

# Part 1: Foundation & Setup

## 1. Introduction to JIRA Automation

### 1.1 What is JIRA?

**JIRA** is a powerful project management and issue tracking tool developed by Atlassian. It's widely used in:
- Software development teams (Agile/Scrum)
- IT service management (ITSM)
- DevOps operations
- Business project management

### 1.2 Why Automate JIRA?

**Manual JIRA Operations Are:**
- ⏰ Time-consuming
- 🔄 Repetitive
- ❌ Error-prone
- 📉 Not scalable

**Automation Benefits:**
- ✅ **Efficiency:** Automate repetitive tasks
- ✅ **Consistency:** Standardized processes
- ✅ **Speed:** Instant ticket creation/updates
- ✅ **Integration:** Connect with other systems
- ✅ **Monitoring:** Real-time alerts
- ✅ **Cost Savings:** Reduced manual effort

### 1.3 Real-World Use Cases

**This Project Demonstrates:**

1. **IT Support Automation**
   - Auto-acknowledge support tickets
   - Route tickets to appropriate teams
   - Send status updates to users

2. **Infrastructure Monitoring**
   - Monitor server health
   - Auto-create tickets for issues
   - Alert on-call engineers

3. **Workflow Optimization**
   - Track unassigned tickets
   - Automated notifications
   - Comment analysis

### 1.4 What You'll Learn

By completing this guide, you'll master:

**Technical Skills:**
- JIRA REST API integration
- Python automation scripting
- SMTP email automation
- SSH/Linux integration
- JQL query language
- Error handling & debugging

**Professional Skills:**
- DevOps practices
- AIOps concepts
- System integration
- Production-ready code
- Security best practices

---

## 2. Understanding JIRA Architecture

### 2.1 JIRA Components

```
┌─────────────────────────────────────────┐
│         JIRA ARCHITECTURE               │
├─────────────────────────────────────────┤
│                                         │
│  ┌───────────────────────────────────┐ │
│  │      JIRA Web Interface           │ │
│  │  (User Dashboard & Forms)         │ │
│  └───────────────────────────────────┘ │
│              ↕                          │
│  ┌───────────────────────────────────┐ │
│  │        REST API Layer             │ │
│  │  (Our Automation Entry Point)     │ │
│  └───────────────────────────────────┘ │
│              ↕                          │
│  ┌───────────────────────────────────┐ │
│  │      Business Logic Layer         │ │
│  │   (Workflows, Permissions)        │ │
│  └───────────────────────────────────┘ │
│              ↕                          │
│  ┌───────────────────────────────────┐ │
│  │       Database Layer              │ │
│  │   (Issues, Comments, Users)       │ │
│  └───────────────────────────────────┘ │
│                                         │
└─────────────────────────────────────────┘
```

### 2.2 Key JIRA Concepts

#### **Projects**
- Container for issues
- Has unique key (e.g., "ST", "AC", "IIP")
- Contains workflows and permissions

**Example from your code:**
```python
project='ST'  # Project key "ST" for Saleem_T project
```

#### **Issues/Tickets**
- Individual work items
- Have unique identifiers (e.g., ST-4, AC-7)
- Contains fields: summary, description, priority, etc.

**Issue Format:**
```
PROJECT_KEY-NUMBER
    ↓        ↓
   ST    -   4
```

#### **Issue Types**
Common types in your project:
- **Issue:** General problems
- **Request:** Service requests
- **Task:** Work items
- **Bug:** Software defects

#### **Fields**
Every issue contains fields:
- `summary`: Brief description
- `description`: Detailed information
- `priority`: Importance level
- `assignee`: Responsible person
- `status`: Current state
- `comments`: Discussion thread

### 2.3 JIRA REST API

**What is REST API?**
- **RE**presentational **S**tate **T**ransfer
- HTTP-based communication
- Uses standard methods: GET, POST, PUT, DELETE

**Your JIRA API Endpoint:**
```
https://saleemalimohammad.atlassian.net/rest/api/latest/issue/ST-4
         ↓                              ↓           ↓
    Your Domain                    API Path    Issue Key
```

**API Structure:**
```
Base URL: https://saleemalimohammad.atlassian.net
API Version: /rest/api/latest/ or /rest/api/3/
Resource: /issue/ST-4
```

---

## 3. Project Overview

### 3.1 Project Architecture

```
JIRA AUTOMATION PROJECT
│
├── 📁 Core JIRA Operations
│   ├── Python_JIRA.py          # Basic operations & field retrieval
│   ├── Jira_ticket_creation.py # Ticket creation with attachments
│   └── Comments.py              # Comment retrieval & display
│
├── 📁 Query & Search
│   ├── JQL_Query.py            # JQL queries & data extraction
│   └── last_comment.py         # Advanced comment filtering
│
├── 📁 Email Automation
│   ├── Email_Sir.py            # Auto-acknowledgment system
│   └── JQL_Query+EMAIL.py      # Query + Email integration
│
├── 📁 System Integration
│   └── Linux_to_JIRA.py        # Server monitoring → JIRA
│
└── 📁 Utilities
    ├── testing_date.py         # Date parsing utilities
    └── test.html               # Email template
```

### 3.2 Project Workflow

```
┌─────────────────────────────────────────────────────┐
│              COMPLETE AUTOMATION FLOW                │
└─────────────────────────────────────────────────────┘

1. SERVER MONITORING (Linux_to_JIRA.py)
   ↓
   [Check Server Health] → [Low Memory?] → [Create JIRA Ticket]
   
2. NEW TICKET DETECTION (JQL_Query+EMAIL.py)
   ↓
   [Query Unassigned Tickets] → [Found?] → [Send Acknowledgment Email]
   
3. TICKET MANAGEMENT (Jira_ticket_creation.py)
   ↓
   [Create Ticket] → [Add Comments] → [Attach Files]
   
4. COMMENT ANALYSIS (last_comment.py)
   ↓
   [Get Comments] → [Filter by Date/Author] → [Display Results]
```

### 3.3 Technologies Used

| Technology | Purpose | Files Using It |
|------------|---------|----------------|
| **jira-python** | JIRA API interaction | All .py files |
| **smtplib** | Email sending | Email_Sir.py, JQL_Query+EMAIL.py |
| **paramiko** | SSH connection | Linux_to_JIRA.py |
| **datetime** | Date operations | last_comment.py, testing_date.py |
| **email.mime** | Email formatting | Email scripts |

### 3.4 Your JIRA Instance Details

**From your code, I identified:**

```python
# Your JIRA Instance
server = "https://saleemalimohammad.atlassian.net"
user = "saleemali.mohammad@gmail.com"

# Your Projects
- "ST" (Saleem_T)
- "AC" (Another project)
- "IIP" (Alnafi project from Email_Sir.py)

# Your Issue Types
- Issue
- Request
- Task
```

---

## 4. Prerequisites & Environment Setup

### 4.1 System Requirements

**Operating System:**
- ✅ Windows (Your current: Windows with PyCharm)
- ✅ Linux
- ✅ macOS

**Python Version:**
```bash
Python 3.7 or higher recommended
```

**Check your Python version:**
```bash
python --version
# or
python3 --version
```

### 4.2 Required Libraries

**Install all dependencies:**

```bash
# Core JIRA library
pip install jira

# SSH/Linux integration
pip install paramiko

# Email libraries (usually built-in)
# email, smtplib come with Python

# Date handling (built-in)
# datetime comes with Python
```

**Installation verification:**
```python
# Test script: test_installation.py
try:
    from jira import JIRA
    print("✅ jira-python installed")
except ImportError:
    print("❌ jira-python NOT installed")

try:
    import paramiko
    print("✅ paramiko installed")
except ImportError:
    print("❌ paramiko NOT installed")

import smtplib
print("✅ smtplib available (built-in)")

import datetime
print("✅ datetime available (built-in)")
```

### 4.3 JIRA Setup

**Step 1: Get Your JIRA Instance URL**
```
Your URL: https://saleemalimohammad.atlassian.net
Format: https://[your-domain].atlassian.net
```

**Step 2: Create API Token**

⚠️ **IMPORTANT SECURITY NOTE:**
Your code contains exposed API tokens. We'll fix this in the security section!

**How to create API token:**
1. Log into JIRA
2. Click your profile icon (top right)
3. Select "Account Settings"
4. Navigate to "Security" tab
5. Click "Create and manage API tokens"
6. Click "Create API token"
7. Give it a name (e.g., "Python Automation")
8. Copy the token (save securely!)

**Token format:**
```
ATATT3xFfGF0BL9FH_fwpo8qSgklxJTWqBBLpN1AkXdfE2jts...
```

### 4.4 Email Setup (Gmail)

**For SMTP email automation:**

**Step 1: Enable 2-Factor Authentication**
1. Go to Google Account settings
2. Security → 2-Step Verification
3. Enable it

**Step 2: Generate App Password**
1. Google Account → Security
2. 2-Step Verification
3. Scroll to "App passwords"
4. Select "Mail" and "Other device"
5. Copy the 16-character password

**Format:**
```
xxxx xxxx xxxx xxxx
```

**Your Gmail addresses in code:**
```python
# Primary
my_mail = "saleemali.mohammad@gmail.com"

# Secondary
my_mail = "saleemali.mohammad211126@gmail.com"

# Automation account
user = "automation52786@gmail.com"
```

### 4.5 Project Structure Setup

**Create your project directory:**

```bash
# Create project folder
mkdir JIRA_Automation
cd JIRA_Automation

# Create subdirectories
mkdir scripts
mkdir config
mkdir logs
mkdir templates
```

**Recommended structure:**
```
JIRA_Automation/
├── config/
│   ├── credentials.py      # Store credentials (gitignored)
│   └── settings.py         # Configuration settings
├── scripts/
│   ├── ticket_operations.py
│   ├── email_automation.py
│   ├── monitoring.py
│   └── queries.py
├── templates/
│   └── email_template.html
├── logs/
│   └── automation.log
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 5. Authentication Methods

### 5.1 Understanding JIRA Authentication

**Your code uses two methods:**

#### **Method 1: Basic Auth (Deprecated) ❌**
```python
# OLD METHOD - Don't use
password = "@Sts602cda"
jira = JIRA(server=server, basic_auth=(user, password))
```

**Why it's bad:**
- ❌ Insecure
- ❌ Deprecated by Atlassian
- ❌ May stop working

#### **Method 2: API Token (Recommended) ✅**
```python
# CURRENT METHOD - Use this
apikey = "ATATT3xFfGF0BL9FH_fwpo8q..."
jira = JIRA(server=server, basic_auth=(user, apikey))
```

**Why it's better:**
- ✅ More secure
- ✅ Can be revoked independently
- ✅ Recommended by Atlassian
- ✅ Doesn't expose real password

### 5.2 Connection Pattern - Line by Line

**From Python_JIRA.py:**

```python
from jira import JIRA  # Import JIRA class

# Your credentials
user = "saleemali.mohammad@gmail.com"  # JIRA account email
server = "https://saleemalimohammad.atlassian.net"  # JIRA instance URL
apikey = "ATATT3xFfGF0BL9FH_fwpo8qSgklx..."  # API token

# Create connection
jira = JIRA(server=server, basic_auth=(user, apikey))
```

**What happens here:**

```python
JIRA(server=server, basic_auth=(user, apikey))
     ↓                         ↓
   URL to                  Authentication
 connect to                  credentials
```

**Behind the scenes:**
1. Python sends HTTP request to JIRA server
2. Includes encoded credentials in header
3. JIRA validates credentials
4. Returns session object
5. Now you can make API calls!

### 5.3 Secure Credential Management

**❌ NEVER do this (from your code):**
```python
# Hardcoded credentials in script - BAD!
apikey = "ATATT3xFfGF0BL9FH_fwpo8qSgklxJTWqBBLpN1AkXdfE..."
my_password = "bkgrpowfabscrrpb"
```

**✅ DO this instead:**

**Option 1: Environment Variables**

```python
# config/credentials.py
import os

# Load from environment
JIRA_USER = os.getenv('JIRA_USER')
JIRA_API_KEY = os.getenv('JIRA_API_KEY')
JIRA_SERVER = os.getenv('JIRA_SERVER')

EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
```

**Set environment variables (Windows):**
```bash
# PowerShell
$env:JIRA_USER = "saleemali.mohammad@gmail.com"
$env:JIRA_API_KEY = "your-api-key"
$env:JIRA_SERVER = "https://saleemalimohammad.atlassian.net"
```

**Set environment variables (Linux/Mac):**
```bash
export JIRA_USER="saleemali.mohammad@gmail.com"
export JIRA_API_KEY="your-api-key"
export JIRA_SERVER="https://saleemalimohammad.atlassian.net"
```

**Option 2: Configuration File (Gitignored)**

```python
# config/credentials.py
# Add this file to .gitignore!

JIRA_CONFIG = {
    'server': 'https://saleemalimohammad.atlassian.net',
    'user': 'saleemali.mohammad@gmail.com',
    'api_key': 'your-api-key-here'
}

EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'user': 'your-email@gmail.com',
    'password': 'your-app-password'
}
```

**Usage in scripts:**
```python
# Your script
from config.credentials import JIRA_CONFIG, EMAIL_CONFIG
from jira import JIRA

# Connect using config
jira = JIRA(
    server=JIRA_CONFIG['server'],
    basic_auth=(JIRA_CONFIG['user'], JIRA_CONFIG['api_key'])
)
```

### 5.4 Connection Verification

**Test your connection:**

```python
# test_connection.py
from jira import JIRA
import sys

def test_jira_connection():
    """Test JIRA connection and display info"""
    
    user = "saleemali.mohammad@gmail.com"
    apikey = "your-api-key"  # Replace with yours
    server = "https://saleemalimohammad.atlassian.net"
    
    try:
        # Attempt connection
        print("🔄 Connecting to JIRA...")
        jira = JIRA(server=server, basic_auth=(user, apikey))
        
        # Test successful - get user info
        current_user = jira.current_user()
        print(f"✅ Assignee: {assignee}")
        return issue
        
    except JIRAError as e:
        if e.status_code == 401:
            print("❌ Authentication failed! Check your API key.")
        elif e.status_code == 404:
            print("❌ Issue not found!")
        else:
            print(f"❌ JIRA Error: {e.text}")
        sys.exit(1)
        
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    safe_jira_operation()
```

**Best practices for error handling:**

```python
# Always wrap API calls in try-except
try:
    issue = jira.issue('ST-4')
except JIRAError as e:
    # Handle JIRA-specific errors
    pass
except Exception as e:
    # Handle other errors
    pass
finally:
    # Cleanup code (if needed)
    pass
```

---

## 8. Working with Issues & Tickets

### 8.1 Reading Issue Data

**From Python_JIRA.py - Complete breakdown:**

```python
from jira import JIRA

# Setup connection
user = "saleemali.mohammad@gmail.com"
apikey = "ATATT3xFfGF0BL9FH_fwpo8qSgklx..."
server = "https://saleemalimohammad.atlassian.net"
jira = JIRA(server=server, basic_auth=(user, apikey))

# Define which ticket to get
ticket = 'AC-7'  # Format: PROJECT_KEY-NUMBER

# Fetch the issue
issue = jira.issue(ticket)
# This makes an HTTP GET request to:
# https://saleemalimohammad.atlassian.net/rest/api/latest/issue/AC-7

# Now 'issue' is a Python object containing all ticket data
```

**What happens behind the scenes:**
```
1. Python sends HTTP GET request
2. JIRA validates your credentials
3. JIRA retrieves issue from database
4. JIRA returns JSON response
5. jira-python converts JSON to Python object
6. You get 'issue' object to work with
```

**Accessing different fields:**

```python
# Project Information
print(issue.fields.project)          # Project object
print(issue.fields.project.key)      # 'AC'
print(issue.fields.project.name)     # 'Account Project'

# Issue Basic Info
print(issue.key)                     # 'AC-7'
print(issue.fields.summary)          # Title/Summary
print(issue.fields.description)      # Detailed description
print(issue.fields.issuetype.name)   # 'Issue', 'Task', etc.

# People
print(issue.fields.assignee.displayName)    # Who's assigned
print(issue.fields.reporter.displayName)    # Who created it

# Status & Priority
print(issue.fields.status.name)      # 'To Do', 'In Progress', etc.
print(issue.fields.priority.name)    # 'High', 'Medium', 'Low'

# Time Information
print(issue.fields.created)          # Creation timestamp
print(issue.fields.updated)          # Last update timestamp

# Time Tracking
print(issue.fields.timetracking.originalEstimate)   # '10h'
print(issue.fields.timetracking.remainingEstimate)  # '7h'
print(issue.fields.timetracking.timeSpent)          # '3h'
```

### 8.2 Creating Issues

**From Jira_ticket_creation.py - Method 1 (Dictionary):**

```python
from jira import JIRA

# Connection setup
user = "saleemali.mohammad@gmail.com"
apikey = "ATATT3xFfGF0BL9FH_fwpo8qSgklx..."
server = "https://saleemalimohammad.atlassian.net"
jira = JIRA(server=server, basic_auth=(user, apikey))

# Method 1: Using dictionary (More control)
issue_dict = {
    'project': {'key': 'ST'},                    # Which project
    'issuetype': {'name': 'Issue'},              # Type of issue
    'summary': 'Account got Locked Seriously',    # Title
    'description': 'Account got Locked Seriously', # Details
    'priority': {'name': 'Highest'},             # Priority level
    'timetracking': {
        "originalEstimate": "1h"                 # Estimated time
    },
    'assignee': {
        'accountId': '712020:fd4e96d4-fe75-4c8d-b754-301be21eafd9'
    }
}

# Create the issue
new_issue = jira.create_issue(fields=issue_dict)
print(new_issue)  # Output: ST-8 (or next available number)
```

**Line-by-line explanation:**

```python
issue_dict = {
    'project': {'key': 'ST'},
    # ↓
    # Specifies which project to create the issue in
    # 'ST' is your project key for "Saleem_T"
    
    'issuetype': {'name': 'Issue'},
    # ↓
    # What type of work item
    # Options: 'Issue', 'Task', 'Bug', 'Story', 'Request'
    
    'summary': 'Account got Locked Seriously',
    # ↓
    # Brief title - appears in lists and searches
    # Keep it concise but descriptive
    
    'description': 'Account got Locked Seriously',
    # ↓
    # Detailed explanation of the issue
    # Can include multiple lines, formatting, etc.
    
    'priority': {'name': 'Highest'},
    # ↓
    # How urgent/important
    # Options: 'Highest', 'High', 'Medium', 'Low', 'Lowest'
    
    'timetracking': {
        "originalEstimate": "1h"
    },
    # ↓
    # How long you estimate this will take
    # Format: '1h', '30m', '2h 30m', '1d', etc.
    
    'assignee': {
        'accountId': '712020:fd4e96d4-fe75-4c8d-b754-301be21eafd9'
    }
    # ↓
    # Who should work on this
    # Uses JIRA account ID (not email!)
}

# Create it!
new_issue = jira.create_issue(fields=issue_dict)
# ↓
# Sends POST request to JIRA
# Returns the created issue object
# You can now use new_issue.key (e.g., 'ST-8')
```

**Method 2: Direct parameters (Simpler):**

```python
# Method 2: Direct parameters
new_issue = jira.create_issue(
    project='ST',
    summary='Testing JIRA',
    description='Testing JIRA',
    issuetype={'name': 'Request'},
    priority={'name': 'Highest'},
    timetracking={'originalEstimate': '10h'},
    reporter={'accountId': '712020:fd4e96d4-fe75-4c8d-b754-301be21eafd9'}
)
print(new_issue)  # Output: ST-9
```

**What's the difference?**
- Method 1: More verbose, better for complex issues
- Method 2: Cleaner, easier to read, same result

**Both methods do the same thing!**

### 8.3 Adding Comments

**From Jira_ticket_creation.py:**

```python
# After creating an issue
new_issue = jira.create_issue(
    project='ST',
    summary='Testing JIRA',
    description='Testing JIRA',
    issuetype={'name': 'Request'}
)

# Add a comment to this new issue
jira.add_comment(new_issue.key, 'Testing JIRA, This is Automated Comment')
# ↓                ↓                ↓
# Method      Issue key        Comment text
```

**Adding comment to existing issue:**

```python
# Add comment to specific ticket
jira.add_comment('ST-8', 'Learning JIRA, This is an Automated Comment')
#                  ↓              ↓
#            Ticket key     Comment text
```

**What happens:**
1. Python sends POST request to JIRA
2. JIRA adds comment to issue
3. Comment appears with your name and timestamp
4. Email notification sent to watchers (if enabled)

**Advanced comment operations:**

```python
# Get all comments on an issue
issue = jira.issue('ST-8')
comments = issue.fields.comment.comments

# Print all comments
for comment in comments:
    print(f"Author: {comment.author.displayName}")
    print(f"Text: {comment.body}")
    print(f"Created: {comment.created}")
    print("-" * 50)

# Update a comment
comment = jira.comment('ST-8', '10001')  # Get comment by ID
comment.update(body='Updated comment text')

# Delete a comment
comment.delete()
```

### 8.4 Adding Attachments

**From Jira_ticket_creation.py - The CORRECT way:**

```python
import os
from jira import JIRA

# Connection
jira = JIRA(server=server, basic_auth=(user, apikey))

# Create issue first
new_issue = jira.create_issue(
    project='ST',
    summary='Testing JIRA',
    description='Testing JIRA',
    issuetype={'name': 'Request'}
)

# ❌ WRONG WAY (from original code):
# f = open('C:\\Users\\User\\Downloads\\yes.jpg', 'rb')
# jira.add_attachment(issue=new_issue.key, attachment=f)
# Problem: File handle closes before upload completes

# ✅ CORRECT WAY (Fixed version):
attachment_files = [
    'C:\\Users\\User\\Downloads\\yes.jpg',
    'C:\\Users\\User\\Downloads\\my.txt'
]

for file_path in attachment_files:
    # Check if file exists first
    if os.path.exists(file_path):
        # Use 'with open' - automatically handles file closing
        with open(file_path, 'rb') as f:
            jira.add_attachment(issue=new_issue.key, attachment=f)
            print(f"✅ Attachment added: {os.path.basename(file_path)}")
    else:
        print(f"⚠️ Warning: File not found at path: {file_path}")

# Add comment after attachments
jira.add_comment(new_issue.key, 'Testing JIRA, This is Automated Comment')
print("✅ Comment Added.")
```

**Why use `with open()`?**

```python
# WITHOUT 'with' (Problematic):
f = open('file.jpg', 'rb')
jira.add_attachment(issue, f)
# Problem: File might not be fully read before it's used
# File handle stays open (memory leak)

# WITH 'with' (Correct):
with open('file.jpg', 'rb') as f:
    jira.add_attachment(issue, f)
# Benefits:
# ✅ File automatically closed after block
# ✅ Proper error handling
# ✅ No memory leaks
# ✅ Guaranteed file availability during upload
```

**Adding attachments to existing ticket:**

```python
# Add to specific ticket
jira.add_comment('ST-8', 'Learning JIRA, This is an Automated Comment')

# Add attachment to that same ticket
with open('C:\\Users\\User\\Downloads\\yes.jpg', 'rb') as f:
    jira.add_attachment('ST-8', attachment=f)
```

**Multiple files at once:**

```python
files_to_attach = [
    'path/to/screenshot.png',
    'path/to/logfile.txt',
    'path/to/document.pdf'
]

for filepath in files_to_attach:
    if os.path.exists(filepath):
        with open(filepath, 'rb') as f:
            jira.add_attachment('ST-8', attachment=f)
        print(f"✅ Uploaded: {os.path.basename(filepath)}")
```

### 8.5 Updating Issues

**Update various fields:**

```python
# Get the issue first
issue = jira.issue('ST-8')

# Update single field
issue.update(summary='New Title')

# Update multiple fields
issue.update(
    summary='Updated Title',
    description='Updated description',
    priority={'name': 'High'}
)

# Update assignee
issue.update(assignee={'accountId': 'user-account-id'})

# Remove assignee (make unassigned)
issue.update(assignee=None)

# Update status (transition)
jira.transition_issue(issue, 'In Progress')
# Or use transition ID:
jira.transition_issue(issue, '21')
```

### 8.6 Adding Worklogs

**From Jira_ticket_creation.py:**

```python
# Create issue
new_issue = jira.create_issue(
    project='ST',
    summary='Account got Locked',
    description='Account got Locked',
    issuetype={'name': 'Issue'}
)

# Log time spent on this issue
jira.add_worklog(new_issue, timeSpent="30m")
#                    ↓            ↓
#                Issue obj    Time format

# Time formats accepted:
# '30m'    - 30 minutes
# '1h'     - 1 hour
# '2h 30m' - 2 hours 30 minutes
# '1d'     - 1 day (usually 8 hours)
# '1w'     - 1 week (usually 5 days)
```

**Advanced worklog:**

```python
from datetime import datetime

# Add worklog with specific date
jira.add_worklog(
    issue='ST-8',
    timeSpent='2h',
    comment='Fixed the account lock issue',
    started=datetime(2025, 1, 15, 9, 0, 0)  # When work started
)
```

---

## 9. JQL (JIRA Query Language)

### 9.1 What is JQL?

**JQL = JIRA Query Language**
- SQL-like syntax for searching JIRA
- Filter issues based on criteria
- Used in `jira.search_issues()`

**Basic structure:**
```
field operator value
  ↓      ↓       ↓
project = "ST"
```

### 9.2 Common Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| = | Equals | `project = "ST"` |
| != | Not equals | `status != "Done"` |
| > | Greater than | `created > -7d` |
| < | Less than | `priority < "High"` |
| >= | Greater or equal | `created >= -30d` |
| <= | Less or equal | `priority <= "Medium"` |
| IN | In list | `status IN ("To Do", "In Progress")` |
| NOT IN | Not in list | `status NOT IN ("Done", "Closed")` |
| IS | Is (for null) | `assignee IS EMPTY` |
| IS NOT | Is not | `assignee IS NOT EMPTY` |
| AND | Logical AND | `project = "ST" AND status = "Open"` |
| OR | Logical OR | `priority = "High" OR priority = "Highest"` |

### 9.3 JQL Examples from Your Code

**From JQL_Query.py:**

#### **Example 1: Basic project filter**
```python
issue_in_project = jira.search_issues('project = "ST" and issuetype = Issue AND status in ("To Do",Building,Done)')
```

**Breaking it down:**
```
project = "ST"              # Only from ST project
AND                         # All conditions must be true
issuetype = Issue           # Only "Issue" type (not Tasks, Bugs, etc.)
AND                         # Another condition
status in ("To Do", Building, Done)  # Status must be one of these
```

**What this query returns:**
- All issues from ST project
- That are type "Issue"
- With status "To Do", "Building", or "Done"

#### **Example 2: Time-based unassigned tickets**
```python
issue_in_project = jira.search_issues('created >= -120m AND project =Saleem_T AND assignee = EMPTY AND resolution = Unresolved')
```

**Breaking it down:**
```
created >= -120m            # Created in last 120 minutes
AND                         # All must be true
project = Saleem_T          # From Saleem_T project
AND
assignee = EMPTY            # No one assigned yet
AND
resolution = Unresolved     # Not resolved/closed
```

**Time formats:**
- `-5m` = Last 5 minutes
- `-2h` = Last 2 hours
- `-1d` = Last 1 day
- `-1w` = Last 1 week
- `-30d` = Last 30 days

**What this finds:**
Recent unassigned tickets that need attention!

### 9.4 Real-World JQL Queries

**Find high-priority unassigned tickets:**
```python
jql = 'project = "ST" AND priority = "Highest" AND assignee = EMPTY'
issues = jira.search_issues(jql)
```

**Find your assigned tickets:**
```python
jql = 'assignee = currentUser() AND resolution = Unresolved'
issues = jira.search_issues(jql)
```

**Find tickets created today:**
```python
jql = 'created >= startOfDay()'
issues = jira.search_issues(jql)
```

**Find overdue tickets:**
```python
jql = 'duedate < now() AND resolution = Unresolved'
issues = jira.search_issues(jql)
```

**Find tickets with specific text:**
```python
jql = 'text ~ "account locked"'
issues = jira.search_issues(jql)
```

### 9.5 Processing Search Results

**From JQL_Query.py - Complete walkthrough:**

```python
from jira import JIRA

# Setup
user = "saleemali.mohammad@gmail.com"
apikey = "ATATT3xFfGF0BL9FH_fwpo8qSgklx..."
server = "https://saleemalimohammad.atlassian.net"
jira = JIRA(server=server, basic_auth=(user, apikey))

# Search with JQL
issue_in_project = jira.search_issues(
    'created >= -120m AND project ="Saleem_T" AND assignee = EMPTY AND resolution = Unresolved'
)

# Get count of results
total = len(issue_in_project)

# Prepare lists to store extracted data
t_number = []      # Ticket numbers
uname = []         # Usernames
e_address = []     # Email addresses

# Loop through each issue found
for issue in issue_in_project:
    # Extract ticket number
    ticket_number = str(issue.key)
    t_number.append(ticket_number)
    # Result: ['ST-5', 'ST-6', 'ST-7']
    
    # Extract reporter (who created it)
    username = str(issue.fields.reporter)
    uname.append(username)
    # Result: ['John Doe', 'Jane Smith', ...]
    
    # Extract email address
    emailAdd = issue.fields.reporter.emailAddress
    e_address.append(emailAdd)
    # Result: ['john@email.com', 'jane@email.com', ...]

# Check if any issues were found
if total == 0:
    print("No issues found in JIRA")
else:
    print(f"There are {total} issues found in JIRA")
    
    # Display all found issues
    for jiraticket in range(total):
        print(t_number[jiraticket])    # ST-5
        print(uname[jiraticket])       # John Doe
        print(e_address[jiraticket])   # john@email.com
```

**Why use lists?**
```python
t_number = []      # Empty list
t_number.append('ST-5')  # Add item
t_number.append('ST-6')  # Add another
# Result: ['ST-5', 'ST-6']

# Access by index:
print(t_number[0])  # 'ST-5'
print(t_number[1])  # 'ST-6'
```

**Safe attribute access:**

```python
# ❌ UNSAFE (could crash if None):
username = str(issue.fields.reporter)
emailAdd = issue.fields.reporter.emailAddress

# ✅ SAFE (checks first):
if issue.fields.reporter:
    username = str(issue.fields.reporter.displayName)
    emailAdd = issue.fields.reporter.emailAddress
else:
    username = "Unknown User"
    emailAdd = "no-email@example.com"
```

---

## 10. Comment Management

### 10.1 Understanding Comments

**Comments in JIRA:**
- Discussion thread on each issue
- Each comment has:
  - Text body
  - Author
  - Timestamp
  - Unique ID

**From Comments.py:**

```python
from jira import JIRA

# Connection
user = "saleemali.mohammad@gmail.com"
apikey = "ATATT3xFfGF0BL9FH_fwpo8qSgklx..."
server = "https://saleemalimohammad.atlassian.net"
jira = JIRA(server=server, basic_auth=(user, apikey))

# Get specific ticket
ticket = 'AC-7'
issue = jira.issue(ticket)

# Get all comments
comment = issue.fields.comment.comments
# This is a LIST of comment objects

# Loop through and display
for comment in comment:
    print("My comment is:", comment.body)
    print("Comment Author is:", comment.author)
    print("Comment time is:", comment.created)
    print("-" * 50)
```

**Output example:**
```
My comment is: We're looking into this issue
Comment Author is: <JIRA User: sameenaAndroid@>
Comment time is: 2025-01-15T14:30:22.840+0600
--------------------------------------------------
My comment is: Issue has been resolved
Comment Author is: <JIRA User: admin>
Comment time is: 2025-01-15T16:45:10.320+0600
--------------------------------------------------
```

### 10.2 Getting the Latest Comment

**From last_comment.py - Method 1 (By ID):**

```python
from jira import JIRA

# Setup connection
jira = JIRA(server=server, basic_auth=(user, apikey))

ticket = 'AC-7'
issue = jira.issue(ticket)

# Get all comments
comments = issue.fields.comment.comments

# Initialize with 0 (lowest possible ID)
commentID = str(0)

# Find the highest (latest) comment ID
for comment in comments:
    if comment.id > commentID:
        commentID = comment.id
        print(comment.id)  # Print each time we find a newer one

# Get the comment with highest ID (most recent)
latest_comment = jira.comment(issue, commentID).body
print(latest_comment)
```

**How it works:**
```
Comments with IDs:
ID: 10001 → "First comment"
ID: 10002 → "Second comment"
ID: 10003 → "Latest comment"  ← We want this one!

Loop compares:
0 < 10001? Yes → commentID = 10001
10001 < 10002? Yes → commentID = 10002
10002 < 10003? Yes → commentID = 10003
Done! commentID = 10003 (latest)
```

**Method 2 (Last in list):**

```python
# Get all comments
comments = issue.fields.comment.comments

# The last comment in the list is the most recent
for comment in comments:
    if comment in comments:  # Always true, just loops through
        latestcomment = comment.body
        
# After loop, latestcomment contains the last one
print(latestcomment)
```

**Method 3 (Using list indexing - BEST):**

```python
comments = issue.fields.comment.comments

if comments:  # Check if there are any comments
    latest = comments[-1]  # -1 gets last item
    print(f"Latest comment: {latest.body}")
    print(f"By: {latest.author.displayName}")
    print(f"At: {latest.created}")
else:
    print("No comments found")
```

### 10.3 Filtering Comments

**Filter by author:**

```python
# Get all comments
comments = issue.fields.comment.comments

# Find comments by specific user
for comment in comments:
    eng = comment.author.displayName
    if eng == "sameenaAndroid@":
        print(comment.body)
```

**What this does:**
```
Loop through all comments:
Comment 1: Author = "admin" → Skip
Comment 2: Author = "sameenaAndroid@" → PRINT! ✅
Comment 3: Author = "john.doe" → Skip
Comment 4: Author = "sameenaAndroid@" → PRINT! ✅
```

**Filter by date:**

```python
import datetime

# Get all comments
comments = issue.fields.comment.comments

for comment in comments:
    # Get timestamp string
    jiratime = comment.created
    # Example: "2025-11-21T14:30:22.840+0600"
    
    # Convert to datetime object
    datetimeobject = datetime.datetime.strptime(
        jiratime, 
        "%Y-%m-%dT%H:%M:%S.%f%z"
    )
    
    # Format to just the date
    mycustom = datetimeobject.strftime("%Y-%m-%d")
    # Result: "2025-11-21"
    
    # Check if it's the date we want
    if mycustom == "2025-11-21":
        print(comment.body)
```

**Date format breakdown:**
```python
"%Y-%m-%dT%H:%M:%S.%f%z"
  ↓   ↓  ↓  ↓  ↓  ↓  ↓  ↓
Year-Mo-DayTHr:Min:Sec.Microseconds+Timezone

Example: 2025-11-21T14:30:22.840+0600
         Year=2025
         Month=11
         Day=21
         Hour=14
         Minute=30
         Second=22
         Microsecond=840
         Timezone=+0600
```

### 10.4 Storing Comments in Lists

**From last_comment.py:**

```python
# Create empty list
mycomment = []

# Add all comments to list
for comment in comments:
    if comment in comments:
        latestcomment = comment.body
        mycomment.append(latestcomment)

# Now mycomment = ["Comment 1", "Comment 2", "Comment 3", ...]

# Access specific comments:
print(mycomment[0])   # First comment
print(mycomment[-1])  # Last comment (latest)
print(len(mycomment)) # Total count
```

**Why use lists for comments?**
- Store all for later processing
- Can sort, filter, analyze
- Keep history
- Export to file/database

---

## 11. Email Integration with SMTP

### 11.1 Understanding SMTP

**SMTP = Simple Mail Transfer Protocol**
- Standard protocol for sending emails
- Uses port 587 (with TLS encryption)
- Requires authentication

**Email flow:**
```
Your Script → SMTP Server → Recipient
    ↓            ↓              ↓
Python code  Gmail servers  User's inbox
```

### 11.2 Gmail SMTP Configuration

**From JQL_Query+EMAIL.py:**

```python
import smtplib
from email.message import EmailMessage

# === EMAIL CONFIGURATION ===
my_mail = "saleemali.mohammad@gmail.com"
my_password = "kxqs chfl bxkl jjme"  # Gmail App Password
smtp_server = 'smtp.gmail.com'
smtp_port = 587
```

**Important notes:**
1. **NOT your regular Gmail password!**
   - This is an "App Password"
   - Generated in Google Account settings
   - 16 characters, format: "xxxx xxxx xxxx xxxx"

2. **SMTP Server Details:**
   - Gmail: `smtp.gmail.com`
   - Port: `587` (TLS encryption)
   - Alternative port: `465` (SSL encryption)

3. **Prerequisites:**
   - 2-Factor Authentication enabled
   - App Password generated
   - "Less secure apps" NOT needed with App Password

### 11.3 Email Components

**From Email_Sir.py:**

```python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
```

**What each does:**

| Module | Purpose | Example Use |
|--------|---------|-------------|
| `MIMEMultipart` | Container for email with multiple parts | Email with text + attachments |
| `MIMEText` | Text content (plain or HTML) | Email body |
| `MIMEBase` | Base for attachments | PDF, ZIP files |
| `MIMEImage` | Image attachments | JPG, PNG files |
| `encoders` | Encode attachments | Make binary files email-safe |

### 11.4 Creating Email Messages

**Basic email structure:**

```python
import smtplib
from email.message import EmailMessage

# Create message object
msg = EmailMessage()

# Set headers
msg['Subject'] = 'Acknowledgment: Your JIRA Ticket ST-4 has been received'
msg['From'] = 'saleemali.mohammad@gmail.com'
msg['To'] = 'recipient@email.com'
msg['Cc'] = 'cc-recipient@email.com'  # Optional

# Set body (plain text)
msg.set_content('Hello, your ticket has been received.')
```

**HTML email (Better formatting):**

```python
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Ticket Acknowledgment'
msg['From'] = my_mail
msg['To'] = recipient_email

# HTML content
html_content = """
<!DOCTYPE html>
<html>
<body>
    <p>Dear User,</p>
    <p>Your JIRA ticket <strong>ST-4</strong> has been received.</p>
    <p>Thank you,<br>Support Team</p>
</body>
</html>
"""

# Add HTML (use add_attachment with subtype='html')
msg.add_attachment(html_content, subtype='html')
```

### 11.5 Sending Emails

**Complete email sending process:**

```python
import smtplib
from email.message import EmailMessage
import sys

# Configuration
my_mail = "saleemali.mohammad@gmail.com"
my_password = "your-app-password"
smtp_server = 'smtp.gmail.com'
smtp_port = 587

try:
    # Step 1: Connect to SMTP server
    connection = smtplib.SMTP(smtp_server, smtp_port)
    print("✅ Connected to SMTP server")
    
    # Step 2: Start TLS encryption
    connection.starttls()
    print("✅ TLS encryption started")
    
    # Step 3: Login with credentials
    connection.login(user=my_mail, password=my_password)
    print("✅ Logged in successfully")
    
    # Step 4: Create message
    msg = EmailMessage()
    msg['Subject'] = 'Test Email'
    msg['From'] = my_mail
    msg['To'] = 'recipient@email.com'
    msg.set_content('This is a test email from Python!')
    
    # Step 5: Send message
    connection.send_message(msg)
    print("✅ Email sent successfully")
    
except Exception as e:
    print(f"❌ Email sending failed: {str(e)}")
    sys.exit(1)
    
finally:
    # Step 6: Close connection (Always!)
    connection.close()
    print("✅ Connection closed")
```

**What each step does:**

```python
# Step 1: Connect
connection = smtplib.SMTP(smtp_server, smtp_port)
# Opens connection to Gmail's SMTP server on port 587

# Step 2: Start TLS
connection.starttls()
# Upgrades connection to encrypted (secure)
# TLS = Transport Layer Security

# Step 3: Login
connection.login(user=my_mail, password=my_password)
# Authenticates with Gmail using App Password

# Step 4: Create message
msg = EmailMessage()
# Creates email object with headers and content

# Step 5: Send
connection.send_message(msg)
# Transmits email to Gmail servers → Recipient

# Step 6: Close
connection.close()
# Terminates connection (important!)
```

### 11.6 JIRA + Email Integration

**From JQL_Query+EMAIL.py - Complete breakdown:**

```python
import smtplib
from email.message import EmailMessage
from jira import JIRA
import sys

# === EMAIL SETUP ===
my_mail = "saleemali.mohammad@gmail.com"
my_password = "kxqs chfl bxkl jjme"  # App Password
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# === JIRA SETUP ===
user = "saleemali.mohammad@gmail.com"
apikey = "ATATT3xFfGF0BL9FH_fwpo8qSgklx..."
server = "https://saleemalimohammad.atlassian.net"

# === HTML TEMPLATE ===
EMAIL_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>JIRA Acknowledgment</title>
</head>
<body>
<p> Dear {reporter_name}, <br> <br> 
Thank You for writing to us. <br> <br> 
This reply is to acknowledge your message request for <strong>JIRA Ticket {ticket_key}</strong>. 
We have received your message and our team is looking into it and will get back to you soon. 
<br> <br> 
Thank You<br> 
Alnafi Support Team 
</p>
</body>
</html>
"""
```

**Why define template OUTSIDE the loop?**

```python
# ❌ BAD: Defining inside loop (wastes resources)
for ticket in tickets:
    EMAIL_TEMPLATE = "..." # Recreated every time!
    
# ✅ GOOD: Define once, use many times
EMAIL_TEMPLATE = "..."
for ticket in tickets:
    email = EMAIL_TEMPLATE.format(...) # Reuse template
```

**Connection and data fetch:**

```python
try:
    # Connect to JIRA
    jira = JIRA(server=server, basic_auth=(user, apikey))
    print("✅ Jira Connection Successful.")
    
    # Connect to SMTP (BEFORE loop!)
    connection = smtplib.SMTP(smtp_server, smtp_port)
    connection.starttls()
    connection.login(user=my_mail, password=my_password)
    print("✅ SMTP Connection Successful.")
    
except Exception as e:
    print(f"❌ Initial Connection Failed. Error: {e}")
    sys.exit(1)

# Fetch unassigned tickets from last 30 minutes
issue_in_project = jira.search_issues(
    'created >= -30m AND project ="Saleem_T" AND assignee = EMPTY AND resolution = Unresolved'
)
total = len(issue_in_project)

# Prepare data lists
t_number = []
uname = []
e_address = []
```

**Data extraction with safety checks:**

```python
# Extract data from each issue
for issue in issue_in_project:
    # Get ticket number (always exists)
    ticket_number = str(issue.key)
    t_number.append(ticket_number)
    
    # Get reporter object
    reporter_obj = issue.fields.reporter
    
    # SAFE extraction of username
    username = str(reporter_obj.displayName) if reporter_obj and hasattr(reporter_obj, 'displayName') else "Unknown User"
    uname.append(username)
    
    # SAFE extraction of email
    emailAdd = str(reporter_obj.emailAddress) if reporter_obj and hasattr(reporter_obj, 'emailAddress') else "Email Not Found"
    e_address.append(emailAdd)
```

**Why the safety checks?**

```python
# ❌ UNSAFE:
username = str(issue.fields.reporter.displayName)
# Crashes if:
# - reporter is None (ticket created by system)
# - reporter doesn't have displayName attribute

# ✅ SAFE:
username = str(reporter_obj.displayName) if reporter_obj and hasattr(reporter_obj, 'displayName') else "Unknown User"
#              ↓                            ↓                    ↓
#         Get attribute                Check exists          Default value
```

**Email dispatch loop:**

```python
if total == 0:
    print("No issues found in JIRA")
else:
    print(f"There are {total} issues found in JIRA. Starting email dispatch...")
    
    # Loop through each ticket
    for jiraticket in range(total):
        ticket_key = t_number[jiraticket]
        reporter_name = uname[jiraticket]
        recipient_email = e_address[jiraticket]
        
        # Skip if email not found or invalid
        if recipient_email == "Email Not Found" or "@" not in recipient_email:
            print(f"⚠️ Skipping {ticket_key}: Reporter email not found or invalid.")
            continue
        
        # Format HTML with current ticket data
        formatted_html = EMAIL_TEMPLATE.format(
            reporter_name=reporter_name,
            ticket_key=ticket_key
        )
        
        # Create message
        msg = EmailMessage()
        msg['Subject'] = f"Acknowledgment: Your JIRA Ticket {ticket_key} has been received"
        msg['From'] = my_mail
        msg['To'] = recipient_email
        # msg['Cc'] = ["other@email.com"]  # Optional
        
        # Add HTML content
        msg.add_attachment(formatted_html, subtype='html')
        
        try:
            # Send email
            connection.send_message(msg)
            print(f"✅ Email successfully sent for ticket {ticket_key} to {recipient_email}.")
        except Exception as e:
            print(f"❌ Failed to send email for {ticket_key}. Error: {e}")

# Close connection AFTER all emails sent
connection.close()
print("\n✅ SMTP Connection Closed. Script finished.")
```

**Key improvements in this code:**

1. **Connection management:**
   - Opens SMTP connection ONCE before loop
   - Reuses same connection for all emails
   - Closes AFTER all emails sent
   - Much more efficient!

2. **Error handling:**
   - Try-catch for initial connections
   - Try-catch for each email send
   - Script continues even if one email fails

3. **Data validation:**
   - Checks if email exists
   - Checks if email has @ symbol
   - Skips invalid recipients

4. **Template formatting:**
   - Uses `.format()` to insert variables
   - Clean separation of template and data

### 11.7 Email with Multipart (Advanced)

**From Email_Sir.py - Full structure:**

```python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import time as t

# Email configuration
my_mail = "automation52786@gmail.com"
password = "bkgrpowfabscrrpb"

# JIRA data (already fetched)
total = len(issue_in_project)  # Number of tickets
tnumber = []      # Ticket numbers
uname = []        # Usernames
eaddress = []     # Email addresses
subdetails = []   # Subject details

# Extract data from JIRA issues
for issues in issue_in_project:
    ticket_number = str(issues.key)
    tnumber.append(ticket_number)
    
    username = str(issues.fields.reporter)
    uname.append(username)
    
    emailadd = issues.fields.reporter.emailAddress
    eaddress.append(emailadd)
    
    sdetails = issues.key + ":" + issues.fields.summary
    subdetails.append(sdetails)
    # Example: "ST-4:Account got locked"

# Check if tickets found
if total == 0:
    print("JIRA not found from last 5 min")
else:
    print("JIRA found")
    
    # Loop through each ticket
    for jiraticket in range(total):
        # Create message
        msg = MIMEMultipart()
        msg['Subject'] = subdetails[jiraticket]
        msg['From'] = my_mail
        msg['To'] = eaddress[jiraticket]
        msg['Cc'] = 'abdealipython@gmail.com'
        
        # Create HTML body
        body = f"""
        <p> Dear {uname[jiraticket]}, <br> <br> 
        Thank you for writing us. <br> <br> 
        This reply to acknowledgment your message. 
        We have received your JIRA ticket number: {tnumber[jiraticket]}. 
        Please provide the approval from your reporting head and our team is looking into it 
        and we will get back to you. We look forward to interact soon. 
        <br><br> 
        Thank you <br> 
        Alnafi Support team
        </p>
        """
        
        # Wait 3 seconds between emails (rate limiting)
        t.sleep(3)
        
        # Attach HTML body
        msg.attach(MIMEText(body, 'html'))
        
        # Send email
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.send_message(msg)
        print(f"Mail has been sent to {uname[jiraticket]}")
        connection.close()
```

**Key differences:**

| Feature | MIMEMultipart | EmailMessage |
|---------|---------------|--------------|
| Import | `email.mime.multipart` | `email.message` |
| Complexity | More verbose | Simpler |
| Body attachment | `msg.attach(MIMEText(...))` | `msg.set_content(...)` |
| Use case | Legacy, complex emails | Modern, recommended |

**Rate limiting with sleep:**

```python
import time as t

for email in emails:
    send_email(email)
    t.sleep(3)  # Wait 3 seconds before next email
    
# Why?
# - Prevents being flagged as spam
# - Gmail has sending limits
# - Gives servers time to process
```

---

## 12. Attachment Handling

### 12.1 Understanding File Operations

**Opening files in Python:**

```python
# Method 1: Manual handling (Problematic)
f = open('file.txt', 'rb')
data = f.read()
f.close()  # Must remember to close!

# Method 2: Context manager (Recommended)
with open('file.txt', 'rb') as f:
    data = f.read()
# File automatically closed after block
```

**File modes:**
- `'r'` = Read text
- `'rb'` = Read binary (for images, PDFs, etc.)
- `'w'` = Write text
- `'wb'` = Write binary

### 12.2 Adding Attachments to JIRA

**From Jira_ticket_creation.py - Fixed version:**

```python
import os
from jira import JIRA

# Connection
user = "saleemali.mohammad@gmail.com"
apikey = "ATATT3xFfGF0BL9FH_fwpo8qSgklx..."
server = "https://saleemalimohammad.atlassian.net"
jira = JIRA(server=server, basic_auth=(user, apikey))

# Create issue
new_issue = jira.create_issue(
    project='ST',
    summary='Testing JIRA',
    description='Testing JIRA',
    issuetype={'name': 'Request'},
    priority={'name': 'Highest'},
    timetracking={'originalEstimate': '10h'},
    reporter={'accountId': '712020:fd4e96d4-fe75-4c8d-b754-301be21eafd9'}
)
print(new_issue)

# ❌ OLD WAY (from original code):
# f = open('C:\\Users\\User\\Downloads\\yes.jpg', 'rb')
# jira.add_attachment(issue=new_issue.key, attachment=f)
# Problem: File handle might close before upload completes

# ✅ NEW WAY (Fixed):
attachment_files = [
    'C:\\Users\\User\\Downloads\\yes.jpg',
    'C:\\Users\\User\\Downloads\\my.txt'
]

for file_path in attachment_files:
    # Check if file exists
    if os.path.exists(file_path):
        # Use 'with open' for safe file handling
        with open(file_path, 'rb') as f:
            jira.add_attachment(issue=new_issue.key, attachment=f)
            print(f"✅ Attachment added: {os.path.basename(file_path)}")
    else:
        print(f"⚠️ Warning: File not found at path: {file_path}")

# Add comment after attachments
jira.add_comment(new_issue.key, 'Testing JIRA, This is Automated Comment')
print("✅ Comment Added.")
```

**Why the fix was necessary:**

```python
# ❌ PROBLEM CODE:
f = open('file.jpg', 'rb')
jira.add_attachment(issue='ST-8', attachment=f)

# What goes wrong:
# 1. File opened
# 2. Python continues immediately
# 3. File might get garbage collected
# 4. JIRA API tries to read → File already closed!
# 5. Result: Empty or failed attachment

# ✅ SOLUTION:
with open('file.jpg', 'rb') as f:
    jira.add_attachment(issue='ST-8', attachment=f)

# What happens:
# 1. File opened in context manager
# 2. Context manager keeps file open during block
# 3. JIRA API reads file successfully
# 4. Block ends → File closed automatically
# 5. Result: Successful attachment!
```

### 12.3 File Path Handling

**Windows path formats:**

```python
# Absolute path (Windows)
path1 = 'C:\\Users\\User\\Downloads\\yes.jpg'  # Double backslash
path2 = r'C:\Users\User\Downloads\yes.jpg'     # Raw string (r prefix)
path3 = 'C:/Users/User/Downloads/yes.jpg'      # Forward slash (works!)

# All three are equivalent!
```

**Using os.path for portability:**

```python
import os

# Get filename from path
filename = os.path.basename('C:\\Users\\User\\Downloads\\yes.jpg')
# Result: 'yes.jpg'

# Check if file exists
if os.path.exists(file_path):
    print("File found!")
    
# Get file size
size = os.path.getsize(file_path)
print(f"Size: {size} bytes")

# Join paths (OS-independent)
base_dir = 'C:\\Users\\User\\Downloads'
filename = 'yes.jpg'
full_path = os.path.join(base_dir, filename)
# Result: 'C:\\Users\\User\\Downloads\\yes.jpg'
```

### 12.4 Adding Multiple Attachments

**Efficient multi-file upload:**

```python
import os
from jira import JIRA

def add_attachments_to_issue(jira, issue_key, file_paths):
    """
    Add multiple attachments to a JIRA issue
    
    Args:
        jira: JIRA connection object
        issue_key: Issue key (e.g., 'ST-8')
        file_paths: List of file paths to attach
    """
    success_count = 0
    fail_count = 0
    
    for file_path in file_paths:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'rb') as f:
                    jira.add_attachment(issue=issue_key, attachment=f)
                    filename = os.path.basename(file_path)
                    print(f"✅ Attached: {filename}")
                    success_count += 1
            except Exception as e:
                print(f"❌ Failed to attach {file_path}: {str(e)}")
                fail_count += 1
        else:
            print(f"⚠️ File not found: {file_path}")
            fail_count += 1
    
    print(f"\n📊 Summary: {success_count} succeeded, {fail_count} failed")
    return success_count, fail_count

# Usage
jira = JIRA(server=server, basic_auth=(user, apikey))

files = [
    'C:\\Users\\User\\Downloads\\screenshot.png',
    'C:\\Users\\User\\Downloads\\logfile.txt',
    'C:\\Users\\User\\Downloads\\report.pdf'
]

add_attachments_to_issue(jira, 'ST-8', files)
```

### 12.5 Working with Different File Types

**Common file types:**

```python
# Images
image_files = [
    'screenshot.png',
    'diagram.jpg',
    'chart.gif'
]

# Documents
doc_files = [
    'report.pdf',
    'data.xlsx',
    'notes.txt'
]

# Logs
log_files = [
    'error.log',
    'access.log',
    'debug.log'
]

# Archives
archive_files = [
    'backup.zip',
    'data.tar.gz'
]

# All opened the same way!
with open(file_path, 'rb') as f:
    jira.add_attachment(issue_key, attachment=f)
```

---

## 13. Time Tracking & Worklogs

### 13.1 Understanding Time Tracking

**JIRA time tracking fields:**

```python
issue = jira.issue('ST-8')

# Original Estimate: Initial time estimate
print(issue.fields.timetracking.originalEstimate)
# Output: '10h' (10 hours)

# Remaining Estimate: Time left to complete
print(issue.fields.timetracking.remainingEstimate)
# Output: '7h' (7 hours)

# Time Spent: Total logged time
print(issue.fields.timetracking.timeSpent)
# Output: '3h' (3 hours)
```

**The relationship:**
```
Original Estimate = 10h (Initial guess)
Time Spent = 3h        (Work done so far)
Remaining = 7h         (Time left)

Original = Time Spent + Remaining
10h = 3h + 7h ✓
```

### 13.2 Setting Time Estimates

**When creating issue:**

```python
# From Jira_ticket_creation.py
new_issue = jira.create_issue(
    project='ST',
    summary='Testing JIRA',
    description='Testing JIRA',
    issuetype={'name': 'Request'},
    priority={'name': 'Highest'},
    timetracking={'originalEstimate': '10h'},  # Set estimate here!
    reporter={'accountId': '712020:fd4e96d4-fe75-4c8d-b754-301be21eafd9'}
)
```

**Time format examples:**
```python
'30m'      # 30 minutes
'1h'       # 1 hour
'2h 30m'   # 2 hours 30 minutes
'1d'       # 1 day (typically 8 hours)
'2d 4h'    # 2 days 4 hours
'1w'       # 1 week (typically 5 days = 40 hours)
'1w 2d'    # 1 week 2 days
```

**Updating estimate later:**

```python
issue = jira.issue('ST-8')

# Update time tracking
issue.update(fields={
    'timetracking': {
        'originalEstimate': '15h',    # New estimate
        'remainingEstimate': '10h'    # Remaining time
    }
})
```

### 13.3 Adding Worklogs

**From Jira_ticket_creation.py:**

```python
# Create issue first
new_issue = jira.create_issue(
    project='ST',
    summary='Account got Locked',
    description='Account got Locked',
    issuetype={'name': 'Issue'}
)

# Log time spent on this issue
jira.add_worklog(new_issue, timeSpent="30m")
#                    ↓            ↓
#               Issue object  Time spent
```

**What this does:**
1. Adds worklog entry to issue
2. Increases "Time Spent" by 30m
3. Decreases "Remaining Estimate" by 30m (if auto-adjust enabled)
4. Creates audit trail of work done

**Advanced worklog:**

```python
from datetime import datetime

# Add worklog with comment and specific start time
jira.add_worklog(
    issue='ST-8',
    timeSpent='2h',
    comment='Fixed account lock issue',
    started=datetime(2025, 1, 15, 9, 0, 0)  # When work started
)
```

**Multiple worklogs:**

```python
# Day 1: 2 hours
jira.add_worklog('ST-8', timeSpent='2h', comment='Initial investigation')

# Day 2: 3 hours
jira.add_worklog('ST-8', timeSpent='3h', comment='Implemented fix')

# Day 3: 1 hour
jira.add_worklog('ST-8', timeSpent='1h', comment='Testing and documentation')

# Total logged: 6 hours
```

### 13.4 Reading Worklogs

**Get all worklogs for an issue:**

```python
# Get issue
issue = jira.issue('ST-8')

# Get worklogs
worklogs = jira.worklogs(issue)

# Display all worklogs
for log in worklogs:
    print(f"Author: {log.author.displayName}")
    print(f"Time Spent: {log.timeSpent}")
    print(f"Started: {log.started}")
    print(f"Comment: {log.comment if hasattr(log, 'comment') else 'No comment'}")
    print("-" * 50)
```

**Output example:**
```
Author: Saleem Ali
Time Spent: 2h
Started: 2025-01-15T09:00:00.000+0600
Comment: Initial investigation
--------------------------------------------------
Author: Saleem Ali
Time Spent: 3h
Started: 2025-01-16T10:00:00.000+0600
Comment: Implemented fix
--------------------------------------------------
```

---

## 14. Linux Server Monitoring Integration

### 14.1 Understanding the Use Case

**Real-world scenario:**
- You have Linux servers to monitor
- Need to check server health (memory, CPU, disk)
- If problem detected → Auto-create JIRA ticket
- Alert appropriate team members

**This is AIOps in action!**

### 14.2 SSH Connection with Paramiko

**From Linux_to_JIRA.py:**

```python
import paramiko
from jira import JIRA
import time

# JIRA configuration
user = "automation52786@gmail.com"
apikey = 'f2Nxb496FAgCCQRJM9OC2510'
server = "https://alnafi.atlassian.net"
jira = JIRA(server, basic_auth=(user, apikey))

# Linux server details
hostname = "192.168.1.6"
username = "aadmin"
password = "123@abd"

# Create SSH client
client = paramiko.SSHClient()

# Auto-accept unknown host keys (use with caution!)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to server
client.connect(hostname=hostname, username=username, password=password)
```

**What's happening:**

```python
client = paramiko.SSHClient()
# Creates SSH client object

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Tells paramiko to automatically trust new servers
# ⚠️ Security note: In production, verify host keys manually!

client.connect(hostname=hostname, username=username, password=password)
# Establishes SSH connection to server
# hostname: Server IP or domain
# username: Linux username
# password: Linux password
```

### 14.3 Executing Remote Commands

**Run command on remote server:**

```python
# Command to check memory
cmd = "free -g"

# Execute command
stdin, stdout, stderr = client.exec_command(cmd)
#  ↓      ↓       ↓
# Input Output  Errors
```

**What each variable contains:**

```python
stdin   # Standard Input (not used here)
stdout  # Standard Output (command results)
stderr  # Standard Error (error messages)
```

**Reading command output:**

```python
# Execute command
stdin, stdout, stderr = client.exec_command("free -g")

# Read output lines
cmdout = stdout.readlines()

# Example output:
# [
#   '              total        used        free      shared  buff/cache   available\n',
#   'Mem:              7           3           1           0           2           3\n',
#   'Swap:             2           0           2\n'
# ]
```

**Parsing the output:**

```python
# Get second line (memory stats)
memory_line = cmdout[1]
# 'Mem:              7           3           1           0           2           3\n'

# Split by spaces
parts = memory_line.split()
# ['Mem:', '7', '3', '1', '0', '2', '3']

# Get available memory (index 6)
available_mem = parts[6]
# '3' (3 GB available)
```

### 14.4 Conditional Ticket Creation

**Complete monitoring logic:**

```python
# Check memory
cmd = "free -g"
stdin, stdout, stderr = client.exec_command(cmd)
cmdout = stdout.readlines()

# Parse available memory
available_mem = cmdout[1].split()[6]

# Check if memory is low
if int(available_mem) <= 1:
    print("Memory is not good")
    
    # Create ticket details
    sum = f"Memory available {available_mem}GB and Server name is {hostname}"
    Desc = f"Hi Team, We found low memory issue on this server {hostname}, \n {sum}"
    
    # Create JIRA issue
    issue_dict = {
        'project': {'key': 'IIP'},
        'issuetype': {'name': 'Issue'},
        'description': Desc,
        'summary': sum,
        'priority': {'name': 'Highest'},
        "timetracking": {"originalEstimate": "1h"}
    }
    
    new_issue = jira.create_issue(fields=issue_dict)
    
    # Wait a bit
    time.sleep(3)
    
    # Assign to specific person
    new_issue.update(assignee={"accountId": "637b7f598fd2d2d5f12d4929"})
    
    print("Ticket has been created")
else:
    print("Memory is good")
```

**Flowchart:**

```
┌──────────────────────────┐
│ Connect to Linux Server  │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Execute: free -g         │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Parse available memory   │
└────────────┬─────────────┘
             ↓
       Is memory <= 1GB?
             ├───Yes─→ Create JIRA Ticket
             │          Assign to engineer
             │          Send notification
             │
             └───No──→ Memory is good
                       Continue monitoring
```

### 14.5 Expanding Monitoring

**Monitor multiple metrics:**

```python
def check_server_health(hostname, username, password):
    """Comprehensive server health check"""
    
    # Connect
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=hostname, username=username, password=password)
    
    issues = []
    
    # 1. Check Memory
    stdin, stdout, stderr = client.exec_command("free -g")
    mem_output = stdout.readlines()
    available_mem = int(mem_output[1].split()[6])
    
    if available_mem <= 1:
        issues.append(f"Low memory: {available_mem}GB available")
    
    # 2. Check Disk Space
    stdin, stdout, stderr = client.exec_command("df -h / | tail -1")
    disk_output = stdout.readlines()[0]
    disk_usage = int(disk_output.split()[4].replace('%', ''))
    
    if disk_usage >= 90:
        issues.append(f"High disk usage: {disk_usage}%")
    
    # 3. Check CPU Load
    stdin, stdout, stderr = client.exec_command("uptime")
    uptime_output = stdout.readlines()[0]
    load_avg = float(uptime_output.split('load average:')[1].split(',')[0].strip())
    
    if load_avg >= 4.0:
        issues.append(f"High CPU load: {load_avg}")
    
    # Close connection
    client.close()
    
    # Create JIRA ticket if issues found
    if issues:
        summary = f"Server Health Issues on {hostname}"
        description = "\n".join(issues)
        
        issue = jira.create_issue(
            project='IIP',
            summary=summary,
            description=description,
            issuetype={'name': 'Issue'},
            priority={'name': 'High'}
        )
        
        print(f"✅ Ticket created: {issue.key}")
        return issue.key
    else:
        print(f"✅ Server {hostname} is healthy")
        return None

# Usage
check_server_health("192.168.1.6", "aadmin", "123@abd")
```

**Monitor multiple servers:**

```python
servers = [
    {"hostname": "192.168.1.6", "username": "aadmin", "password": "123@abd"},
    {"hostname": "192.168.1.7", "username": "admin", "password": "pass123"},
    {"hostname": "192.168.1.8", "username": "root", "password": "secure123"}
]

for server in servers:
    check_server_health(**server)
```

---

## 15. Date & Time Operations

### 15.1 Understanding Datetime in Python

**From testing_date.py:**

```python
import datetime

# JIRA timestamp format
timestr = "2025-11-20T11:40:18.840+0600"

# Parse string to datetime object
datetimeobject = datetime.datetime.strptime(timestr, "%Y-%m-%dT%H:%M:%S.%f%z")

print(datetimeobject)
# Output: 2025-11-20 11:40:18.840000+06:00

# Format to custom string
mycustom = datetimeobject.strftime("%Y-%m-%d")
print(mycustom)
# Output: 2025-11-20
```

### 15.2 DateTime Format Codes

**Common format codes:**

| Code | Meaning | Example |
|------|---------|---------|
| `%Y` | Year (4 digits) | 2025 |
| `%m` | Month (2 digits) | 11 |
| `%d` | Day (2 digits) | 20 |
| `%H` | Hour (24-hour) | 14 |
| `%M` | Minute | 40 |
| `%S` | Second | 18 |
| `%f` | Microsecond | 840000 |
| `%z` | Timezone offset | +0600 |
| `%a` | Weekday (short) | Wed |
| `%A` | Weekday (full) | Wednesday |
| `%b` | Month (short) | Nov |
| `%B` | Month (full) | November |

### 15.3 JIRA Timestamp Parsing

**From last_comment.py:**

```python
import datetime

# Get comments
comments = issue.fields.comment.comments

for comment in comments:
    # Get JIRA timestamp
    jiratime = comment.created
    # Format: "2025-11-21T14:30:22.840+0600"
    
    # Parse to datetime object
    datetimeobject = datetime.datetime.strptime(
        jiratime, 
        "%Y-%m-%dT%H:%M:%S.%f%z"
    )
    
    # Format to just date
    mycustom = datetimeobject.strftime("%Y-%m-%d")
    
    # Filter by date
    if mycustom == "2025-11-21":
        print(comment.body)
```

**Why the fix was needed:**

```python
# ❌ ORIGINAL (Broken):
datetimeobject = datetime.datetime.strptime(jiratime, "%Y-%m-%dT%H:%M:%S.%f")
# Error! Missing timezone parsing (%z)

# ✅ FIXED:
datetimeobject = datetime.datetime.strptime(jiratime, "%Y-%m-%dT%H:%M:%S.%f%z")
# Correctly handles "+0600" timezone
```

### 15.4 Common Date Operations

**Get current date/time:**

```python
from datetime import datetime

# Current datetime
now = datetime.now()
print(now)
# Output: 2025-01-15 14:30:22.123456

# Current date only
today = datetime.now().date()
print(today)
# Output: 2025-01-15

# Current time only
current_time = datetime.now().time()
print(current_time)
# Output: 14:30:22.123456
```

**Date arithmetic:**

```python
from datetime import datetime, timedelta

# Current date
today = datetime.now()

# Add days
future = today + timedelta(days=7)
print(f"One week from now: {future}")

# Subtract days
past = today - timedelta(days=30)
print(f"30 days ago: {past}")

# Add hours
later = today + timedelta(hours=2)
print(f"2 hours from now: {later}")
```

**Compare dates:**

```python
from datetime import datetime

date1 = datetime(2025, 1, 15)
date2 = datetime(2025, 1, 20)

if date1 < date2:
    print("date1 is earlier")

# Calculate difference
difference = date2 - date1
print(f"Days between: {difference.days}")
# Output: Days between: 5
```

### 15.6 Timezone Handling

**Working with timezones:**

```python
from datetime import datetime
import pytz

# Create timezone-aware datetime
dhaka_tz = pytz.timezone('Asia/Dhaka')
now_dhaka = datetime.now(dhaka_tz)
print(now_dhaka)

# Convert to different timezone
utc_tz = pytz.UTC
now_utc = now_dhaka.astimezone(utc_tz)
print(now_utc)
```

---

## 16. Auto-Acknowledgment Email System

### 16.1 System Overview

**Purpose:**
- Monitor for new unassigned JIRA tickets
- Send automatic acknowledgment emails to reporters
- Keep users informed immediately

**Workflow:**
```
1. Query JIRA for new unassigned tickets
2. Extract reporter information
3. Generate personalized email
4. Send via SMTP
5. Log results
```

### 16.2 Complete Implementation Analysis

**From JQL_Query+EMAIL.py - Full breakdown:**

```python
import smtplib
from email.message import EmailMessage
from jira import JIRA
import sys

# === CONFIGURATION ===
# Email settings
my_mail = "saleemali.mohammad@gmail.com"
my_password = "kxqs chfl bxkl jjme"  # Gmail App Password
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# JIRA settings
user = "saleemali.mohammad@gmail.com"
apikey = "ATATT3xFfGF0BL9FH_fwpo8qSgklx..."
server = "https://saleemalimohammad.atlassian.net"

# === EMAIL TEMPLATE ===
# Define once, use many times
EMAIL_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>JIRA Acknowledgment</title>
</head>
<body>
<p> Dear {reporter_name}, <br> <br> 
Thank You for writing to us. <br> <br> 
This reply is to acknowledge your message request for <strong>JIRA Ticket {ticket_key}</strong>. 
We have received your message and our team is looking into it and will get back to you soon. 
<br> <br> 
Thank You<br> 
Alnafi Support Team 
</p>
</body>
</html>
"""

# === ESTABLISH CONNECTIONS ===
try:
    # Connect to JIRA
    jira = JIRA(server=server, basic_auth=(user, apikey))
    print("✅ Jira Connection Successful.")
    
    # Connect to SMTP (before loop for efficiency)
    connection = smtplib.SMTP(smtp_server, smtp_port)
    connection.starttls()
    connection.login(user=my_mail, password=my_password)
    print("✅ SMTP Connection Successful.")
    
except Exception as e:
    print(f"❌ Initial Connection Failed. Error: {e}")
    sys.exit(1)

# === FETCH JIRA DATA ===
# Search for recent unassigned tickets
issue_in_project = jira.search_issues(
    'created >= -30m AND project ="Saleem_T" AND assignee = EMPTY AND resolution = Unresolved'
)
total = len(issue_in_project)

# Prepare data storage
t_number = []
uname = []
e_address = []

# === EXTRACT DATA ===
for issue in issue_in_project:
    # Get ticket number (always exists)
    ticket_number = str(issue.key)
    t_number.append(ticket_number)
    
    # Get reporter object
    reporter_obj = issue.fields.reporter
    
    # SAFE extraction with fallbacks
    username = (
        str(reporter_obj.displayName) 
        if reporter_obj and hasattr(reporter_obj, 'displayName') 
        else "Unknown User"
    )
    uname.append(username)
    
    emailAdd = (
        str(reporter_obj.emailAddress) 
        if reporter_obj and hasattr(reporter_obj, 'emailAddress') 
        else "Email Not Found"
    )
    e_address.append(emailAdd)

# === SEND EMAILS ===
if total == 0:
    print("No issues found in JIRA")
else:
    print(f"There are {total} issues found in JIRA. Starting email dispatch...")
    
    for jiraticket in range(total):
        ticket_key = t_number[jiraticket]
        reporter_name = uname[jiraticket]
        recipient_email = e_address[jiraticket]
        
        # Validate email
        if recipient_email == "Email Not Found" or "@" not in recipient_email:
            print(f"⚠️ Skipping {ticket_key}: Invalid email.")
            continue
        
        # Format HTML with current data
        formatted_html = EMAIL_TEMPLATE.format(
            reporter_name=reporter_name,
            ticket_key=ticket_key
        )
        
        # Create message
        msg = EmailMessage()
        msg['Subject'] = f"Acknowledgment: Your JIRA Ticket {ticket_key} has been received"
        msg['From'] = my_mail
        msg['To'] = recipient_email
        
        # Add HTML content
        msg.add_attachment(formatted_html, subtype='html')
        
        try:
            # Send email
            connection.send_message(msg)
            print(f"✅ Email sent for {ticket_key} to {recipient_email}")
        except Exception as e:
            print(f"❌ Failed to send email for {ticket_key}. Error: {e}")

# === CLEANUP ===
connection.close()
print("\n✅ SMTP Connection Closed. Script finished.")
```

### 16.3 Key Design Patterns

**1. Connection Reuse:**
```python
# ✅ GOOD: One connection for all emails
connection = smtplib.SMTP(smtp_server, smtp_port)
connection.starttls()
connection.login(user=my_mail, password=my_password)

for email in emails:
    connection.send_message(email)  # Reuse connection

connection.close()

# ❌ BAD: New connection per email (slow!)
for email in emails:
    connection = smtplib.SMTP(smtp_server, smtp_port)
    connection.starttls()
    connection.login(user=my_mail, password=my_password)
    connection.send_message(email)
    connection.close()  # Reconnecting each time!
```

**2. Template Pattern:**
```python
# Define template once
TEMPLATE = "Dear {name}, your ticket {ticket} is received."

# Use many times
for ticket in tickets:
    message = TEMPLATE.format(name=ticket.reporter, ticket=ticket.key)
```

**3. Error Isolation:**
```python
# Don't let one failure stop everything
for item in items:
    try:
        process(item)
        print(f"✅ Success: {item}")
    except Exception as e:
        print(f"❌ Failed: {item}, Error: {e}")
        continue  # Keep going!
```

---

## 17. Unassigned Ticket Monitoring

### 17.1 The Problem

**Common scenario:**
- Tickets created but not assigned
- Sit unnoticed for hours/days
- Users waiting for response
- SLA (Service Level Agreement) violations

**Solution:**
Automated monitoring and alerting!

### 17.2 Implementation

**From JQL_Query.py:**

```python
from jira import JIRA

# Connection
user = "saleemali.mohammad@gmail.com"
apikey = "ATATT3xFfGF0BL9FH_fwpo8qSgklx..."
server = "https://saleemalimohammad.atlassian.net"
jira = JIRA(server=server, basic_auth=(user, apikey))

# Query for unassigned tickets
issue_in_project = jira.search_issues(
    'created >= -120m AND project =Saleem_T AND assignee = EMPTY AND resolution = Unresolved'
)
total = len(issue_in_project)

# Storage lists
t_number = []
uname = []
e_address = []

# Extract data
for issue in issue_in_project:
    t_number.append(str(issue.key))
    uname.append(str(issue.fields.reporter))
    e_address.append(issue.fields.reporter.emailAddress)

# Report results
if total == 0:
    print("No issues found in JIRA")
else:
    print(f"There are {total} issues found in JIRA")
    for jiraticket in range(total):
        print(t_number[jiraticket])
        print(uname[jiraticket])
        print(e_address[jiraticket])
```

### 17.3 Scheduling the Monitor

**Run periodically using cron (Linux) or Task Scheduler (Windows):**

**Linux cron:**
```bash
# Edit crontab
crontab -e

# Run every 30 minutes
*/30 * * * * /usr/bin/python3 /path/to/unassigned_monitor.py

# Run every hour
0 * * * * /usr/bin/python3 /path/to/unassigned_monitor.py
```

**Windows Task Scheduler:**
1. Open Task Scheduler
2. Create Basic Task
3. Trigger: Every 30 minutes
4. Action: Start a program
5. Program: `python.exe`
6. Arguments: `C:\path\to\unassigned_monitor.py`

**Python alternative (continuous monitoring):**
```python
import time
from datetime import datetime

def monitor_unassigned_tickets():
    """Monitor and alert on unassigned tickets"""
    
    while True:
        print(f"\n🔍 Checking at {datetime.now()}")
        
        # Query JIRA
        issues = jira.search_issues(
            'project = ST AND assignee = EMPTY AND resolution = Unresolved'
        )
        
        if len(issues) > 0:
            print(f"⚠️ Found {len(issues)} unassigned tickets!")
            
            # Send alert email to team lead
            send_alert_email(issues)
        else:
            print("✅ All tickets assigned")
        
        # Wait 30 minutes
        time.sleep(1800)  # 1800 seconds = 30 minutes

# Run monitor
monitor_unassigned_tickets()
```

---

## 18. Server Health Monitoring

### 18.1 Complete Monitoring System

**Expanded from Linux_to_JIRA.py:**

```python
import paramiko
from jira import JIRA
import time
from datetime import datetime

class ServerMonitor:
    """Monitor Linux servers and create JIRA tickets for issues"""
    
    def __init__(self, jira_server, jira_user, jira_apikey):
        """Initialize JIRA connection"""
        self.jira = JIRA(jira_server, basic_auth=(jira_user, jira_apikey))
    
    def connect_ssh(self, hostname, username, password):
        """Establish SSH connection"""
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=hostname, username=username, password=password)
            return client
        except Exception as e:
            print(f"❌ Failed to connect to {hostname}: {e}")
            return None
    
    def check_memory(self, client, hostname):
        """Check memory and return issue if low"""
        stdin, stdout, stderr = client.exec_command("free -g")
        cmdout = stdout.readlines()
        available_mem = int(cmdout[1].split()[6])
        
        if available_mem <= 1:
            return {
                'type': 'memory',
                'severity': 'high',
                'message': f"Low memory: {available_mem}GB available on {hostname}"
            }
        return None
    
    def check_disk(self, client, hostname):
        """Check disk usage"""
        stdin, stdout, stderr = client.exec_command("df -h / | tail -1")
        disk_output = stdout.readlines()[0]
        disk_usage = int(disk_output.split()[4].replace('%', ''))
        
        if disk_usage >= 90:
            return {
                'type': 'disk',
                'severity': 'high',
                'message': f"High disk usage: {disk_usage}% on {hostname}"
            }
        return None
    
    def check_cpu(self, client, hostname):
        """Check CPU load"""
        stdin, stdout, stderr = client.exec_command("uptime")
        uptime_output = stdout.readlines()[0]
        load_avg = float(uptime_output.split('load average:')[1].split(',')[0].strip())
        
        if load_avg >= 4.0:
            return {
                'type': 'cpu',
                'severity': 'medium',
                'message': f"High CPU load: {load_avg} on {hostname}"
            }
        return None
    
    def create_ticket(self, issues, hostname):
        """Create JIRA ticket for issues"""
        if not issues:
            return None
        
        # Build summary and description
        summary = f"Server Health Alert: {hostname}"
        description = f"Detected issues on {hostname} at {datetime.now()}:\n\n"
        description += "\n".join([f"- {issue['message']}" for issue in issues])
        
        # Determine priority
        has_high_severity = any(i['severity'] == 'high' for i in issues)
        priority = 'Highest' if has_high_severity else 'High'
        
        # Create issue
        new_issue = self.jira.create_issue(
            project='IIP',
            summary=summary,
            description=description,
            issuetype={'name': 'Issue'},
            priority={'name': priority},
            timetracking={'originalEstimate': '2h'}
        )
        
        # Assign to on-call engineer
        time.sleep(2)
        new_issue.update(assignee={"accountId": "637b7f598fd2d2d5f12d4929"})
        
        return new_issue.key
    
    def monitor_server(self, hostname, username, password):
        """Complete server health check"""
        print(f"\n🔍 Monitoring {hostname}...")
        
        # Connect
        client = self.connect_ssh(hostname, username, password)
        if not client:
            return
        
        # Run checks
        issues = []
        
        mem_issue = self.check_memory(client, hostname)
        if mem_issue:
            issues.append(mem_issue)
        
        disk_issue = self.check_disk(client, hostname)
        if disk_issue:
            issues.append(disk_issue)
        
        cpu_issue = self.check_cpu(client, hostname)
        if cpu_issue:
            issues.append(cpu_issue)
        
        # Close connection
        client.close()
        
        # Create ticket if needed
        if issues:
            ticket = self.create_ticket(issues, hostname)
            print(f"⚠️ Issues found! Ticket created: {ticket}")
        else:
            print(f"✅ {hostname} is healthy")

# Usage
monitor = ServerMonitor(
    jira_server="https://alnafi.atlassian.net",
    jira_user="automation52786@gmail.com",
    jira_apikey="f2Nxb496FAgCCQRJM9OC2510"
)

# Monitor single server
monitor.monitor_server("192.168.1.6", "aadmin", "123@abd")

# Monitor multiple servers
servers = [
    {"hostname": "192.168.1.6", "username": "aadmin", "password": "123@abd"},
    {"hostname": "192.168.1.7", "username": "admin", "password": "pass123"},
]

for server in servers:
    monitor.monitor_server(**server)
```

---

## 19. Comment Analysis & Filtering

### 19.1 Advanced Comment Operations

**From last_comment.py - All methods:**

```python
from jira import JIRA
import datetime

# Connection
user = "saleemali.mohammad@gmail.com"
apikey = "ATATT3xFfGF0BL9FH_fwpo8qSgklx..."
server = "https://saleemalimohammad.atlassian.net"
jira = JIRA(server=server, basic_auth=(user, apikey))

ticket = 'AC-7'
issue = jira.issue(ticket)
comments = issue.fields.comment.comments

# === METHOD 1: Get latest by ID ===
commentID = str(0)
for comment in comments:
    if comment.id > commentID:
        commentID = comment.id

latest = jira.comment(issue, commentID).body
print("Latest comment (by ID):", latest)

# === METHOD 2: Get latest from list ===
if comments:
    latest = comments[-1].body
    print("Latest comment (by index):", latest)

# === METHOD 3: Filter by author ===
engineer_comments = []
for comment in comments:
    if comment.author.displayName == "sameenaAndroid@":
        engineer_comments.append(comment.body)

print(f"Found {len(engineer_comments)} comments from engineer")

# === METHOD 4: Filter by date ===
target_date = "2025-11-21"
for comment in comments:
    jiratime = comment.created
    datetimeobject = datetime.datetime.strptime(
        jiratime, 
        "%Y-%m-%dT%H:%M:%S.%f%z"
    )
    mycustom = datetimeobject.strftime("%Y-%m-%d")
    
    if mycustom == target_date:
        print(f"Comment from {target_date}: {comment.body}")
```

### 19.2 Comment Analytics

**Analyze comment patterns:**

```python
def analyze_comments(issue_key):
    """Analyze comment patterns on an issue"""
    
    issue = jira.issue(issue_key)
    comments = issue.fields.comment.comments
    
    # Count by author
    author_counts = {}
    for comment in comments:
        author = comment.author.displayName
        author_counts[author] = author_counts.get(author, 0) + 1
    
    # Find most active commenter
    most_active = max(author_counts, key=author_counts.get)
    
    # Calculate response time
    if len(comments) >= 2:
        first = datetime.datetime.strptime(
            comments[0].created, 
            "%Y-%m-%dT%H:%M:%S.%f%z"
        )
        second = datetime.datetime.strptime(
            comments[1].created, 
            "%Y-%m-%dT%H:%M:%S.%f%z"
        )
        response_time = (second - first).total_seconds() / 60
    else:
        response_time = None
    
    # Print analysis
    print(f"📊 Comment Analysis for {issue_key}")
    print(f"Total comments: {len(comments)}")
    print(f"Most active: {most_active} ({author_counts[most_active]} comments)")
    if response_time:
        print(f"First response time: {response_time:.1f} minutes")
    
    print("\nComment frequency by author:")
    for author, count in sorted(author_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {author}: {count}")

# Usage
analyze_comments('AC-7')
```

---

## 20. Security Best Practices

### 20.1 Critical Security Issues in Your Code

**⚠️ EXPOSED CREDENTIALS:**

```python
# ❌ FOUND IN YOUR CODE:
apikey = "ATATT3xFfGF0BL9FH_fwpo8qSgklx..."  # EXPOSED!
my_password = "bkgrpowfabscrrpb"               # EXPOSED!
password = "123@abd"                           # EXPOSED!
```

**These are PUBLICLY VISIBLE if you push to GitHub!**

### 20.2 Secure Credential Management

**Solution 1: Environment Variables**

```python
# config/credentials.py
import os

def get_jira_config():
    """Get JIRA credentials from environment"""
    return {
        'server': os.getenv('JIRA_SERVER'),
        'user': os.getenv('JIRA_USER'),
        'api_key': os.getenv('JIRA_API_KEY')
    }

def get_email_config():
    """Get email credentials from environment"""
    return {
        'user': os.getenv('EMAIL_USER'),
        'password': os.getenv('EMAIL_PASSWORD'),
        'smtp_server': os.getenv('SMTP_SERVER', 'smtp.gmail.com'),
        'smtp_port': int(os.getenv('SMTP_PORT', '587'))
    }

def get_ssh_config():
    """Get SSH credentials from environment"""
    return {
        'hostname': os.getenv('SSH_HOST'),
        'username': os.getenv('SSH_USER'),
        'password': os.getenv('SSH_PASSWORD')
    }
```

**Usage:**
```python
from config.credentials import get_jira_config, get_email_config

# Get JIRA credentials
jira_config = get_jira_config()
jira = JIRA(
    server=jira_config['server'],
    basic_auth=(jira_config['user'], jira_config['api_key'])
)

# Get email credentials
email_config = get_email_config()
connection = smtplib.SMTP(email_config['smtp_server'], email_config['smtp_port'])
connection.login(email_config['user'], email_config['password'])
```

**Set environment variables:**

```bash
# Windows (PowerShell)
$env:JIRA_SERVER = "https://saleemalimohammad.atlassian.net"
$env:JIRA_USER = "saleemali.mohammad@gmail.com"
$env:JIRA_API_KEY = "your-actual-api-key"

# Linux/Mac (bash)
export JIRA_SERVER="https://saleemalimohammad.atlassian.net"
export JIRA_USER="saleemali.mohammad@gmail.com"
export JIRA_API_KEY="your-actual-api-key"
```

**Solution 2: Config File (MUST BE GITIGNORED)**

```python
# config/secrets.py
# ⚠️ ADD THIS FILE TO .gitignore!

JIRA_CONFIG = {
    'server': 'https://saleemalimohammad.atlassian.net',
    'user': 'saleemali.mohammad@gmail.com',
    'api_key': 'your-api-key-here'
}

EMAIL_CONFIG = {
    'user': 'saleemali.mohammad@gmail.com',
    'password': 'your-app-password',
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587
}

SSH_CONFIG = {
    'hostname': '192.168.1.6',
    'username': 'aadmin',
    'password': 'your-password'
}
```

**Create template file for GitHub:**

```python
# config/secrets.example.py
# Copy this to secrets.py and fill in your values

JIRA_CONFIG = {
    'server': 'https://your-domain.atlassian.net',
    'user': 'your-email@gmail.com',
    'api_key': 'your-api-key'
}

EMAIL_CONFIG = {
    'user': 'your-email@gmail.com',
    'password': 'your-app-password',
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587
}

SSH_CONFIG = {
    'hostname': 'your-server-ip',
    'username': 'your-username',
    'password': 'your-password'
}
```

### 20.3 .gitignore (CRITICAL!)

```gitignore
# Sensitive credentials
config/secrets.py
config/credentials.py
*.key
*.pem

# API keys and tokens
.env
.env.local
*.apikey

# Passwords
*password*
*secret*

# SSH keys
id_rsa
id_rsa.pub
known_hosts

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Database
*.db
*.sqlite3
```

### 20.4 Additional Security Practices

**1. Use SSH keys instead of passwords:**

```python
# Instead of password authentication
client.connect(hostname=hostname, username=username, password=password)

# Use SSH key authentication
key = paramiko.RSAKey.from_private_key_file('/path/to/private_key')
client.connect(hostname=hostname, username=username, pkey=key)
```

**2. Validate SSL certificates:**

```python
from jira import JIRA

# ✅ GOOD: Verify SSL (default)
jira = JIRA(server=server, basic_auth=(user, apikey))

# ❌ BAD: Skip SSL verification (insecure!)
jira = JIRA(server=server, basic_auth=(user, apikey), options={'verify': False})
```

**3. Rotate API keys regularly:**
- Generate new JIRA API token every 3-6 months
- Revoke old tokens after rotation
- Update credentials in secure storage

**4. Use principle of least privilege:**
- Create separate JIRA accounts for automation
- Grant only necessary permissions
- Don't use admin accounts for scripts

### 20.5 Security Checklist

```
✅ Never hardcode credentials in code
✅ Use environment variables or secure config files
✅ Add sensitive files to .gitignore
✅ Use HTTPS/TLS for all connections
✅ Validate SSL certificates
✅ Use SSH keys instead of passwords
✅ Rotate credentials regularly
✅ Use app-specific passwords for email
✅ Enable 2FA on all accounts
✅ Log security events
✅ Review code before committing
✅ Never commit .env or secrets files
✅ Use secret scanning tools
✅ Implement rate limiting
✅ Handle errors securely (don't expose credentials in logs)
```

---

## 21. Error Handling & Debugging

### 21.1 Common Errors and Solutions

**Error 1: Authentication Failed (401)**

```python
# Error message:
# JIRAError: HTTP 401: "Unauthorized"

# Causes:
# - Wrong API key
# - Wrong email
# - API key expired/revoked

# Solution:
try:
    jira = JIRA(server=server, basic_auth=(user, apikey))
except JIRAError as e:
    if e.status_code == 401:
        print("❌ Authentication failed!")
        print("Check your email and API key")
        print("Generate new API key at: https://id.atlassian.com/manage-profile/security/api-tokens")
```

**Error 2: Issue Not Found (404)**

```python
# Error message:
# JIRAError: HTTP 404: "Issue Does Not Exist"

# Solution:
try:
    issue = jira.issue('ST-999')
except JIRAError as e:
    if e.status_code == 404:
        print(f"❌ Issue not found!")
        print("Check the ticket number")
```

**Error 3: Permission Denied (403)**

```python
# Error message:
# JIRAError: HTTP 403: "Forbidden"

# Causes:
# - No permission to access project
# - No permission to create issues
# - No permission to edit issue

# Solution:
try:
    new_issue = jira.create_issue(project='ST', ...)
except JIRAError as e:
    if e.status_code == 403:
        print("❌ Permission denied!")
        print("Check your JIRA permissions")
```

**Error 4: Email Send Failure**

```python
# Error: SMTPAuthenticationError

# Causes:
# - Wrong app password
# - 2FA not enabled
# - Using regular password instead of app password

# Solution:
try:
    connection.login(user=my_mail, password=my_password)
except smtplib.SMTPAuthenticationError:
    print("❌ Email authentication failed!")
    print("Steps:")
    print("1. Enable 2-Factor Authentication")
    print("2. Generate App Password")
    print("3. Use App Password, not regular password")
```

**Error 5: SSH Connection Failed**

```python
# Error: paramiko.ssh_exception.AuthenticationException

# Causes:
# - Wrong username/password
# - Server not reachable
# - Firewall blocking connection

# Solution:
try:
    client.connect(hostname=hostname, username=username, password=password)
except paramiko.AuthenticationException:
    print("❌ SSH authentication failed!")
    print("Check username and password")
except paramiko.SSHException as e:
    print(f"❌ SSH error: {e}")
except Exception as e:
    print(f"❌ Connection error: {e}")
```

### 21.2 Comprehensive Error Handling Pattern

```python
from jira import JIRA
from jira.exceptions import JIRAError
import smtplib
import sys
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='automation.log'
)

def safe_jira_operation():
    """JIRA operations with complete error handling"""
    
    try:
        # Connect to JIRA
        logging.info("Connecting to JIRA...")
        jira = JIRA(server=server, basic_auth=(user, apikey))
        logging.info("✅ JIRA connection successful")
        
        # Search for issues
        logging.info("Searching for issues...")
        issues = jira.search_issues('project = ST AND status = "To Do"')
        logging.info(f"✅ Found {len(issues)} issues")
        
        # Process each issue
        for issue in issues:
            try:
                # Get issue details
                summary = issue.fields.summary
                
                # Add comment
                jira.add_comment(issue, "Processed by automation")
                logging.info(f"✅ Processed {issue.key}")
                
            except JIRAError as e:
                logging.error(f"❌ Failed to process {issue.key}: {e.text}")
                continue  # Skip to next issue
                
            except Exception as e:
                logging.error(f"❌ Unexpected error with {issue.key}: {str(e)}")
                continue
        
        return True
        
    except JIRAError as e:
        if e.status_code == 401:
            logging.error("❌ Authentication failed - Check API key")
        elif e.status_code == 403:
            logging.error("❌ Permission denied - Check JIRA permissions")
        elif e.status_code == 404:
            logging.error("❌ Resource not found")
        else:
            logging.error(f"❌ JIRA Error {e.status_code}: {e.text}")
        return False
        
    except Exception as e:
        logging.error(f"❌ Unexpected error: {str(e)}")
        return False
        
    finally:
        logging.info("Script execution completed")

if __name__ == "__main__":
    success = safe_jira_operation()
    sys.exit(0 if success else 1)
```

### 21.3 Debugging Techniques

**1. Print debugging:**

```python
# Add debug prints
print(f"DEBUG: Connecting to {server}")
jira = JIRA(server=server, basic_auth=(user, apikey))
print("DEBUG: Connection successful")

print(f"DEBUG: Searching with JQL: {jql_query}")
issues = jira.search_issues(jql_query)
print(f"DEBUG: Found {len(issues)} issues")
```

**2. Logging (Better):**

```python
import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Connecting to JIRA")
jira = JIRA(server=server, basic_auth=(user, apikey))
logging.info("Connection successful")

logging.debug(f"Searching with JQL: {jql_query}")
issues = jira.search_issues(jql_query)
logging.info(f"Found {len(issues)} issues")
```

**3. Interactive debugging with pdb:**

```python
import pdb

# Set breakpoint
pdb.set_trace()

# Now you can:
# - Inspect variables
# - Step through code
# - Run commands
```

**4. Validate data before use:**

```python
# Check if reporter exists
if issue.fields.reporter:
    email = issue.fields.reporter.emailAddress
    print(f"Email: {email}")
else:
    print("Warning: No reporter found")

# Check if assignee exists
if issue.fields.assignee:
    assignee = issue.fields.assignee.displayName
else:
    assignee = "Unassigned"
```

---

## 22. Performance Optimization

### 22.1 Batch Operations

**❌ SLOW: Multiple API calls**

```python
# Gets each issue individually (100 calls!)
for i in range(1, 101):
    issue = jira.issue(f'ST-{i}')
    print(issue.fields.summary)
```

**✅ FAST: Single batch query**

```python
# Gets all issues in one call!
issues = jira.search_issues('project = ST AND key in (ST-1, ST-2, ..., ST-100)')
for issue in issues:
    print(issue.fields.summary)
```

### 22.2 Connection Reuse

**❌ SLOW: New connection each time**

```python
for email_address in emails:
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()
    connection.login(user, password)
    send_email(connection, email_address)
    connection.close()  # Reconnecting is slow!
```

**✅ FAST: Reuse connection**

```python
connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls()
connection.login(user, password)

for email_address in emails:
    send_email(connection, email_address)

connection.close()  # Close once at end
```

### 22.3 Pagination for Large Results

```python
# Get many issues efficiently
start_at = 0
max_results = 50
all_issues = []

while True:
    issues = jira.search_issues(
        'project = ST',
        startAt=start_at,
        maxResults=max_results
    )
    
    all_issues.extend(issues)
    
    if len(issues) < max_results:
        break  # No more results
    
    start_at += max_results

print(f"Total issues: {len(all_issues)}")
```

### 22.4 Caching

```python
from functools import lru_cache
import time

@lru_cache(maxsize=128)
def get_user_info(account_id):
    """Cache user lookups"""
    return jira.user(account_id)

# First call: makes API request
user1 = get_user_info('12345')

# Second call: returns cached result (instant!)
user2 = get_user_info('12345')
```

---

## 23. Production Deployment

### 23.1 Production Checklist

```
✅ Security
  - No hardcoded credentials
  - Environment variables configured
  - .gitignore properly set
  - SSL/TLS enabled
  - Credentials rotated

✅ Error Handling
  - Try-catch blocks everywhere
  - Logging configured
  - Email alerts for failures
  - Graceful degradation

✅ Monitoring
  - Log files rotating
  - Disk space monitored
  - Script health checks
  - Performance metrics

✅ Documentation
  - README complete
  - Code commented
  - API docs generated
  - Runbook created

✅ Testing
  - Unit tests written
  - Integration tests passed
  - Edge cases handled
  - Load tested

✅ Backup
  - Config backed up
  - Logs archived
  - Disaster recovery plan
  - Rollback procedure
```

### 23.2 Logging Configuration

```python
import logging
from logging.handlers import RotatingFileHandler

# Configure logging
logger = logging.getLogger('jira_automation')
logger.setLevel(logging.INFO)

# File handler (rotates when 10MB, keeps 5 backups)
file_handler = RotatingFileHandler(
    'automation.log',
    maxBytes=10*1024*1024,  # 10MB
    backupCount=5
)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
))
logger.addHandler(file_handler)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(
    '%(levelname)s - %(message)s'
))
logger.addHandler(console_handler)

# Usage
logger.info("Script started")
logger.warning("Low memory detected")
logger.error("Failed to send email")
logger.critical("JIRA connection lost")
```

### 23.3 Configuration Management

```python
# config/settings.py
import os

class Config:
    """Application configuration"""
    
    # JIRA settings
    JIRA_SERVER = os.getenv('JIRA_SERVER')
    JIRA_USER = os.getenv('JIRA_USER')
    JIRA_API_KEY = os.getenv('JIRA_API_KEY')
    
    # Email settings
    SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
    SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
    EMAIL_USER = os.getenv('EMAIL_USER')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
    
    # Monitoring settings
    CHECK_INTERVAL = int(os.getenv('CHECK_INTERVAL', '1800'))  # 30 min
    MEMORY_THRESHOLD = int(os.getenv('MEMORY_THRESHOLD', '1'))  # 1 GB
    DISK_THRESHOLD = int(os.getenv('DISK_THRESHOLD', '90'))     # 90%
    
    # Logging
    LOG_FILE = os.getenv('LOG_FILE', 'automation.log')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    
    @classmethod
    def validate(cls):
        """Validate required settings"""
        required = [
            'JIRA_SERVER', 'JIRA_USER', 'JIRA_API_KEY',
            'EMAIL_USER', 'EMAIL_PASSWORD'
        ]
        
        missing = [key for key in required if not getattr(cls, key)]
        
        if missing:
            raise ValueError(f"Missing required settings: {', '.join(missing)}")
        
        return True

# Usage
from config.settings import Config

Config.validate()
jira = JIRA(Config.JIRA_SERVER, basic_auth=(Config.JIRA_USER, Config.JIRA_API_KEY))
```

### 23.4 Health Check Script

```python
# health_check.py
"""Check if automation system is healthy"""

import sys
from jira import JIRA
import smtplib
from config.settings import Config

def check_jira():
    """Test JIRA connection"""
    try:
        jira = JIRA(Config.JIRA_SERVER, basic_auth=(Config.JIRA_USER, Config.JIRA_API_KEY))
        jira.current_user()
        print("✅ JIRA: OK")
        return True
    except Exception as e:
        print(f"❌ JIRA: FAILED - {e}")
        return False

def check_email():
    """Test email connection"""
    try:
        connection = smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT)
        connection.starttls()
        connection.login(Config.EMAIL_USER, Config.EMAIL_PASSWORD)
        connection.close()
        print("✅ Email: OK")
        return True
    except Exception as e:
        print(f"❌ Email: FAILED - {e}")
        return False

def main():
    """Run all health checks"""
    print("🏥 Running health checks...\n")
    
    checks = [
        check_jira(),
        check_email()
    ]
    
    if all(checks):
        print("\n✅ All systems operational")
        sys.exit(0)
    else:
        print("\n❌ Some systems failing")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

---

## 24. Complete Code Reference

### 24.1 Minimal Working Example

```python
"""
Minimal JIRA automation example
Demonstrates core concepts
"""

from jira import JIRA
import os

# Get credentials from environment
JIRA_SERVER = os.getenv('JIRA_SERVER')
JIRA_USER = os.getenv('JIRA_USER')
JIRA_API_KEY = os.getenv('JIRA_API_KEY')

# Connect
jira = JIRA(JIRA_SERVER, basic_auth=(JIRA_USER, JIRA_API_KEY))

# Create issue
new_issue = jira.create_issue(
    project='ST',
    summary='Test Issue',
    description='Created by automation',
    issuetype={'name': 'Task'}
)

print(f"Created: {new_issue.key}")

# Add comment
jira.add_comment(new_issue, 'This is an automated comment')

# Get issue
issue = jira.issue(new_issue.key)
print(f"Summary: {issue.fields.summary}")
print(f"Status: {issue.fields.status.name}")
```

### 24.2 Production-Ready Template

```python
"""
Production-ready JIRA automation script
Includes error handling, logging, and configuration
"""

import logging
from logging.handlers import RotatingFileHandler
from jira import JIRA
from jira.exceptions import JIRAError
import sys
import os

# === LOGGING SETUP ===
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = RotatingFileHandler('automation.log', maxBytes=10*1024*1024, backupCount=5)
handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
))
logger.addHandler(handler)

# === CONFIGURATION ===
class Config:
    JIRA_SERVER = os.getenv('JIRA_SERVER')
    JIRA_USER = os.getenv('JIRA_USER')
    JIRA_API_KEY = os.getenv('JIRA_API_KEY')

# === MAIN LOGIC ===
def main():
    """Main automation logic"""
    
    try:
        # Connect
        logger.info("Connecting to JIRA...")
        jira = JIRA(
            Config.JIRA_SERVER,
            basic_auth=(Config.JIRA_USER, Config.JIRA_API_KEY)
        )
        logger.info("✅ Connected successfully")
        
        # Search for issues
        logger.info("Searching for unassigned tickets...")
        issues = jira.search_issues(
            'project = ST AND assignee = EMPTY AND resolution = Unresolved'
        )
        logger.info(f"✅ Found {len(issues)} unassigned tickets")
        
        # Process each issue
        for issue in issues:
            try:
                logger.info(f"Processing {issue.key}")
                
                # Add comment
                jira.add_comment(issue, 'Auto-assigned by system')
                
                # Assign to default user
                issue.update(assignee={'accountId': 'default-user-id'})
                
                logger.info(f"✅ Processed {issue.key}")
                
            except JIRAError as e:
                logger.error(f"❌ Failed to process {issue.key}: {e.text}")
                continue
        
        logger.info("✅ Script completed successfully")
        return 0
        
    except JIRAError as e:
        logger.error(f"❌ JIRA Error: {e.text}")
        return 1
        
    except Exception as e:
        logger.error(f"❌ Unexpected error: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

---

## 25. Troubleshooting Guide

### 25.1 Common Issues

**Issue: "ModuleNotFoundError: No module named 'jira'"**

```bash
# Solution:
pip install jira

# Verify installation:
python -c "import jira; print(jira.__version__)"
```

**Issue: "AttributeError: 'NoneType' object has no attribute 'displayName'"**

```python
# Problem: Accessing attribute on None object
assignee = issue.fields.assignee.displayName  # Crashes if no assignee!

# Solution: Check before accessing
if issue.fields.assignee:
    assignee = issue.fields.assignee.displayName
else:
    assignee = "Unassigned"
```

**Issue: "Empty attachment uploaded"**

```python
# Problem: File closed before upload
f = open('file.jpg', 'rb')
jira.add_attachment(issue, f)  # File might be closed!

# Solution: Use context manager
with open('file.jpg', 'rb') as f:
    jira.add_attachment(issue, f)
```

**Issue: "SMTPAuthenticationError: Username and Password not accepted"**

```
Solution:
1. Enable 2-Factor Authentication on Gmail
2. Generate App Password (not regular password!)
3. Use App Password in script
4. Format: "xxxx xxxx xxxx xxxx" (16 characters)
```

**Issue: "JIRAError: Field 'assignee' cannot be set"**

```python
# Problem: Using email instead of account ID
issue.update(assignee='user@email.com')  # Wrong!

# Solution: Use account ID
issue.update(assignee={'accountId': '712020:fd4e96...'})
```

### 25.2 Debug Checklist

```
When script fails, check:

✅ Credentials
  - API key valid?
  - Email correct?
  - App password correct?

✅ Permissions
  - Can access project?
  - Can create issues?
  - Can edit issues?

✅ Network
  - Internet connected?
  - Firewall blocking?
  - Proxy configured?

✅ Data
  - Issue exists?
  - Field has value?
  - Format correct?

✅ Environment
  - Python version OK?
  - Libraries installed?
  - Environment variables set?
```

---

## 26. API Reference

### 26.1 JIRA Class Methods

```python
from jira import JIRA

jira = JIRA(server, basic_auth=(user, apikey))

# === Issue Operations ===
issue = jira.issue('ST-4')                    # Get issue
jira.create_issue(fields={...})               # Create issue
issue.update(fields={...})                    # Update issue
issue.delete()                                # Delete issue

# === Search ===
issues = jira.search_issues('JQL query')      # Search with JQL

# === Comments ===
jira.comments(issue)                          # Get all comments
jira.add_comment(issue, 'text')               # Add comment
comment = jira.comment(issue, comment_id)     # Get specific comment
comment.update(body='new text')               # Update comment
comment.delete()                              # Delete comment

# === Attachments ===
jira.add_attachment(issue, file)              # Add attachment
jira.attachment(attachment_id)                # Get attachment

# === Worklogs ===
jira.worklogs(issue)                          # Get worklogs
jira.add_worklog(issue, timeSpent='2h')       # Add worklog

# === Users ===
user = jira.user('account_id')                # Get user
jira.search_users('query')                    # Search users
jira.current_user()                           # Get current user

# === Projects ===
projects = jira.projects()                    # Get all projects
project = jira.project('ST')                  # Get specific project

# === Fields ===
fields = jira.fields()                        # Get all fields

# === Transitions ===
transitions = jira.transitions(issue)         # Get available transitions
jira.transition_issue(issue, 'Done')          # Transition issue
```

### 26.2 Issue Fields Reference

```python
issue = jira.issue('ST-4')

# === Basic Info ===
issue.key                                     # 'ST-4'
issue.id                                      # '10000'
issue.fields.summary                          # Title
issue.fields.description                      # Description
issue.fields.issuetype.name                   # 'Issue', 'Task', etc.

# === People ===
issue.fields.assignee.displayName             # Assignee name
issue.fields.assignee.emailAddress            # Assignee email
issue.fields.assignee.accountId               # Assignee ID
issue.fields.reporter.displayName             # Reporter name
issue.fields.creator.displayName              # Creator name

# === Status & Priority ===
issue.fields.status.name                      # 'To Do', 'Done', etc.
issue.fields.priority.name                    # 'High', 'Low', etc.
issue.fields.resolution                       # Resolution if closed

# === Dates ===
issue.fields.created                          # Creation timestamp
issue.fields.updated                          # Last update timestamp
issue.fields.duedate                          # Due date if set

# === Time Tracking ===
issue.fields.timetracking.originalEstimate    # Original estimate
issue.fields.timetracking.remainingEstimate   # Remaining time
issue.fields.timetracking.timeSpent           # Time logged

# === Related ===
issue.fields.comment.comments                 # List of comments
issue.fields.attachment                       # List of attachments
issue.fields.project.key                      # Project key
issue.fields.project.name                     # Project name
```

---

## 27. Resources & Further Learning

### 27.1 Official Documentation

**JIRA REST API:**
- https://developer.atlassian.com/cloud/jira/platform/rest/v3/

**jira-python Library:**
- https://jira.readthedocs.io/

**Atlassian Developer:**
- https://developer.atlassian.com/

### 27.2 Learning Resources

**Python:**
- Python.org Tutorial: https://docs.python.org/3/tutorial/
- Real Python: https://realpython.com/

**DevOps:**
- DevOps Roadmap: https://roadmap.sh/devops
- AIOps Fundamentals

**APIs:**
- REST API Tutorial: https://restfulapi.net/
- HTTP Methods

### 27.3 Tools & Libraries

```python
# Core libraries used
jira                  # JIRA API client
paramiko              # SSH client
smtplib               # Email sending (built-in)
email.mime            # Email formatting (built-in)
datetime              # Date/time handling (built-in)

# Recommended additions
requests              # HTTP requests
python-dotenv         # Environment variable management
pytest                # Testing
black                 # Code formatting
pylint                # Code linting
```

### 27.4 Next Steps

**1. Expand your automation:**
- Add Slack notifications
- Integrate with monitoring tools
- Create dashboards
- Add machine learning predictions

**2. Improve code quality:**
- Write unit tests
- Add type hints
- Improve documentation
- Implement CI/CD

**3. Scale up:**
- Use databases for logging
- Implement message queues
- Add redundancy
- Monitor performance

**4. Learn more:**
- Study advanced JQL
- Explore JIRA webhooks
- Learn Agile methodology
- Practice DevOps principles

---

## 🎓 Conclusion

Congratulations! You've completed this comprehensive JIRA with Python automation guide!

### What You've Learned

✅ **JIRA Fundamentals:** Architecture, API, authentication
✅ **Python Integration:** jira-python library, best practices
✅ **Automation Workflows:** Ticket creation, email notifications, monitoring
✅ **Real-World Applications:** Server health monitoring, auto-acknowledgment
✅ **Security:** Credential management, secure coding practices
✅ **Production Deployment:** Error handling, logging, performance

### Your Project Achievement

Your project demonstrates:
- 🔧 **10 functional Python scripts**
- 📧 **Email automation integration**
- 🐧 **Linux server monitoring**
- 🎯 **JQL query expertise**
- 📝 **Comment management**
- 📎 **Attachment handling**

### Portfolio Value

This project shows employers you can:
- Build production-ready automation
- Integrate multiple systems
- Handle real-world DevOps scenarios
- Write secure, maintainable code
- Document your work professionally

### Keep Learning!

Your journey in AIOps and automation is just beginning. Keep building, keep learning, and keep automating!

---

**Author:** Saleem Ali  
**Course:** AIOps - Al-Nafi International College  
**LinkedIn:** https://www.linkedin.com/in/saleem-ali-189719325/  
**GitHub:** https://github.com/ali4210

---

*This guide is part of a comprehensive JIRA Python automation project documentation.*

**Version:** 1.0  
**Last Updated:** January 2025  
**License:** For educational purposes✅ Connection Successful!")
        print(f"📧 Logged in as: {current_user}")
        
        # Get projects
        projects = jira.projects()
        print(f"📁 Available Projects: {len(projects)}")
        for project in projects:
            print(f"   - {project.key}: {project.name}")
        
        return True
        
    except Exception as e:
        print(f"❌ Connection Failed!")
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_jira_connection()
    sys.exit(0 if success else 1)
```

**Expected output:**
```
🔄 Connecting to JIRA...
✅ Connection Successful!
📧 Logged in as: saleemali.mohammad@gmail.com
📁 Available Projects: 3
   - ST: Saleem_T
   - AC: Another Project
   - IIP: IT Infrastructure Project
```

---

## 6. JIRA REST API Fundamentals

### 6.1 REST API Basics

**What is REST?**
- Architectural style for web services
- Uses HTTP methods
- Stateless communication
- Resource-based URLs

**HTTP Methods Used:**
| Method | Purpose | JIRA Example |
|--------|---------|--------------|
| GET | Retrieve data | Get issue details |
| POST | Create new data | Create ticket |
| PUT | Update existing data | Update ticket |
| DELETE | Remove data | Delete comment |

### 6.2 JIRA API Endpoints

**From your code, you're using:**

```python
# General format
https://saleemalimohammad.atlassian.net/rest/api/latest/issue/ST-3
        ↓                                  ↓            ↓      ↓
   Your domain                         API path    Version  Resource
```

**Common endpoints:**

```
# Get issue
GET /rest/api/3/issue/{issueKey}

# Create issue
POST /rest/api/3/issue

# Update issue
PUT /rest/api/3/issue/{issueKey}

# Get comments
GET /rest/api/3/issue/{issueKey}/comment

# Add comment
POST /rest/api/3/issue/{issueKey}/comment

# Get user
GET /rest/api/3/user?accountId={accountId}
```

### 6.3 API Response Structure

**When you call `jira.issue('ST-4')`:**

```json
{
  "id": "10000",
  "key": "ST-4",
  "fields": {
    "summary": "Account got Locked",
    "description": "User cannot login",
    "status": {
      "name": "To Do"
    },
    "priority": {
      "name": "High"
    },
    "assignee": {
      "displayName": "Saleem Ali",
      "emailAddress": "saleemali.mohammad@gmail.com"
    },
    "reporter": {
      "displayName": "User Name"
    },
    "created": "2025-01-15T10:30:00.000+0600",
    "comment": {
      "comments": [...]
    }
  }
}
```

**Accessing fields in Python:**
```python
issue = jira.issue('ST-4')

# Access nested fields
summary = issue.fields.summary
status = issue.fields.status.name
assignee_name = issue.fields.assignee.displayName
assignee_email = issue.fields.assignee.emailAddress
```

### 6.4 Understanding Field Access

**From Python_JIRA.py - Line by line:**

```python
ticket = 'AC-7'  # Issue key
issue = jira.issue(ticket)  # Fetch issue object

# Now issue is a Python object with nested attributes:

print(issue.fields.project)
# Output: <JIRA Project: key='AC', name='Account Project'>

print(issue.fields.project.key)
# Output: 'AC'

print(issue.fields.project.name)
# Output: 'Account Project'

print(issue.fields.summary)
# Output: 'Account got Locked Seriously'

print(issue.fields.assignee.displayName)
# Output: 'sameenaAndroid@'

print(issue.fields.status.name)
# Output: 'To Do'
```

**Why the dot notation?**
```python
issue.fields.assignee.displayName
  ↓      ↓       ↓          ↓
Object  Field  Nested   Property
               Object
```

This is **object traversal** - moving through nested data structures.

### 6.5 Available Fields

**From Python_JIRA.py:**

```python
print(jira.fields())
```

**This returns ALL available fields:**
```python
[
    {'id': 'summary', 'name': 'Summary', 'custom': False},
    {'id': 'description', 'name': 'Description', 'custom': False},
    {'id': 'priority', 'name': 'Priority', 'custom': False},
    {'id': 'assignee', 'name': 'Assignee', 'custom': False},
    # ... many more
]
```

**Common fields you'll use:**
```python
# Basic Info
issue.fields.summary          # Brief title
issue.fields.description      # Detailed description
issue.fields.issuetype.name   # Type: Issue, Task, Bug, etc.

# People
issue.fields.assignee         # Assigned person
issue.fields.reporter         # Person who created it
issue.fields.creator          # Original creator

# Status & Priority
issue.fields.status.name      # Current status
issue.fields.priority.name    # Priority level

# Dates
issue.fields.created          # Creation timestamp
issue.fields.updated          # Last update timestamp

# Time Tracking
issue.fields.timetracking.originalEstimate
issue.fields.timetracking.remainingEstimate
issue.fields.timetracking.timeSpent

# Comments
issue.fields.comment.comments  # List of all comments

# Attachments
issue.fields.attachment       # List of files

# Project Info
issue.fields.project.key      # Project key
issue.fields.project.name     # Project name
```

---

## 7. Python JIRA Library Deep Dive

### 7.1 Library Architecture

**The jira-python library provides:**
- High-level Python interface
- Automatic request handling
- Object-oriented approach
- Error handling

**Installation:**
```bash
pip install jira
```

**Import:**
```python
from jira import JIRA
```

### 7.2 Core Classes

#### **JIRA Class**
Main class for all operations:

```python
from jira import JIRA

jira = JIRA(
    server='https://saleemalimohammad.atlassian.net',
    basic_auth=('user@email.com', 'api-token')
)
```

**Common methods:**
```python
# Issue operations
jira.issue(key)              # Get issue
jira.create_issue(fields)    # Create issue
jira.search_issues(jql)      # Search issues

# Comment operations
jira.comments(issue)         # Get comments
jira.add_comment(issue, text) # Add comment
jira.comment(issue, comment_id) # Get specific comment

# Attachment operations
jira.add_attachment(issue, file) # Add file

# Worklog operations
jira.add_worklog(issue, timeSpent) # Log time

# User operations
jira.current_user()          # Get current user
jira.search_users(query)     # Search users

# Project operations
jira.projects()              # Get all projects
jira.project(key)            # Get specific project
```

#### **Issue Class**
Represents a JIRA issue:

```python
issue = jira.issue('ST-4')

# Attributes
issue.key                    # 'ST-4'
issue.id                     # '10000'
issue.fields                 # All fields object
issue.permalink()            # Full URL to issue

# Methods
issue.update(fields)         # Update issue
issue.delete()               # Delete issue (careful!)
```

#### **Comment Class**
Represents a comment:

```python
comments = issue.fields.comment.comments

for comment in comments:
    comment.id              # Comment ID
    comment.body            # Comment text
    comment.author          # Author object
    comment.created         # Timestamp
    comment.updated         # Last update
```

### 7.3 Working with Issue Objects

**From Python_JIRA.py - Complete analysis:**

```python
from jira import JIRA

# 1. Connection
user = "saleemali.mohammad@gmail.com"
server = "https://saleemalimohammad.atlassian.net"
apikey = "ATATT3xFfGF0BL9FH_fwpo8qSgklx..."
jira = JIRA(server=server, basic_auth=(user, apikey))

# 2. Get all available fields (useful for exploration)
print(jira.fields())
# Returns: List of all field definitions

# 3. Fetch specific issue
ticket = 'AC-7'
issue = jira.issue(ticket)

# 4. Check object type
print(type(issue))
# Output: <class 'jira.resources.Issue'>

# 5. Access project information
print(issue.fields.project)
# Output: <JIRA Project: key='AC', name='Account Project'>

print(issue.fields.project.key)
# Output: 'AC' (string)

print(issue.fields.project.name)
# Output: 'Account Project' (string)

# 6. Get issue type
print(issue.fields.issuetype.name)
# Output: 'Issue' or 'Task' or 'Bug', etc.

# 7. Get summary (title)
print(issue.fields.summary)
# Output: 'Account got Locked Seriously'

# 8. Get description (detailed text)
print(issue.fields.description)
# Output: Full description text

# 9. Get assignee information
print(issue.fields.assignee.displayName)
# Output: 'sameenaAndroid@'

# Note: If no assignee, this could be None
# Safe access:
if issue.fields.assignee:
    print(issue.fields.assignee.displayName)
else:
    print("No assignee")

# 10. Get current status
print(issue.fields.status.name)
# Output: 'To Do', 'In Progress', 'Done', etc.

# 11. Get priority
print(issue.fields.priority)
# Output: <JIRA Priority: name='High'>

# 12. Get time tracking info
print(issue.fields.timetracking)
# Output: Time tracking object

print(issue.fields.timetracking.remainingEstimate)
# Output: '5h' or None

print(issue.fields.timetracking.originalEstimate)
# Output: '10h' or None

print(issue.fields.timetracking.timeSpent)
# Output: '2h 30m' or None

# 13. Get all comments
comments = issue.fields.comment.comments
for comment in comments:
    print(comment.body)
    # Output: Comment text
```

### 7.4 Error Handling

**Common errors you'll encounter:**

```python
from jira import JIRA
from jira.exceptions import JIRAError
import sys

def safe_jira_operation():
    user = "saleemali.mohammad@gmail.com"
    apikey = "your-api-key"
    server = "https://saleemalimohammad.atlassian.net"
    
    try:
        # Connection
        jira = JIRA(server=server, basic_auth=(user, apikey))
        
        # Get issue
        issue = jira.issue('ST-4')
        
        # Access field safely
        if issue.fields.assignee:
            assignee = issue.fields.assignee.displayName
        else:
            assignee = "Unassigned"
        
        print(f"
