''' This module provides a reusable byline for the author's services. '''

#Imports

import math
import statistics

#Variables

bus_name: str = "StClair Data Analytics"
bus_email: str = "sean.fakename@fakeemail.com"
bus_phone: str = "1-123-456-7899"
bus_active_hours : str = "12:30pm-9pm CDT"
count_active_projects: int = 3
count_total_projects: int = 13
average_client_satisfaction: float = 4.5
currently_taking_clients: bool = True
services_offered: list = ["Data Analysis", "Data Warehousing", "Data Structure Auditing"]
satisfaction_scores: list = [4.6, 4.3, 4.0, 5.0, 5.0, 5.0, 3.7, 4.6, 4.9, 4.5]

#Formatted Strings

active_projects_string: str = f"Active Projects: {count_active_projects}"
currently_taking_clients_string: str = f"Taking Clients: {currently_taking_clients}"
services_offered_string: str = f"Services_offered: {services_offered}"
client_satisfaction_string: str = f"Average Client Rating: {average_client_satisfaction}"

smallest= min(satisfaction_scores)
largest= max(satisfaction_scores)
total= sum(satisfaction_scores)
count= len(satisfaction_scores)
mean= statistics.mean(satisfaction_scores)
mode= statistics.mode(satisfaction_scores)
median= statistics.median(satisfaction_scores)
standard_deviation=statistics.stdev(satisfaction_scores)

#calculate descriptive statistics

average_satisfaction_score = statistics.mean(satisfaction_scores)

stats_string: str = f"""
Statistics for Client Satisfaction Scores:
  Smallest: {smallest}
  Largest: {largest}
  Total: {total}
  Count: {count}
  Mean: {mean}
  Mode: {mode}
  Median: {median}
  Standard Deviation: {standard_deviation}
"""

#Byline strings

byline: str = f"""
{bus_name}

{'Contact Information'}
{bus_email}
{bus_phone}
{bus_active_hours}

{'Services offered'}
{services_offered}

{active_projects_string}
{currently_taking_clients_string}
{client_satisfaction_string}
{stats_string}
"""

def main():
  ''' Display all output'''
print(bus_name)

print('Contact Information')
print(bus_email)
print(bus_phone)
print(bus_active_hours)

print ('Services offered')
print(services_offered)
print(active_projects_string)
print(currently_taking_clients_string)
print(client_satisfaction_string)
print(stats_string)

# If all of the above works, then the byline should work too:
print(byline)

if __name__ == '__main__':
    main()