class QuizBrain:

    # konstruktor
    def __init__(self, q_list):
        self.q_list = q_list
        self.question_number = 0
        self.score = 0

    # Přiřazení aktuální otázky, odpověď uživatele a volání funkce na kontrolu odpovědi
    def evaluate_question(self, index):
        current_question = self.q_list[index]
        self.question_number += 1
        user_answer = input(f"\n\nOtázka č. {self.question_number}: {current_question.text} (ano/ne): ")
        self.check_answer(user_answer, current_question.answer, current_question.correct_answer)

    # Kontrola odpovědi uživatele
    def check_answer(self, user_ansr, correct_ansr, correct_ansr_text):
        if user_ansr.lower() == correct_ansr.lower():
            print("\nUhádli jste! Odpověď je správná")
            self.score += 1
            print(f"Vaše skóre je: {self.score} z {self.question_number} ({round((self.score/self.question_number)*100)} %)")
        else:
            print("\nOdpověď je bohužel špatná")
            if correct_ansr_text != "":
                print(f"Správná odpověď: {correct_ansr_text}")
            print(f"Vaše skóre je: {self.score} z {self.question_number} ({round((self.score/self.question_number)*100)} %)")
        input("Stiskni ENTER pro pokračování...")

    # Kontrola duplicity otázky v daném kvízu
    def compare_question_numbers(self, number, num_list):
        if num_list == []:
            num_list.append(number)
            return True
        else:
            for one_number in num_list:
                if one_number == number:
                    return False
            num_list.append(number)
            return True

        

