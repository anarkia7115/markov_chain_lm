import random
def markov_o1(source_text:str, generate_size):
    letter = source_text[random.randint(0, len(source_text))]
    return_string = letter
    for _ in range(generate_size):
        rand_start = random.randint(0, len(source_text))
        letter_pos = source_text.find(letter, rand_start) + 1
        print(source_text[letter_pos-10:letter_pos-1] + " [" + 
            source_text[letter_pos-1:letter_pos+1] + "] " + 
            source_text[letter_pos+1:letter_pos+10])
        if letter_pos == 0:
            letter_pos = random.randint(0, len(source_text))
            print("next letter is choosed randomly, consider more text source")
        letter = source_text[letter_pos]
        return_string += letter
    return return_string
