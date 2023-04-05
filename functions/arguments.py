def year_birth(name,age):
    year = 2023-age
    print(f"Hello{name},you were born in{year}")

def my_country(country = "Kenya"):
    print(f"Hello you are from{country}")

def hello(*names):
    for name in names:
        print(f"Hello{names}")

def sum(*nums):
    answer = 0
    for num in nums:
        answer += num
    return answer

def multiplymany(**kwargs):
    answer = 1
    for num in kwargs.values():
        answer *= num
    return answer

# ASSIGMENT
# A function named concatenate_args that takes any number of string arguments in
#  positional arguments format and concatenates them into a single string
def concatenate_arg(*name):

    joining="".join(name)
    return(joining)

# A function named concatenate_kwargs that takes any number of string arguments in
#  keyword arguments  format and concatenates them into a single string
def concatenate_kwargs(**kwargs):
    answer=""
    for name in kwargs.value():
        answer += name
    return answer