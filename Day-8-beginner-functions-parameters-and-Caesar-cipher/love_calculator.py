def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()

    t = combined_names.count("t")
    r = combined_names.count("r")
    u = combined_names.count("u")
    e = combined_names.count("e")
    true_score = t + r + u + e

    l = combined_names.count("l")
    o = combined_names.count("o")
    v = combined_names.count("v")
    e = combined_names.count("e")

    love_score = l + o + v + e
    final_score = int(str(true_score) + str(love_score))
    print(final_score)
calculate_love_score("rahma", "alamin")