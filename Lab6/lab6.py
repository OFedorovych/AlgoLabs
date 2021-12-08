def read_data():
    with open ("words_in.txt") as f:
        temp = f.readlines()
    words = []
    for word in temp:
        words.append(word.strip("\n"))
    words.sort(key=len)
    return words

def search_max_path(words):
    words_chain = {}
    len_path = 1
    if len(words) == 0:
        return len(words)
    else:
        for word in words:
            for letter in range(0, len(word)):
                word_check = word[:letter] + word[letter + 1:]
                if word_check in words_chain and len_path < words_chain[word_check]:
                    len_path = words_chain[word_check]
            words_chain[word] = len_path + 1
        return len_path

def main():
    words = read_data()
    print(search_max_path(words))

if __name__ == '__main__':
    main()
