def sortPeople(names, heights):
    combined = list(zip(heights,names))
    combined.sort(reverse=True)
    result = []
    for height, name in combined:
        result.append(name)
    return result
names = ["Mary","John","Emma"]
heights = [180,165,170]
sorted_names = sortPeople(names, heights)
print("Sorted Names by Height (Descending):", sorted_names)