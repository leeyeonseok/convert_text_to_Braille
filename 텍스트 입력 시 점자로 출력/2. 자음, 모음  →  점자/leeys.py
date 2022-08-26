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


def separation_text(input_list):
    separation_list = []
    for word in list(input_list.strip()):
        # 영어인 경우 구분 해서 작성함.
        if '가' <= word <= '힣':
            # 588개 마다 초성이 바뀜.
            char1 = (ord(word) - ord('가')) // 588
            # 중성은 총 28가지 종류
            char2 = ((ord(word) - ord('가')) - (588 * char1)) // 28
            char3 = (ord(word) - ord('가')) - (588 * char1) - 28 * char2
            if not char3:
                separation_list.append([CHOSUNG[char1], JUNGSUNG[char2]])
            else:
                separation_list.append([CHOSUNG[char1], JUNGSUNG[char2], JONGSUNG[char3]])
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


def check_abbreviation_2(jamo, i):
    abb_list = []
    for j in range(len(abbreviation_2)):
        if abbreviation_2[j] == jamo[i][len(jamo[i]) - len(abbreviation_2[j]):len(jamo[i])]:
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
            elif j == 11:
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
            elif j == 24:
                abb_list = [1, 1, 1, 1, 1, 0]  # ㅣㄴ
            else:
                abb_list = [[0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 0]]  # 것
            return 1, abb_list
    return 0, abb_list


def main():
    i = 0
    jamo = separation_text(input("텍스트 입력 : "))
    while not i >= len(jamo):
        if check_abbreviation_1(jamo, i)[0]:
            print(*check_abbreviation_1(jamo, i)[1])
            i += check_abbreviation_1(jamo, i)[0]
            continue
        if check_abbreviation_2(jamo, i)[0]:
            print(check_abbreviation_2(jamo, i)[1])
        i += 1
    print(jamo)


if __name__ == '__main__':
    main()
