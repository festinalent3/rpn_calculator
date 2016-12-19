from infix_converter.models import decode_and_convert
import operator

def calculate(string):
    try:
        numbers = decode_and_convert(string)
        return RpnCalculator().calculator(numbers)
    except Exception as e:
        raise e

class RpnCalculator():

    def calculator(self, expression):
        OPS = { "+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul }
        stack = []

        for val in expression.split(' '):
            try:
                if val in OPS: self.perform_calculation(stack, val, OPS) # time to perform an actual calculation
                else: stack.append(float(val)) # add number to the stack
            except ZeroDivisionError:
                raise ZeroDivisionError("You're not Chuck Norris... can't divide by zero.")
    
        return stack.pop() #answer is now last value in stack


    def perform_calculation(self, stack, val, OPS):
        val1 = stack.pop() 
        val2 = stack.pop()
        stack.append(OPS[val](val2, val1)) #perform the calculation and add to stack
        
