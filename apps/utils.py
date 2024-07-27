
def change_phone(phone):
    return phone[4:].replace('-', '').replace('(', '').replace(')', '').replace(' ', '')