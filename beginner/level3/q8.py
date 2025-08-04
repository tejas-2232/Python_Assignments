def decode_string(encoded_string):
    #split string by zero
    parts = encoded_string.split("0")
    print("after split",parts)

    #remove empty strings
    parts = [part for part in parts if part]
    print("after removing empty strings=",parts)

    #convert id to int
    id = int(parts[2])
    print("id to integer=",id)

    #return dictionary
    return {"first_name": parts[0], "last_name": parts[1], "id": id}

if __name__ == "__main__":
    encoded_string = "Robert000Smith000123"
    print(decode_string(encoded_string))