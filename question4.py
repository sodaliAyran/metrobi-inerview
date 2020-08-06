# I'm not ashamed to say I found this answer on this site: https://levelup.gitconnected.com/valid-parentheses-interview-problem-in-python3-f98fb99c9cf
#  But let me just say they thought this to me in school and I did know to use stacks to solve this problem


def is_valid_paren(input_str):
    pairs = {'(': ')', '[': ']', '{': '}'}
    stack = []

    for char in input_str:
        if char in pairs.keys():
            stack.append(char)
        elif len(stack) > 0 and pairs.get(stack[-1]) == char:
            stack.pop()
        else:
            print(input_str, "contains invalid parentheses.")
            return False

    if len(stack) == 0:
        print(input_str, "contains valid parentheses.")
        return True
    else:
        print(input_str, "contains invalid parentheses.")
        return False

input1 = "{{}}()[()]"
input2 = "{][}"
input3 = ")"
input4 = "{[]}"
input5 = "{(])}"

is_valid_paren(input1)
is_valid_paren(input2)
is_valid_paren(input3)
is_valid_paren(input4)
is_valid_paren(input5)
