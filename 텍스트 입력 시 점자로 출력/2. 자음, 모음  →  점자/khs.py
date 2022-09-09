#숫자 및 연산
NUMBER=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '+', '-', '*', '%', '=']
#수표
NUM_CHECK=[0, 1, 0, 1, 1, 1]
#NUM_L[][6]=[[0, 1, 1, 1, 0, 0],[0, 1, 0, 1, 1, 1],[1, 0, 1, 0, 0, 0]]

def seperate_n(input_num):  #숫자
    n_list=[]
    for w in list(input_num.strip()):
        n_list.append([w])
    return n_list

def NumtoBraille(input_n,index1): #숫자 to 점자로(수표+숫자)
    braille = []
    if input_n[index1][0] == '0':   #누적..? 조건문 뭔가 이상
        if input_n[0][0] == '0':
            braille = [NUM_CHECK, [0, 1, 1, 1, 0, 0]]
        else:
            braille = [0, 1, 1, 1, 0, 0]
    elif input_n[index1][0] == '1':
        braille = [NUM_CHECK, [0, 1, 0, 1, 1, 1]]
    elif input_n[index1][0] == '2':
        braille = [NUM_CHECK, [1, 0, 1, 0, 0, 0]]
    elif input_n[index1][0] == '3':
        braille = [NUM_CHECK, [1, 1, 0, 0, 0, 0]]
    elif input_n[index1][0]== '4':
        braille = [NUM_CHECK, [1, 1, 0, 1, 0, 0]]
    elif input_n[index1][0] == '5':
        braille = [NUM_CHECK, [1, 0, 0, 1, 0, 0]]
    elif input_n[index1][0]== '6':
        braille = [NUM_CHECK, [0, 0, 1, 0, 0, 0]]
    elif input_n[index1][0]== '7':
        braille = [NUM_CHECK, [0, 0, 1, 0, 0, 1]]
    elif input_n[index1][0]== '8':
        braille = [NUM_CHECK, [0, 0, 0, 1, 1, 0]]
    elif input_n[index1][0]== '9':
        braille = [NUM_CHECK, [1, 0, 0, 0, 0, 1]]
    else:
        pass
    #print(braille)
    return braille

def PunctoBraille(input_n,index1): #문장부호 to 점자
    braille = []
    if input_n[index1][0] == '.':
        braille = [0, 0, 1, 1, 0, 1]
    elif input_n[index1][0] == '?':
        braille = [0, 0, 1, 0, 1, 1]
    elif input_n[index1][0] == '!':
        braille = [0, 0, 1, 1, 1, 0]
    elif input_n[index1][0] == ',':  #수의 자리점 표시하는 쉼표는 [0, 0, 1, 0, 0, 0] 나중에 따로
        braille = [0, 0, 0, 1, 0, 0]
    else:
        pass
    return braille

def CalctoBraille(input_n,index1): #사칙연산 to 점자
    braille = []
    if input_n[index1][0] == '+':
        braille = [0, 0, 1, 0, 0, 1]
    elif input_n[index1][0] == '-':
        braille = [0, 0, 0, 1, 1, 0]
    elif input_n[index1][0] == 'x' or 'X':
        braille = [1, 0, 0, 0, 0, 1]
    elif input_n[index1][0] == '%':
        braille = [[0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0]]
    else:
        pass
    return braille

def print_braille(braille_list):  #점자 출력
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
    n=input("입력: ")
    numb = seperate_n(n)
    print(numb)

    for index1 in range(len(numb)):
        braille_list.append(NumtoBraille(numb, index1))
        # braille_list.append(PunctoBraille(numb, index1))
        # braille_list.append(CalctoBraille(numb,index1))
        index1+=1

    print(braille_list)
    print_braille(braille_list)

    #숫자는 수표를 앞세워
    #첫글자 앞에만 수표 나옴-> 이거 해결해야함

    #숫자 다음에 한글-> 숫자 한글 붙여쓴다 + 여러 조건
    #숫자와 혼동되는 ㄴㄷㅁㅁㅋㅌㅍㅎ 의 첫 소리 글자와 '운'의 약자가 숫자 다음에 이어나올 때에는 숫자와 한글을 띄어쓴다
if __name__ == '__main__':
    main()