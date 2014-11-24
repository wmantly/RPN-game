import random 

class RPN:
    def __init__(self, operatorLimit, numberLimit, lengthLimit):
        self.expression = self.generate_expression(operatorLimit, numberLimit, lengthLimit)
        # self.solution = self.generate_solution(self.expression)

    # def chooseRandom(operatorLimit,numberLimit):
    #     Operators = ["+","-","*"] # "/"
    #     chosenOperator = Operators[random.randint(0,operatorLimit)]
    #     chosenFirstNumber = str(random.randint(1,numberLimit))
    #     chosenSecondNumber = str(random.randint(1,numberLimit))
    #     return chosenOperator, chosenFirstNumber, chosenSecondNumber

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
        unshuffled = []
        final = []
        for i in range(0, lengthLimit):
            these_operators.append(ops[random.randint(0,operatorLimit)])
        numbers.append(random.randint(0, numberLimit))
        for i in range(0, lengthLimit):
            numbers.append(random.randint(0, numberLimit))
        final.append(numbers.pop(0))
        final.append(numbers.pop(0))
        numberCount = 1
        #here need to add a number or operator, randomly.... need numbers always one more than operators

        final = final + unshuffled
        for i in final:
            i = str(i)
        return final




        # chosenLength = random.randint(1,lengthLimit)
        # TestString = []
        # length = 0
        # difficulty = 0 

        # while length < chosenLength:
        #     currentOperator, currentFirstNumber, currentSecondNumber = RPN.chooseRandom(operatorLimit, numberLimit)
        #     if length == 0:
        #         TestString.append(currentFirstNumber)
        #         TestString.append(currentSecondNumber)
        #         TestString.append(currentOperator)
        #     else:
        #         TestString.append(currentFirstNumber)
        #         TestString.append(currentOperator)
        #     length += 1
        
        # return TestString

rpn = RPN(1,10, 4)
print(rpn.expression)
# answer = rpn.solution
# print(answer)