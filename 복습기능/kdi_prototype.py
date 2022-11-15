# 한글자 = 리스트
# 문장 = 이차원리스트 [[글자], [글자],]
# 를 받고, 하나를 클릭하면 다음 글자 / 하나를 클릭하면 전 글자 / 스페이스바를 누르면 그 리스트 부터~ 다시 스페이스바를
# 눌렀을때 까지 의 글자들 리스트 저장해서 하나의 리스트로 옮김.
# time.sleep 넣은 이유 : while True: 가 키보드 입력 시간 동안 여러번 루프를 돌기 때문이다.

import keyboard
import time
import NaverClova


def main():
        """""
        print("저장공간을 지정하세요")

        li = 0
        big_list = ['1_List', '2_List', '3_List']

        list_1 = []
        list_2 = []
        list_3 = []

        print(big_list[li])

        stopper = 1

        while stopper:
                if keyboard.read_key() == "q":
                        li += 1
                        if li > 2:
                                li -= 3
                        print(big_list[li])
                        time.sleep(0.5)
                elif keyboard.read_key() == "e":
                        stopper = 0
                        time.sleep(0.5)
        print(big_list[li], end=' ')
        print('에 저장을 시작합니다.')
        print('')
        """
        # 저장소 분류
        dial_index = 0
        #upper = index / 10  # 대분류 번호(십의 자리)
        #lower = index % 10  # 소분류 번호(일의 자리)
        information_list = [
                [], [], [], [], [], [], [], [], [], [],  # 0~9
                [], [], [], [], [], [], [], [], [], [],  # 10~19
                [], [], [], [], [], [], [], [], [], [],  # 20~29
                [], [], [], [], [], [], [], [], [], [],  # 30~39
                [], [], [], [], [], [], [], [], [], [],  # 40~49
                [], [], [], [], [], [], [], [], [], [],  # 50~59    4  대분류 다이얼  5 소분류 다이얼  0을 다시 눌러서 끝 지정해.
                [], [], [], [], [], [], [], [], [], [],  # 60~69
                [], [], [], [], [], [], [], [], [], [],  # 70~79
                [], [], [], [], [], [], [], [], [], [],  # 80~89
                [], [], [], [], [], [], [], [], [], []  # 90~99
        ]

        # content = input("조작할 내용을 입력하시오 : ")
        #content_list = [['한'], ['글'], ['문'], ['제'], ['출'], ['력'], ['테'], ['스'], ['트']]
        content_list=list(NaverClova.main())[1]
        
        # 사용 설명서
        print('복습기능을 시작합니다.')
        print('###########################')
        print('지정된 키는')
        print('[0] = 저장 시작 / 한번 더 클릭 : 저장 완료') 2 #저장시작 저장완료 다른 스위치(2개)
        print('[1] = 이전 문자')1
        print('[2] = 다음 문자')1
        print('[3] = 임시 저장 내용 출력')
        print('[4] = 큰 다이얼 +')1
        print('[5] = 작은 다이얼 +')1
        print('[6] = 큰 다이얼 -')1
        print('[7] = 작은 다이얼 -')1
        print('[r] = 현재 다이얼 저장 내용 출력')
        print('###########################')
        print('')
        # 현재 인덱스
        now_index = 0

        # 처음 현재 dial을 출력 - 다이얼 출력
        print("현재 다이얼 넘버 = ", end='')
        print(dial_index)

        # 처음 시작 시 첫 문자를 출력
        print("보고있는 글자 = ", end='')
        print(content_list[now_index])
        print('')

        # 인덱스 조작을 위한 초기, 마지막 인덱스 값 / 인덱스의 길이
        length_index = len(content_list)
        init_index = 0
        last_index = length_index - 1

        # 저장 기능을 위한 변수 설정
        save_count = 0
        saved_list = []

        while True:
                # 키를 눌렀을때, 앞으로 가거나 뒤로가라
                key = keyboard.read_key()

                # dial 넘기기
                if key == '4':
                        dial_index += 10
                        dial_index = dial_index - (dial_index % 10)  # 큰 다이얼을 넘기면 대 분류의 가장 첫 번쨰로 넘어가기
                        print("현재 다이얼 넘버 = ", end='')
                        print(dial_index)
                        time.sleep(0.5)
                elif key == '5':
                        dial_index += 1
                        print("현재 다이얼 넘버 = ", end='')
                        print(dial_index)
                        time.sleep(0.5)
                elif key == '6':
                        dial_index -= 10
                        if dial_index < 0:
                                dial_index = 0
                                print('다이얼 넘버가 0입니다')
                        dial_index = dial_index - (dial_index % 10)  # 큰 다이얼을 넘기면 대 분류의 가장 첫 번쨰로 넘어가기
                        print("현재 다이얼 넘버 = ", end='')
                        print(dial_index)
                        time.sleep(0.5)
                elif key == '7':
                        dial_index -= 1
                        if dial_index < 0:
                                dial_index = 0
                                print('다이얼 넘버가 0입니다')
                        print("현재 다이얼 넘버 = ", end='')
                        print(dial_index)
                        time.sleep(0.5)

                # '0'을 눌렀을때 저장 시작 / 다시 한번 누를 시 저장 끝. 및 save_count 초기화
                elif key == '0':
                        save_count += 1

                        if save_count == 1:
                                save_init_index = now_index
                                print('저장 시작 - 현재 문자는 ->', end='')
                                print(content_list[now_index])
                                print('')
                                # 저장 리스트 초기화
                                saved_list = []

                        elif save_count == 2:
                                save_last_index = now_index
                                saved_list = content_list[save_init_index: save_last_index+1]
                                print('저장 완료 - 현재 문자는 ->', end='')
                                print(content_list[now_index])
                                print('')

                                # 큰 리스트에 넣어주기
                                information_list[dial_index].append(saved_list)
                                # 세이브카운트 초기화
                                save_count = 0

                        time.sleep(0.5)

                # 저장 시작이 되지 않고, 1을 눌렀을때
                elif key == "1" and save_count != 1:
                        now_index -= 1

                        # 리스트의 크기 밖 인덱스 숫자가 되면 초기화하라 ex) -1 - > lenth -1 = 리스트의 마지막값
                        if now_index < init_index:
                                now_index += length_index
                                print('----------------------')
                                print(' 문장 마지막으로 돌아갑니다')
                                print('----------------------')
                        elif now_index > last_index:
                                now_index -= length_index
                                print('----------------------')
                                print('문장 처음으로 돌아갑니다')
                                print('----------------------')

                        # 현재 보고있는 문자를 출력
                        print("보고있는 글자 = ", end='')
                        print(content_list[now_index])

                        time.sleep(0.5)

                # '2'을 눌렀을때
                elif key == "2":
                        now_index += 1

                        # 리스트의 크기 밖 인덱스 숫자가 되면 초기화하라 ex) -1 - > lenth -1 = 리스트의 마지막값
                        if now_index < init_index:
                                now_index += length_index
                                print('----------------------')
                                print('문장 마지막으로 돌아갑니다')
                                print('----------------------')
                        elif now_index > last_index:
                                now_index -= length_index
                                print('----------------------')
                                print('문장 처음으로 돌아갑니다')
                                print('----------------------')

                        # 현재 보고있는 문자를 출력
                        print("보고있는 글자 = ", end='')
                        print(content_list[now_index])

                        time.sleep(0.5)

                # '7'을 눌렀을때 저장된 리스트 출력해주기.
                elif key == '3':
                        print(saved_list)
                        time.sleep(0.5)

                # information_list(dial_index)을 출력하라.
                elif key == 'r':
                        print(dial_index, end=' ')
                        print(information_list[dial_index])
                        time.sleep(0.5)

                # 예외처리 : 저장 시작되고 이전 문자로는 못가게 막음
                else:
                        print('')
                        print('저장이 시작되어 이전 문자로 돌아갈 수 없습니다. 재저장하려면 0을 2번 누르시오')
                        print('-> 현재 문자는', end='')
                        print(content_list[now_index], end='')
                        print('입니다.')
                        print('')
                        time.sleep(0.5)

