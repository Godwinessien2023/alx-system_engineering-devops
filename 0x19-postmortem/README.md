 0x19-postmortem

https://docs.google.com/document/d/1NBXKow1a6XIK1vN9Xj7ZgM4wByexmPbQbzljTcxVuhI/edit?usp=sharing

Postmortem Report: 
User Authentication Service Outage
Issue Summary:
User authentication service for Piggy-Vest Wallet Limited experienced an outage from 10:30 AM to 12:15 PM GMT on June 10, 2024. During this period, users were unable to log in or register on the web application platform, resulting in approximately 30% of the user base to be affected. This issue caused significant inconvenience as users were unable to access their accounts, wallets or sign up for new ones.


Impact:
Service Affected: User authentication service
User Experience: Users were unable to log in or register.
Affected Users: Approximately 30% of total user base

Root Cause:
A misconfigured database connection  caused the authentication service to exhaust  available connections, leading to failed authentication requests throughout the time.

Timeline:
10:30 AM GMT: Issue detected by automated monitoring alerts indicating a spike in authentication failures.
10:32 AM GMT: Engineering team notified via Slack channel.
10:35 AM GMT: Initial investigation began, focusing on the authentication service logs.
10:45 AM GMT: Database health check performed; no immediate issues found.
11:00 AM GMT: Hypothesis formed around potential API rate limiting issues.
11:20 AM GMT: Investigations revealed no rate limiting; suspicion shifted to database connectivity.
11:30 AM GMT: Deeper analysis of database connections revealed exhaustion of connection pool.
11:45 AM GMT: Incident escalated to the database administration team.
12:00 PM GMT: Configuration error identified in the database connection pool settings.
12:10 PM GMT: Database connection pool settings corrected and service restarted.
12:15 PM GMT: Authentication service fully restored; users able to log in and register again.

Root Cause and Resolution:
The root cause of the outage was a misconfiguration in the database connection pool settings, which limited the number of connections available to the authentication service. This misconfiguration caused the service to exhaust its connection pool during peak usage, resulting in failed authentication attempts.
The issue was resolved by correcting the database connection pool configuration to allow for more connections. After updating the settings, the authentication service was restarted, and normal functionality was restored.

Corrective and Preventative Measures:
To prevent similar issues in the future, the following steps will be taken:
Increase Database Connection Pool Size: Adjust the connection pool settings to accommodate higher loads.
Add Monitoring for Connection Pool Usage: Implement monitoring to track connection pool usage and alert the team if thresholds are approached.

Conduct Load Testing: Regular load testing to ensure the system can handle peak traffic conditions.

Review and Document Configuration Changes: Establish a procedure for reviewing and documenting all configuration changes.

Improve Incident Response Training: Conduct training sessions for the engineering team on identifying and resolving connection pool issues.

Task List:
Patch Nginx server to handle increased traffic efficiently.
Add monitoring on server memory and database connection pool usage.
Implement automated alerts for high connection pool usage.
Schedule regular load testing sessions.
Document current database connection pool settings and update change management process.
Provide training for the engineering team on connection pool management and incident response.


This postmortem report aims to provide a clear and concise overview of the outage, the actions taken to resolve it, and the steps being implemented to prevent future occurrences.

