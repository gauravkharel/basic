def get_formatted_name(first_name, last_name):
    """return a full name, neatly formatted"""
    full_name = first_name + " " + last_name
    return full_name.title()

print(get_formatted_name('gaurav', 'fox'))