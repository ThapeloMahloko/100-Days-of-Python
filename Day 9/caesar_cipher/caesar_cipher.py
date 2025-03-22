from alphabet import alphabets

def caesar_cipher(task:str, original_text:str, shift_amount:int):
    results = ""
    if task.lower() == "encode":
        for i in range(len(original_text)):
            if original_text[i] in alphabets:
                position = alphabets.index(original_text[i])
                new_position = position + shift_amount
                results += alphabets[new_position % 25]
            else:
                results += original_text[i]
    elif task.lower() == "decode":
        for i in range(len(original_text)):
            if original_text[i] in alphabets:
                position = alphabets.index(original_text[i])
                new_position = position - shift
                if new_position < 0:
                    new_position -= 1
                results += alphabets[new_position]
            else:
                results += original_text[i]
    else:
        print("Please choose between Encode and Decode next time")
    print(results)
