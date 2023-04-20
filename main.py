with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    result = {}
    for i in file_contents.lower():
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(file_contents.split())} words found in the document")
    print()
    sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    sorted_result = dict(sorted_result)
    for i in sorted_result:
        if i.isalpha():
            print(f"The '{i}' character was found {sorted_result[i]} times")
    print("--- End report ---")