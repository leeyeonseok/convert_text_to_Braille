# 한글자 = 리스트
# 문장 = 이차원리스트 [[글자], [글자],]
# 를 받고, 하나를 클릭하면 다음 글자 / 하나를 클릭하면 전 글자 / 스페이스바를 누르면 그 리스트 부터~ 다시 스페이스바를
# 눌렀을때 까지 의 글자들 리스트 저장해서 하나의 리스트로 옮김.
# time.sleep 넣은 이유 : while True: 가 키보드 입력 시간 동안 여러번 루프를 돌기 때문이다.

#state는 24개 단위로 끊어진 1중 리스트다 .즉, state는 한 글자의 쉬프트 레지스터용 전달 신호다.states는 state로 이루어진 이중리스트다. 즉 states는 Plus의 점자 결과를 쉬프트레지스터용 입력 신호로 바꾼 것들의 집합이다.

import RPi.GPIO as gpio
import keyboard
import time
import NaverClova
import Plus
import Resgister

def main():

    ####gpio 세팅###
    gpio.setwarnings(False)

    pin_data = 14
    pin_clock = 18
    pin_latch = 15
    pin_clear = 2

    gpio.setmode(gpio.BCM)

    gpio.setup(pin_data, gpio.OUT)
    gpio.setup(pin_clock, gpio.OUT)
    gpio.setup(pin_latch, gpio.OUT)
    gpio.setup(pin_clear, gpio.OUT)

    gpio.output(pin_clear, True)
    ##### pin 세팅####
    Next_word=20



    def Make_state_list(lst):  # 24개 단위로 리스트 나누기
        state = [lst[i:i + 24] for i in range(0, len(lst), 24)]
        return state

    def Make_states(lst):  # Plus의 이중 리스트의 결과를 받아서 1중 리스트로 바꿔주는 함수.
        lst.reverse()
        states = []
        for braille in lst:
            # print(braille)
            braille.extend([0, 0])
            states.extend(braille)
        return states


    # 저장소 분류
    dial_index = 0
    # upper = index / 10  # 대분류 번호(십의 자리)
    # lower = index % 10  # 소분류 번호(일의 자리)
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
    states = Make_states(Plus.main())  #자음 모음 단위로 이루어져 이중 리스트로 전달 된 것을 쉬프트레지스터 전달용 states로 만듦.
    content_list = Make_state_list(states)  # states를 24개 단위로 끊어주어 state를 요소로 갖는 이중 리스트를 만든다.
    # 사용 설명서
    print('복습기능을 시작합니다.')
    print('###########################')
    print('지정된 키는')
    print('[0] = 저장 시작 / 한번 더 클릭 : 저장 완료')
      # 저장시작 저장완료 다른 스위치(2개)
    print('[1] = 이전 문자')
    print('[2] = 다음 문자')
    print('[3] = 임시 저장 내용 출력')
    print('[4] = 큰 다이얼 +')
    print('[5] = 작은 다이얼 +')
    print('[6] = 큰 다이얼 -')
    print('[7] = 작은 다이얼 -')
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
    Resgister.main(content_list[now_index],pin_data,pin_clock,pin_latch,pin_clear)
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
                Resgister.main(content_list[now_index],pin_data,pin_clock,pin_latch,pin_clear)
                print('')
                # 저장 리스트 초기화
                saved_list = []

            elif save_count == 2:
                save_last_index = now_index
                saved_list = content_list[save_init_index: save_last_index + 1]
                print('저장 완료 - 현재 문자는 ->', end='')
                Resgister.main(content_list[now_index], pin_data, pin_clock, pin_latch, pin_clear)
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
            Resgister.main(content_list[now_index],pin_data,pin_clock,pin_latch,pin_clear)

            time.sleep(0.5)

        # '2'을 눌렀을때
        #elif key == "2":
        elif gpio.input(Next_word) == 1:
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
            Resgister.main(content_list[now_index],pin_data,pin_clock,pin_latch,pin_clear)

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


if __name__ == '__main__':
    main()
