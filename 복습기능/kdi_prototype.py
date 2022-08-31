# 한글자 = 리스트
# 문장 = 이차원리스트 [[글자], [글자],]
# 를 받고, 하나를 클릭하면 다음 글자 / 하나를 클릭하면 전 글자 / 스페이스바를 누르면 그 리스트 부터~ 다시 스페이스바를
# 눌렀을때 까지 의 글자들 리스트 저장해서 하나의 리스트로 옮김.

import keyboard
1
def main():

        # content = input("조작할 내용을 입력하시오 : ")
        content_list = [['한'], ['글'], ['문'], ['제']]
        now_index = 0
        print(content_list[now_index])

        while True:
                key = keyboard.read_key()
                if key == "1":
                        now_index -= 1
                        print(content_list[now_index])
                elif key == "2":
                        now_index += 1
                        print(content_list[now_index])
                else:
                        print(content_list[now_index])


if __name__ == '__main__':
        main()
