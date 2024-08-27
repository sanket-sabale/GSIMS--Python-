from datetime import datetime, timedelta

def display_dates_between(start_date, end_date, date_list):
    # Convert string dates to datetime objects
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # Iterate through the date range and display dates within the range
    # print((end_date - start_date))
    # print((end_date - start_date).days + 1)
    for delta in range((end_date - start_date).days + 1):
        # print(delta)
        current_date = start_date + timedelta(days=delta)
        print(type(current_date))
        current_date_str = current_date.strftime("%Y-%m-%d")
        
        if current_date_str in date_list:
            print(current_date_str)

# Example usage
date_list = ["2022-01-15", "2023-05-20", "2021-12-05", "2024-03-10"]

start_date_input = input("Enter the start date (YYYY-MM-DD): ")
end_date_input = input("Enter the end date (YYYY-MM-DD): ")

display_dates_between(start_date_input, end_date_input, date_list)
