def dist(a, b):
    def rec(i, l):
        if i == 0 or l == 0:
            return max(i, l) # если одна из строк пустая, то расстояние равно длине другой
        elif a[i-1] == b[l-1]:
            return rec(i-1, l-1) # если последние символы одинаковы - опускаем их
        else: 
            return 1 + min(
                rec(i, l-1), # удаление символа
                rec(i-1, l), # вставка символа
                rec(i-1, l-1) # замена символа
            )
    return rec(len(a), len(b))

str1 = 'Преветабстр'
str2 = 'Приветики'
print(dist(str1, str2))