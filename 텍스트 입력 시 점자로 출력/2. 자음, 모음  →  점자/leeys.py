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


def separation_text(input_list):        # 텍스트 각각의 자음, 모음으로 분리
    separation_list = []
    for word in list(input_list.strip()):
        if '가' <= word <= '힣':
            char1 = (ord(word) - ord('가')) // 588
            char2 = ((ord(word) - ord('가')) - (588 * char1)) // 28
            char3 = (ord(word) - ord('가')) - (588 * char1) - 28 * char2
            if not char3:
                separation_list.append([CHOSUNG[char1], JUNGSUNG[char2]])
            else:
                JONGSUNG[char3] = separate_double_consonant(char3)      # 종성의 쌍자음을 각각의 자음으로 분리
                separation_list.append([CHOSUNG[char1], JUNGSUNG[char2], *JONGSUNG[char3]])
        else:
            separation_list.append([word])
    return separation_list


def check_abbreviation_1(jamo, i):    # 약어 검사 함수
    abb_list = []
    for j in range(len(abbreviation_1)):
        if abbreviation_1[j][0:len(abbreviation_1[j])] == jamo[i:i + len(abbreviation_1[j])]:
            if not j:
                abb_list = [[1, 0, 0, 0, 0, 0], [0, 1, 1, 0, 1, 0]]   # 그래서
            elif j == 1:
                abb_list = [[1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0]]   # 그러나
            elif j == 2:
                abb_list = [[1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0]]   # 그러면
            elif j == 3:
                abb_list = [[1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 1]]   # 그러므로
                return 4, abb_list
            elif j == 4:
                abb_list = [[1, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0]]   # 그런데
            elif j == 5:
                abb_list = [[1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 1]]   # 그리고
            else:
                abb_list = [[1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 1]]   # 그리하여
                return 4, abb_list
            return 3, abb_list
    return 0, abb_list


def check_abbreviation_2(jamo, i):      # 약자 검사 함수
    abb_list = []
    for j in range(len(abbreviation_2)):
        for k in range(len(jamo[i])):
            if abbreviation_2[j] == jamo[i][k:k + len(abbreviation_2[j])]:
                if 11 <= j <= 24:
                    if j == 11:
                        abb_list = [1, 1, 0, 1, 0, 1]  # ㅓㄱ
                    elif j == 12:
                        abb_list = [0, 1, 1, 1, 1, 1]  # ㅓㄴ
                    elif j == 13:
                        abb_list = [0, 1, 1, 1, 1, 0]  # ㅓㄹ
                    elif j == 14:
                        abb_list = [1, 0, 0, 0, 0, 1]  # ㅕㄴ
                    elif j == 15:
                        abb_list = [1, 0, 1, 1, 0, 1]  # ㅕㄹ
                    elif j == 16:
                        abb_list = [1, 1, 1, 1, 0, 1]  # ㅕㅇ
                    elif j == 17:
                        abb_list = [1, 1, 0, 0, 1, 1]  # ㅗㄱ
                    elif j == 18:
                        abb_list = [1, 0, 1, 1, 1, 1]  # ㅗㄴ
                    elif j == 19:
                        abb_list = [1, 1, 1, 1, 1, 1]  # ㅗㅇ
                    elif j == 20:
                        abb_list = [1, 1, 1, 1, 0, 0]  # ㅜㄴ
                    elif j == 21:
                        abb_list = [1, 1, 1, 0, 1, 1]  # ㅜㄹ
                    elif j == 22:
                        abb_list = [1, 0, 0, 1, 1, 1]  # ㅡㄴ
                    elif j == 23:
                        abb_list = [0, 1, 1, 0, 1, 1]  # ㅡㄹ
                    else:
                        abb_list = [1, 1, 1, 1, 1, 0]  # ㅣㄴ
                    return 1, abb_list
                else:
                    if not j:
                        abb_list = [1, 1, 1, 0, 0, 1]  # 가
                    elif j == 1:
                        abb_list = [1, 1, 0, 0, 0, 0]  # 나
                    elif j == 2:
                        abb_list = [0, 1, 1, 0, 0, 0]  # 다
                    elif j == 3:
                        abb_list = [1, 0, 0, 1, 0, 0]  # 마
                    elif j == 4:
                        abb_list = [0, 1, 0, 1, 0, 0]  # 바
                    elif j == 5:
                        abb_list = [1, 0, 1, 0, 1, 0]  # 사
                    elif j == 6:
                        abb_list = [0, 1, 0, 0, 0, 1]  # 자
                    elif j == 7:
                        abb_list = [1, 1, 1, 0, 0, 0]  # 카
                    elif j == 8:
                        abb_list = [1, 0, 1, 1, 0, 0]  # 타
                    elif j == 9:
                        abb_list = [1, 1, 0, 1, 0, 0]  # 파
                    elif j == 10:
                        abb_list = [0, 1, 1, 1, 0, 0]  # 하
                    else:
                        abb_list = [[0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 0]]  # 것
                    return 2, abb_list
    return 0, abb_list


