
def results(n):
    result = []
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if (i + j) <= n and n % (i + j) == 0:
                result.append(f"{i}{j}")

    return"".join(result)


for i in range(3, 21):
    print(f"{i} - {results(i)}")




