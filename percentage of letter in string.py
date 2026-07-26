def percentageletterinstring(s, letter):
    count = 0
    for ch in s:
        if ch == letter:
            count += 1
    percentage = (count * 100) // len(s)

    return percentage
print(percentageletterinstring("foobar", "o")) 
print(percentageletterinstring("jjjj", "k"))   