def snake_to_camel(variable):
    """Converts a variable name from snake case to camel case"""

    if type(variable) == str:

        v_lst = variable.split("_")
        result = ""
        for index, word in enumerate(v_lst):
            if result == "":
                result += word.lower()
            else:
                result += word[0].title() + word[1:].lower() if len(word) >= 1 else ""
        return result

    return NotImplementedError


# 1. split by _
# __my_ranDom_snake__cased_phrase
# ['my', 'ranDom', 'snake' ...]

# 2. capitalized for each word



#### SAMPLE TEST CASES (You may add your own) ####

# snake_case_example
# camelCaseExample

#### Part One ####
print(snake_to_camel('my_random_snake_cased_phrase')) # myRandomSnakeCasedPhrase
print(snake_to_camel('__MY_ranDom_snake__cased_phrase')) # myRandomSnakeCasedPhrase


# print(snake_to_camel(''))
print(snake_to_camel([]))
print(snake_to_camel({}))
# print(snake_to_camel(None))
# print(snake_to_camel(123))

#### Part Two ####



def convert_json_case(json_dict):
    """Converts keys in a JSON dictionary from snake case to camel case"""
    result = dict()
    for key, value in json_dict.items():
        result[snake_to_camel(key)] = value

    return result


#### SAMPLE TEST CASES (You may add your own) ####

print(convert_json_case({'hello_there': 123, 'method_two': 123}))
# expect: helloThere: 123,




#### Part Three ####


def convert_json_case2(json_dict):
    """Converts keys in a JSON dictionary from snake case to camel case"""
    result = dict()
    for key, value in json_dict.items():

        if type(value) == dict:
            result[snake_to_camel(key)] = convert_json_case2(value)
        else:
            result[snake_to_camel(key)] = value

    return result


#### SAMPLE TEST CASES (You may add your own) ####

print(convert_json_case2({'method_one': {'hello_there': 123, 'method_two': 123}}))




#### Part Four ####
# print(convert_json_case({'hello_there': [{'method_one': 123, 'method_two': 123}]}))
# print(convert_json_case({'hello_there': [{'method_one': 123, 'method_two': 123}, {'three': 3}]}))


# # print(convert_json_case([{'hello_there': 1
# }, {'yes_hi': 2}, 123, None]))
# # expect: [helloThere, ]


def convert_json_case3(json_dict):
    """Converts keys in a JSON dictionary from snake case to camel case"""
    result = dict()
    for key, value in json_dict.items():
        print (key)
        if type(value) == dict:
            result[snake_to_camel(key)] = convert_json_case3(value)
        elif type(value) == list:
            result[snake_to_camel(key)] = [convert_json_case3(v) for v in value]
        else:
            result[snake_to_camel(key)] = value

    return result


#### SAMPLE TEST CASES (You may add your own) ####

print(convert_json_case3({'method_one': [{'method_one2': 123, 'method_two': 123}], 'method_two2': [{'method_one3': 123, 'method_two3': 123}]}))

# n = number of key for `json_dict`, m = length of array
# O(n * m)
