import json

"""
class j_variant():
    vnumber = int()
    vtext = str()

    def __init__(self, number):
        self.vnumber = number

    def __init__(self, number, text):
        self.vnumber = number
        self.vtext = text

class j_question():
    qnumber = int()
    qtext = str()
    qball = float()
    vlist = list(j_variant())

    def __init__(self, number):
        self.qnumber = number
        self.vlist.append(j_variant(1))
        self.qball = 1

    def __init__(self, number, text):
        self.qnumber = number
        self.qball = 1
        self.qtext = text
        self.vlist.append(j_variant(1))

    def __init__(self, number, text, ball):
        self.qnumber = number
        self.qball = ball
        self.qtext = text
        self.vlist.append(j_variant(1))
    
    def __init__(self, number, text, ball, variant):
        self.qnumber = number
        self.qball = ball
        self.qtext = text
        self.vlist.append(variant)
    
    def add_variant(self, variant):
        self.vlist.append(variant)


class j_test():
    id = int()
    author_id = int()
    answer_id = int()
    tmin = float()
    tmax = float()
    qlist = list(j_question)

    def __init__(self, id, author_id, answer_id):
        self.id = id
        self.author_id = author_id
        self.answer_id = answer_id
        self.tmin = 0
        self.tmax = 0
        self.qlist.append(j_question(1))

    def make_json(self, ):
        pass

"""

class tmakermanager():

    def make_variant_blank(self):
        variant_blank  = { 
            "vnumber": 1,
            "vtext": "Text for variant" 
        }
        return variant_blank

    def make_variant(self, text):
        variant  = { 
            "vnumber": 1,
            "vtext": text 
        }
        return variant

    def make_question_blank(self):
        question_blank = {
            "qnumber": 1,
            "qtext": "Question text",
            "qball": 1,
            "vlist": []
        }
        question_blank['vlist'].append(self.make_variant_blank())
        return question_blank

    def make_question(self, text, ball = 1):
        question = {
            "qnumber": 1,
            "qtext": text,
            "qball": ball,
            "vlist": []
        }
        return question

    def make_test_blank(self):
        test_blank = {
            "author_id": None,
            "tmin": None,
            "tmax":None,
            "qlist": []
        }
        test_blank['qlist'].append(self.make_question_blank())
        return test_blank

    def get_variant(self, question, number):
        try:
            return question['vlist'][number - 1]
        except IndexError:
            return None

    def get_question(self, test, number):
        try:
            return test['qlist'][number - 1]
        except IndexError:
            return None

    def add_variant_blank(self, question):
        question['vlist'].append(self.make_variant_blank())
        num = len(question['vlist'])
        question['vlist'][num - 1]['vnumber'] = num

    def add_question_blank(self, test):
        test['qlist'].append(self.make_question_blank())
        num = len(test['qlist'])
        test['qlist'][num - 1]['qnumber'] = num

    def clear_variant(self, question, num):
        try:
            question['vlist'].pop(num - 1)
            for i in range(len(question['vlist'])):
                question['qlist'][i]['vnumber'] = i + 1
            return True
        except IndexError:
            return False

    def clear_question(self, test, num):
        try:
            test['qlist'].pop(num - 1)
            for i in range(len(test['qlist'])):
                test['qlist'][i]['qnumber'] = i + 1
            return True
        except IndexError:
            return False

    def add_variant(self, question, text):
        question['vlist'].append(self.make_variant_blank())
        num = len(question['vlist'])
        question['vlist'][num - 1]['vnumber'] = num
        question['qlist'][num - 1]['vtext'] = text

    def add_question(self, test, text, ball = 1):
        test['qlist'].append(self.make_question_blank())
        num = len(test['qlist'])
        test['qlist'][num - 1]['qnumber'] = num
        test['qlist'][num - 1]['qtext'] = text
        test['qlist'][num - 1]['qball'] = ball

    def edit_variant(self, question, variant, num):
        try:
            question['vlist'][num - 1] = variant
            question['vlist'][num - 1]['vnumber'] = num
        except IndexError:
            return False

    def edit_question(self, test, question, num):
        try:
            test['qlist'][num - 1] = question
            test['qlist'][num - 1]['qnumber'] = num
        except IndexError:
            return False

            

    






if __name__ == "__main__":
    tm = tmakermanager()
    ttest = tm.make_test_blank()
    tm.add_question_blank(ttest)
    tm.add_question_blank(ttest)
    tm.add_question(ttest, "Testing Question", ball = 3)
    tm.edit_question(ttest, tm.make_question("Testing Question 2", ball = 5), 2)

    with open("t1.json","w") as write_file: 
        json.dump(ttest, write_file)