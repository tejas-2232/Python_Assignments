def run_length_encoding(s):
    #initialize empty string
    
    if not s:
        return ""

    encoded_string = []
    prev_char = s[0]
    count = 1
    
    for ch in s[1:]:
        if ch == prev_char:
            count += 1
        else:
            encoded_string.append(f"{prev_char}{count}")
            prev_char = ch
            count = 1

    encoded_string.append(f"{prev_char}{count}")

    return "".join(encoded_string)

if __name__ == "__main__":
    s = "wwwwaaadebbbbbw"
    print(run_length_encoding(s))