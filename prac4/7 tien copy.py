import pickle
from shutil import copyfile
copyfile('student_info.pkl', 'updated_info.pkl')

def add_student_info(new_student):
    with open('updated_info.pkl', 'rb') as f:
        student_info = pickle.load(f)
        check = False

        if 'id' in new_student.keys():
            for j in range(len(student_info)):
                if new_student['id'] == student_info[j]['id']:
                    check = True
                    break
            if check == False:
                student_info.append(new_student)
            else:
                student_info[j] = new_student


        with open("updated_info.pkl", "wb") as fw:
            pickle.dumps("student_info = ")
            pickle.dump(student_info,fw)
