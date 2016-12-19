from django.db import models
from .utils import convert_from_base64, add_spaces, check_if_valid_expression, InfixConverterHelpers
from numbers import Number

def decode_and_convert(stringToConvert):
    result = add_spaces(convert_from_base64(stringToConvert))
    check_if_valid_expression(result, helper = InfixConverterHelpers())
    return InfixConverter().string_to_rpn(result, helper = InfixConverterHelpers())	


class InfixConverter():

	def string_to_rpn(self, numbers, helper):
	    stack = []
	    expression = []

	    for val in numbers.split(' '):
	        if val == ')': helper.parentheses_pop_to_expression(stack, expression) # time to pop operators between parantheses
	        elif val in helper.OPERATIONS: 
	            if helper.should_add_to_stack(val, stack): stack.append(val) # add operator to stack if no precedence problems
	            else: helper.pop_stack_until_valid(stack, expression, val) # must pop stack to expression until operator can be added when it does not have precedence 
	        else: expression.append(val) # simply add number directly onto expression	  
	    
	    while len(stack) > 0: expression.append(stack.pop()) # pop remaining operators in stack
	      
	    return ' '.join(expression)
	  
