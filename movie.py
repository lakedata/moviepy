#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#상영영화검색서비스
Movies  = [{"제목":"Spider Man", "감독":"존 왓츠", "제작사":"마블", "주인공":"톰홀랜드", "개봉년도":"2021"},
           {"제목":"Dune", "감독":"드니 빌뇌브", "제작사":"워너 브라더스", "주인공":"티모시 샬라메", "개봉년도":"2021"},
           {"제목":"Parasite", "감독":"봉준호", "제작사":" 바른손이앤에이", "주인공":"송강호", "개봉년도":"2019"},
           {"제목":"Matric", "감독":"워쇼스키", "제작사":"실버 픽쳐스", "주인공":"리브스", "개봉년도":"1999"},
           {"제목":"Home Alone", "감독":"크리스 콜롬버스", "제작사":"고치", " 주인공 ":"맥컬린 컬킨", "개봉년도":"1990"}] #Movies 안에 영화제목, 감독, 제작사 등 영화정보 입력
           
keyword = {'1':'제목', '2':'감독', '3':'제작사'}    #keyword 변수에 제목, 감독, 제작사에 각각 key 부여

def inputSearchKeyword():                          #key 유무 확인          
    while(True):
        key = input("영화 검색 키워드\n  1.영화명\n  2.감독명\n  3.제작사명\n선택(1,2,3) : ")
        if key == '1' or key =='2' or key == '3':  #key값 검사
            return key
        else:
            print("1, 2, 3 중 하나로 입력해주세요.\n")   

            
def inputSearchWord(key):                           #함수 keyword의 값과 일치하는지 확인
    return input('{} >>> '.format(keyword.get(key))) #>>>사용자가 입력한 값을 어떤 변수에 대입하고 싶을 때
                                                     #format()함수는 문자열을 출력할때 서식 지정자를 사용하여 출력하고자할때
                                                     #get함수를 이용하여 keyword딕셔너리에 key 이용해 찾기

def findMovies(searchKeyword):
    matchList = []
    for idx, val in enumerate(Movies):                 #enumerate 내장되어 있는 순서가 있는 자료형 값과 값을 열거함.
        if searchKeyword == val.get(keyword.get(key)): #Value를 호출함
            matchList.append(idx)                      #리스트에 새로운 원소를 추가
    
    return matchList


import re

lowerCase = re.compile('[a-z]')  #re.compile을 사용하여 정규 표현식을 컴파일

def lowerToUpper(word):          #소문자로 입력해도 대문자로 인식하기
    temp = ''
    for each in word:
        if lowerCase.search(each):
            each = each.upper()

        temp += each

    return temp



def printResult(findResult):       #결과출력
    for target in findResult:
        print("\n제 목: {}\n감 독: {}\n제작사: {}\n주인공: {}".format(Movies[target].get('제목'),
                                 Movies[target].get('감독'),
                                 Movies[target].get('제작사'),
                                 Movies[target].get('주인공')))

# 실행로직
key = inputSearchKeyword()
search = inputSearchWord(key)
refinedSearch = search
findResult = findMovies(refinedSearch)
printResult(findResult) if findResult != [] else print("\n검색한 영화가 없습니다.")


#영화예매서비스
from datetime import datetime#날짜 관련 라이브러리 임포트하기
def getCurrent() :
    curDate = datetime.today() #현재 날짜 및 시간을 구함
    return curDate

nowDate = None
nowDate = getCurrent()
print("\n오늘의 예매 날짜는 ", nowDate, "입니다")

seat=["○","○","○","○","○","○","○","○"] #○를 빈 좌석으로 표시함
Number=[]
movies = ["Spider Man", "Dune", "Parasite", "Matrix", "Home Alone"] #movie 안에 리스트타입으로 영화이름 입력
print()
print("===========영화 목록===========") #영화목록을 출력하기 위해 for문을 사용,item이라는 변수에 movie의 값을 하나씩 넣어서 출력

for item in movies:
    print(item)
print("==============================")
print("예매하실 영화를 선택해주세요 :")
choice = input()                        #choice 라는 변수에 input을 사용해서 영화제목을 입력받기
while choice not in movies:             #while문의 반복조건으로 입력한 값이 movie 안에 있는 지를 물어보기
    print('예매할 수 없는 영화입니다.')  #만약 없다면 While이 실행, 있다면 while 실행하지 않음
    choice = input()
