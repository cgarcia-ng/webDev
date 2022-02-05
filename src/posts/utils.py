'''Helper functions'''

def calculate_time_diff(diff):
    '''Calcula la diferencia de tiempo entre la hora del servidor y la hora de publica
    del post
    '''
    days = diff.days
    hours = diff.seconds // 3600
    minutes = int(((diff.seconds / 3600) - hours) * 60)
    years = int(days / 365)

    if days != 0:
        if days == 1:
            text = f'Last updated {days} day, {hours} hours and {minutes} minutes ago'
        elif days < 365 and days > 0:
            text = f'Last updated {days} days, {hours} hours and {minutes} minutes ago'
        else:
            text = f'Last updated {years} years, {(days / 365 - years) * 365} days, {hours} hours and {minutes} minutes ago'
    else:
        if minutes > 60:
            text = f'Last updated {hours} hours and {minutes} minutes ago'
        else:
            if minutes == 1:
                text = f'Last updated {minutes} minute and {int(((diff.seconds / 60) - diff.seconds // 60) * 60)} seconds ago'
            elif minutes > 1:
                text = f'Last updated {minutes} minutes and {int(((diff.seconds / 60) - diff.seconds // 60) * 60)} seconds ago'
            else:
                text = f'Last updated {diff.seconds} seconds ago'

    return text
