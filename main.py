cisla = [5, 2, 4, 1]  # Seznam čísel, která chceme seřadit

def insertion_sort(cisla):  # Vytvoření funkce pro řazení čísel
    n = len(cisla)  # Zjistí počet čísel v seznamu

    for i in range(1, n):  # Prochází seznam od druhého čísla
        klic = cisla[i]  # Uloží aktuální číslo, které chceme zařadit
        j = i - 1  # Nastaví pozici před aktuálním číslem

        while j >= 0 and cisla[j] > klic:  # Kontroluje, jestli je předchozí číslo větší než klíč
            cisla[j + 1] = cisla[j]  # Posune větší číslo o jednu pozici doprava
            j -= 1  # Posune se o jednu pozici doleva

        cisla[j + 1] = klic  # Vloží klíč na správné místo
        print(cisla)  # Vypíše seznam po každém průchodu

    return print(cisla)  # Vypíše konečný seřazený seznam

insertion_sort(cisla)  # Zavolá funkci a předá jí seznam čísel