def guess(word, previous_words, time):
    if time < 0 or not word:
        raise ValueError

    try:
        if not previous_words or (word[0] == previous_words[-1][-1] and word not in previous_words and time <= 3):
            return True
    except:
        raise ValueError

    return False
