from datetime import datetime

def sort_dates(dates):
    # Custom key function to convert string dates to datetime objects
    def date_key(date_str):
        return datetime.strptime(date_str, "%Y-%m-%d")

    # Sort the list of dates using the custom key function
    sorted_dates = sorted(dates, key=date_key)

    return sorted_dates

# Example usage
date_list = ["2022-01-15", "2023-05-20", "2021-12-05", "2024-03-10"]

sorted_dates = sort_dates(date_list)

print("Original dates:", date_list)
print("Sorted dates:", sorted_dates)
