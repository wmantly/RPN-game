import random
class User:
	def __init__(self,name_given):
		self.name = name_given
		# maybe score should be here

class DB:
	def __init__(self,db_name):
		self.db_name = db_name+".db"
	
	def create_user(self):
		pass
	def update_user_stats(self):
		pass

class RPN:
    def __init__(self, operatorLimit, numberLimit, lengthLimit):
        self.expression = self.generate_expression(operatorLimit, numberLimit, lengthLimit)
        self.solution = self.generate_solution(self.expression)

    def chooseRandom(operatorLimit,numberLimit):
        Operators = ["+","-","*"] # "/"
        chosenOperator = Operators[random.randint(0,operatorLimit)]
        chosenFirstNumber = str(random.randint(1,numberLimit))
        chosenSecondNumber = str(random.randint(1,numberLimit))
        return chosenOperator, chosenFirstNumber, chosenSecondNumber

    # broken
    def generate_solution(self, expression):
        x = 0
        ops = ["+", "-", "*"] # "\", "mod"
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
        chosenLength = random.randint(1,lengthLimit)
        TestString = []
        length = 0
        difficulty = 0 

        while length < chosenLength:
            currentOperator, currentFirstNumber, currentSecondNumber = RPN.chooseRandom(operatorLimit, numberLimit)
            if length == 0:
                TestString.append(currentFirstNumber)
                TestString.append(currentSecondNumber)
                TestString.append(currentOperator)
            else:
                TestString.append(currentFirstNumber)
                TestString.append(currentOperator)
            length += 1
        
        return TestString

    def compare_user_answer(self, user_answer):
        pass

# test 
rpn = RPN(2,10, 7)
print(rpn.expression)
