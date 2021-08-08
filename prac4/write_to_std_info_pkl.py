import pickle as pkl

student_info = [ { 'id': 20200000, 'name': 'Nguyen Van A','score': {'math': 7.8,'english': 8.9,'physics': 9.0,}}, {'id': 20200001,'name': 'Le Van B','score': {'math': 9.8,'english': 8.7,'physics': 7.6}}]

for dictionary in student_info:
    for ele in dictionary:
        print('%5s'%ele,' ', dictionary[ele])
        
with open('student_info.pkl', 'wb') as f:
    pkl.dumps('student_info = ')
    pkl.dump(student_info, f)