def convert_CHOSUNG_to_Braille(jamo, i):
    braille = []
    if jamo[i][0] == 'ㄱ':
        braille = [0, 0, 0, 1, 0, 0]
    elif jamo[i][0] == 'ㄴ':
        braille = [1, 0, 0, 1, 0, 0]
    elif jamo[i][0] == 'ㄷ':
        braille = [0, 1, 0, 1, 0, 0]
    elif jamo[i][0] == 'ㄹ':
        braille = [0, 0, 0, 0, 1, 0]
    elif jamo[i][0] == 'ㅁ':
        braille = [1, 0, 0, 0, 1, 0]
    elif jamo[i][0] == 'ㅂ':
        braille = [0, 0, 0, 1, 1, 0]
    elif jamo[i][0] == 'ㅅ':
        braille = [0, 0, 0, 0, 0, 1]
    elif jamo[i][0] == 'ㅇ':
        braille = [1, 1, 0, 1, 1, 0]
    elif jamo[i][0] == 'ㅈ':
        braille = [0, 0, 0, 1, 0, 1]
    elif jamo[i][0] == 'ㅊ':
        braille = [0, 0, 0, 0, 1, 1]
    elif jamo[i][0] == 'ㅋ':
        braille = [1, 1, 0, 1, 0, 0]
    elif jamo[i][0] == 'ㅌ':
        braille = [1, 1, 0, 0, 1, 0]
    elif jamo[i][0] == 'ㅍ':
        braille = [1, 0, 0, 1, 1, 0]
    elif jamo[i][0] == 'ㅎ':
        braille = [0, 1, 0, 1, 1, 0]
    elif jamo[i][0] == 'ㄲ':
        braille = [[0, 0, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0]]
    elif jamo[i][0] == 'ㄸ':
        braille = [[0, 0, 0, 0, 0, 1], [0, 1, 0, 1, 0, 0]]
    elif jamo[i][0] == 'ㅃ':
        braille = [[0, 0, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0]]
    elif jamo[i][0] == 'ㅆ':
        braille = [[0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1]]
    elif jamo[i][0] == 'ㅉ':
        braille = [[0, 0, 0, 0, 0, 1], [0, 0, 0, 1, 0, 1]]
    else:
        pass
    return braille


def convert_JUNGSUNG_to_Braille(jamo, i):
    MATCH_H2B_JOONG = {
        u'ㅏ': [[1, 1, 0, 0, 0, 1]],
        u'ㅑ': [[0, 0, 1, 1, 1, 0]],
        u'ㅓ': [[0, 1, 1, 1, 0, 0]],
        u'ㅕ': [[1, 0, 0, 0, 1, 1]],
        u'ㅗ': [[1, 0, 1, 0, 0, 1]],
        u'ㅛ': [[0, 0, 1, 1, 0, 1]],
        u'ㅜ': [[1, 0, 1, 1, 0, 0]],
        u'ㅠ': [[1, 0, 0, 1, 0, 1]],
        u'ㅡ': [[0, 1, 0, 1, 0, 1]],
        u'ㅣ': [[1, 0, 1, 0, 1, 0]],
        u'ㅐ': [[1, 1, 1, 0, 1, 0]],
        u'ㅔ': [[1, 0, 1, 1, 1, 0]],
        u'ㅒ': [[0, 0, 1, 1, 1, 0], [1, 1, 1, 0, 1, 0]],
        u'ㅖ': [[0, 0, 1, 1, 0, 0]],
        u'ㅘ': [[1, 1, 1, 0, 0, 1]],
        u'ㅙ': [[1, 1, 1, 0, 0, 1], [1, 1, 1, 0, 1, 0]],
        u'ㅚ': [[1, 0, 1, 1, 1, 1]],
        u'ㅝ': [[1, 1, 1, 1, 0, 0]],
        u'ㅞ': [[1, 1, 1, 1, 0, 0], [1, 1, 1, 0, 1, 0]],
        u'ㅟ': [[1, 0, 1, 1, 0, 0], [1, 1, 1, 0, 1, 0]],
        u'ㅢ': [[0, 1, 0, 1, 1, 1]],
    }

    MATCH_H2B_JONG = {
        u'ㄱ': [[1, 0, 0, 0, 0, 0]],
        u'ㄴ': [[0, 1, 0, 0, 1, 0]],
        u'ㄷ': [[0, 0, 1, 0, 1, 0]],
        u'ㄹ': [[0, 1, 0, 0, 0, 0]],
        u'ㅁ': [[0, 1, 0, 0, 0, 1]],
        u'ㅂ': [[1, 1, 0, 0, 0, 0]],
        u'ㅅ': [[0, 0, 1, 0, 0, 0]],
        u'ㅇ': [[0, 1, 1, 0, 1, 1]],
        u'ㅈ': [[1, 0, 1, 0, 0, 0]],
        u'ㅊ': [[0, 1, 1, 0, 0, 0]],
        u'ㅋ': [[0, 1, 1, 0, 1, 0]],
        u'ㅌ': [[0, 1, 1, 0, 0, 1]],
        u'ㅍ': [[0, 1, 0, 0, 1, 1]],
        u'ㅎ': [[0, 0, 1, 0, 1, 1]],

        u'ㄲ': [[1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0]],
        u'ㄳ': [[1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0]],
        u'ㄵ': [[0, 1, 0, 0, 1, 0], [1, 0, 1, 0, 0, 0]],
        u'ㄶ': [[0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 1]],
        u'ㄺ': [[0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0]],
        u'ㄻ': [[0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1]],
        u'ㄼ': [[0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0]],
        u'ㄽ': [[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0]],
        u'ㄾ': [[0, 1, 0, 0, 0, 0], [0, 1, 1, 0, 0, 1]],
        u'ㄿ': [[0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1]],
        u'ㅀ': [[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 1, 1]],
        u'ㅄ': [[1, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0]],
        u'ㅆ': [[0, 0, 1, 1, 0, 0]],
    }


