def get_formatted_name(first,last, middle=''):
    #~ full_name = first + ' ' + last
    #~ full_name = first + middle + last
    if middle:
        full_name = first + ' ' + middle + ' ' +last
    else:
        full_name = first + ' ' + last
    return full_name.title()
