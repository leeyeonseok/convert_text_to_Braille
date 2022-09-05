import NaverClova


abbreviation_1 = [[['ㄱ', 'ㅡ'], ['ㄹ', 'ㅐ'], ['ㅅ', 'ㅓ']], [['ㄱ', 'ㅡ'], ['ㄹ', 'ㅓ'], ['ㄴ', 'ㅏ']],
                 [['ㄱ', 'ㅡ'], ['ㄹ', 'ㅓ'], ['ㅁ', 'ㅕ', 'ㄴ']], [['ㄱ', 'ㅡ'], ['ㄹ', 'ㅓ'], ['ㅁ', 'ㅡ'], ['ㄹ', 'ㅗ']],
                 [['ㄱ', 'ㅡ'], ['ㄹ', 'ㅓ', 'ㄴ'], ['ㄷ', 'ㅔ']], [['ㄱ', 'ㅡ'], ['ㄹ', 'ㅣ'], ['ㄱ', 'ㅗ']],
                 [['ㄱ', 'ㅡ'], ['ㄹ', 'ㅣ'], ['ㅎ', 'ㅏ'], ['ㅇ', 'ㅕ']]]
                # 그래서, 그러나, 그러면, 그러므로, 그런데, 그리고, 그리하여
abbreviation_2 = [['ㄱ', 'ㅏ'], ['ㄴ', 'ㅏ'], ['ㄷ', 'ㅏ'], ['ㅁ', 'ㅏ'], ['ㅂ', 'ㅏ'], ['ㅅ', 'ㅏ'], ['ㅈ', 'ㅏ'],
                  ['ㅋ', 'ㅏ'], ['ㅌ', 'ㅏ'], ['ㅍ', 'ㅏ'], ['ㅎ', 'ㅏ'], ['ㄲ', 'ㅏ'], ['ㅆ', 'ㅏ'], ['ㅓ', 'ㄱ'],
                  ['ㅓ', 'ㄴ'], ['ㅓ', 'ㄹ'], ['ㅕ', 'ㄴ'], ['ㅕ', 'ㄹ'], ['ㅕ', 'ㅇ'], ['ㅗ', 'ㄱ'], ['ㅗ', 'ㄴ'],
                  ['ㅗ', 'ㅇ'], ['ㅜ', 'ㄴ'], ['ㅜ', 'ㄹ'], ['ㅡ', 'ㄴ'], ['ㅡ', 'ㄹ'], ['ㅣ', 'ㄴ'], ['ㄱ', 'ㅓ', 'ㅅ'],
                  ['ㄲ', 'ㅓ', 'ㅅ']]
                # 가, 나, 다, 마, 바, 사, 자, 카, 타, 파, 하, 까, 싸
                # ㅓㄱ, ㅓㄴ, ㅓㄹ, ㅕㄴ, ㅕㄹ, ㅕㅇ, ㅗㄱ, ㅗㄴ, ㅗㅇ, ㅜㄴ, ㅜㄹ, ㅡㄴ, ㅡㄹ, ㅣㄴ, 것, 껏
abbreviation_3 = [['ㅅ', 'ㅓ', 'ㅇ'], ['ㅆ', 'ㅓ', 'ㅇ'], ['ㅈ', 'ㅓ', 'ㅇ'], ['ㅉ', 'ㅓ', 'ㅇ'], ['ㅊ', 'ㅓ', 'ㅇ']]
                # 성, 썽, 정, 쩡, 청
# 초성 리스트. 00 ~ 18
CHOSUNG = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 중성 리스트. 00 ~ 20
JUNGSUNG = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ',
                 'ㅣ'] # 2, 9, 13, 14
# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
                 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def separate_double_consonant(char):        # 종성의 쌍자음을 각각의 자음으로 분리
    # 'ㄲ', 'ㄳ', 'ㄵ', 'ㄶ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅄ', 'ㅆ'
    if JONGSUNG[char] == 'ㄲ':
        JONGSUNG[char] = [JONGSUNG[1], JONGSUNG[1]]
    elif JONGSUNG[char] == 'ㄳ':
        JONGSUNG[char] = [JONGSUNG[1], JONGSUNG[19]]
    elif JONGSUNG[char] == 'ㄵ':
        JONGSUNG[char] = [JONGSUNG[4], JONGSUNG[22]]
    elif JONGSUNG[char] == 'ㄶ':
        JONGSUNG[char] = [JONGSUNG[4], JONGSUNG[27]]
    elif JONGSUNG[char] == 'ㄺ':
        JONGSUNG[char] = [JONGSUNG[8], JONGSUNG[1]]
    elif JONGSUNG[char] == 'ㄻ':
        JONGSUNG[char] = [JONGSUNG[8], JONGSUNG[16]]
    elif JONGSUNG[char] == 'ㄼ':
        JONGSUNG[char] = [JONGSUNG[8], JONGSUNG[17]]
    elif JONGSUNG[char] == 'ㄽ':
        JONGSUNG[char] = [JONGSUNG[8], JONGSUNG[19]]
    elif JONGSUNG[char] == 'ㄾ':
        JONGSUNG[char] = [JONGSUNG[8], JONGSUNG[25]]
    elif JONGSUNG[char] == 'ㄿ':
        JONGSUNG[char] = [JONGSUNG[8], JONGSUNG[26]]
    elif JONGSUNG[char] == 'ㅀ':
        JONGSUNG[char] = [JONGSUNG[8], JONGSUNG[27]]
    elif JONGSUNG[char] == 'ㅄ':
        JONGSUNG[char] = [JONGSUNG[17], JONGSUNG[19]]
    elif JONGSUNG[char] == 'ㅆ':
        JONGSUNG[char] = [JONGSUNG[19], JONGSUNG[19]]
    else:
        pass
    return JONGSUNG[char]


def separation_text(input_list):
    separation_list = []
    for word in input_list:  # 양쪽 공백 지우기
        # 영어인 경우 구분 해서 작성함.
        if '가' <= word <= '힣':
            # 588개 마다 초성이 바뀜.
            char1 = (ord(word) - ord('가')) // 588  #몫을 반환,하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환합니다.
            # 중성은 총 28가지 종류
            char2 = ((ord(word) - ord('가')) - (588 * char1)) // 28
            char3 = (ord(word) - ord('가')) - (588 * char1) - 28 * char2
            if not char3:  #char3값이 FAlSE면 실행.
                separation_list.append([CHOSUNG[char1], JUNGSUNG[char2]])
            else:
                separation_list.append([CHOSUNG[char1], JUNGSUNG[char2], JONGSUNG[char3]])
        else:
            separation_list.append([word])
    return separation_list


def check_abbreviation_1(jamo, index1):   # 약어 검사 함수
    abb_list = []
    for i in range(len(abbreviation_1)):  #예외1의 리스트 길이만큼의 range 객체 (0~7) 생성
        if abbreviation_1[i][0:len(abbreviation_1[i])] == jamo[index1:index1 + len(abbreviation_1[i])]:
            if not i:
                abb_list = [[1, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 0]]   # 그래서
            elif i == 1:
                abb_list = [[1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0]]   # 그러나
            elif i == 2:
                abb_list = [[1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0]]   # 그러면
            elif i == 3:
                abb_list = [[1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 1]]   # 그러므로
                return 4, abb_list
            elif i == 4:
                abb_list = [[1, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0]]   # 그런데
            elif i == 5:
                abb_list = [[1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 1]]   # 그리고
            else:
                abb_list = [[1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 1]]   # 그리하여
                return 4, abb_list
            return 3, abb_list
    return 0, abb_list


