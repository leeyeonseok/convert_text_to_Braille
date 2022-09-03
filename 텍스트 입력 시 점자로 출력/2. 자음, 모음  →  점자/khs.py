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

def NumtoBraille(input_n): #숫자를 점자로(수표+숫자)
    braille = []
    if input_n[0] == '0':
        braille = [NUM_CHECK, [0, 1, 1, 1, 0, 0]]
    elif input_n[0] == '1':
        braille = [NUM_CHECK, [0, 1, 0, 1, 1, 1]]
    elif input_n[0] == '2':
        braille = [NUM_CHECK, [1, 0, 1, 0, 0, 0]]
    elif input_n[0] == '3':
        braille = [NUM_CHECK, [1, 1, 0, 0, 0, 0]]
    elif input_n[0]== '4':
        braille = [NUM_CHECK, [1, 1, 0, 1, 0, 0]]
    elif input_n[0] == '5':
        braille = [NUM_CHECK, [1, 0, 0, 1, 0, 0]]
    elif input_n[0]== '6':
        braille = [NUM_CHECK, [0, 0, 1, 0, 0, 0]]
    elif input_n[0]== '7':
        braille = [NUM_CHECK, [0, 0, 1, 0, 0, 1]]
    elif input_n[0]== '8':
        braille = [NUM_CHECK, [0, 0, 0, 1, 1, 0]]
    elif input_n[0]== '9':
        braille = [NUM_CHECK, [1, 0, 0, 0, 0, 1]]
    else:
        pass
    print(braille)
    return braille


def main():
    braille_list = []
    #index1 = 0
    n=input("입력: ")
    numb = seperate_n(n)
    print(numb)
    NumtoBraille(n)

    #숫자는 수표를 앞세워
    #숫자 다음에 한글-> 숫자 한글 붙여쓴다 + 여러 조건

if __name__ == '__main__':
    main()