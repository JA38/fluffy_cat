print("Hello word")

#과제 1. 별찍기 (4월 20일까지)
print(' 과제1. 별찍기')
for i in range(10,0,-1):
    print('*'*i)

#과제 2. 구구단 2단 
print('\n 과제2. 구구단 2단 출력')
for i in range(1,10):
    print(f'2x{i}={2*i}')

#과제 3. while 문을 활용하여 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보세요.
print('\n 과제3. while문 활용해서 1~1000 중 3의 배수의 합을 구하기')
i = 0
count = 0
while i < 1001:
    if i%3 != 0:
        i += 1
        continue
    i += 1
    count += i
print(count)

#과제 4. for 문을 활용하여 멋사 학생들의 평균 점수를 구해보세요. (4월 20일까지)
print('\n 과제4. for 활용 멋사 학생들 평균점수 구하기')
mutsa_scores = [90, 77, 40, 55, 90, 100, 88]
hap = 0
for score in mutsa_scores:
    hap += score
print(f'멋사 학생들의 평균 점수는 {hap/len(mutsa_scores)}')

# 과제5. input.py
# 파이썬에서 입력을 받는 함수가 있습니다~~ 구글링해서 찾아보세요!
print('/n 과제5. input.py')
print('문제 1. 전화번호 받기')
num = input('전화번호를 입력하세요>>')
print('조건 1. 저장할 때는 공백 문자 없이')
print('조건 2. -, ., , 등이 들어올 때 전부 제외 하고 숫자만 저장!')
num = num.replace('-','')
num = num.replace('.','')
num = num.replace(',','')
num = num.replace(' ','')
print(f'잘 저장되었는지 확인: {num}\n')

print('문제 2. 영어 이름 받기')
print('choi juwon 을 입력 받으면,')
print('first name : Choi, last name: Juwon 이 출력되게 만들기')
name = input("영어이름을 입력하세요>>")
name_split = name.split(' ')
first_name = name_split[0].capitalize()
last_name = name_split[1].capitalize()
print(f'first name:{first_name}, last name:{last_name}')
