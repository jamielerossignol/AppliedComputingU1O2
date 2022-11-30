##################################
#Program by: J. Le Rossignol
#Date Written: 21/04/2020
##################################
# Description: MathsHow to use Python to do maths stuff

#Declare Variables
i_one = 7
i_two = 4
i_three = 0
i_answer = 0

#Test Set 1
# Addition
i_answer = i_one + i_two
print(str(i_one) + " plus " + str(i_two) + " equals " + str(i_answer))

# Subtraction
i_answer = i_one - i_two
print(str(i_one) + " minus " + str(i_two) + " equals " + str(i_answer))

# Times
i_answer = i_one * i_two
print(str(i_one) + " times " + str(i_two) + " equals " + str(i_answer))

# Division
i_answer = int(i_one % i_two)
print(str(i_one) + " modulus " + str(i_two) + " equals " + str(i_answer))

#Test Set 2
i_two = int(input("Type in a number: "))
# Addition
i_answer = i_one + i_two
print(str(i_one) + " plus " + str(i_two) + " equals " + str(i_answer))

# Subtraction
i_answer = i_one - i_two
print(str(i_one) + " minus " + str(i_two) + " equals " + str(i_answer))

# Times
i_answer = i_one * i_two
print(str(i_one) + " times " + str(i_two) + " equals " + str(i_answer))

# Division
i_answer = int(i_one / i_two)
print(str(i_one) + " division " + str(i_two) + " equals " + str(i_answer))
