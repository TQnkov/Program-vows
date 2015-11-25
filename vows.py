def vow_search():
    vows = ["a", "e", "i", "o", "u"]
    vows_in_word = []
    i = 0
    while True:
        word = input("Type a word, pleace!")
        if word.isalpha():
            break
    for let in word:
        if let in vows:
            i += 1
            vows_in_word.append(let)
    return print(i, vows_in_word)
    
    
  vow_search()
