class myfunctions():
    def subfields():
        lists=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        print("Sub-Fields in AI are:")
        for i in lists:
            print(i)

    
    def OddEven():
        num=int(input("Enter a number:"))
        if (num%2==0):
            print(num,"is Even number")
        else :
            print(num,"is Odd number")

    
    def Eligible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(gender=="male"):
           if(age>=21):
              print("YOU ARE ELIGIBLE")
           else:
              print("NOT ELIGIBLE")
        elif(gender=="female"):
            if(age>=18):
              print("YOU ARE ELIGIBLE")
            else:
              print("NOT ELIGIBLE")
        else:
            print("INVALID GENDER")

    
    def percentage():
        sub1=int(input("Subject1="))
        sub2=int(input("Subject2="))
        sub3=int(input("Subject3="))
        sub4=int(input("Subject4="))
        sub5=int(input("Subject5="))
        Total=sub1+sub2+sub3+sub4+sub5
        print("Total:",Total)
        percentage=(Total/500)*100
        print("Percentage:",percentage)

    
    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        area=(height*breadth)/2
        print("Area of Triangle:",area)
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth2=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeter=height1+height2+breadth2
        print("Perimeter of Triangle:",perimeter)
    