def check_abbreviation_2(jamo, index1):      # 약자 검사 함수
    abb_list = []
    for i in range(len(abbreviation_2)):
        for j in range(len(jamo[index1]) - (len(abbreviation_2[i]) - 1)):
            if abbreviation_2[i] == jamo[index1][j:j + len(abbreviation_2[i])]:
                if 13 <= i <= 26:
                    if i == 13:
                        abb_list = [1, 1, 0, 1, 0, 1]  # ㅓㄱ
                    elif i == 14:
                        abb_list = [0, 1, 1, 1, 1, 1]  # ㅓㄴ
                    elif i == 15:
                        abb_list = [0, 1, 1, 1, 1, 0]  # ㅓㄹ
                    elif i == 16:
                        abb_list = [1, 0, 0, 0, 0, 1]  # ㅕㄴ
                    elif i == 17:
                        abb_list = [1, 0, 1, 1, 0, 1]  # ㅕㄹ
                    elif i == 18:
                        abb_list = [1, 1, 1, 1, 0, 1]  # ㅕㅇ
                    elif i == 19:
                        abb_list = [1, 1, 0, 0, 1, 1]  # ㅗㄱ
                    elif i == 20:
                        abb_list = [1, 0, 1, 1, 1, 1]  # ㅗㄴ
                    elif i == 21:
                        abb_list = [1, 1, 1, 1, 1, 1]  # ㅗㅇ
                    elif i == 22:
                        abb_list = [1, 1, 1, 1, 0, 0]  # ㅜㄴ
                    elif i == 23:
                        abb_list = [1, 1, 1, 0, 1, 1]  # ㅜㄹ
                    elif i == 24:
                        abb_list = [1, 0, 0, 1, 1, 1]  # ㅡㄴ
                    elif i == 25:
                        abb_list = [0, 1, 1, 0, 1, 1]  # ㅡㄹ
                    else:
                        abb_list = [1, 1, 1, 1, 1, 0]  # ㅣㄴ
                    return 1, abb_list
                else:
                    if (1 <= i <= 4 or 6 <= i <= 10) and index1 < len(jamo) - 1 and jamo[index1 + 1][0] == 'ㅇ':
                        if i == 1:                           # 나, 다, 마, 바, 자, 카, 타, 파, 하 뒤에 모음이 오는 예외일 경우
                            abb_list = [[1, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 1]]  # 나
                        elif i == 2:
                            abb_list = [[0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1]]  # 다
                        elif i == 3:
                            abb_list = [[1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 1]]  # 마
                        elif i == 4:
                            abb_list = [[0, 1, 0, 1, 0, 0], [1, 0, 1, 0, 0, 1]]  # 바
                        elif i == 6:
                            abb_list = [[0, 1, 0, 0, 0, 1], [1, 0, 1, 0, 0, 1]]  # 자
                        elif i == 7:
                            abb_list = [[1, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1]]  # 카
                        elif i == 8:
                            abb_list = [[1, 0, 1, 1, 0, 0], [1, 0, 1, 0, 0, 1]]  # 타
                        elif i == 9:
                            abb_list = [[1, 1, 0, 1, 0, 0], [1, 0, 1, 0, 0, 1]]  # 파
                        elif i == 10:
                            abb_list = [[0, 1, 1, 1, 0, 0], [1, 0, 1, 0, 0, 1]]  # 하
                        else:
                            pass
                    else:
                        if not i:
                            abb_list = [1, 1, 1, 0, 0, 1]  # 가
                        elif i == 1:
                            abb_list = [1, 1, 0, 0, 0, 0]  # 나
                        elif i == 2:
                            abb_list = [0, 1, 1, 0, 0, 0]  # 다
                        elif i == 3:
                            abb_list = [1, 0, 0, 1, 0, 0]  # 마
                        elif i == 4:
                            abb_list = [0, 1, 0, 1, 0, 0]  # 바
                        elif i == 5:
                            abb_list = [1, 0, 1, 0, 1, 0]  # 사
                        elif i == 6:
                            abb_list = [0, 1, 0, 0, 0, 1]  # 자
                        elif i == 7:
                            abb_list = [1, 1, 1, 0, 0, 0]  # 카
                        elif i == 8:
                            abb_list = [1, 0, 1, 1, 0, 0]  # 타
                        elif i == 9:
                            abb_list = [1, 1, 0, 1, 0, 0]  # 파
                            if jamo[index1] == ['ㅍ', 'ㅏ', 'ㅅ', 'ㅅ']:
                                abb_list = [[1, 1, 0, 1, 0, 0], [1, 0, 1, 0, 0, 1]]  # 파
                        elif i == 10:
                            abb_list = [0, 1, 1, 1, 0, 0]  # 하
                        elif i == 11:
                            abb_list = [[0, 0, 0, 0, 0, 1], [1, 1, 1, 0, 0, 1]]  # 까
                        elif i == 12:
                            abb_list = [[0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 1, 0]]  # 싸
                        elif i == 27:
                            abb_list = [[0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 0]]  # 것
                            return 3, abb_list
                        else:
                            abb_list = [[0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 0]]  # 껏
                            return 4, abb_list
                    return 2, abb_list
    return 0, abb_list


def check_abbreviation_3(jamo, index1):
    for i in range(len(abbreviation_3)):
        if jamo[index1] == abbreviation_3[i]:
            return 1
    return 0


def check_vowel_chain_1(jamo, index1):
    for i in range(len(JUNGSUNG)):
        if index1 < len(jamo) - 1 and jamo[index1][-1] == JUNGSUNG[i] and jamo[index1 + 1] == ['ㅇ', 'ㅖ']:
            vowel_chain_list = convert_JUNGSUNG_to_Braille(jamo, index1)
            return vowel_chain_list
    return 0


