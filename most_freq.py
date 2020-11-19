
def most_frequent_char(str1):

           dict1 = {}

           max_repeat_count = 0

           for letter in strg:

                   if letter not in dict1:

                           dict1[letter] = 1

                   else:

                           dict1[letter] += 1

                   if dict1[letter]> max_repeat_count:

                           max_repeat_count = dict1[letter]

                           most_repeated_char = letter
                           print(max_repeat_count)

           return most_repeated_char

if __name__ == '__main__':

       strg ="mississippi";#raw_input("Enter the string : ")

       print( "Most Frequent Character : " + most_frequent_char(strg))
