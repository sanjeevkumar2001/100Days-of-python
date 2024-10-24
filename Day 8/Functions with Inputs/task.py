def calculate_love_score(name1, name2):
    count = 0

    for check in "true":

        if check in name1.lower():
            count += 1

        if check in name2.lower():
            count += 1

    count1 = 0
    for check1 in "love":
        if check1 in name1.lower():
            count1 += 1
        if check1 in name2.lower():
            count1 += 1

    print(f"{count}" + f"{count1}")


calculate_love_score(name1="SWATHA", name2="sanjeevkumar")
