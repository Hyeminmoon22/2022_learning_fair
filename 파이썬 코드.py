num = 1
while(num==1):
    print('그린스마트시티학과 여러분, 식물학퀴즈에 온 걸 환영해요!')
    print("총 세 파트의 퀴즈를 진행할 것입니다!!")
    plant = int(input('1.교목, 2.관목, 3.만경목 (퀴즈를 시작하려면 1을 눌러주세요.) : '))

    if(plant==1):
        print("")
        print("문제1. 교목의 정의는 무엇일까요?")
        dap=input()
        print("수고했어요! 첫 문제였으니까  조금 더 확실한 정의를 알려줄게요!")
        print("교목이란 줄기가 곧고 굵으며 높이가 8m를 넘는 나무이면 수간과 가지의 구별이 뚜렷하고, 수간이 1개이고, 가치 밑부분까지의 수간 길이가 큰 나무입니다.")
        print("")
        print("다음문제부터 달려볼까요?")
        
        number=0
        while True:
            print("문제2. 느티나무의 성상은 무엇일까요?")
            print("1. 상록침엽수")
            print("2. 낙엽활엽수")
            print("3. 상록활엽수")
            print("4. 낙엽만경목")

            number=int(input("정답 :"))
            if number!=2:
                print("틀렸습니다")
            else:
                number==2
                break
        print("정답입니다.")
        print("")
        
        prompt="""
문제3. 느티나무의 용도 및 목적은 무엇일까요?
1. 녹음용
2. 방지용
3. 차폐용
4. 방화용
        """

        number=0
        while True:
            print(prompt)
            number=int(input("정답 :"))
            if number!=1:
                print("틀렸습니다")
            else:
                number==1
                break
        print("정답입니다.")
        print("")
        
        prompt="""
문제4. 소나무의 성상은 무엇일까요?
1. 상록침엽수
2. 낙엽활엽수
3. 상록활연수
4. 낙엽만경목
        """

        number=0
        while True:
            print(prompt)
            number=int(input("정답 :"))
            if number!=1:
                print("틀렸습니다")
            else:
                number==1
                break
        print("정답입니다.")
        print("")

        prompt="""
문제5. 소나무의 개화시기는 언제일까요?
1. 4월
2. 7월
3. 5월
4. 10월
        """
        number=0
        while True:
            print(prompt)
            number=int(input("정답 :"))
            if number!=3:
                print("틀렸습니다")
            else:
                number==3
                break
        print("정답입니다.")
        print("")
     
        prompt="""
문제6. 소나무 잎의 모양은 무엇일까요?
1. 침형
2. 선형
3. 난형
4. 광타원형
        """

        number=0
        while True:
            print(prompt)
            number=int(input("정답 :"))
            if number!=1:
                print("틀렸습니다")
            else:
                number==1
                break
        print("정답입니다.")
        print("")

        prompt="""
문제7. 은행나무의 성상은 무엇일까요?
1. 낙엽침엽수
2. 낙엽활엽수
3. 상록침엽수
4. 상록활엽수
        """

        number=0
        while True:
            print(prompt)
            number=int(input("정답 :"))
            if number!=1:
             print("틀렸습니다")
            else:
                number==1
                break 
        print("정답입니다.")
        print("")

        prompt="""
문제8. 은행나무의 용도는 무엇일까요?
1. 녹음용
2. 차폐용
3. 방풍용
4. 방화용
        """

        number=0
        while True:
            print(prompt)
            number=int(input("정답 :"))
            if number!=4:
                print("틀렸습니다")
            else:
                number==4
                break
        print("정답입니다.")
        print("")

        prompt="""
문제9. 은행나무 잎의 모양은 무엇일까요?
1. 심장형
2. 타원형
3. 부채꼴형
4. 관통형
        """

        number=0
        while True:
            print(prompt)
            number=int(input("정답 :"))
            if number!=3:
                print("틀렸습니다")
            else:
                number==3
                break
        print("정답입니다.")
        print("")

        print("교목 파트는 이제 끄읕~~ 수고 많았어요! 기초가 탄탄해지는 느낌이 들죠??")

        print("이제 관목 파트로 넘어갈거에요! 다들 준비 됐지요??")
        print("관목 문제는 문제수가 더 적으니 파이팅!!")
        print("렛츠고~~~")

        prompt="""
문제10. 개나리의 성상은?
1. 상록침엽수
2. 낙엽활엽수
3. 상록활엽수
4. 낙엽만경목
        """

        number=0
        while True:
            print(prompt)
            number=int(input("정답 :"))
            if number!=2:
                print("틀렸습니다. 다시 시도해보세요")
            else:
                number==2
                break
        print("정답입니다.")

        prompt="""
문제11. 개나리가 자주 쓰이는 용도는 무엇일까요?
1. 녹음용
2. 방화용
3. 방연용
4. 차폐용
        """

        number=0
        while True:
            print(prompt)
            number=int(input("정답 :"))
            if number!=4:
                print("틀렸습니다")
            else:
                number==4
                break
        print("정답입니다.")
        print("")

        prompt="""
문제12. 회양목의 성상은?
1. 상록침엽수
2. 낙엽활엽수
3. 낙엽침엽수
4. 상록활엽수
        """

        number=0
        while True:
            print(prompt)
            number=int(input("정답 :"))
            if number!=4:
                print("틀렸습니다")
            else:
                number==4
                break
        print("정답입니다.")
        print("")

        prompt="""
문제13. 회양목의 잎차례는?
1. 대생
2. 호생
3. 윤생
4. 근생
        """

        number=0
        while True:
            print(prompt)
            number=int(input("정답 :"))
            if number!=1:
                print("틀렸습니다")
            else:
                number==1
                break
        print("정답입니다.")
        print("")

        prompt="""
문제14.회양목 열매종류는은?
1. 시과
2. 협과
3. 핵과
4. 삭과
        """

        number=0
        while True:
            print(prompt)
            number=int(input("정답 :"))
            if number!=4:
                print("틀렸습니다")
            else:
                number==4
                break
        print("정답입니다.")
        print("")

        print("와우")
        print("이정도면 교목과 관목은 거의 마스터 수준! 마지막으로 만경목 퀴즈까지 고고~!")
        print("문제 시작 ~~~~~~")


        prompt="""
문제15. 송악의 성상은은?
1. 상록활엽수
2. 낙엽활엽수
3. 상록칩엽수
4. 낙엽침엽수
        """

        number=0
        while True:
            print(prompt)
            number=int(input("정답 :"))
            if number!=1:
                print("틀렸습니다")
            else:
                number==1
                break
        print("정답입니다.")
        print("")

    
        prompt="""
문제16. 송악의 개화시기는?
1. 12월
2. 10월 ~ 11월
3. 1월 ~ 2월
4. 7월
        """

        number=0
        while True:
            print(prompt)
            number=int(input("정답 :"))
            if number!=2:
                print("틀렸습니다")
            else:
                number==2
            break
        print("정답입니다.")
        print("")
        print("")
        
        
        prompt="""
문제17. 송악의 잎의 형태는은?
1. 도피침형
2. 광타원형
3. 능형
4. 난형
        """

        number=0
        while True:
            print(prompt)
            number=int(input("정답 :"))
            if number!=4:
                print("틀렸습니다")
            else:
                number==4
                break
        print("정답입니다.")
        print("")

        prompt="""
문제18. 줄사철의 성상은?
1. 상록침엽수
2. 상록활엽수
3. 낙엽침엽수
4. 낙엽활엽수
        """

        number=0
        while True:
            print(prompt)
            number=int(input("정답 :"))
            if number!=2:
                print("틀렸습니다")
            else:
                number==2
                break
        print("정답입니다.")
        print("")

        prompt="""
문제19.줄사철의 꽃차례는?
1. 취산화서
2. 산형화서
3. 총상화서
4. 산방화서
        """

        number=0
        while True:
            print(prompt)
            number=int(input("정답 :"))
            if number!=1:
                print("틀렸습니다")
            else:
                number==1
                break
        print("정답입니다.")
        print("")


        prompt="""
문제20. 담쟁이덩굴의 열매종류는?
1. 시과
2. 협과
3. 장과
4. 수과
        """

        number=0
        while True:
            print(prompt)
            number=int(input("정답 :"))
            if number!=3:
                print("틀렸습니다")
            else:
                number==3
                break
        print("정답입니다.")
        print("")

        prompt="""
문제21.담쟁이덩굴의 잎차례는?
1. 호생
2. 대생
3. 윤생
4. 근생
        """

        number=0
        while True:
            print(prompt)
            number=int(input("정답 :"))
            if number!=1:
                print("틀렸습니다")
            else:
                number==1
                break
        print("정답입니다.")
        print("")

        prompt="""
문제22.담쟁이덩굴의 용도는?
1. 녹음용
2. 방화용
3. 차폐용
4. 벽면녹화
        """

        number=0
        while True:
            print(prompt)
            number=int(input("정답 :"))
            if number!=4:
                print("틀렸습니다")
            else:
                number==4
                break
            
        print("정답입니다.")
       
        print("")
        
        oxquiz = 0
        guess = input('송악은 주로 해안이나 도서지방의 숲속 등의 지역에서 서식한다 : ')
        guess = int(guess)
        if guess != oxquiz:
            print ( '틀렸습니다!')
        if guess == oxquiz:
            print ( '맞추셨습니다!')

        print("")
        print("마지막 0,X 퀴즈에요 !!")

        oxquiz = 0
        guess = input('담쟁이덩굴은 주로 냉온대 ~ 난온대의 기후에서 서식한다 : ')
        guess = int(guess)
        if guess != oxquiz:
            print ( '틀렸습니다!')
        if guess == oxquiz:
            print ( '맞추셨습니다!')
        print("정말 수고 많았어요 ! 식물학 전공 기초 퀴즈 테스트는 여기까지에요!")
        print("")
        

        print("")
        
        print("어떠셨나요?? 자신의 수준을 확인해보셨나요??")
        print("다음번에는 다른 파트의 심화 문제로 만든 게임으로 돌아올게요 ㅎㅎ")
        print("그때까지 으쌰으쌰 공부 파이팅 해요 ! 수고했어요!~~~!")
    break