def check_vowel_chain_2(jamo, index1):
    for i in 2, 9, 13, 14:
        if index1 < len(jamo) - 1 and jamo[index1][-1] == JUNGSUNG[i] and jamo[index1 + 1] == ['ㅇ', 'ㅐ']:
            vowel_chain_list = convert_JUNGSUNG_to_Braille(jamo, index1)
            return vowel_chain_list
    return 0
#-------------------------------------위는 예외 처리---------------------------------------------------

def convert_CHOSUNG_to_Braille(jamo, index1):
    braille = []
    if jamo[index1][0] == 'ㄱ':
        braille = [0, 1, 0, 0, 0, 0]
    elif jamo[index1][0] == 'ㄴ':
        braille = [1, 1, 0, 0, 0, 0]
    elif jamo[index1][0] == 'ㄷ':
        braille = [0, 1, 1, 0, 0, 0]
    elif jamo[index1][0] == 'ㄹ':
        braille = [0, 0, 0, 1, 0, 0]
    elif jamo[index1][0] == 'ㅁ':
        braille = [1, 0, 0, 1, 0, 0]
    elif jamo[index1][0] == 'ㅂ':
        braille = [0, 1, 0, 1, 0, 0]
    elif jamo[index1][0] == 'ㅅ':
        braille = [0, 0, 0, 0, 0, 1]
    elif jamo[index1][0] == 'ㅇ':
        braille = [1, 1, 1, 1, 0, 0]
    elif jamo[index1][0] == 'ㅈ':
        braille = [0, 1, 0, 0, 0, 1]
    elif jamo[index1][0] == 'ㅊ':
        braille = [0, 0, 0, 1, 0, 1]
    elif jamo[index1][0] == 'ㅋ':
        braille = [1, 1, 1, 0, 0, 0]
    elif jamo[index1][0] == 'ㅌ':
        braille = [1, 0, 1, 1, 0, 0]
    elif jamo[index1][0] == 'ㅍ':
        braille = [1, 1, 0, 1, 0, 0]
    elif jamo[index1][0] == 'ㅎ':
        braille = [0, 1, 1, 1, 0, 0]
    elif jamo[index1][0] == 'ㄲ':
        braille = [[0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0]]
    elif jamo[index1][0] == 'ㄸ':
        braille = [[0, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 0]]
    elif jamo[index1][0] == 'ㅃ':
        braille = [[0, 0, 0, 0, 0, 1], [0, 1, 0, 1, 0, 0]]
    elif jamo[index1][0] == 'ㅆ':
        braille = [[0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1]]
    elif jamo[index1][0] == 'ㅉ':
        braille = [[0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1]]
    else:
        pass
    return braille


def convert_JUNGSUNG_to_Braille(jamo, index1):
    braille = []
    if jamo[index1][1] == 'ㅏ':
        braille = [1, 0, 1, 0, 0, 1]
    elif jamo[index1][1] == 'ㅑ':
        braille = [0, 1, 0, 1, 1, 0]
    elif jamo[index1][1] == 'ㅓ':
        braille = [0, 1, 1, 0, 1, 0]
    elif jamo[index1][1] == 'ㅕ':
        braille = [1, 0, 0, 1, 0, 1]
    elif jamo[index1][1] == 'ㅗ':
        braille = [1, 0, 0, 0, 1, 1]
    elif jamo[index1][1] == 'ㅛ':
        braille = [0, 1, 0, 0, 1, 1]
    elif jamo[index1][1] == 'ㅜ':
        braille = [1, 1, 0, 0, 1, 0]
    elif jamo[index1][1] == 'ㅠ':
        braille = [1, 1, 0, 0, 0, 1]
    elif jamo[index1][1] == 'ㅡ':
        braille = [0, 1, 1, 0, 0, 1]
    elif jamo[index1][1] == 'ㅣ':
        braille = [1, 0, 0, 1, 1, 0]
    elif jamo[index1][1] == 'ㅐ':
        braille = [1, 0, 1, 1, 1, 0]
    elif jamo[index1][1] == 'ㅔ':
        braille = [1, 1, 0, 1, 1, 0]
    elif jamo[index1][1] == 'ㅒ':
        braille = [[0, 1, 0, 1, 1, 0], [1, 0, 1, 1, 1, 0]]
    elif jamo[index1][1] == 'ㅖ':
        braille = [0, 1, 0, 0, 1, 0]
    elif jamo[index1][1] == 'ㅘ':
        braille = [1, 0, 1, 0, 1, 1]
    elif jamo[index1][1] == 'ㅙ':
        braille = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 1, 1, 0]]
    elif jamo[index1][1] == 'ㅚ':
        braille = [1, 1, 0, 1, 1, 1]
    elif jamo[index1][1] == 'ㅝ':
        braille = [1, 1, 1, 0, 1, 0]
    elif jamo[index1][1] == 'ㅞ':
        braille = [[1, 1, 1, 0, 1, 0], [1, 0, 1, 1, 1, 0]]
    elif jamo[index1][1] == 'ㅟ':
        braille = [[1, 1, 0, 0, 1, 0], [1, 0, 1, 1, 1, 0]]
    elif jamo[index1][1] == 'ㅢ':
        braille = [0, 1, 1, 1, 0, 1]
    else:
        pass
    return braille


