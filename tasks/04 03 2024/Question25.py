# Quiz Game in Python 



class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [

    "India is a federal union comprising twenty-eight states and how many union territories??\nA) 8\nB) 7\nC) 6 \nD) 9\n",

    "Who wrote 'Romeo and Juliet'?\n(a) Charles Dickens\n(b) Jane Austen\n(c) William Shakespeare\n(d) Mark Twain\n",

    "What is 2 + 2?\n(a)3\n(b)4\n(c)5\n(d)6\n",

    "What is the largest mammal?\n(a) Elephant\n(b) Giraffe\n(c) Blue Whale\n(d) Hippopotamus\n",

    "Who painted the Mona Lisa?\n(a) Michelangelo\n(b) Leonardo da Vinci\n(c) Pablo Picasso\n(d) Vincent van Gogh\n",

    "What is the chemical symbol for water?\n(a) O2\n(b) H2O\n(c) CO2\n(d) NaCl\n",

    "Which planet is known as the Red Planet?\n(a) Venus\n(b) Jupiter\n(c) Mars\n(d) Saturn\n",

    "What is the tallest mountain in the world?\n(a) K2\n(b) Mount Everest\n(c) Kilimanjaro\n(d) Mont Blanc\n",

    "What is the currency of Japan?\n(a) Yen\n(b) Won\n(c) Yuan\n(d) Euro\n",

    "Who is the current President of the United States?\n(a) Barack Obama\n(b) Joe Biden\n(c) Donald Trump\n(d) George W. Bush\n"
]

questions_list = [
    Question(questions[0], 'a'),
    Question(questions[1], 'c'),
    Question(questions[2], 'b'),
    Question(questions[3], 'c'),
    Question(questions[4], 'b'),
    Question(questions[5], 'b'),
    Question(questions[6], 'c'),
    Question(questions[7], 'b'),
    Question(questions[8], 'a'),
    Question(questions[9], 'b')
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            score += 1
    return score

if __name__ == "__main__":
    print("Welcome to the Quiz Game!")
    print("Please select the correct option (a, b, c, d) for each question.")
    print("")

    user_score = run_quiz(questions_list)

    print("")
    print("Quiz complete!")
    print(f"You got {user_score} out of {len(questions_list)} questions correct.")
