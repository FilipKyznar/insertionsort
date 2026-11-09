cisla = [5, 2, 4, 1]

def insertion_sort(cisla):
    n = len(cisla)
    for i in range(1, n):
        klic = cisla[i]
        j = i - 1
        while j >= 0 and cisla[j] > klic:
            cisla[j + 1] = cisla[j]
            j -= 1
        cisla[j + 1] = klic
        print(cisla)

    return print(cisla)

insertion_sort(cisla)