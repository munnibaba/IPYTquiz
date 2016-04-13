#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      student
#
# Created:     13/04/2016
# Copyright:   (c) student 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

print("Welcome to Eyelash's text adventure game!")
print("Answer the following questions to get today's hint for her real name")
print("This program will add the total number of questions you answered.")
print("If you get at least 15 correct, you will get a hint!")
print("Please type 1, 2, or 3 as your answer option. Anything else will end the game.")

ready = input("Are you ready?")

score = 0

while(True):

    if(ready == "yes" or "Yes" or "YES"):
        print("Let's do this then!")
        choice = input(
        "\nPick a category:"
        "\n1. variables"
        "\n2. if/elif/else"
        "\n3. while loop"
        "\n4. for loop"
        "\n5. input/output"
        "\n6. everything else")

    if(choice == "1"):
        print("Let's see how much you have learned about variables!")

        v_question1 = input("What are the three types of variable we have learned?" +
        "\n1. input, output, string"
        "\n2. string, int, print"
        "\n3. int, string, boolean")
        v_answer1 = "3"
        if(v_question1 == v_answer1):
            print("You are correct!")
            score += 1
        else:
            print("Sorry, better try next time!")
            break

        v_question2 = input("If you have "
        "\nage = input(what is your age?)"
        "\nHow do you change the age variable from string to int?"
        "\n1. int(age)"
        "\n2. age = int(age)"
        "\n3. int(age) = age")
        v_answer2 = "2"
        if(v_question2 == v_answer2):
            print("You are correct!")
            score += 1
        else:
            print("Sorry, better try next time!")
            break

        v_question3 = input("If you have a variable \n var = 'True' \n"
        "Is it a boolean or a string?")
        v_answer3 = "string"
        if(v_question3 == v_answer3):
            print("You are correct!")
            score += 1
            continue
        else:
            print("Sorry, better try next time!")
    elif(choice == "2"):
        c_question1 = input("What is needed at the end of an if statement?"
        "\n1. ;"
        "\n2. :"
        "\n3. '")
        c_answer1 = "2"
        if(c_question1 == c_answer1):
            print("You are correct!")
            score += 1
        else:
            print("Sorry, better try next time!")
            break

        c_question2 = input("There are three things wrong with the following code."
        "\nWhat are they?:"
        '\ninstructor = input("Who is your instructor?")'
        "\nif(instructor = Eyelash):"
        "\nprint(You are taking IPYT course!)"
        "\n\n1. need == instead of = for input, and inside the if statement"
        "\n2. need == instead of = for just inside the if statement"
        "\n3. need == instead of = for inside the if statement, and print statement needs to be indented "
        "\n4. all of the above"
        "\n5. none of the above")
        c_answer2 = "5"
        if(c_question2 == c_answer2):
            print("You are correct!")
            score += 1
        else:
            print("Sorry, better try next time!")
            break

        c_question3 = input("")
        c_answer3 = "3"
        if(c_question3 == c_answer3):
            print("You are correct!")
            score += 1
            continue
        else:
            print("Sorry, better try next time!")
            break

    elif(choice == "3"):
        w_question1 = input("")
        w_answer1 = ""
        if(w_question1 == w_answer1):
            print("You are correct!")
            score += 1
        else:
            print("Sorry, better try next time!")
            break

        w_question2 = input("")
        w_answer2 = ""
        if(w_question2 == w_answer2):
            print("You are correct!")
            score += 1
        else:
            print("Sorry, better try next time!")
            break

        w_question3 = input("")
        w_answer3 = ""
        if(w_question1 == w_answer1):
            print("You are correct!")
            score += 1
            continue
        else:
            print("Sorry, better try next time!")
            break

    elif(choice == "4"):
        f_question1 = input("")
        f_answer1 = ""
        if(f_question1 == f_answer1):
            print("You are correct!")
            score += 1
        else:
            print("Sorry, better try next time!")
            break

        f_question2 = input("")
        f_answer2 = ""
        if(f_question2 == f_answer2):
            print("You are correct!")
            score += 1
        else:
            print("Sorry, better try next time!")
            break

        f_question3 = input("")
        f_answer3 = ""
        if(f_question1 == f_answer1):
            print("You are correct!")
            score += 1
            continue
        else:
            print("Sorry, better try next time!")
            break

    elif(choice == "5"):
        o_question1 = input("")
        o_answer1 = ""
        if(o_question1 == o_answer1):
            print("You are correct!")
            score += 1
        else:
            print("Sorry, better try next time!")
            break

        o_question2 = input("")
        o_answer2 = ""
        if(f_question2 == f_answer2):
            print("You are correct!")
            score += 1
        else:
            print("Sorry, better try next time!")
            break

        o_question3 = input("")
        o_answer3 = ""
        if(o_question1 == o_answer1):
            print("You are correct!")
            score += 1
            continue
        else:
            print("Sorry, better try next time!")
            break

    elif(choice == "6"):
        e_question1 = input("")
        e_answer1 = ""
        if(e_question1 == e_answer1):
            print("You are correct!")
            score += 1
        else:
            print("Sorry, better try next time!")
            break

        e_question2 = input("")
        e_answer2 = ""
        if(e_question2 == e_answer2):
            print("You are correct!")
            score += 1
        else:
            print("Sorry, better try next time!")
            break

        e_question3 = input("")
        e_answer3 = ""
        if(e_question1 == e_answer1):
            print("You are correct!")
            score += 1
            continue
        else:
            print("Sorry, better try next time!")
            break


    else:
        print("Oh Well! You can try again later.")
