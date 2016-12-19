import base64


def convert_from_base64(string):
    decoded = base64.b64decode(string).decode('utf-8')
    return decoded    

def add_spaces(string, newstring=''):
    string = "".join(string.split())
    
    for i, c in enumerate(string):
        if string[i].isdigit() and string[i+1].isdigit(): newstring += string[i]
        else: newstring += string[i] + ' '
    return newstring.rstrip() #remove whitespace from end of string

def check_if_valid_expression(numbers, helper):
    leftp = 0
    rightp = 0
    
    for val in numbers.split(' '):
        if val not in helper.OPERATIONS and not val.isdigit(): raise ValueError('You must use numbers and operations. The following is not allowed: ' + str(val) + '. Allowed operations are: ' + str(helper.OPERATIONS))
        if val == '(': leftp+=1
        if val == ')': rightp+=1
    
    if rightp!= leftp: raise Exception('Must use equal no of parantheses silly!')    


class InfixConverterHelpers():

    OPERATIONS = ['(', '-', '+', '*', '/', ')']

    def pop_stack_until_valid(self, stack, expression, val):
        while not self.should_add_to_stack(val, stack): expression.append(stack.pop()) #add to expression if it does not belong on stack
        stack.append(val) # add the value to the stack 

    def parentheses_pop_to_expression(self, stack, expression):
        while stack[-1] != '(': expression.append(stack.pop())
        stack.pop() # get rid of '('

    def should_add_to_stack(self, val, stack):
        return True if len(stack) == 0 or self.operator_has_precedence(stack[-1], val) else False
      
    def operator_has_precedence(self, first, second):
        if first == '(': return True # we want to add these to the stack
        if second == first: return False # not allowed in stack
        lower = ['-', '+']
        higher = ['/', '*']
        return False if first in higher and second in lower else True # actual precedence check


