def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count += 1
    return count
        
assert count_upper_case("") == 0, "Empty String"
assert count_upper_case("H") == 1, "One Uppercase"
assert count_upper_case("h") == 0, "One Lowercase"
assert count_upper_case("68@$") == 0, "special"
assert count_upper_case("Hey Bro") == 2, "Two uppercase"

print("All the tests passed")