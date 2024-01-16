from collections import Counter

import numpy as np
from fuzzywuzzy import fuzz


def calculate_similarity(string_list):
    n = len(string_list)
    similarity_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1, n):
            similarity = fuzz.token_set_ratio(string_list[i], string_list[j])
            similarity_matrix[i, j] = similarity
            similarity_matrix[j, i] = similarity

    average_similarity = np.mean(similarity_matrix)
    return round(average_similarity / 100, 2)


def find_most_common_string(string_list):
    counter = Counter(string_list)
    if most_common := counter.most_common(1):
        return most_common[0][0]
    else:
        return "Unknown"


def find_most_common_string2(string_list):
    counter = Counter(string_list)
    if most_common := counter.most_common(1):
        most_common_string, count = most_common[0]
        confidence = count / len(string_list) * 100
        return most_common_string, round(confidence, 2)
    else:
        return "Unknown", 0


string_lists = [
    ["Sandal Plc", "IEEE Registration Authority", "Sandal Plc"],
    ["Espressif", "Espressif Inc.", "Espressif Inc."],
    ["Ubiquiti Networks", "Ubiquiti Inc", "Ubiquiti Inc"],
    ["Tuya Smart", "Tuya Smart Inc.", "Tuya Smart Inc."],
    ["iRobot", "iRobot Corporation", "iRobot Corporation "],
    [
        "Seongji Industry Company",
        "Seongji Industry Company",
        "Seongji Industry Company",
    ],
    ["iRobot", "Ubiquiti Networks", "IEEE Registration Authority"],
    [
        "iRobot",
        "Ubiquiti Networks",
        "IEEE Registration Authority",
        "IEEE Registration Authority",
        "IEEE Registration Authority",
    ],
]

for string_list in string_lists:
    print(calculate_similarity(string_list))
    print(find_most_common_string(string_list))
    print(find_most_common_string2(string_list))
    print()
