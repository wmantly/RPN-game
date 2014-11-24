import random 

class RPN:
    def __init__(self, operatorLimit, numberLimit, lengthLimit):
        self.expression = self.generate_expression(operatorLimit, numberLimit, lengthLimit)
        self.solution = self.generate_solution(self.expression)

    def generate_solution(self, expression):
        x = 0
        ops = ["+", "-", "*"] # "\", "%"
        stack = []
        while x < len(expression):
            if not expression[x] in ops:
                stack.append(expression[x])
            else:
                y = stack.pop()
                stringy = stack.pop() + expression[x] + y
                stack.append(str(eval(stringy)))
            x += 1
        return (stack[0])


    def generate_expression(self, operatorLimit, numberLimit, lengthLimit):
        ops = ["+", "-", "*"] # "\", "%"
        numbers = []
        these_operators = []
        final = []
        for i in range(0, lengthLimit):
            these_operators.append(ops[random.randint(0,operatorLimit)])
            numbers.append(random.randint(1, numberLimit))            
        numbers.append(random.randint(0, numberLimit))
        final.append(str(numbers.pop()))
        final.append(str(numbers.pop()))
        numberCount = 1
        get_shuffled = numbers + these_operators
        random.shuffle(get_shuffled)
        print(get_shuffled)
        for i in get_shuffled:
            if numberCount == 0 and type(i) == str:
                get_shuffled.append(i)
            elif numberCount > 0 and type(i) == str:
                final.append(i)
                numberCount -= 1
            else:
                final.append(str(i))
                numberCount += 1
        return final