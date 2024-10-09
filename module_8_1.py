def add_everything_up(a, b):
    sum_ = 0
    try:
        sum_ = round((a + b), 3)  # без "round" выдает много знаков после запятой
    except TypeError:
        sum_ = str(a) + str(b)
    finally:
        return sum_


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))


print()
print('Немного юмора в стиле лектора, но с пользой :)')
      # Развернутый вариант с комментариями в ущерб краткости кода - в учебных целях:
      # добавлен 4-й вариант (когда оба слагаемых не числа) и комментарии в зависимости от положения слагаемого,
      # не являющегося числом (первое, второе, оба или наоборот: оба слагаемых - числа)
print()
def add_everything_up(a, b):
    sum_ = 0
    try:
        sum_ = round((a + b), 3)  # без "round" выдает много знаков после запятой
    except TypeError as exc:
        if isinstance(a, (int, float)):
            comment = f'Программисты могут всё - и даже использовать {exc}:'
        elif isinstance(b, (int, float)):
            comment = f'Программисты могут всё - и даже если {exc}:'
        else:
            comment = f'Программисты могут складывать, даже если {exc}:'
        sum_ = f'{comment}\n{str(a) + str(b)}'
    else:
        comment = f'Складывать числа? Проще простого:'
        sum_ = f'{comment}\n{str(a) + str(b)}'
    finally:
        return sum_


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up('груша', 'слива'))  # для полноты описания исключений при суммировании (вовсе нет чисел)
