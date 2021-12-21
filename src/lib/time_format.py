
HOUR = 3600
MINMUTE = 60

def format(time: int):

    hours = time // HOUR
    time -= hours * HOUR

    minutes = time // MINMUTE
    time -= minutes * MINMUTE

    seconds = time

    fmt_time = f'{hours}:' if hours != 0 else ''

    fmt_time += f'{__zero_fmt(minutes)}:{__zero_fmt(seconds)}'

    return fmt_time

def __zero_fmt(num: int):

    num_str = str(num)

    return '0' + num_str if len(num_str) == 1 else num_str