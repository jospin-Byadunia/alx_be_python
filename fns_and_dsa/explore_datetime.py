from datetime import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}")

display_current_datetime()
days = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date(days):
    future_date = datetime.now() + timedelta(days=days)
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")

# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

calculate_future_date(days)