key = input('Введите ключ(name или account):').lower()

account1 = {'login': 'Ivan', 'password': 'q1'}
account2 = {'login': 'Petr', 'password': 'q2'}
account3 = {'login': 'Olga', 'password': 'q3'}
account4 = {'login': 'Anna', 'password': 'q4'}


user1 = {'name': 'Иван', 'age': '20', 'account': {'login': 'Ivan', 'password': 'q1'}}
user2 = {'name': 'Пётр', 'age': '25', 'account': {'login': 'Petr', 'password': 'q2'}}
user3 = {'name': 'Ольга', 'age': '18', 'account': {'login': 'Olga', 'password': 'q3'}}
user4 = {'name': 'Анна', 'age': '27', 'account': {'login': 'Anna', 'password': 'q4'}}


name = f'''значение ключа name для юзера 1 = {user1['name']}
значение ключа name для юзера 2 = {user2['name']}
значение ключа name для юзера 3 = {user3['name']}
значение ключа name для юзера 4 = {user4['name']}
'''
#создано для отображения введенного пользователем ключа


account = f'''значение ключа account для юзера 1 = {account1['login']}
значение ключа account для юзера 2 = {account2['login']}
значение ключа account для юзера 3 = {account3['login']}
значение ключа account для юзера 4 = {account4['login']}
'''
#смотреть комент выше


if key == 'name':
    print(name)
elif key == 'account':
    print(account)
else:
    print("Введенный ключ не найден")


user_list = [user1, user2, user3, user4]

num = input('Введите порядковый номер:')

summ = (int(user1['age']) + int(user2['age']) + int(user3['age']) + int(user4['age']))/4

try:
    x = user_list[int(num)+ int(-1)]
    number = f'''Данные по юзеру № {num}:
имя: {x['name']}
возраст: {x['age']}
логин: {x['account']['login']}
пароль: {x['account']['password']}
Cредний возраст пользователей: {summ}
'''
    print(number)
except IndexError:
    print('Пользователь с указанным номером не найден')


add = int(input('Введите номер пользователя, которого нужно перенести в конец:'))
print ('Список до изменений:')
print (user_list)
print(f"Пользователь с именем {user_list[add + int(-1)]['name']} перемещен в конец.\nСписок после изменений:")
element = user_list.append(user_list.pop(add + int(-1)))
print (user_list)