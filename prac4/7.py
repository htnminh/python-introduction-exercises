import pickle as pkl
from shutil import copyfile
copyfile('student_info.pkl', 'updated_info.pkl')

def add_student_info(new_student):
    with open('updated_info.pkl', 'rb') as f:
        check_done = False
        student_info = pkl.load(f)
        
        if 'id' in new_student.keys():
            for i in range(len(student_info)):
                if new_student['id'] == student_info[i]['id']:
                    check_done = True
                    break
            if check_done == False:
                student_info.append(new_student)
            else:
                student_info[i] = new_student
        with open('updated_info.pkl', 'wb') as f1:
            pkl.dumps('student_info = ')
            pkl.dump(student_info, f1)

# replace = ok
# add = ok
# nothing replace = ok
# nothing add = ok

'''
new_student = {
        #'id': 2020,
        'name': 'a',
        'score': {
            'math': 7.8,
            'english': 8.4,
            'physics': 8.0,
        }
    }
add_student_info(new_student)
new_student = {}
'''