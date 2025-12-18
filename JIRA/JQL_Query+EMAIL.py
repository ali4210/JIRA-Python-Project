import smtplib
from email.message import EmailMessage
from jira import JIRA
import sys
import config

# === EMAIL CONFIGURATION ===
# NOTE: This password is a GMAIL APP PASSWORD, NOT your regular Gmail password.
my_mail = "saleemali.mohammad@gmail.com"
my_password = config.GMAIL_APP_PASSWORD
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# === JIRA CONFIGURATION ===
user = "saleemali.mohammad@gmail.com"
apikey = config.JIRA_API_TOKEN

# === 1. Define HTML Template (Must be outside the loop) ===
EMAIL_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>JIRA Acknowledgment</title>
</head>
<body>
<p> Dear {reporter_name}, <br> <br> Thank You for writing to us. <br> <br> This reply is to acknowledge your message request for **JIRA Ticket {ticket_key}**. We have received your message and our team is looking into it and will get back to you soon. <br> <br> Thank You<br> Alnafi Support Team </p>
</body>
</html>
"""

# === 2. Connection Logic (Outside the Loop) ===
try:
    jira = JIRA(server=server, basic_auth=(user, apikey))
    print("✅ Jira Connection Successful.")

    # Establish SMTP connection BEFORE the email loop
    connection = smtplib.SMTP(smtp_server, smtp_port)
    connection.starttls()
    connection.login(user=my_mail, password=my_password)
    print("✅ SMTP Connection Successful.")

except Exception as e:
    print(f"❌ Initial Connection Failed. Error: {e}")
    sys.exit(1)

# === 3. JIRA Data Fetch ===
issue_in_project = jira.search_issues(
    'created >= -30m AND project ="Saleem_T" AND assignee = EMPTY AND resolution = Unresolved')
total = len(issue_in_project)

t_number = []
uname = []
e_address = []

# === Data Extraction Loop with FIXES ===
for issue in issue_in_project:
    ticket_number = str(issue.key)
    t_number.append(ticket_number)

    reporter_obj = issue.fields.reporter

    # FIX 1a: Safely extract username
    username = str(reporter_obj.displayName) if reporter_obj and hasattr(reporter_obj,'displayName') else "Unknown User"
    uname.append(username)

    # FIX 1b: Safely extract emailAddress
    emailAdd = str(reporter_obj.emailAddress) if reporter_obj and hasattr(reporter_obj,'emailAddress') else "Email Not Found"
    e_address.append(emailAdd)

if total == 0:
    print("No issues found in JIRA")
else:
    print(f"There are {total} issues found in JIRA. Starting email dispatch...")

    # === 4. Email Dispatch Loop (With FIXES) ===
    for jiraticket in range(total):
        ticket_key = t_number[jiraticket]
        reporter_name = uname[jiraticket]
        recipient_email = e_address[jiraticket]  # Use the fetched email

        # Skip if the email address couldn't be found
        if recipient_email == "Email Not Found" or "@" not in recipient_email:
            print(f"⚠️ Skipping {ticket_key}: Reporter email not found or invalid.")
            continue

        # FIX 2: FORMAT the HTML string with current ticket data
        formatted_html = EMAIL_TEMPLATE.format(
            reporter_name=reporter_name,
            ticket_key=ticket_key
        )

        msg = EmailMessage()
        msg['Subject'] = f"Acknowledgment: Your JIRA Ticket {ticket_key} has been received"
        msg['From'] = my_mail
        msg['To'] = recipient_email  # Send to the reporter
        #msg['Cc'] = ["saleemali.mohammad211126@gmail.com", "yousuf3597494@gmail.com"]

        # Add the HTML content
        msg.add_attachment(formatted_html, subtype='html')

        try:
            connection.send_message(msg)
            print(f"✅ Email successfully sent for ticket {ticket_key} to {recipient_email}.")
        except Exception as e:
            print(f"❌ Failed to send email for {ticket_key}. Error: {e}")

# === 5. Final Closure (Outside the Loop) ===
connection.close()
print("\n✅ SMTP Connection Closed. Script finished.")



#https://saleemalimohammad.atlassian.net/rest/api/3/user?accountId={712020:fd4e96d4-fe75-4c8d-b754-301be21eafd9}