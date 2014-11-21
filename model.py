import random
class User:
	def __init__(self,name_given):
		self.name = name_given
		# maybe score should be here

class DB:
	def __init__(self,db_name):
		self.db_name = db_name+"db"
	
	def create_user(self):
		pass
	def update_user_stats(self):
		pass

class RPN:
	def __init__(self):
		self.equation = ""
		self.answer_equation = ""
		self.User_answer = ""

	def chooseRandom(self,operatorLimit,numberLimit):
		Operators = ["+","-","*","/"]
		chosenOperator = Operators[random.randint(0,operatorLimit)]
		chosenFirstNumber = str(random.randint(1,numberLimit))
		chosenSecondNumber = str(random.randint(1,numberLimit))
		return chosenOperator, chosenFirstNumber, chosenSecondNumber

	# broken
	@staticmethod
	def answer_equation(equation):
		x = 0
		ops = ["+", "-", "*"] # "\", "mod"
		stack = []
		while x < len(equation):
			if not equation[x] in ops:
				stack.append(equation[x])
			else:
				y = stack.pop()
				stringy = stack.pop() + equation[x] + y
				stack.append(str(eval(stringy)))
			x += 1
		return (stack[0])


	def generate_equation(self,operatorLimit,numberLimit,lengthLimit):
		chosenLength = random.randint(1,lengthLimit)
		TestString = []
		length = 0

		while length < chosenLength:
			currentOperator, currentFirstNumber, currentSecondNumber = self.chooseRandom(operatorLimit,numberLimit)
			if length == 0:
				TestString.append(currentFirstNumber)
				TestString.append(currentSecondNumber)
				TestString.append(currentOperator)
			else:
				TestString.append(currentFirstNumber)
				TestString.append(currentOperator)
			length += 1
		return TestString

	def compare_user_answer(self,user_answer):
		pass

# test 

# if __name__ == '__main__':
# 	rpn = RPN()
# 	eq = rpn.generate_equation(2,10,5)
# 	print(eq)
# 	rpn.answer_equation([])