def convert_JONGSUNG_to_Braille(jamo, index1, index2):
    braille = []
    if len(jamo[index1]) - index2 == 1:
        if jamo[index1][-1] == 'ㄱ':
            braille = [1, 0, 0, 0, 0, 0]
        elif jamo[index1][-1] == 'ㄴ':
            braille = [0, 0, 1, 1, 0, 0]
        elif jamo[index1][-1] == 'ㄷ':
            braille = [0, 0, 0, 1, 1, 0]
        elif jamo[index1][-1] == 'ㄹ':
            braille = [0, 0, 1, 0, 0, 0]
        elif jamo[index1][-1] == 'ㅁ':
            braille = [0, 0, 1, 0, 0, 1]
        elif jamo[index1][-1] == 'ㅂ':
            braille = [1, 0, 1, 0, 0, 0]
        elif jamo[index1][-1] == 'ㅅ':
            braille = [0, 0, 0, 0, 1, 0]
        elif jamo[index1][-1] == 'ㅇ':
            braille = [0, 0, 1, 1, 1, 1]
        elif jamo[index1][-1] == 'ㅈ':
            braille = [1, 0, 0, 0, 1, 0]
        elif jamo[index1][-1] == 'ㅊ':
            braille = [0, 0, 1, 0, 1, 0]
        elif jamo[index1][-1] == 'ㅋ':
            braille = [0, 0, 1, 1, 1, 0]
        elif jamo[index1][-1] == 'ㅌ':
            braille = [0, 0, 1, 0, 1, 1]
        elif jamo[index1][-1] == 'ㅍ':
            braille = [0, 0, 1, 1, 0, 1]
        elif jamo[index1][-1] == 'ㅎ':
            braille = [0, 0, 0, 1, 1, 1]
        else:
            pass
    else:
        if jamo[index1][-2:] == ['ㄱ', 'ㄱ']:
            braille = [[1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0]]
        elif jamo[index1][-2:] == ['ㄱ', 'ㅅ']:
            braille = [[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0]]
        elif jamo[index1][-2:] == ['ㄴ', 'ㅈ']:
            braille = [[0, 0, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0]]
        elif jamo[index1][-2:] == ['ㄴ', 'ㅎ']:
            braille = [[0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 1, 1]]
        elif jamo[index1][-2:] == ['ㄹ', 'ㄱ']:
            braille = [[0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0]]
        elif jamo[index1][-2:] == ['ㄹ', 'ㅁ']:
            braille = [[0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 1]]
        elif jamo[index1][-2:] == ['ㄹ', 'ㅂ']:
            braille = [[0, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0]]
        elif jamo[index1][-2:] == ['ㄹ', 'ㅅ']:
            braille = [[0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0]]
        elif jamo[index1][-2:] == ['ㄹ', 'ㅌ']:
            braille = [[0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 1, 1]]
        elif jamo[index1][-2:] == ['ㄹ', 'ㅍ']:
            braille = [[0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 1]]
        elif jamo[index1][-2:] == ['ㄹ', 'ㅎ']:
            braille = [[0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1]]
        elif jamo[index1][-2:] == ['ㅂ', 'ㅅ']:
            braille = [[1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0]]
        elif jamo[index1][-2:] == ['ㅅ', 'ㅅ']:
            braille = [0, 1, 0, 0, 1, 0]
        else:
            pass
    return braille


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
    text_list = NaverClova.main()
    for text in text_list:
        braille_list = []
        index1 = 0
        jamo = separation_text(text)
        while index1 < len(jamo):
            if check_abbreviation_1(jamo, index1)[0]:                                # 제 7절 약어 - 예외까지 구현 완료
                if jamo[index1 - 1] == [' '] or not index1:
                    braille_list.append(check_abbreviation_1(jamo, index1)[1])
                    index1 += check_abbreviation_1(jamo, index1)[0]
                    continue

            index2 = 0
            if check_abbreviation_2(jamo, index1)[0] == 1:                           # 모음, 자음이 결합되어 있는 약어 판단
                if jamo[index1][0] != 'ㅇ':                                    # [ ㅇ으로 시작되지 않을 때만
                    braille_list.append(convert_CHOSUNG_to_Braille(jamo, index1))            # 초성 출력 ]
                index2 += 1
                braille_list.append(check_abbreviation_2(jamo, index1)[1])
                index2 += 2
                if index2 >= len(jamo[index1]):
                    index1 += 1
                    continue
                braille_list.append(convert_JONGSUNG_to_Braille(jamo, index1, index2))

            elif check_abbreviation_2(jamo, index1)[0] == 2:                        # 가, 나, 다, 마.... 등의 약어 판단
                braille_list.append(check_abbreviation_2(jamo, index1)[1])
                index2 += 2
                if index2 >= len(jamo[index1]):
                    index1 += 1
                    continue
                braille_list.append(convert_JONGSUNG_to_Braille(jamo, index1, index2))

            elif check_abbreviation_2(jamo, index1)[0] == 3:                        # '것' 약어 판단
                braille_list.append(check_abbreviation_2(jamo, index1)[1])
                index1 += 1
                continue

            elif check_abbreviation_2(jamo, index1)[0] == 4:                        # '껏' 약어 판단
                index2 += 2
                if len(jamo[index1]) - index2 == 1:
                    braille_list.append([0, 0, 0, 0, 0, 1])
                    braille_list.append(check_abbreviation_2(jamo, index1)[1])
                    index1 += 1
                    continue
                else:                                                               # '껐' 판단
                    braille_list.append(convert_CHOSUNG_to_Braille(jamo, index1))
                    braille_list.append(convert_JUNGSUNG_to_Braille(jamo, index1))
                    braille_list.append(convert_JONGSUNG_to_Braille(jamo, index1, index2))
                    index1 += 1
                    continue

            elif check_abbreviation_3(jamo, index1):                                # 성, 썽, 정, 쩡, 청 예외 판단
                braille_list.append(convert_CHOSUNG_to_Braille(jamo, index1))
                braille_list.append([1, 1, 1, 1, 0, 1])     # 'ㅕㅇ'
                index1 += 1
                continue

            elif check_vowel_chain_1(jamo, index1):                                 # 모음 + '예' 연쇄 판단
                if jamo[index1][0] != 'ㅇ':
                    braille_list.append(convert_CHOSUNG_to_Braille(jamo, index1))
                braille_list.append(check_vowel_chain_1(jamo, index1))
                braille_list.append([0, 0, 0, 0, 1, 1])     # 붙임표
                braille_list.append([0, 1, 0, 0, 1, 0])     # '예'
                index1 += 2
                continue

            elif check_vowel_chain_2(jamo, index1):                                 # ㅑ, ㅘ, ㅜ, ㅝ + '애' 연쇄 판단
                if jamo[index1][0] != 'ㅇ':
                    braille_list.append(convert_CHOSUNG_to_Braille(jamo, index1))
                braille_list.append(check_vowel_chain_2(jamo, index1))
                braille_list.append([0, 0, 0, 0, 1, 1])     # 붙임표
                braille_list.append([1, 0, 1, 1, 1, 0])     # '애'
                index1 += 2
                continue

            else:
                if jamo[index1][0] != 'ㅇ':
                    braille_list.append(convert_CHOSUNG_to_Braille(jamo, index1))
                index2 += 1
                braille_list.append(convert_JUNGSUNG_to_Braille(jamo, index1))
                index2 += 1
                if index2 >= len(jamo[index1]):
                    index1 += 1
                    continue
                braille_list.append(convert_JONGSUNG_to_Braille(jamo, index1, index2))
            index1 += 1
        print(jamo)
        print_braille(braille_list)


if __name__ == '__main__':
    main()
