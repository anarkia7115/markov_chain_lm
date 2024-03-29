import random
def markov_o1_bf(source_text:str, generate_size):
    # letter = source_text[random.randint(0, len(source_text))]
    letter = ". "
    return_string = ""
    for _ in range(generate_size):
        rand_start = random.randint(0, len(source_text))
        letter_pos = source_text.find(letter, rand_start) + len(letter)
        if letter_pos - len(letter) < 0:
            letter_pos = random.randint(0, len(source_text))
            print("next letter is choosed randomly, consider more text source")

        print(source_text[letter_pos-10:letter_pos-len(letter)] + " [" + 
            source_text[letter_pos-len(letter):letter_pos+1] + "] " + 
            source_text[letter_pos+1:letter_pos+10])
        letter = source_text[letter_pos]
        return_string += letter
    return return_string

def markov_chain(source_text:str, order, generate_size):
    starter = random.choice(source_text)
    from .markov_chain import MarkovChain
    mc = MarkovChain()

    # build markov chain
    for i in range(order, len(source_text)):
        for odr in range(1, order+1):
            mc.add_trainsition(source_text[i-odr:i], source_text[i])

    # generate string
    generated = mc.next(". ")
    for _ in range(generate_size):
        generated += mc.next(generated[-order:])
    return generated
