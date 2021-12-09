def build(pattern):
    pattern_len = len(pattern)
    pi = [None] * pattern_len
    i = 1
    j = 0
    pi[0] = 0
    while(i < pattern_len):
        if(pattern[i] == pattern[j]):
            j += 1
            pi[i] = j
            i += 1
        elif(j == 0):
            pi[i] = 0
            i += 1
        else:
            j = pi[j-1]
            
            
    return pi

def find_match(text, pattern, pi):
    text_len = len(text)
    pattern_len = len(pattern)
    pattern_pos = 0
    text_pos = 0
    while(text_pos + pattern_len - pattern_pos <= text_len):
        if(pattern[pattern_pos] == text[text_pos]):
            pattern_pos += 1
            text_pos += 1
        
            if(pattern_pos == pattern_len):
                #print("Match at", text_pos - pattern_pos )
                return text_pos - pattern_pos
        elif(pattern_pos != 0):
            pattern_pos = pi[pattern_pos - 1]
        else:
            text_pos += 1

    #print("No match")
    return -1

def main():
    text = "abababcababababba"
    pattern = "ababababba"

    text = "Hello world!"
    pattern = "world"
    pi = build(pattern)
    # print(pi)
    pos = find_match(text, pattern, pi)
    if pos != -1:
        print("Position of substring", pattern, "in", text, "is", pos)
    else:
        print("Substring", pattern, "is not found in", text)


if __name__ == "__main__":
    main()
