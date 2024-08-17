def add_time(start, duration, starting_day=None):
    # Define days of the week in order
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Helper function to find the index of the day in the days_of_week list
    def find_day_index(day):
        if day:
            day = day.lower().capitalize()
            return days_of_week.index(day)
        return None
    
    # Parse start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    if period == 'PM' and start_hour != 12:
        start_hour += 12
    elif period == 'AM' and start_hour == 12:
        start_hour = 0
    
    # Parse duration time
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    # Calculate new time
    end_minute = start_minute + duration_minute
    end_hour = start_hour + duration_hour + (end_minute // 60)
    end_minute = end_minute % 60
    days_later = end_hour // 24
    end_hour = end_hour % 24
    
    # Determine the period (AM/PM)
    if end_hour == 0:
        end_period = "AM"
        end_hour = 12
    elif end_hour < 12:
        end_period = "AM"
    elif end_hour == 12:
        end_period = "PM"
    else:
        end_period = "PM"
        end_hour -= 12
    
    # Determine the new day of the week if provided
    if starting_day:
        day_index = find_day_index(starting_day)
        new_day_index = (day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
    else:
        new_day = None
    
    # Format the new time
    new_time = f"{end_hour}:{end_minute:02d} {end_period}"
    if new_day:
        new_time += f", {new_day}"
    
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"
    
    return new_time

# Example usage
print(add_time('3:00 PM', '3:10'))
print(add_time('11:30 AM', '2:32', 'Monday'))
print(add_time('11:43 AM', '00:20'))
print(add_time('10:10 PM', '3:30'))
print(add_time('11:43 PM', '24:20', 'tueSday'))
print(add_time('6:30 PM', '205:12'))