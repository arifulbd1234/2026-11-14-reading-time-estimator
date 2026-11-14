# Day 39: Reading Time Estimator - 2026-11-14
# Kono boi, article ba lekha porte koto somoy lagbe ta ber korar tool.
# Jara boi pore, porikkhar preparation ney ba article pore -
# shobar jonno kaje lage, karon age theke jana jay koto somoy dorkar.

AVERAGE_WPM = 200        # ekjon sadharon manush minute e ~200 shobdo pore
SLOW_WPM = 150           # aste porle
FAST_WPM = 300           # druto porle
WORDS_PER_PAGE = 300     # ek page e garh ~300 shobdo


def count_words(text):
    """Lekhar shobdo gono."""
    if not text or not text.strip():
        return 0
    return len(text.split())


def estimate_minutes(word_count, wpm=AVERAGE_WPM):
    """Shobdo sonkha ar porar goti diye minute e somoy ber koro."""
    if word_count <= 0:
        return 0
    if wpm <= 0:
        raise ValueError("Porar goti (wpm) 0 er beshi hote hobe.")
    return word_count / wpm


def format_time(minutes):
    """Minute ke 'X ghonta Y minute' akare sajao."""
    total = round(minutes)
    if total < 1:
        return "1 minuter kom"
    hours, mins = divmod(total, 60)
    if hours == 0:
        return f"{mins} minute"
    if mins == 0:
        return f"{hours} ghonta"
    return f"{hours} ghonta {mins} minute"


def estimate_for_text(text, wpm=AVERAGE_WPM):
    """Puro lekha diye porar somoy ber koro."""
    words = count_words(text)
    minutes = estimate_minutes(words, wpm)
    return words, minutes, format_time(minutes)


def estimate_for_pages(pages, wpm=AVERAGE_WPM, words_per_page=WORDS_PER_PAGE):
    """Page sonkha diye boi porte koto somoy lagbe ber koro."""
    if pages <= 0:
        raise ValueError("Page sonkha 0 er beshi hote hobe.")
    words = pages * words_per_page
    minutes = estimate_minutes(words, wpm)
    return words, minutes, format_time(minutes)


def reading_plan(word_count, minutes_per_day, wpm=AVERAGE_WPM):
    """Protidin kotokkhon porle koy dine shesh hobe ber koro."""
    if minutes_per_day <= 0:
        raise ValueError("Protidin porar somoy 0 er beshi hote hobe.")
    total_minutes = estimate_minutes(word_count, wpm)
    days = total_minutes / minutes_per_day
    words_per_day = minutes_per_day * wpm
    return days, words_per_day


if __name__ == "__main__":
    # Example 1: choto article porte koto somoy lagbe
    article = ("Porar ovvas manusher jibone onek boro sompod. Protidin "
               "olpo somoy boi porle gyan bare, mon shanto thake ar "
               "notun notun chinta mathay ashe.")
    words, mins, pretty = estimate_for_text(article)
    print(f"Article: {words} shobdo -> porte lagbe {pretty}")

    # Example 2: 250 page er boi, sadharon gotite
    words, mins, pretty = estimate_for_pages(250)
    print(f"250 page er boi: {words} shobdo -> porte lagbe {pretty}")

    # Example 3: protidin 30 minute porle 60,000 shobder boi koy dine shesh
    days, per_day = reading_plan(60000, 30)
    print(f"Protidin 30 minute porle 60,000 shobder boi shesh hobe "
          f"{days:.1f} dine (protidin ~{int(per_day)} shobdo)")
