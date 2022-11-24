# test_list = [[0, 1, 1, 1, 0, 0], [1, 0, 0, 1, 1, 1], [0, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 1], [0, 0, 0, 1, 0, 0], [1, 0, 0, 1, 1, 0], [1, 1, 0, 0, 0, 0], [1, 0, 0, 1, 1, 1]]
# test_list.reverse()
# states=[]
# for braille in test_list:
#     #print(braille)
#     print(braille)
#     braille.extend([0,0])
#     print(braille)
#     states.extend(braille)
# print(states)
#
# def get_states(test_list):
#     test_list.reverse()
#     states=[]
#     for braille in test_list:
#         braille.extend([0, 0])
#         states.extend(braille)
#     return states
#
# print(get_states(test_list))

# def list_chunk(lst):
#     return [lst[i:i + 24] for i in range(0, len(lst), 24)]
#
# print(list_chunk([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))

# def Make_content_list(lst):
#     states = [lst[i:i + 24] for i in range(0, len(lst), 24)]
#     return states
#
# content_list = Make_content_list([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
# print(content_list)

def Make_states(lst):  # Plus의 이중 리스트의 결과를 받아서 1중 리스트로 바꿔주는 함수.
    lst.reverse()
    states = []
    for braille in lst:
        # print(braille)
        braille.extend([0, 0])
        states.extend(braille)
    return states
print(Make_states([[0, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]]))