
HOUR = 3600
MINMUTE = 60

def format(time: int):

    hours = time // HOUR
    time -= hours * HOUR

    minutes = time // MINMUTE
    time -= minutes * MINMUTE

    seconds = time

    fmt_time = f'{hours}:' if hours != 0 else ''

    fmt_time += f'{minutes}:{seconds}'

    return fmt_time