calls = 0

def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [item.lower() for item in
                      list_to_search]
    return string in list_to_search
    



result1 = string_info('capybara')
result2 = is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
print(string_info('capybara'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(calls)



