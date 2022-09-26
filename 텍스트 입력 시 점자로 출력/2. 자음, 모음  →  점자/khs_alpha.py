#영어변환
#import NaverClova
import re

def separation_text(input_list):
    separation_list = []
    for word in input_list:
        if '가' <= word <= '힣':
            char1 = (ord(word) - ord('가')) // 588
            char2 = ((ord(word) - ord('가')) - (588 * char1)) // 28
            char3 = (ord(word) - ord('가')) - (588 * char1) - 28 * char2
            # if not char3:
            #     separation_list.append([CHOSUNG[char1], JUNGSUNG[char2]])
            # else:
            #     separation_list.append([CHOSUNG[char1], JUNGSUNG[char2], JONGSUNG[char3]])
        elif ord('a') <= ord(word.lower()) <= ord('z'): #영어
            separation_list.append([word])
        else: #여기에 숫자,영어 등 경우 추가
            separation_list.append([word])
    return separation_list

def islanguage(input_list): #입력받은 문자열 언어
    k_count=0
    e_count=0
    for c in input_list:
        if ord('가') <= ord(c) <= ord('힣'):
            k_count += 1
        elif ord('a') <= ord(c.lower()) <= ord('z'):
            e_count += 1
    return "k" if k_count>1 else "e"

# def check_eng(jamo):
#     is_english=re.compile('[-a-zA-Z]')
#     temp = is_english.findall(jamo)
#     if len(temp) > 0:
#         return jamo.append([0, 0, 1, 1, 0, 1])
#     else:
#         return jamo

def alpha_to_braille(jamo, index1): #영어 변환
    braille = []
    if jamo[index1][0] == 'A':
        braille = [[0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0]]
    elif jamo[index1][0] == 'B':
        braille = [[0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0]]
    elif jamo[index1][0] == 'C':
        braille = [[0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0]]
    elif jamo[index1][0] == 'D':
        braille = [[0, 0, 0, 0, 0, 1], [1, 1, 0, 1, 0, 0]]
    elif jamo[index1][0] == 'E':
        braille = [[0, 0, 0, 0, 0, 1], [1, 0, 0, 1, 0, 0]]
    elif jamo[index1][0] == 'F':
        braille = [[0, 0, 0, 0, 0, 1], [1, 1, 1, 0, 0, 0]]
    elif jamo[index1][0] == 'G':
        braille = [[0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0]]
    elif jamo[index1][0] == 'H':
        braille = [[0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 0]]
    elif jamo[index1][0] == 'I':
        braille = [[0, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 0]]
    elif jamo[index1][0] == 'J':
        braille = [[0, 0, 0, 0, 0, 1], [0, 1, 1, 1, 0, 0]]
    elif jamo[index1][0] == 'K':
        braille = [[0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0]]
    elif jamo[index1][0] == 'L':
        braille = [[0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 1, 0]]
    elif jamo[index1][0] == 'M':
        braille = [[0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 1, 0]]
    elif jamo[index1][0] == 'N':
        braille = [[0, 0, 0, 0, 0, 1], [1, 1, 0, 1, 1, 0]]
    elif jamo[index1][0] == 'O':
        braille = [[0, 0, 0, 0, 0, 1], [1, 0, 0, 1, 1, 0]]
    elif jamo[index1][0] == 'a':
        braille = [1, 0, 0, 0, 0, 0]
    elif jamo[index1][0] == 'b':
        braille = [1, 0, 1, 0, 0, 0]
    elif jamo[index1][0] == 'c':
        braille = [1, 1, 0, 0, 0, 0]
    elif jamo[index1][0] == 'd':
        braille = [1, 1, 0, 1, 0, 0]
    elif jamo[index1][0] == 'e':
        braille = [1, 0, 0, 1, 0, 0]
    elif jamo[index1][0] == 'f':
        braille = [1, 1, 1, 0, 0, 0]
    elif jamo[index1][0] == 'g':
        braille = [1, 1, 1, 1, 0, 0]
    elif jamo[index1][0] == 'h':
        braille = [1, 0, 1, 1, 0, 0]
    elif jamo[index1][0] == 'i':
        braille = [0, 1, 1, 0, 0, 0]
    elif jamo[index1][0] == 'j':
        braille = [0, 1, 1, 1, 0, 0]
    elif jamo[index1][0] == 'k':
        braille = [1, 0, 0, 0, 1, 0]
    elif jamo[index1][0] == 'l':
        braille = [1, 0, 1, 0, 1, 0]
    elif jamo[index1][0] == 'm':
        braille = [1, 1, 0, 0, 1, 0]
    elif jamo[index1][0] == 'n':
        braille = [1, 1, 0, 1, 1, 0]
    elif jamo[index1][0] == 'o':
        braille = [1, 0, 0, 1, 1, 0]
    elif jamo[index1][0] == 'p':
        braille = [1, 1, 1, 0, 1, 0]
    elif jamo[index1][0] == 'q':
        braille = [1, 1, 1, 1, 1, 0]
    elif jamo[index1][0] == 'r':
        braille = [1, 0, 1, 1, 1, 0]
    elif jamo[index1][0] == 's':
        braille = [0, 1, 1, 0, 1, 0]
    elif jamo[index1][0] == 't':
        braille = [0, 1, 1, 1, 1, 0]
    elif jamo[index1][0] == 'u':
        braille = [1, 0, 0, 0, 1, 1]
    elif jamo[index1][0] == 'v':
        braille = [1, 0, 1, 0, 1, 1]
    elif jamo[index1][0] == 'w':
        braille = [0, 1, 1, 1, 0, 1]
    elif jamo[index1][0] == 'x':
        braille = [1, 1, 0, 0, 1, 1]
    elif jamo[index1][0] == 'y':
        braille = [1, 1, 0, 1, 1, 1]
    elif jamo[index1][0] == 'z':
        braille = [1, 0, 0, 1, 1, 1]
    return braille

    # def check_eng(jamo):
    #     is_english=re.compile('[-a-zA-Z]')
    #     temp = is_english.findall(jamo)
    #     if len(temp) > 0:
    #         return jamo.append([0, 0, 1, 1, 0, 1])
    #     else:
    #         return jamo


def print_braille(braille_list):
    for i in range(1, 6, 2):
        for j in range(len(braille_list)):
            if len(braille_list[j]) == 2:
                for k in range(2):
                    braille = ['●' for _ in range(2)]
                    for m in range(i - 1, i + 1):
                        if not braille_list[j][k][m]:
                            braille[m % 2] = ' '
                    for m in braille:
                        print(m, end=' ')
                    print(end='  ')
            else:
                braille = ['●' for _ in range(2)]
                for k in range(i - 1, i + 1):
                    if not braille_list[j][k]:
                        braille[k % 2] = ' '
                for k in braille:
                    print(k, end=' ')
                print(end='  ')
        print()

def main():
    braille_list = []
    index1 = 0
    n= input("영어 입력: ")
    jamo=separation_text(n)
    print(jamo)

    while index1 < len(jamo):
        if islanguage(n)=="e":
            braille_list.append(alpha_to_braille(jamo, index1))
            index1+=1
        elif islanguage(n)=="k":
            braille_list.append([0, 0, 0, 0, 0, 0])
            index1 += 1

        # 국어 문장 안에 로마자가 나올 때에는, 그 앞에는 로마자 표(0)를
        # 적고 그 뒤에는 로마자 종료표(4)를 적어 나타낸다.S

    print(braille_list)
    print_braille(braille_list)


if __name__ == '__main__':
    main()
