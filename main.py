from data import question_data
from question import Question
from quiz_brain import QuizBrain
from world_logo import world_logo
import random

print("Vítejte v Geografickém kvízu")
print(world_logo)
print("Můžeme začít")
print()

question_list = []
question_count = 0

# Každou položku v dictionary questiona_data převedeme na objekt
for one_item in question_data:
    one_object = Question(one_item["text"], one_item["answer"], one_item["correct answer"])
    question_list.append(one_object)

# Definice náhodného čísla, který reprezentuje index objektu v question_list
random_number = 0
# Definice prázdného listu, který postupně naplníme objekty s náhodnými indexy
random_num_list = []
# Instance třídy QuizBrain
quiz = QuizBrain(question_list)
# Každý kvíz obsahuje 10 náhodně vygenerovaných otázek
while quiz.question_number < 10:
    random_number = random.randint(0, len(question_list)-1)
    # Kontrola duplicity otázky
    if quiz.compare_question_numbers(random_number, random_num_list) == True:
        # Vyhodnocení odpovědi na otázku
        quiz.evaluate_question(random_number)
        question_count += 1
print("\n\nKonec kvízu")
print(f"Váš konečný výsledek: {quiz.score} z {question_count} ({round((quiz.score / question_count) * 100)} %)")


