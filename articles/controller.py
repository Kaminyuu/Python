from view import UserInterface


class Controller:
    def __init__(self):
        self.article_model = None  # model
        self.user_interface = UserInterface()  # view

    def run(self):
        answer = None
        while answer != "q":
            answer = self.user_interface.wait_user_answer()



