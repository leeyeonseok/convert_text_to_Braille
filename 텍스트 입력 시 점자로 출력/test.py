#초기 숫자 코드
#옮겨 놓은 것

abbreviation_1 = [[['ㄱ', 'ㅡ'], ['ㄹ', 'ㅐ'], ['ㅅ', 'ㅓ']], [['ㄱ', 'ㅡ'], ['ㄹ', 'ㅓ'], ['ㄴ', 'ㅏ']],
                 [['ㄱ', 'ㅡ'], ['ㄹ', 'ㅓ'], ['ㅁ', 'ㅕ', 'ㄴ']], [['ㄱ', 'ㅡ'], ['ㄹ', 'ㅓ'], ['ㅁ', 'ㅡ'], ['ㄹ', 'ㅗ']],
                 [['ㄱ', 'ㅡ'], ['ㄹ', 'ㅓ', 'ㄴ'], ['ㄷ', 'ㅔ']], [['ㄱ', 'ㅡ'], ['ㄹ', 'ㅣ'], ['ㄱ', 'ㅗ']],
                 [['ㄱ', 'ㅡ'], ['ㄹ', 'ㅣ'], ['ㅎ', 'ㅏ'], ['ㅇ', 'ㅕ']]]
                # 그래서, 그러나, 그러면, 그러므로, 그런데, 그리고, 그리하여
abbreviation_2 = [['ㄱ', 'ㅏ'], ['ㄴ', 'ㅏ'], ['ㄷ', 'ㅏ'], ['ㅁ', 'ㅏ'], ['ㅂ', 'ㅏ'], ['ㅅ', 'ㅏ'], ['ㅈ', 'ㅏ'],
                  ['ㅋ', 'ㅏ'], ['ㅌ', 'ㅏ'], ['ㅍ', 'ㅏ'], ['ㅎ', 'ㅏ'], ['ㅓ', 'ㄱ'], ['ㅓ', 'ㄴ'], ['ㅓ', 'ㄹ'],
                  ['ㅕ', 'ㄴ'], ['ㅕ', 'ㄹ'], ['ㅕ', 'ㅇ'], ['ㅗ', 'ㄱ'], ['ㅗ', 'ㄴ'], ['ㅗ', 'ㅇ'], ['ㅜ', 'ㄴ'],
                  ['ㅜ', 'ㄹ'], ['ㅡ', 'ㄴ'], ['ㅡ', 'ㄹ'], ['ㅣ', 'ㄴ'], ['ㄱ', 'ㅓ', 'ㅅ']]
                # 가, 나, 다, 마, 바, 사, 자, 카, 타, 파, 하,
                # ㅓㄱ, ㅓㄴ, ㅓㄹ, ㅕㄴ, ㅕㄹ, ㅕㅇ, ㅗㄱ, ㅗㄴ, ㅗㅇ, ㅜㄴ, ㅜㄹ, ㅡㄴ, ㅡㄹ, ㅣㄴ, 것
# 초성 리스트. 00 ~ 18
CHOSUNG = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 중성 리스트. 00 ~ 20
JUNGSUNG = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ',
                 'ㅣ']
# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
                 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
#숫자 및 연산
NUMBER=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '+', '-', '*', '%', '=']

def seperate_n(input_num):  #숫자
    n_list=[]
    for w in list(input_num.strip()):
        n_list.append([w])
    return n_list

def number_to_braille(numb, index1):  #숫자를 점자로(수표+숫자)
    braille = []
    if numb[index1][0] == '0':
        braille = [[0, 1, 0, 1, 1, 1], [0, 1, 1, 1, 0, 0]]
    elif numb[index1][0] == '1':
        #braille = [[0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 1, 1]]
        braille = [0, 1, 0, 1, 1, 1]
    elif numb[index1][0] == '2':
        braille = [[0, 1, 0, 1, 1, 1], [1, 0, 1, 0, 0, 0]]
    elif numb[index1][0] == '3':
        braille = [[0, 1, 0, 1, 1, 1], [1, 1, 0, 0, 0, 0]]
    elif numb[index1]== '4':
        braille = [[0, 1, 0, 1, 1, 1], [1, 1, 0, 1, 0, 0]]
    elif numb[index1] == '5':
        braille = [[0, 1, 0, 1, 1, 1], [1, 0, 0, 1, 0, 0]]
    elif numb[index1]== '6':
        braille = [[0, 1, 0, 1, 1, 1], [0, 0, 1, 0, 0, 0]]
    elif numb[index1]== '7':
        braille = [[0, 1, 0, 1, 1, 1], [0, 0, 1, 0, 0, 1]]
    elif numb[index1]== '8':
        braille = [[0, 1, 0, 1, 1, 1], [0, 0, 0, 1, 1, 0]]
    elif numb[index1]== '9':
        braille = [[0, 1, 0, 1, 1, 1], [1, 0, 0, 0, 0, 1]]
    else:
        pass
    return braille
#
# def isNum(text):
#     y = text.isnumeric()
#     print(y)

def print_braille(braille_list): #점자 출력 함수
    for i in range(1, 6, 2):  #1부터 6전까지 2칸씩
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
    n=input("텍스트 입력 : ")
    numb=seperate_n(n)
    print(numb)

    #숫자-한글 이어서 나올때 붙여쓰기 ex)1권


    while index1 < len(numb):
        braille_list.append(number_to_braille(numb, index1))
        # if n.isnumeric==1:
        #     braille_list.append(number_to_braille(jamo, index1))
    print_braille(braille_list)

if __name__ == '__main__':
    main()