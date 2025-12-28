# 🎯 JIRA with Python - Complete Automation Suite

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![JIRA API](https://img.shields.io/badge/JIRA-REST%20API-blue)](https://developer.atlassian.com/cloud/jira/platform/rest/v3/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-production--ready-success)](https://github.com/ali4210)

> **Intelligent JIRA automation system combining Python, REST APIs, email notifications, and Linux monitoring for streamlined DevOps operations.**

**Author:** Saleem Ali | **Course:** AIOps @ Al-Nafi International College  
**LinkedIn:** [saleem-ali-189719325](https://www.linkedin.com/in/saleem-ali-189719325/) | **GitHub:** [@ali4210](https://github.com/ali4210)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Project Architecture](#-project-architecture)
- [Technologies Used](#-technologies-used)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage Examples](#-usage-examples)
- [Project Structure](#-project-structure)
- [Scripts Overview](#-scripts-overview)
- [Real-World Use Cases](#-real-world-use-cases)
- [Security Best Practices](#-security-best-practices)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🌟 Overview

This comprehensive JIRA automation suite demonstrates production-ready DevOps and AIOps capabilities through intelligent integration of JIRA's REST API, automated email notifications, and real-time server monitoring. Built as part of my AIOps coursework at Al-Nafi International College, this project showcases practical automation skills essential for modern IT operations.

### What This Project Does

- **Automates JIRA Operations:** Create, update, and manage tickets programmatically
- **Email Notifications:** Automatic acknowledgment emails for new ticket reporters
- **Server Monitoring:** Real-time Linux server health checks with auto-ticket creation
- **Comment Management:** Advanced filtering and analysis of ticket discussions
- **Time Tracking:** Automated worklog entries and time estimation
- **Attachment Handling:** Seamless file uploads to JIRA issues

---

## ✨ Key Features

### 🎫 Ticket Automation
- **Programmatic ticket creation** with custom fields, priorities, and assignments
- **Bulk operations** for processing multiple issues efficiently
- **Automated comment addition** with rich formatting support
- **File attachment handling** with multiple format support
- **Time tracking integration** with worklog management

### 📧 Email Integration
- **Auto-acknowledgment system** for new unassigned tickets
- **HTML email templates** with personalized content
- **SMTP integration** with Gmail/Office365 support
- **Bulk email dispatch** with connection reuse optimization
- **Error handling** with retry logic

### 🖥️ Server Monitoring
- **SSH-based health checks** via Paramiko
- **Memory monitoring** with configurable thresholds
- **Disk usage tracking** and alerts
- **CPU load monitoring** for performance issues
- **Automatic ticket creation** when issues detected
- **Multi-server support** with parallel monitoring

### 🔍 Advanced Queries
- **JQL (JIRA Query Language)** expertise
- **Time-based filtering** (last N minutes/hours/days)
- **Complex multi-condition queries**
- **Unassigned ticket detection**
- **Status-based reporting**

### 🛡️ Production-Ready
- **Comprehensive error handling** with logging
- **Secure credential management** via environment variables
- **Rate limiting** to prevent API throttling
- **Connection pooling** for performance
- **Detailed documentation** and inline comments

---

## 🏗️ Project Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   JIRA AUTOMATION SUITE                     │
└─────────────────────────────────────────────────────────────┘
                            │
                ┌───────────┴───────────┐
                │                       │
        ┌───────▼────────┐      ┌──────▼──────┐
        │  JIRA REST API │      │  SMTP Server │
        └───────┬────────┘      └──────┬───────┘
                │                      │
    ┌───────────┼──────────┬───────────┼────────────┐
    │           │          │           │            │
┌───▼────┐ ┌───▼────┐ ┌──▼────┐ ┌────▼─────┐ ┌───▼────┐
│ Ticket │ │Comment │ │ Query │ │  Email   │ │ Server │
│ Ops    │ │ Mgmt   │ │ & JQL │ │  Notify  │ │ Monitor│
└────────┘ └────────┘ └───────┘ └──────────┘ └────────┘
     │          │          │           │            │
     └──────────┴──────────┴───────────┴────────────┘
                         │
                 ┌───────▼────────┐
                 │  Linux Servers │
                 │  via SSH/Paramiko│
                 └────────────────┘
```

---

## 🛠️ Technologies Used

| Technology | Purpose | Version |
|------------|---------|---------|
| **Python** | Core programming language | 3.7+ |
| **jira-python** | JIRA REST API client | Latest |
| **Paramiko** | SSH client for server monitoring | Latest |
| **smtplib** | Email sending (built-in) | - |
| **email.mime** | Email formatting (built-in) | - |
| **datetime** | Date/time operations (built-in) | - |

### APIs & Services
- **JIRA REST API v3** - Issue tracking and project management
- **Gmail SMTP** - Email delivery service
- **SSH/Linux** - Remote server administration

---

## 📦 Installation

### Prerequisites

```bash
# Python 3.7 or higher
python --version

# pip package manager
pip --version
```

### Step 1: Clone Repository

```bash
git clone https://github.com/ali4210/JIRA-Python-Automation.git
cd JIRA-Python-Automation
```

### Step 2: Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt

# Or install individually
pip install jira
pip install paramiko
```

### Step 3: Verify Installation

```bash
python -c "import jira; import paramiko; print('✅ All dependencies installed')"
```

---

## ⚙️ Configuration

### 1. JIRA API Setup

**Generate API Token:**
1. Log into your JIRA account
2. Navigate to: Profile → Account Settings → Security
3. Click "Create and manage API tokens"
4. Generate new token and save securely

**Your JIRA Details:**
- **Server:** `https://your-domain.atlassian.net`
- **Email:** Your JIRA account email
- **API Key:** Generated token

### 2. Gmail App Password Setup

**Enable 2-Factor Authentication:**
1. Google Account → Security → 2-Step Verification
2. Enable 2FA

**Generate App Password:**
1. Google Account → Security → App passwords
2. Select "Mail" and "Other device"
3. Copy the 16-character password

### 3. Environment Variables Setup

**Create `.env` file:**

```bash
# JIRA Configuration
JIRA_SERVER=https://your-domain.atlassian.net
JIRA_USER=your-email@gmail.com
JIRA_API_KEY=your-jira-api-token

# Email Configuration
EMAIL_USER=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587

# SSH Configuration (for server monitoring)
SSH_HOST=192.168.1.6
SSH_USER=your-username
SSH_PASSWORD=your-password

# Monitoring Thresholds
MEMORY_THRESHOLD=1
DISK_THRESHOLD=90
CPU_THRESHOLD=4.0
```

**⚠️ IMPORTANT:** Add `.env` to `.gitignore` to prevent credential exposure!

### 4. Update Script Configuration

**Option A: Use environment variables (Recommended)**

```python
import os

JIRA_SERVER = os.getenv('JIRA_SERVER')
JIRA_USER = os.getenv('JIRA_USER')
JIRA_API_KEY = os.getenv('JIRA_API_KEY')
```

**Option B: Use configuration file**

```python
from config.secrets import JIRA_CONFIG, EMAIL_CONFIG

jira = JIRA(JIRA_CONFIG['server'], basic_auth=(JIRA_CONFIG['user'], JIRA_CONFIG['api_key']))
```

---

## 🚀 Usage Examples

### Example 1: Create JIRA Ticket

```python
from jira import JIRA

# Connect to JIRA
jira = JIRA(
    server='https://your-domain.atlassian.net',
    basic_auth=('your-email@gmail.com', 'your-api-key')
)

# Create new issue
new_issue = jira.create_issue(
    project='ST',
    summary='Server Memory Alert',
    description='Low memory detected on production server',
    issuetype={'name': 'Issue'},
    priority={'name': 'High'},
    timetracking={'originalEstimate': '2h'}
)

print(f"✅ Created ticket: {new_issue.key}")
```

### Example 2: Auto-Acknowledgment Email

```python
from jira import JIRA
import smtplib
from email.message import EmailMessage

# Connect to JIRA
jira = JIRA(server, basic_auth=(user, apikey))

# Search for unassigned tickets
issues = jira.search_issues(
    'created >= -30m AND assignee = EMPTY AND resolution = Unresolved'
)

# Send email to each reporter
connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls()
connection.login(email_user, email_password)

for issue in issues:
    msg = EmailMessage()
    msg['Subject'] = f'Ticket {issue.key} Received'
    msg['From'] = email_user
    msg['To'] = issue.fields.reporter.emailAddress
    msg.set_content(f'Your ticket {issue.key} has been received. We will respond soon.')
    
    connection.send_message(msg)
    print(f"✅ Email sent for {issue.key}")

connection.close()
```

### Example 3: Server Health Monitoring

```python
import paramiko
from jira import JIRA

# Connect to server via SSH
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.1.6', username='admin', password='password')

# Check memory
stdin, stdout, stderr = client.exec_command('free -g')
output = stdout.readlines()
available_mem = int(output[1].split()[6])

# Create ticket if low memory
if available_mem <= 1:
    jira = JIRA(server, basic_auth=(user, apikey))
    
    issue = jira.create_issue(
        project='IIP',
        summary=f'Low Memory Alert - {available_mem}GB available',
        description=f'Server 192.168.1.6 has low memory',
        issuetype={'name': 'Issue'},
        priority={'name': 'Highest'}
    )
    
    print(f"⚠️ Alert ticket created: {issue.key}")

client.close()
```

### Example 4: JQL Query & Data Extraction

```python
from jira import JIRA

jira = JIRA(server, basic_auth=(user, apikey))

# Advanced JQL query
jql = '''
    project = "ST" 
    AND status IN ("To Do", "In Progress") 
    AND priority = "High" 
    AND created >= -7d
'''

issues = jira.search_issues(jql)

# Extract and display data
for issue in issues:
    print(f"Ticket: {issue.key}")
    print(f"Summary: {issue.fields.summary}")
    print(f"Assignee: {issue.fields.assignee.displayName if issue.fields.assignee else 'Unassigned'}")
    print(f"Status: {issue.fields.status.name}")
    print("-" * 50)
```

---

## 📂 Project Structure

```
JIRA-Python-Automation/
│
├── 📄 README.md                    # This file
├── 📄 requirements.txt             # Python dependencies
├── 📄 .gitignore                   # Git ignore rules
├── 📄 LICENSE                      # MIT License
│
├── 📁 scripts/                     # Main automation scripts
│   ├── Python_JIRA.py             # Basic JIRA operations
│   ├── Jira_ticket_creation.py    # Ticket creation with attachments
│   ├── Comments.py                # Comment retrieval and display
│   ├── JQL_Query.py               # JQL search examples
│   ├── JQL_Query+EMAIL.py         # Query + Email integration
│   ├── Email_Sir.py               # Email automation system
│   ├── last_comment.py            # Advanced comment filtering
│   ├── Linux_to_JIRA.py           # Server monitoring integration
│   └── testing_date.py            # Date parsing utilities
│
├── 📁 config/                      # Configuration files
│   ├── settings.py                # Application settings
│   ├── secrets.example.py         # Template for credentials
│   └── .env.example               # Environment variable template
│
├── 📁 templates/                   # Email templates
│   └── test.html                  # HTML email template
│
├── 📁 logs/                        # Log files (gitignored)
│   └── automation.log
│
└── 📁 docs/                        # Documentation
    ├── MASTER_GUIDE.md            # Comprehensive learning guide
    ├── API_REFERENCE.md           # API documentation
    └── TROUBLESHOOTING.md         # Common issues and solutions
```

---

## 📜 Scripts Overview

### Core JIRA Operations

#### `Python_JIRA.py`
**Purpose:** Demonstrates basic JIRA API operations  
**Features:**
- JIRA connection and authentication
- Fetching issue details
- Accessing all issue fields
- Reading project information
- Status and priority handling

**Key Functions:**
```python
# Fetch issue and display all fields
issue = jira.issue('AC-7')
print(issue.fields.summary)
print(issue.fields.assignee.displayName)
print(issue.fields.status.name)
```

---

#### `Jira_ticket_creation.py`
**Purpose:** Advanced ticket creation with attachments  
**Features:**
- Create issues with custom fields
- Set priority and time estimates
- Assign to specific users
- Add comments automatically
- Upload multiple attachments
- Log work time

**Key Functions:**
```python
# Create issue
new_issue = jira.create_issue(
    project='ST',
    summary='Testing JIRA',
    issuetype={'name': 'Request'},
    priority={'name': 'Highest'},
    timetracking={'originalEstimate': '10h'}
)

# Add attachments
with open('file.jpg', 'rb') as f:
    jira.add_attachment(new_issue.key, f)

# Add comment
jira.add_comment(new_issue.key, 'Automated comment')
```

---

#### `Comments.py`
**Purpose:** Comment retrieval and display  
**Features:**
- Fetch all comments on an issue
- Display comment author
- Show creation timestamp
- Iterate through comment history

**Key Functions:**
```python
issue = jira.issue('AC-7')
comments = issue.fields.comment.comments

for comment in comments:
    print(f"Author: {comment.author}")
    print(f"Text: {comment.body}")
    print(f"Time: {comment.created}")
```

---

### Query & Search

#### `JQL_Query.py`
**Purpose:** JQL queries and data extraction  
**Features:**
- Search issues with JQL
- Time-based filtering
- Extract reporter information
- Bulk data collection

**Key Functions:**
```python
# Find unassigned tickets from last 2 hours
issues = jira.search_issues(
    'created >= -120m AND assignee = EMPTY'
)

# Extract data
for issue in issues:
    ticket_number = issue.key
    reporter_name = issue.fields.reporter.displayName
    reporter_email = issue.fields.reporter.emailAddress
```

---

#### `last_comment.py`
**Purpose:** Advanced comment filtering and analysis  
**Features:**
- Find latest comment by ID
- Filter comments by author
- Filter comments by date
- Store comments in lists

**Key Functions:**
```python
# Get latest comment
latest = comments[-1].body

# Filter by author
for comment in comments:
    if comment.author.displayName == "Engineer Name":
        print(comment.body)

# Filter by date
for comment in comments:
    if comment_date == "2025-11-21":
        print(comment.body)
```

---

### Email Automation

#### `Email_Sir.py`
**Purpose:** Auto-acknowledgment email system  
**Features:**
- Monitor new tickets
- Extract reporter emails
- Send personalized HTML emails
- Rate limiting between sends

**Key Functions:**
```python
# Find new tickets
issues = jira.search_issues('created >= -5m AND assignee = EMPTY')

# Send acknowledgment email
msg = MIMEMultipart()
msg['Subject'] = f"Ticket {ticket_number} Received"
msg['To'] = reporter_email

connection.send_message(msg)
```

---

#### `JQL_Query+EMAIL.py`
**Purpose:** Production-ready query + email integration  
**Features:**
- Comprehensive error handling
- Connection reuse optimization
- Safe data extraction
- Email validation
- HTML template formatting

**Key Functions:**
```python
# Search and send emails
issues = jira.search_issues('created >= -30m AND assignee = EMPTY')

connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls()
connection.login(user, password)

for issue in issues:
    msg = create_email(issue)
    connection.send_message(msg)

connection.close()
```

---

### System Integration

#### `Linux_to_JIRA.py`
**Purpose:** Server health monitoring with auto-ticketing  
**Features:**
- SSH connection to Linux servers
- Memory usage monitoring
- Disk space checking
- CPU load monitoring
- Automatic ticket creation on issues
- Assign to on-call engineer

**Key Functions:**
```python
# Connect via SSH
client = paramiko.SSHClient()
client.connect('192.168.1.6', username='admin', password='pass')

# Check memory
stdin, stdout, stderr = client.exec_command('free -g')
available_mem = parse_output(stdout)

# Create ticket if low
if available_mem <= 1:
    issue = jira.create_issue(
        project='IIP',
        summary=f'Low Memory: {available_mem}GB',
        priority={'name': 'Highest'}
    )
```

---

### Utilities

#### `testing_date.py`
**Purpose:** Date/time parsing utilities  
**Features:**
- Parse JIRA timestamp format
- Convert to Python datetime
- Format date strings
- Handle timezone offsets

**Key Functions:**
```python
# Parse JIRA timestamp
timestr = "2025-11-20T11:40:18.840+0600"
dt = datetime.strptime(timestr, "%Y-%m-%dT%H:%M:%S.%f%z")

# Format to custom string
custom_date = dt.strftime("%Y-%m-%d")
```

---

## 🎯 Real-World Use Cases

### 1. IT Support Automation
**Scenario:** New support tickets need immediate acknowledgment

**Solution:**
- Monitor for new unassigned tickets every 5 minutes
- Extract reporter email from JIRA
- Send personalized acknowledgment email
- Log all actions

**Benefits:**
- Instant user communication
- 100% acknowledgment rate
- Reduced manual workload
- Improved user satisfaction

---

### 2. Infrastructure Monitoring
**Scenario:** Production servers need 24/7 monitoring

**Solution:**
- SSH into servers every 30 minutes
- Check memory, disk, CPU metrics
- Create JIRA ticket if threshold exceeded
- Assign to on-call engineer automatically

**Benefits:**
- Proactive issue detection
- Faster response time
- Audit trail of all incidents
- SLA compliance

---

### 3. Workflow Optimization
**Scenario:** Unassigned tickets sit unnoticed

**Solution:**
- Query for unassigned tickets hourly
- Send report to team lead
- Escalate tickets older than 2 hours
- Track assignment metrics

**Benefits:**
- No tickets fall through cracks
- Improved team efficiency
- Better workload distribution
- Data-driven management

---

## 🔒 Security Best Practices

### ⚠️ Critical: Never Commit Credentials

```bash
# Add to .gitignore
.env
config/secrets.py
*.key
*.pem
*password*
```

### Use Environment Variables

```python
import os

# ✅ GOOD: Read from environment
JIRA_API_KEY = os.getenv('JIRA_API_KEY')

# ❌ BAD: Hardcoded in script
JIRA_API_KEY = "ATATT3xFfGF0..."  # Never do this!
```

### Secure Credential Storage

**Option 1: Environment variables**
```bash
export JIRA_API_KEY="your-key"
export EMAIL_PASSWORD="your-password"
```

**Option 2: Encrypted config file**
```python
from cryptography.fernet import Fernet

# Encrypt credentials
key = Fernet.generate_key()
cipher = Fernet(key)
encrypted = cipher.encrypt(b"my-api-key")
```

### Additional Security Measures

- ✅ Use API tokens, not passwords
- ✅ Enable 2-Factor Authentication
- ✅ Rotate credentials every 3 months
- ✅ Use HTTPS/TLS for all connections
- ✅ Validate SSL certificates
- ✅ Implement rate limiting
- ✅ Log security events
- ✅ Review code before committing

---

## 🐛 Troubleshooting

### Common Issues

**Issue: "ModuleNotFoundError: No module named 'jira'"**

```bash
# Solution
pip install jira

# Verify
python -c "import jira; print('OK')"
```

---

**Issue: "JIRAError: HTTP 401 Unauthorized"**

**Causes:**
- Wrong API key
- Expired token
- Wrong email address

**Solution:**
1. Verify JIRA credentials
2. Generate new API token
3. Update configuration

---

**Issue: "SMTPAuthenticationError"**

**Causes:**
- Using regular password instead of app password
- 2FA not enabled

**Solution:**
1. Enable 2-Factor Authentication in Gmail
2. Generate App Password
3. Use app password in script (format: `xxxx xxxx xxxx xxxx`)

---

**Issue: "AttributeError: 'NoneType' object has no attribute 'displayName'"**

**Cause:** Accessing attribute on None object (e.g., unassigned ticket)

**Solution:**
```python
# ❌ BAD
assignee = issue.fields.assignee.displayName  # Crashes if None!

# ✅ GOOD
if issue.fields.assignee:
    assignee = issue.fields.assignee.displayName
else:
    assignee = "Unassigned"
```

---

**Issue: "Empty attachment uploaded to JIRA"**

**Cause:** File closed before upload completed

**Solution:**
```python
# ❌ BAD
f = open('file.jpg', 'rb')
jira.add_attachment(issue, f)  # File might close!

# ✅ GOOD
with open('file.jpg', 'rb') as f:
    jira.add_attachment(issue, f)  # File stays open
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit changes** (`git commit -m 'Add AmazingFeature'`)
4. **Push to branch** (`git push origin feature/AmazingFeature`)
5. **Open Pull Request**

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/JIRA-Python-Automation.git

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Check code style
pylint scripts/
black scripts/
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Saleem Ali

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 📞 Contact

**Saleem Ali**  
AIOps Student @ Al-Nafi International College

- 📧 **Email:** saleemali.mohammad@gmail.com
- 💼 **LinkedIn:** [linkedin.com/in/saleem-ali-189719325](https://www.linkedin.com/in/saleem-ali-189719325/)
- 🐙 **GitHub:** [@ali4210](https://github.com/ali4210)
- 🌐 **Portfolio:** [github.com/ali4210/repositories](https://github.com/ali4210?tab=repositories)

---

## 🙏 Acknowledgments

- **Al-Nafi International College** - AIOps Program
- **Atlassian** - JIRA Platform and Documentation
- **Python Community** - jira-python library
- **Paramiko Team** - SSH client library

---

## 📈 Project Stats

- **Scripts:** 10 Python files
- **Lines of Code:** 800+
- **Features:** 15+ automation capabilities
- **Documentation:** 250+ pages
- **Status:** Production-ready

---

## 🎓 Learning Outcomes

This project demonstrates proficiency in:

✅ **Python Programming** - Advanced scripting and automation  
✅ **REST API Integration** - JIRA API v3  
✅ **DevOps Practices** - Infrastructure monitoring and automation  
✅ **AIOps Concepts** - Intelligent operations automation  
✅ **Email Automation** - SMTP and MIME protocols  
✅ **Linux Administration** - SSH and remote command execution  
✅ **Security** - Credential management and secure coding  
✅ **Documentation** - Professional technical writing

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

**Made with ❤️ by [Saleem Ali](https://github.com/ali4210)**

**#Python #JIRA #Automation #DevOps #AIOps**

</div>
