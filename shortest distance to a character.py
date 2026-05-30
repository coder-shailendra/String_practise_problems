def shortest_distance_to_a_character(s, c):
    result = []
    for i in range(len(s)):
        min_distance = len(s)
        for j in range(len(s)):
            if s[j] == c:
                distance = abs(i - j)
                min_distance = min(min_distance, distance)
        result.append(min_distance)
    return result
s = "loveleetcode"
c = "e"
print(shortest_distance_to_a_character(s, c))