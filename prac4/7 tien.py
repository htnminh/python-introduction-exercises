import pickle
from shutil import copyfile
copyfile('student_info.pkl', 'updated_info.pkl')

def add_student_info(new_student):
    with open('updated_info.pkl', 'rb') as f:
        a = pickle.load(f)
        check = 0

        if 'id' in new_student.keys():
            for j in range(len(a)):
                if new_student['id'] == a[j]['id']:
                    check = 1
                    break
            if check == 0:
                a.append(new_student)
            else:
                a[j] = new_student


        with open("updated_info.pkl", "wb") as fw:
            pickle.dumps("student_info = ")
            pickle.dump(a,fw)