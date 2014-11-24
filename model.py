import random
import sqlite3
import hashlib
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
        c.execute("SELECT * FROM user WHERE name LIKE (?)",(name,))
        result = c.fetchall()
        if(len(result)==0):
            pin = hashlib.md5( pin)
            c.execute("INSERT INTO user(name,pin) VALUES (?,?)",(name,pin.hexdigest()))
            c.execute('SELECT max(id) FROM user')
            max_id = c.fetchall()
            c.execute("SELECT * FROM user WHERE user.id = (?)", (max_id[0]))
            this_row = c.fetchall()
            last_inserted_user = User(this_row[0][1], this_row[0][0])
            conn.commit()
            c.close()
            return last_inserted_user
        else:
            conn.commit()
            c.close()
            return False
 
    def fetch_user(self,name,pin):
        pin = hashlib.md5( pin)
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT name,id FROM user WHERE user.pin=(?) and user.name=(?)",(pin.hexdigest(),name))
        try:
            user_data = c.fetchall()[0]
            user = User(user_data[0],user_data[1])
            conn.commit()
            c.close()
            return user
        except IndexError:
            conn.commit()
            c.close()
            return False

    # inorder for this code to work this needs the session id
    def save_turn(self,turn_obj):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("INSERT INTO turns ('session_id', 'difficulty_lvl', 'correct_incorrect', 'time_taken') VALUES(?,?,?,?)",(self.sesh_id,turn_obj.difficulty_lvl,turn_obj.correct_incorrect,turn_obj.time_taken))
        conn.commit()
        c.close()

    def save_sesh(self, user_id):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()        
        c.execute("INSERT INTO sessions ('user_id') VALUES(?)",(user_id,))
        self.sesh_id = c.lastrowid
        conn.commit()
        c.close()        

    def get_high(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT * FROM user ORDER BY name ASC")
        these_users = c.fetchall()
        return these_users        


class Turns:
    def __init__(self, difficulty):
        self.start_time = None
        self.end_time = None
        self.difficulty_lvl = difficulty
        self.correct_incorrect = None 
        self.time_taken = None
        self.rpn = RPN(1, 10, difficulty + 2) if difficulty < 5 else RPN(2, 10, difficulty + 2)

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
        numbers.append(random.randint(1, numberLimit))
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

