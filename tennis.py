def guess(word: str, previous_words: list[str], time: float) -> bool:
    if time < 0 or not word:
        raise ValueError

    try:
        if not previous_words or (word[0] == previous_words[-1][-1] and word not in previous_words and time <= 3):
            return True
    except:
        raise ValueError

    return False