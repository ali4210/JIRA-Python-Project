
# Jira Automation & DevOps Pipeline

**Author:** Saleem Ali
**Domain:** DevOps, ITSM, & Python Automation
**Tech Stack:** Python, Jira API, Linux (SSH), SMTP

---

## ==>> Project Overview

This repository hosts a suite of **IT Service Management (ITSM) Automation tools**. It moves beyond simple API calls by integrating **Infrastructure Monitoring** directly with **Issue Tracking**.

The core system monitors Linux servers for performance bottlenecks (e.g., Low RAM) and automatically raises Jira tickets, assigns them to engineers, and notifies stakeholders via email—all without human intervention.

---

## ==>> Architecture Workflow



**1. Monitor:** Python script connects to Linux Servers via SSH (`paramiko`).
**2. Analyze:** Script executes system commands (`free -g`) to check health metrics.
**3. Act:** If metrics breach thresholds, the script uses the **Jira REST API** to create an incident ticket.
**4. Notify:** The system queries Jira for new tickets and sends HTML acknowledgment emails to reporters via SMTP.

---

## ==>> Key Features

### => 1. Infrastructure-as-Ticket (IaT)
* **Automated Incidents:** Automatically converts server health alerts (Low Memory, High CPU) into Jira tickets.
* **Smart Assignment:** Auto-assigns tickets to specific engineers based on the server IP or issue type.

### => 2. Jira API Engineering
* **Bulk Operations:** Capability to process attachments and comments in bulk.
* **JQL Intelligence:** Advanced filtering logic to identify "Stale" or "Unassigned" tickets for cleanup.
* **History Tracking:** Scripts to audit the "Last Comment" or "Status Change" timestamps (`last_comment.py`).

### => 3. Communication Automation
* **HTML Emails:** Sends professional, formatted email notifications to ticket reporters using Python's `smtplib`.
* **Acknowledgment Loop:** Ensures every new user request gets an immediate "Received" confirmation.

---

## ==>> Setup & Installation

### => Prerequisites
* Python 3.8+
* Jira Cloud Account (API Token required)
* Linux Server (for monitoring module)

### => Step 1: Install Dependencies
```bash
pip install jira paramiko

```

### => Step 2: Configure Credentials

Update the `apikey` and `server` variables in the scripts:

```python
user = "your_email@domain.com"
apikey = "YOUR_ATLASSIAN_TOKEN"
server = "[https://your-domain.atlassian.net](https://your-domain.atlassian.net)"

```

### => Step 3: Run the Monitor

To start monitoring the Linux server:

```bash
python Linux_to_JIRA.py

```

---

## ==>> Project Structure

```text
├── JIRA/
│   ├── Linux_to_JIRA.py       # Server Health Monitor -> Jira
│   ├── JQL_Query+EMAIL.py     # Auto-Email Responder
│   ├── Jira_ticket_creation.py # CRUD Operations
│   ├── Comments.py            # Comment Analysis
│   └── Email_Sir.py           # Legacy Email Logic
└── README.md                  # Documentation

```

---

## ==>> Contact

**Saleem Ali**

* **Role:** Automation Engineer
* **Focus:** Integrating Systems & Automating Workflows.

```
