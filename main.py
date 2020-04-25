import requests
import random

def create_seq_from_buckets(starting_word, sequence_string):
    buckets = get_buckets(starting_word)
    output_string = starting_word + ' '
    for char in list(sequence_string):
        if char == 'x':
             output_string += 'x '
        else:
            output_string += random.choice(buckets[int(char)-1])['word'] + ' '
    return output_string


def get_buckets(starting_word):
    syllable_buckets = [[],[],[],[],[]]
    corpus = rhymes_by_word(starting_word)
    for t in corpus:
        syllable_buckets[int(t['syllables'])-1].append(t)
    return syllable_buckets



def rhymes_by_word(word,number=30):
    r = requests.get(f"https://rhymebrain.com/talk?function=getRhymes&word={word}&maxResults={number}")
    if r.status_code == 200:
        return r.json()
    else:
        print("Rate Limited")
        return []




if __name__ == '__main__':
    test_seq = '2232'
    test_word = 'see'
    print(create_seq_from_buckets(test_word,test_seq))
    # print(get_buckets('air'))