def add_time(start, duration, weekday=''):
    '''
    Examples:
    
    add_time("11:43 PM", "24:20", "tueSday")
    # Returns: 12:03 AM, Thursday (2 days later)
    
    add_time("6:30 PM", "205:12")
    # Returns: 7:42 AM (9 days later)
    '''

    start_time, meridiem = [int(i) for i in start[:-3].split(':')], start[-2:]
    duration_time = [int(i) for i in duration.split(':')]
    meridiem_list = ('AM', 'PM')
    weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    if meridiem == 'PM':
        start_time[0] += 12
  
  
    final_hours = start_time[0] + duration_time[0] + (start_time[1] + duration_time[1])//60
    final_minutes = (start_time[1] + duration_time[1])%60
    final_meridiem = meridiem_list[((final_hours % 24) // 12)]
  
    final_time = [(final_hours % 12), final_minutes]
    if final_time[0] == 0:
        final_time[0] = 12
    days_passed = final_hours // 24
    days_str = ''
    if days_passed == 1:
        days_str = ' (next day)'
    elif days_passed > 1:
        days_str = f' ({days_passed} days later)' 
  
  
    if weekday:
        weekday_index = weekdays.index(weekday.capitalize())
        weekday = f', {weekdays[(weekday_index + days_passed) % 7]}'
  
    final_time = f'{final_time[0]}:{str(final_time[1]).zfill(2)} {final_meridiem}{weekday}{days_str}'
  
    return final_time
