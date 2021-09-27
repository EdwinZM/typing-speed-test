import tkinter as tk
import random
import time

window = tk.Tk()
window.title("Typing Speed Test")
window.minsize(width="1000", height="700")
window.config(padx=20, pady=20)
window.grid_columnconfigure(0, weight=1)

sample_texts = {
    "text1": "Never thought I'd make it. Three days grade school,\n three days high school. Those were awkward.\n Three days college. I'm glad I took a day and hitchhiked around the hive.\n You did come back different.",
    "text2": "Tonight we're talking to Barry Benson. Did you ever think, I'm a kid from the hive.\n I can't do this? Bees have never been afraid to change the world. What about Bee Columbus? Bee Gandhi? Bejesus?\n Where I'm from, we'd never sue humans. We were thinking of stickball or candy stores. ",
    "text3": "I pick up some pollen here, sprinkle it over here. Maybe a dash over there, a pinch on that one. See that?\n It's a little bit of magic. That's amazing. Why do we do that? That's pollen power.\nMore pollen, more flowers, more nectar, more honey for us."
}


title_label = tk.Label(text="Welcome to the Typing Speed Text!", font=("Helvetica", 30, "bold"))
title_label.grid(row=0, column=0)

explanation_label = tk.Label(text="Test out your typing speed with a random text sample.", font=("Helvetica", 15))
explanation_label.grid(row=1, column=0, columnspan=2, pady=80)

def start_test():
    global sample_texts
    explanation_label.destroy
    start_button.destroy()
    key = random.choice(list(sample_texts.keys()))
    text = sample_texts[key]

    text_array = text.split(" ")

    word_count = 0

    for word in text_array:
        word_count += 1

    t0 = time.time()
    
    text_label = tk.Label(text=text, font=("Helvetica", 20, "italic"))
    text_label.grid(row=2, column=0, columnspan=2)

    answer_entry = tk.Entry(text="Type the text here!")
    answer_entry.grid(row=3, column=0, columnspan=2, padx=100, pady = 80)

    def take_time(answer_entry):
        t1 = time.time()
        time_taken = int(t1 - t0)

        answer_list = answer_entry.get().split(" ")
        answer_count = 0
        for word in answer_list:
            answer_count += 1

        wordPM = int((answer_count/time_taken) * 60)

        finish_button.destroy()
        text_label.destroy()
        answer_entry.destroy()
        explanation_label.destroy()

        congrats_label = tk.Label(text=f"Congratulations!\n You can type:\n{wordPM} words per minute", font=("Helvetica", 30, "bold"))
        congrats_label.grid(row=4, column=0)
        

    finish_button = tk.Button(text="Finish Test", command= lambda: take_time(answer_entry))
    finish_button.grid(row=4, column=0)

start_button = tk.Button(text="Start Test", command=start_test)
start_button.grid(row=2, column=0)


window.mainloop()