def convert_JONGSUNG_to_Braille(jamo, i):
    braille = []
    if jamo[i][0] == 'ㄱ':
        braille = [1, 0, 0, 0, 0, 0]
    elif jamo[i][0] == 'ㄴ':
        braille = [0, 1, 0, 0, 1, 0]
    elif jamo[i][0] == 'ㄷ':
        braille = [0, 1, 0, 1, 0, 0]
    elif jamo[i][0] == 'ㄹ':
        braille = [0, 0, 0, 0, 1, 0]
    elif jamo[i][0] == 'ㅁ':
        braille = [1, 0, 0, 0, 1, 0]
    elif jamo[i][0] == 'ㅂ':
        braille = [0, 0, 0, 1, 1, 0]
    elif jamo[i][0] == 'ㅅ':
        braille = [0, 0, 0, 0, 0, 1]
    elif jamo[i][0] == 'ㅇ':
        braille = [1, 1, 0, 1, 1, 0]
    elif jamo[i][0] == 'ㅈ':
        braille = [0, 0, 0, 1, 0, 1]
    elif jamo[i][0] == 'ㅊ':
        braille = [0, 0, 0, 0, 1, 1]
    elif jamo[i][0] == 'ㅋ':
        braille = [1, 1, 0, 1, 0, 0]
    elif jamo[i][0] == 'ㅌ':
        braille = [1, 1, 0, 0, 1, 0]
    elif jamo[i][0] == 'ㅍ':
        braille = [1, 0, 0, 1, 1, 0]
    elif jamo[i][0] == 'ㅎ':
        braille = [0, 1, 0, 1, 1, 0]
    elif jamo[i][0] == 'ㄲ':
        braille = [[0, 0, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0]]
    elif jamo[i][0] == 'ㄸ':
        braille = [[0, 0, 0, 0, 0, 1], [0, 1, 0, 1, 0, 0]]
    elif jamo[i][0] == 'ㅃ':
        braille = [[0, 0, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0]]
    elif jamo[i][0] == 'ㅆ':
        braille = [[0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1]]
    elif jamo[i][0] == 'ㅉ':
        braille = [[0, 0, 0, 0, 0, 1], [0, 0, 0, 1, 0, 1]]
    else:
        pass
    return braille

def main():
    i = 0
    jamo = separation_text(input("텍스트 입력 : "))
    print(jamo)
    while not i >= len(jamo):
        if check_abbreviation_1(jamo, i)[0]:                                # 제 7절 약어 - 예외까지 구현 완료
            if jamo[i - 1] == [' '] or not i:
                print(*check_abbreviation_1(jamo, i)[1])
                i += check_abbreviation_1(jamo, i)[0]
                continue

        if check_abbreviation_2(jamo, i)[0]:
            if jamo[i][0] == 'ㅇ':
                print(check_abbreviation_2(jamo, i)[1])
                if len(jamo[i]) == 4:
                    print()
            else:
                print(convert_CHOSUNG_to_Braille(jamo, i))
                print(check_abbreviation_2(jamo, i)[1])
        i += 1


if __name__ == '__main__':
    main()
