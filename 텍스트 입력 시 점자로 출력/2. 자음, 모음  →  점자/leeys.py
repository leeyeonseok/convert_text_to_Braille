abbreviation = [[['ㄱ', 'ㅡ'], ['ㄹ', 'ㅐ'], ['ㅅ', 'ㅓ']], [['ㄱ', 'ㅡ'], ['ㄹ', 'ㅓ'], ['ㄴ', 'ㅏ']],
                [['ㄱ', 'ㅡ'], ['ㄹ', 'ㅓ'], ['ㅁ', 'ㅕ', 'ㄴ']], [['ㄱ', 'ㅡ'], ['ㄹ', 'ㅓ'], ['ㅁ', 'ㅡ'], ['ㄹ', 'ㅗ']],
                [['ㄱ', 'ㅡ'], ['ㄹ', 'ㅓ', 'ㄴ'], ['ㄷ', 'ㅔ']], [['ㄱ', 'ㅡ'], ['ㄹ', 'ㅣ'], ['ㄱ', 'ㅗ']],
                [['ㄱ', 'ㅡ'], ['ㄹ', 'ㅣ'], ['ㅎ', 'ㅏ'], ['ㅇ', 'ㅕ']]]
                # 그래서, 그러나, 그러면, 그러므로, 그런데, 그리고, 그리하여
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


def check_abbreviation(jamo, i):    # 약어 검사 함수
    abb_list = []
    for j in range(7):
        if abbreviation[j][0:len(abbreviation[j])] == jamo[i:i + len(abbreviation[j])]:
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


def main():
    i = 0
    jamo = separation_text(input("텍스트 입력 : "))
    while not i == len(jamo):
        if check_abbreviation(jamo, i)[0]:
            print(*check_abbreviation(jamo, i)[1])
            i += check_abbreviation(jamo, i)[0]
            continue
        i += 1


if __name__ == '__main__':
    main()
