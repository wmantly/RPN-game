import random
import sqlite3

defaultdb = "rpngame.db"

class User:
    def __init__(self,name_given,user_id):
        self.name = name_given
        self.user_id = user_id

class DB:
    def __init__(self):
        self.db_name = defaultdb
        self.sesh_id = None

    # please use number for pins
    def create_user(self,name,pin):
        conn = sqlite3.connect(self.db_name)
        c  = conn.cursor() 
        c.execute("INSERT INTO user(name,pin)VALUES (?,?)",(name,pin))
        cursor = sqlite3.execute('SELECT max(id) FROM user')
        last_inserted_user = cursor.fetchone()
        conn.commit()
        c.close()
        return last_inserted_user
    
    def update_user_stats(self):
        pass

    def fetch_user(self,name,pin):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT name,id FROM user WHERE user.pin=(?) and user.name=(?)",(pin,name))
        try:
            user_data = c.fetchall()[0]
            user = User(user_data[0],user_data[1])
            conn.commit()
            c.close()
            return user
        except IndexError:
            return False

    # inorder for this code to work this needs the session id
    def save_turn(self,turn_obj):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("INSERT INTO turns VALUES(?,?,?,?)",(self.sesh_id,turn_obj.difficulty_lvl,turn_obj.correct_incorrect,turn_obj.time_taken))
        conn.comit()
        c.close()

    def save_sesh(self, user_id):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()        
        c.execute("INSERT INTO sessions VALUES(?)",(user_id))
        conn.commit()
        c.close()        
        self.sesh_id = c.lastrowid


class Turns:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.difficulty_lvl = 1
        self.correct_incorrect = None 
        self.time_taken = None
        self.rpn = RPN(1, 10, 7)

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
# rpn = RPN(1,10, 7)
# print(rpn.expression)
# print(rpn.generate_solution)
