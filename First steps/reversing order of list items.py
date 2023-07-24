def digitize(n):
    draft_list = []
    for i in reversed(str(n)):
        draft_list.append(int(i))
    return draft_list


print(digitize(123456))