"""""
        # 분류하여 저장 기능55544455545555544445554555562211020222220220r22222255r2r555564222020r
        


        dial_index = 0
        #upper = index / 10  # 대분류 번호(십의 자리)
        #lower = index % 10  # 소분류 번호(일의 자리)
        information_list = [
                [], [], [], [], [], [], [], [], [], []  # 0~9
                [], [], [], [], [], [], [], [], [], []  # 10~19
                [], [], [], [], [], [], [], [], [], []  # 20~29
                [], [], [], [], [], [], [], [], [], []  # 30~39
                [], [], [], [], [], [], [], [], [], []  # 40~49
                [], [], [], [], [], [], [], [], [], []  # 50~59    4  대분류 다이얼  5 소분류 다이얼  0을 다시 눌러서 끝 지정해.  
                [], [], [], [], [], [], [], [], [], []  # 60~69    
                [], [], [], [], [], [], [], [], [], []  # 70~79
                [], [], [], [], [], [], [], [], [], []  # 80~89
                [], [], [], [], [], [], [], [], [], []  # 90~99

        ]
        #saved list에 원하는 내용이 담겨져 있는 상태. 이걸 어떻게 저기에 넣을거냐
        #dial 넘기기
        if key=='4':
                dial_index+=10
                dial_index=int((dial_index%100)/10) #큰 다이얼을 넘기면 대 분류의 가장 첫 번쨰로 넘어가기
        elif key=='5': dial_index+=1

        #dila index의 저장소에 정보 저장하기
        information_list[dial_index]=saved_list


        #어떻게 다시 꺼내쓸거냐
        printI(information_list(dial_index))
"""

if __name__ == '__main__':
        main()
