# import pickle
 
# name = 'james'
# age = 17
# address = '서울시 서초구 반포동'
# scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}
 
# with open('james.p', 'wb') as file:    # hello.txt 파일을 바이너리 쓰기 모드(wb)로 열기
#     pickle.dump(name, file)
#     pickle.dump(age, file)
#     pickle.dump(address, file)
#     pickle.dump(scores, file)





# with open('james.p', 'rb') as file:    # hello.txt 파일을 바이너리 읽기 모드(rb)로 열기
#     name = pickle.load(file)
#     age = pickle.load(file)
#     address = pickle.load(file)
#     scores = pickle.load(file)
#     print(name)
#     print(age)
#     print(address)
#     print(scores)


with open ('words.txt', 'w') as file:
    file.write('Fortunately, however, for the reputation of Asteroid B-612, a Turkish dictator made a law that his subjects, under pain of death, should change to European costume. So in 1920 the astronomer gave his demonstration all over again, dressed with impressive style and elegance. And this time everybody accepted his report.')

with open ('words.txt', 'r') as file:
    a = (file.read()).split()

for i in a:
    if "c" in i:
        print(i.strip(',.'))



