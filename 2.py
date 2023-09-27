'''
 Напишите функцию, которая будет принимать один аргумент. Если в
функцию передаётся множество, то найти сумму всех элементов.
Если список, то найти произведение между первым и вторым
отрицательными элементами. Максимальный и минимальный элемент
поменять местами.
Число – сумму цифр.
Строка – вывести на экран самое длинное слово.
Сделать проверку со всеми этими случаями.
'''
def process_input(data):
    if isinstance(data, set):
        return sum(data)
    elif isinstance(data, list):
        max_value = max(data)
        max_index = data.index(max_value)
        min_value = min(data)
        min_index = data.index(min_value)
        data[max_index], data[min_index] = data[min_index], data[max_index]
        print("Новый список: ", data)
        negative_numbers = [num for num in data if num < 0]
        if len(negative_numbers) >= 2:
            return negative_numbers[0] * negative_numbers[1]
        else:
            return "Not enough negative numbers"
    elif isinstance(data, int):
        return sum(int(digit) for digit in str(data))
    elif isinstance(data, str):
        words = data.split()
        longest_word = max(words, key=len)
        return longest_word
    else:
        return "Invalid input"
set_input = {1, 2, 3, 4, 5}
print("Сумма всех элементов множества: ", process_input(set_input))

list_input = [-2, 4, -6, 8, -10]
print("Произведение первых двух отрицательных элементов: ", process_input(list_input))

number_input = 12345
print("Сумма цифр числа: ", process_input(number_input))

string_input = "Мышка кот собака рысь"
print("Самое длинное слово: ", process_input(string_input))