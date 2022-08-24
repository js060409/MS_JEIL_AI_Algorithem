##  22학년도 AI 알고리즘 동아리 랜덤 추첨 프로그램 

def random_num():
    import random

    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    num_3 = random.randint(1, 10)

    print('추첨 번호:', num_1 , num_2, num_3)

def auto_num():
    import random

    class_number = input('학번을 입력해주세요')

    print('자동 번호 선택을 시작합니다. ')

    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    num_3 = random.randint(1, 10)
    
    print(class_number,'의 자동 선택된 번호:\n' ,num_1, num_2, num_3)

answer = input('어떤 기능을 사용하시겠습니까? (A = 번호 추첨) , (B = 번호 자동 선택)')

if answer == 'A':

    random_num()

elif answer == 'B':

    auto_num()

