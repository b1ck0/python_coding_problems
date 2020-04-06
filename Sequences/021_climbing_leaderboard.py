def dense_ranking(array):
    current_rank = 1
    ranking_vector = [current_rank]
    for i in range(1, len(array)):
        if array[i] == array[i - 1]:
            ranking_vector.append(current_rank)
        else:
            current_rank += 1
            ranking_vector.append(current_rank)

    return ranking_vector


def linear_search_greater(array, number, start_from=None):
    if start_from is None:
        start_from = len(array) - 1

    if array[0] <= number:
        return 0

    if array[-1] >= number:
        return len(array)

    while array[start_from] <= number:
        start_from -= 1

    return start_from + 1


def climbing_leaderboard(leaderboard_scores: list, alice_scores: list) -> list:
    """
    https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
    leaderboard positions in desnse ranking
    :param leaderboard_scores: scores in descending order
    :param alice_scores: scores in ascending order
    :return: position_i for i in alice_scores after adding it to leaderboard_scores
    """
    last_index = None
    alice_rankings = []

    standalone_rankings = dense_ranking(leaderboard_scores)
    last_index = None

    while len(alice_scores):
        current_score = alice_scores.pop(0)
        i = last_index if last_index is not None else len(standalone_rankings) - 1
        if leaderboard_scores[i - 1] > current_score:
            alice_rankings.insert(0, standalone_rankings[i] - 1)

    return alice_rankings


if __name__ == "__main__":
    print(climbing_leaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
    print(climbing_leaderboard([1], [1, 1]))
    print(climbing_leaderboard(
        [998, 995, 995, 991, 989, 989, 984, 979, 968, 964, 955, 955, 947, 945, 942, 934, 933, 930, 928, 927, 918, 916,
         905, 900, 898, 895, 895, 895, 892, 887, 882, 881, 878, 876, 872, 872, 858, 856, 846, 844, 839, 823, 808, 806,
         804, 800, 799, 794, 793, 789, 784, 772, 766, 765, 764, 762, 762, 759, 757, 751, 747, 745, 738, 725, 720, 708,
         706, 703, 699, 697, 693, 691, 690, 685, 682, 677, 662, 661, 656, 648, 642, 641, 640, 634, 632, 625, 623, 618,
         618, 617, 601, 601, 600, 591, 585, 583, 578, 552, 550, 550, 546, 543, 539, 509, 505, 503, 503, 494, 486, 474,
         472, 472, 472, 468, 467, 464, 439, 438, 434, 434, 427, 421, 420, 405, 399, 395, 392, 388, 386, 384, 377, 374,
         368, 356, 350, 344, 342, 341, 337, 331, 298, 296, 296, 294, 290, 260, 259, 248, 245, 244, 244, 233, 228, 215,
         211, 210, 206, 202, 201, 189, 186, 181, 178, 168, 163, 162, 161, 159, 151, 147, 143, 142, 142, 141, 139, 132,
         130, 128, 125, 125, 120, 112, 111, 95, 92, 91, 88, 81, 69, 66, 63, 48, 44, 20, 18, 17, 14, 8, 1, 1],
        [18, 31, 38, 126, 152, 170, 198, 199, 202, 243, 369, 376, 376, 408, 560, 572, 614, 665, 666, 942]))
