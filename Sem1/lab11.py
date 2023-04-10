# Сидоров Максим ИУ7-12Б

# Вариант 7

# Входные данные: массив строк

# Выходные данные: результат операции в соответствии с меню


#Проверка на натуральное положительное неотрицательное число
def IsNumber_int(y):
    if y.isdigit():
        return True
    return False

# Инициализация максимума
def inMax(text):
    len_max = len(text[0])
    for i in text:
        len_max = max(len_max, len(i))
    return len_max

def clear_text(text):
    n = len(text)-1
    row = []
    while n >= 0:
        row = text[n]
        if len(row) == 0:
            del text[n]
            n-=1
        n -= 1
            
def align_right(s, len_max):
    new = ' '.join(s.split())
    new = ' ' * (len_max - len(new)) + new
    return new


def prob(text):
    for i in range(len(text)):
        row = text[i]
        j = 0
        while text[j] == " ":
            text[j] = "-"
            j += 1
        text[i] = row
            
            
def align_width(t):
    text = t
    for i in range(len(text)):
        text[i] = ' '.join(text[i].split())
    maxLen = len(text[0])
    for stroka in text:
        maxLen = max(maxLen, len(stroka))
    for i in range(len(text)):
        if len(text[i]) != maxLen:
            words = text[i].split()  #слова в строке
            if len(words) == 1:
                if (maxLen - len(text[i])) % 2 == 0:
                    text[i] = ' ' * ((maxLen - len(text[i])) // 2) + words[0] + ' ' * ((maxLen - len(text[i])) // 2)
                else:
                    text[i] = ' ' * ((maxLen - len(text[i])) // 2) + words[0] + ' ' * (
                                (maxLen - len(text[i])) // 2 + 1)
            elif len(words) > 1:
                symb_count = 0  #количество не пробелов в строке
                for word in words:
                    symb_count += len(word)
                space_count = (maxLen - symb_count) // (len(words) - 1)  #количество пробелов
                dop = maxLen - symb_count - space_count * (len(words) - 1)  #дополнительные пробелы
                text[i] = words[0]
                for k in range(1, len(words)):  #проходимся по всем словам
                    if dop != 0:
                        text[i] = text[i] + " " * (space_count + 1) + words[k]
                        dop -= 1
                    else:
                        text[i] = text[i] + " " * space_count + words[k]
    return text

def Max_sentence(let):

    letter_low = let.lower()
    letter_up = let.upper()
    puncts = ['.','?','!']
    row = ""
    for i in range(len(text)):
        s = text[i].split()
        for j in range(len(s)):
            row += s[j] + " "
    Max_sent = 0
    cur = ""
    sentence = ""
    Max_string = 0
    for i in range(len(row)):
        if not(row[i] in puncts):
            sentence += row[i]
        else:
            sentence += row[i]
            sentence = str(sentence)
            sentence = sentence.split()
            for j in range(len(sentence)):
                word = sentence[j]
                if word[0] == letter_up or word[0] == letter_low:
                    Max_string += 1
            if Max_string > Max_sent:
                cur = ""
                Max_sent = Max_string
                for h in range(len(sentence)):
                    cur += sentence[h] + " "
                Max_string = 0
            sentence = ""
    if Max_sent == 0:
        print()
        print("В предложениях нет слов на эту букву")
        print()
    else:
        print()
        print(cur)
        print()
    
def change(t, word, word2):
    puncts = [' ', '.', ',', '?', '!']
    text = t
    for line in range(len(text)):
        string = text[line].split()
        #Разделение на слова по пробелам и проверка на длину слов и пунктуацию по краям от слова
        for i in range(len(string)):
            if (word in string[i] and (string[i].find(word) == 0 or string[i][string[i].find(word) - 1] in puncts)
                    and (string[i].find(word) + len(word) == len(string[i])
                         or string[i][string[i].find(word) + len(word)] in puncts)):
                string[i] = string[i].replace(word, word2, 1)
        text[line] = ' '.join(string)
    return text


def prod_quot(a, b, symb):
    if symb == '*':
        return a * b
    return a // b


def slice(s, start, end, left, right, symb):
    text = s
    if end == len(text) - 1:
        if start == 0:
            text = str(prod_quot(int(left[::-1]), int(right), symb))
        else:
            text = text[0:start + 1] + str(prod_quot(int(left[::-1]), int(right), symb))
    else:
        if start == 0:
            text = str(prod_quot(int(left[::-1]), int(right), symb)) + text[end::]
        else:
            text = text[0:start + 1] + str(prod_quot(int(left[::-1]), int(right), symb)) + text[end::]
    return text


def find_expression(s, symb):
    text = s
    k = 0
    numbers = "0123456789"
    while k != len(text) - 1:
        # Умножение
        if text[k] == symb:
            left = None  # Справа от знака
            right = None  # Слева от знака
            start = 0
            end = 0
            if k != 0:
                j = k - 1
                if text[j] == " ":
                    if j != 0:
                        j -= 1
                        while text[j] in numbers:
                            if left is None:
                                left = ""
                            left += text[j]
                            if j == 0:
                                break
                            j -= 1
                elif text[j] in numbers:
                    while text[j] in numbers:
                        if left is None:
                            left = ""
                        left += text[j]
                        if j == 0:
                            break
                        j -= 1
                start = j
            # Нашлась левая часть
            if left is not None:
                j = k + 1
                if text[j] == " ":
                    if j != len(text) - 1:
                        j += 1
                        while text[j] in numbers:
                            if right is None:
                                right = ""
                            right += text[j]
                            if j == len(text) - 1:
                                break
                            j += 1
                elif text[j] in numbers:
                    while text[j] in numbers:
                        if right is None:
                            right = ""
                        right += text[j]
                        if j == len(text) - 1:
                            break
                        j += 1
                end = j
            # Нашлась операция
            if left is not None and right is not None:
                if symb == '*':
                    text = slice(text, start, end, left, right, symb)
                    k = start
                    continue
                elif symb == '/' and int(right) != 0:
                    text = slice(text, start, end, left, right, symb)
                    k = start
                    continue
        k += 1
    return text


def operations_prod_quot(t):
    text = t
    # Проход по строке до символа * или /. И поиск выражения слева и справа от него
    for i in range(len(text)):
        text[i] = find_expression(text[i], '/')
        text[i] = find_expression(text[i], '*')
    return text


def symb_in_sentence(t):
    text = t
    sentence = 1
    punct = ['.', '!', '?']
    d = {}
    flag = True
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j] in punct:
                sentence += 1
                if sentence % 2 == 1 and sentence != 1:
                    flag = False
                    max_val = 0
                    symbol = ''
                    # Прохожусь по словарю и определяю символ
                    for symb, val in d.items():
                        if val > max_val:
                            max_val = val
                            symbol = symb
                    if symbol == ' ':
                        symbol = 'пробел'
                    print(f'Самый часто встречающийся символ в предложении номер {sentence - 1}: {symbol}')
                    d = {}
            if sentence % 2 == 0:
                flag = True
                # Записываю вхождения в словарь
                if d.get(text[i][j]) == None:
                    d.setdefault(text[i][j], 1)
                else:
                    d[text[i][j]] += 1
    if not flag:
        if sentence % 2 != 1:
            max_val = 0
            symbol = ''
            for symb, val in d.items():
                if val > max_val:
                    max_val = val
                    symbol = symb
            if symbol == ' ':
                symbol = 'пробел'
            print(f'Самый часто встречающийся символ в предложении номер {sentence - 1}: {symbol}')



text = [
    "она одна",
    "Она предает нас. Россия одна 6*2 быть спасительницей",
    "Европы. Наш благодетель 4/2 свое высокое призвание и",
    "будет верен ему. Вот",
    "одно, во что я верю."
    ]

len_max = len(text[0])
align = 0  # Выравнивание             
while True:
    len_max = inMax(text)
    #Вывод пунктов меню
    print('''
------------------------------------------------------------------------------
| Выберите операцию, которую применить к массиву:                            |
| 0) Выйти из программы                                                      |
| 1) Выровнять текст по левому краю                                          |
| 2) Выровнять текст по правому краю                                         |
| 3) Выровнять текст по ширине                                               |
| 4) Удалить все вхождения заданного слова                                   |
| 5) Замена одного слова другим во всем тексте                               |
| 6) Вычисление выражений с умножением и делением в тексте                   |
| 7) В каждом четном предложении определить самый часто встречающийся символ |
------------------------------------------------------------------------------
''')
    # Инициализация операции
    operation = str(input("Ведите пункт меню от 0 до 7: "))
    while True:
        if not IsNumber_int(operation):
            print("Пунк меню должен быть целым неотрицательным числом")
            operation = str(input("Ведите пунк меню от 0 до 7: "))
        elif not(0 <= int(operation) <= 7):
            print("Существуют пункты меню только от 0 до 7")
            operation = str(input("Ведите пунк меню от 0 до 7: "))
        else:
            break
    operation = int(operation)

    if operation == 0:
        break

    if operation == 1:

        align = 0
        for i in range(len(text)):
            text[i] = ' '.join(text[i].split())
            
    elif operation == 2:
        
        align = 1
        for i in range(len(text)):
            text[i] = align_right(text[i], len_max)
            
    elif operation == 3:
        
        align = 2
        text = align_width(text)
        
    elif operation == 4:
        
        word = input('Введите слово, которое следует убрать: ')
        text = change(text, word, ' ')
        # Выравнивание
        len_max = inMax(text)
        for i in range(len(text)):
            text[i] = ' '.join(text[i].split())
        clear_text(text)
        if align == 1:
            for i in range(len(text)):
                text[i] = align_right(text[i], len_max)
        if align == 2:
            text = align_width(text)
            
    elif operation == 5:
        
        word = input('Введите слово, которое следует заменить: ')
        word_on_change = input('Введите слово, на которое следует заменить: ')
        text = change(text, word, word_on_change)
        # Выравнивание
        len_max = inMax(text)
        for i in range(len(text)):
            text[i] = ' '.join(text[i].split())
        clear_text(text)
        if align == 1:
            for i in range(len(text)):
                text[i] = align_right(text[i], len_max)
        if align == 2:
            text = align_width(text)
            
    elif operation == 6:

        text = operations_prod_quot(text)
        #Выравнивание
        for i in range(len(text)):
            text[i] = ' '.join(text[i].split())
        len_max = inMax(text)
        if align == 1:
            for i in range(len(text)):
                text[i] = align_right(text[i], len_max)
        if align == 2:
            text = align_width(text)
        
    elif operation == 7:
        
        symb_in_sentence(text)

    for i in text:
        len_max = max(len_max, len(i))
        print(i)