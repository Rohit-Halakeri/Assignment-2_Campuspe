#Grade Calculator
subject_1=int(input("Enter marks for subject out of 100:"))
subject_2=int(input("Enter marks for subject of 100 :"))
subject_3=int(input("Enter marks for subject of 100:"))
subject_4=int(input("Enter marks for subject of 100:"))
subject_5=int(input("Enter marks for subject of 100:"))

Total_Marks=subject_1+subject_2+subject_3+subject_4+subject_5 


percentage=(Total_Marks/500)*100
 
print("Subject 1:",subject_1)
print("Subject 2:",subject_2)
print("Subject 3:",subject_3)
print("Subject 4:",subject_4)
print("Subject 5:",subject_5)

print("Total Marks:",Total_Marks)

print("Percentage :",percentage)

if percentage>90:
    print("Grade:A+(Outstanding)")
elif (percentage>80 and percentage<90):
            print("Grade:A(Excellent)")


elif percentage>70 and percentage<80:
    print("Grade:B(Good)")
elif(percentage>60 and percentage<70):
    print("Grade:C (Average)")
elif percentage > 50 and  percentage<60:
      print("Grade:D (Pass)")
else:
      print("Below 50% :F (Fail)")

if (subject_1 or subject_2 or subject_3 or subject_4 or subject_5 )>=40:
      print("Pass")
else:
      print("Fail")
    


