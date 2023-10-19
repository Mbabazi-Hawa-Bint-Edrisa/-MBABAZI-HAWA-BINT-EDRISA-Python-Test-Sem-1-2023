#Question 1(i)Re write the following in snake case and camel case
#snake case
#student_marks
#studentMarks
#total_average_mark
#totalAverageMark

#(ii) convert the variable to float value mand print the data type
age=22
age1=float(age)
print(age1)
print(type(age1))

#Question 2(i) A function to find the average of two numbers 

x=50
y=40
sum=(x+y)
average=sum/2
print(average)


#Question 2(ii)
numbers=("number!,number_2,number_3")
number_1=input("Enter number_1:")
number_2=input("Enter number_2:")
number_3=input("Enter number_3:")

if (number_1<number_2 and number_1<number_3):
    print("The minimum number is "+""+ str(number_1))
        


#Question 3(i)
student_marks=[78,83,90,88,75]
sum_of_marks=(78+83+90+88+75)
print( sum_of_marks)
print("The sum of the items in the list student marks is "+ ""+str(sum_of_marks))

#(ii)
print(student_marks[0])
print(student_marks[4])

#(iii)
student_marks=[78,83,90,88,75]
student_marks.append(96)
print(student_marks)

#(iv)
student_marks=[78,83,90,88,75]
student_marks[0]=87
print(student_marks)



