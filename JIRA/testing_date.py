import datetime
timestr="2025-11-20T11:40:18.840+0600"

# The original format: "%Y-%m-%dT%H:%M:%S.%f"
# The FIXED format:    "%Y-%m-%dT%H:%M:%S.%f%z"  <-- The '%z' handles the +0600
datetimeobject = datetime.datetime.strptime(timestr, "%Y-%m-%dT%H:%M:%S.%f%z")

print(datetimeobject)

mycustom = datetimeobject.strftime("%Y-%m-%d")
print(mycustom)
