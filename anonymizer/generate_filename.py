from datetime import datetime
def generate_filename():
    now = datetime.now()
    dt_string = now.strftime("%d.%m.%Y-%H:%M:%S")

    return dt_string

# generate_filename()