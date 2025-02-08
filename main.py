def sort_on(dict):
        return dict["count"]

def main():

    
    #with open('books/frankenstein.txt') as f:
        #file_contents = f.read()
        #print(file_contents)
    
    #with open('books/frankenstein.txt') as f:
        #file_contents = f.read()
        #words = file_contents.split()
        #word_count = len(words)
        #print(f" Number of words = {word_count}!")

    #with open('books/frankenstein.txt') as f:
        #characters = {}
        #file_contents = f.read()
        #characters_string = file_contents.lower()
        #characters_lower = list(characters_string)                      #First Working Solution
        #for character in characters_lower:
            #if character in characters:
                #characters[character] += 1
            #else:characters[character] = 1
        #print(characters)

    #with open('books/frankenstein.txt') as f:
        #characters = {}
        #character_list = []
        #for character in f.read().lower():
            #characters[character] = characters.get(character, 0) + 1     #working solution given by boots. 
        #print(characters)

    with open('books/frankenstein.txt') as f:
        characters = {}
        character_list = []
        for character in f.read().lower():
            if character.isalpha():
                characters[character] = characters.get(character, 0) + 1
        for key, value in characters.items():
             character_list.append({"char": key, "count": value})
        character_list.sort(reverse=True, key=sort_on)
        

        print('''--- Begin report of books/frankenstein.txt ---
77986 words found in the document
        ''')
        for char_dict in character_list:
             print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
        
        print("--- End report ---")



        #print('--- Begin report of books/frankenstein.txt ---')
        #print()    #need to print # of words found in the document
        #print()    #print 'The 'insert letter here' character was found 'insert number here' times' for each letter
        #print('--- End report ---')


if __name__ == "__main__":
    main()