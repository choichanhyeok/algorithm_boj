def get_melon_best_album(genre_array, play_array):
    n = len(genre_array)
    genre_play_dict = {}
    genre_index_dict = {}

    #TODO 1. 청취 시간 별로 장르 순서 정하기
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]

        if genre not in genre_play_dict:
            genre_play_dict[genre] = play
            genre_index_dict[genre] = [[i, play]]
        else:
            genre_play_dict[genre] += play
            genre_index_dict[genre].append([i, play])

    sorted_genre_play_dict = sorted(genre_play_dict.items(), key= lambda item: item[1], reverse= True)
    #TODO 2. 최대 2개 까지 reuslt에 추가. 단, index 순으로 정렬된 리스트에 기인
    result = []
    for genre, _value in sorted_genre_play_dict:
        sorted_genre_index_dict = sorted(genre_index_dict[genre], key=lambda item: item[1], reverse=True)

        for i in range(len(sorted_genre_index_dict)):
            if i > 1:
                break
            result.append(sorted_genre_index_dict[i][0])
    return result



















# def get_melon_best_album(genre_array, play_array):
#     n = len(genre_array)
#     genre_cout_dict = {}
#     genre_index_dict = {}
#
#     #TODO 1. 가장 많이 재생된 장르를 먼저 수록
#     for i in range(n):
#         genre = genre_array[i]
#         play = play_array[i]
#
#         if genre not in genre_cout_dict:
#             genre_cout_dict[genre] = play
#             genre_index_dict[genre] = [[i, play]]
#         else:
#             genre_cout_dict[genre] += play
#             genre_index_dict[genre].append([i, play])
#
#     #TODO 2. 장르 내에서 많이 재생된 노래를 먼저 수록
#     sorted_genre_cout_array = sorted(genre_cout_dict.items(), key=lambda item: item[1], reverse=True)
#
#     result = []
#     #TODO 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록
#     for genre, _value in sorted_genre_cout_array:
#         index_count_array = genre_index_dict[genre]
#
#         sorted_index_count_array = sorted(index_count_array, key=lambda item: item[1], reverse=True)
#
#         for i in range(len(sorted_index_count_array)):
#             if i > 1:
#                 break
#             result.append(sorted_index_count_array[i][0])
#     return result
#
#
#























# def get_melon_best_album(genre_array, play_array):
#     n  = len(genre_array)
#     genre_total_play_dicy = {}
#     genre_index_play_array_dict = {}
#
#     for i in range(n):
#         genre = genre_array[i]
#         play = play_array[i]
#
#         if genre not in genre_total_play_dicy:
#             genre_total_play_dicy[genre] = play
#             genre_index_play_array_dict[genre] = [[i, play]]
#         else:
#             genre_total_play_dicy[genre] += play
#             genre_index_play_array_dict[genre].append([i, play])
#
#     sorted_genre_play_array = sorted(genre_total_play_dicy.items(), key=lambda item: item[1], reverse=True)
#
#     result = []
#     for genre, _value in sorted_genre_play_array:
#         index_play_array = genre_index_play_array_dict[genre]
#         sorted_by_play_and_index_play_index_array = sorted(index_play_array, key=lambda item: item[1], reverse=True)
#         for i in range(len(sorted_by_play_and_index_play_index_array)):
#             if i > 1:
#                 break
#             result.append(sorted_by_play_and_index_play_index_array[i][0])
#     return result



print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))