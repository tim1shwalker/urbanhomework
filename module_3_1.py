calls = 0

def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if i == string:
            return True
        return False



result1 = string_info('capybara')
result2 = is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
print(string_info('capybara'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(calls)



