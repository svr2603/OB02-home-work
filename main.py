#Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей,
# имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.
#Требования:
#1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе:
# ID, имя и уровень доступа ('user' для обычных сотрудников).
#2.Класс Admin: Этот класс должен наследоваться от класса User.
# Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы add_user и remove_user, которые позволяют добавлять и удалять пользователей
# из списка (представь, что это просто список экземпляров User).
#3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).



class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id  # Уникальный идентификатор пользователя
        self.__name = name  # Имя пользователя
        self.__access_level = 'user'  # Уровень доступа по умолчанию - обычный пользователь

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'  # Уровень доступа для администратора
        self.__user_list = {}  # Словарь для хранения пользователей (ID: User)

    def add_user(self, new_user):
        if new_user.get_user_id() not in self.__user_list:
            self.__user_list[new_user.get_user_id()] = new_user
            print(f"Пользователь {new_user.get_name()} успешно добавлен.")
        else:
            print("Пользователь с таким ID уже существует.")

    def remove_user(self, user_id):
        if user_id in self.__user_list:
            removed_user = self.__user_list.pop(user_id)
            print(f"Пользователь {removed_user.get_name()} успешно удален.")
        else:
            print("Пользователь с таким ID не найден.")

user1 = User("001", 'Иван')
user2 = User("003", "Татьяна")
user3 = User('004', "Василий")
admin1 = Admin("007", "Петр")

admin1.add_user(user1)
admin1.add_user(user2)
admin1.add_user(user3)
admin1.remove_user("001")