print("예매하실 영화 :",choice,"를 선택하셨습니다.")
check = False                  #인원수를 체크하기 위해 check라는 변수를 만들어 false를 넣기
while(not check): 
    print("관람 인원 수 입력:")
    people = int(input())      #people에 input()을 사용하여 인원수 입력, int()를 사용해 숫자로 변환시키기
    if people < 1 :
        print("관람 인원 수는 양수만 가능합니다.")
    else:
        print("관람할 인원수는 %d명 입니다."%people)
        check=True
                 
i = 1
while  (i <= people):
    print(i,"번째 좌석을 선택하세요(1-8번)")
    print("현재좌석:",seat)
    select=int(input())
    if select >=1 and select <=8:
        if seat[select-1]=="●":           #예약된 좌석은 ●로 표시함
            print("이미 예약된 좌석이니, 다른 좌석을 선택하세요") # 선택한 좌석이 이미 예약된 좌석이면 선택이 되지않음
        else:
            seat[select-1]="●"
            print(select,"번 좌석이 예약되었습니다")
            print("현재좌석:", seat,"\n")
            Number.append(select)
            
            if i == people:
                print("좌석예약을 종료합니다.")             #예약이 끝나면, 총 금액과 예약한 좌석을 출력함
 
                break
            i += 1
                
    else:
        print("1-8번 좌석 중 선택하세요!!")
        continue
        
coupon_dic = {'WELCOME':2000, 'VALENTINE':3000, 'CHRISTMAS':4000, 'INDEPENDENCE':5000}
process = True                #coupon_dic에 쿠폰 정보를 입력하고, process라는 변수에 True를 넣어 While문을 계속할지 빠져나갈지 결정하기
print("할인권을 사용하시려면 y, 금액 확인으로 넘어가시려면 n을 입력해주세요:")
usage = input()               #usage에 input()으로 쿠폰 사용 여부를 묻고, while문 안에는 사용하는 경우(usage=='y')와 사용하지 않는 경우 (usage=='n')
while process:
    if usage=='y':
        coupon = input("쿠폰코드를 입력해주세요 :")  
        if coupon in coupon_dic:
            sale = coupon_dic[coupon]
            print('%d원 할인됩니다.'%sale)
            break
        else:
            print('존재하지 않는 할인권입니다.')
    elif usage=='n':
        sale = 0
        print('할인권을 사용하지 않았습니다.')   #만약 쿠폰을 사용하지 않으면 sale에 0을 넣고, 할인권을 사용하지 않는다는 안내와 함께 while 빠져나가기
        break
    else:
        usage = input('잘못된 입력입니다. 다시 입력해주세요:')
origin_price = 12000                          # 가격계산하기 기본요금 12000원, 할인가격 sale이고, 총 가격은 기본요금에서 할인가를 빼고 인원수만큼 곱하기
sale_price = sale
total_price = (origin_price-sale_price)*people

class Print :
    Cho = "" #영화 제목
    xPeo = 0 #관람 인원
    Oprice = 0#합산 금액
    Sprice = 0 #할인 금액
    Tprice = 0 #실 결제액
    
    def to(self, Cho, xPeo, Oprice, Sprice, Tprice) :
        self.Cho = Cho
        self.xPeo = xPeo
        self.Oprice = Oprice
        self.Sprice = Sprice
        self.Tprice = Tprice
    
    def __del__(self) : #__del__()메소드 :객체가 제거될때 자동호출
        print("")
        print("<예매 상세 내역>")
        print("==============================")
        print('영화 제목 : %s'%self.Cho)
        print('관람 인원 : %d명'%self.xPeo)
        print('합산 금액 : %d원'%self.Oprice)
        print('할인 금액 : %d원'%self.Sprice)
        print("------------------------------")
        print('실 결제액 : %d원'%self.Tprice)
        print("==============================")
        
print = Print() #클래스이름이 Print인 객체 생성
print.to(choice, people, origin_price, sale_price, total_price) #속성대입
del(print)


# In[ ]:




