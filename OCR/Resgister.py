#######모듈에 전달####
import RPi.GPIO as gpio
from time import sleep


def main(state,pin_data,pin_clock,pin_latch,pin_clear):


    # jamo_list=Plus_result #이중리스트 자음과 모음의 점자들로 이루어진 이중리스트. 글자간 구분 없는 자음과 모음의 연속
    #
    # def get_state(jamo_list):  #이중리스트를 입력으로 받아서 쉬프트 레지스터에 들어갈 수 있도록 뒤집은 다음 각 자음당 뒤에다가 0 두개 붙이기
    #     jamo_list.reverse()
    #     state=[]
    #     for braille in jamo_list:
    #         braille.extend([0, 0])
    #         state.extend(braille)
    #     return state





        #jamo_list = [[0, 1, 1, 1, 0, 0], [1, 0, 0, 1, 1, 1], [0, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 1], [0, 0, 0, 1, 0, 0], [1, 0, 0, 1, 1, 0], [1, 1, 0, 0, 0, 0], [1, 0, 0, 1, 1, 1]]
    #state=get_state(jamo_list)  #[1,0,0,,0,1,.....] 이 전달 됨.
    #list1 = sum(state, [])

    def send_byte(state): #입력(state)이 총 24개의 1,0으로 구성 된 1중 리스트여야 한다.
        for s in state:
            gpio.output(pin_data, int(s))
            gpio.output(pin_clock, True)
            sleep(.1)
            gpio.output(pin_clock, False)
            gpio.output(pin_data, False)
        gpio.output(pin_latch, True)
        sleep(.1)
        gpio.output(pin_latch, False)

    def clear_register():
        gpio.output(pin_clear, False)
        sleep(.1)
        gpio.output(pin_clear, True)
        gpio.output(pin_latch, True)
        sleep(.1)
        gpio.output(pin_latch, False)

    send_byte(state)
    sleep(1)
    send_byte([0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0])
    sleep(1)
    clear_register()

if __name__ == '__main__':
        main()
    # def get_state(jamo_list):  #이중리스트를 입력으로 받아서 쉬레에 들어갈 수 있도록 뒤집은 다음 각 자음당 뒤에다가 0 두개 붙이기
    #     jamo_list.reverse()
    #     state=[]
    #     for braille in jamo_list:
    #         braille.extend([0, 0])
    #         state.extend(braille)
    #     return state
    #
    # def excute():  #모뎀에 한 글자씩 띄워주고 (클리어 레지스터) 하고 모뎀 내리는 함수. 입력은 이중 리스트이다.