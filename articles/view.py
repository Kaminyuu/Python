class UserInterface:
    def wait_user_answer(self):
        print(" Ввод пользовательских данных ".center(50, "="))
        print("Действие со статьями:")
        print("q - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        print("=" * 50)
        return user_answer
