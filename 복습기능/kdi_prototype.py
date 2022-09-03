# 한글자 = 리스트
# 문장 = 이차원리스트 [[글자], [글자],]
# 를 받고, 하나를 클릭하면 다음 글자 / 하나를 클릭하면 전 글자 / 스페이스바를 누르면 그 리스트 부터~ 다시 스페이스바를
# 눌렀을때 까지 의 글자들 리스트 저장해서 하나의 리스트로 옮김.
# time.sleep 넣은 이유 : while True: 가 키보드 입력 시간 동안 여러번 루프를 돌기 때문이다.

import keyboard
import time




def main():

        # content = input("조작할 내용을 입력하시오 : ")
        content_list = [['한'], ['글'], ['문'], ['제'], ['출'], ['력'], ['테'], ['스'], ['트']]

        # 사용 설명서
        print('복습기능을 시작합니다.')
        print('###########################')
        print('지정된 키는')
        print('[0] = 저장 시작 / 한번 더 클릭 : 저장 완료')
        print('[1] = 이전 문자')
        print('[2] = 다음 문자')
        print('[7] = 저장 내용 출력')
        print('###########################')
        print('')
        # 현재 인덱스222222222202222222207
        now_index = 0

        # 처음 시작 시 첫 문자를 출력
        print(content_list[now_index])

        # 인덱스 조작을 위한 초기, 마지막 인덱스 값 / 인덱스의 길이
        length_index = len(content_list)
        init_index = 0
        last_index = length_index - 1

        # 저장 기능을 위한 변수 설정
        save_count = 0
        saved_list = []

        while True:
                #키를 눌렀을때, 앞으로 가거나 뒤로가라
                key = keyboard.read_key()

                # '0'을 눌렀을때 저장 시작 / 다시 한번 누를 시 저장 끝. 및 save_count 초기화
                if key == '0':
                        save_count += 1

                        if save_count == 1:
                                save_init_index = now_index
                                print('********')
                                print('저장 시작')
                                print('********')
                                # 저장 리스트 초기화
                                saved_list = []

                        elif save_count == 2:
                                save_last_index = now_index
                                saved_list = content_list[save_init_index: save_last_index+1]
                                print('********')
                                print('저장 완료')
                                print('********')
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
                                print('문장 마지막으로 돌아갑니다')
                                print('----------------------')
                        elif now_index > last_index:
                                now_index -= length_index
                                print('----------------------')
                                print('문장 처음으로 돌아갑니다')
                                print('----------------------')

                        # 현재 보고있는 문자를 출력
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
                        print(content_list[now_index])

                        time.sleep(0.5)

                # '7'을 눌렀을때 저장된 리스트 출력해주기.2222201
                elif key == '7':
                        print(saved_list)
                        time.sleep(0.5)

                # 예외처리 : 저장 시작되고 이전 문자로는 못가게 막음
                else:
                        print('저장이 시작되어 이전 문자로 돌아갈 수 없습니다. 재저장하려면 0을 2번 누르시오')
                        print('-> 현재 문자는', end='')
                        print(content_list[now_index], end='')
                        print('입니다.')
                        time.sleep(0.5)

if __name__ == '__main__':
        main()
