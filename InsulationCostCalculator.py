#Required modules have been imported
import math as mt
from scipy.special import lambertw

import warnings

#Function to check which radius is to be chosen from two radii according to critical radius 
def rad_check_condition(r1,r2,critical_radius):
        if (((r1<critical_radius)and(r2<critical_radius))or((r1>critical_radius)and(r2>critical_radius))):
            print "\nSome values are unreal since the values of r1 and r2 are greater than critical radius or both are less than critical radius i.e",round(r1,3),round(r2,7),"."
            Insulation_Radius = 0
        else:
            if ((r1 or r2)<0):
                if (r1<0):
                    if (r2>Outer_Radius):
                        Insulation_Radius = r2
                    else:
                        print "\nSome values are unreal since one solution is negative and other is less than outer radius."
                if (r2<0):
                    if (r1>Outer_Radius):
                        Insulation_Radius = r2
                    else:
                        print "\nSome values are unreal since one solution is negative and other is less than outer radius."
            else:
                if (critical_radius>Outer_Radius):
                    if ((r1<critical_radius)and(r1>Outer_Radius)):
                        Insulation_Radius = r1
                    if ((r2<critical_radius)and(r2>Outer_Radius)):
                        Insulation_Radius = r2
                    if ((r1<critical_radius)and(r1<Outer_Radius)):
                        Insulation_Radius = r2
                    if ((r2<critical_radius)and(r2<Outer_Radius)):
                        Insulation_Radius = r1
                else:
                    if(r1>Outer_Radius):
                        Insulation_Radius = r1
                    if(r2>Outer_Radius):
                        Insulation_Radius = r2
        return Insulation_Radius

    

while True:
    print '''\nThis Program provides solution for insulation (90% reduction in energy loss) over a wall, tube and sphere."
Cost of Insulation is also calculated.\n'''
    
#Table for material to be chosen by user.
    
    Table_Material =[["Aluminium(Pure)              ",204],
 ["Al-Cu(Duralumin)             ",164],
 ["Al-Si(Silumin,copper-bearing)",137],
 ["Al-Si(Alusil)                ",161],
 ["Al-Mg-Si(97%Al,1%Mg,1%Si,1%Mn",177],
 ["Nickel Steel(Ni-0%)          ",73],
 ["Nickel Steel(Ni-40%)         ",10],
 ["Inwar(36%Ni)                 ",10.7],
 ["Chrome Steel(Cr-0%)          ",73],
 ["Chrome Steel(Cr-1%)          ",61],
 ["Chrome Steel(Cr-5%)          ",40],
 ["Steel (C 0.5%)               ",54],
 ["Steel (C 1.0%)               ",43],
 ["Steel (C 1.5%)               ",36]]

#Printing the Table_Material
    print "\t\tINSULATING MATERIAL\t\tCONDUCTIVITY(SI)"
    for i in range(len(Table_Material)):
        print i+1,"\t\t",Table_Material[i][0],"\t\t",Table_Material[i][1]

#Taking user input from Table_Material
    choice = int(raw_input("\nPlease Select any material from above list by entering its corresponding number: "))
    while(choice>14):
        print "Please input correctly from list."
        choice = int(raw_input("Please Select any material from above list by entering its corresponding number: "))

#Printing out user's choice
    print "\nSo, Your choice is",Table_Material[(choice-1)][0],"whose thermal conductivity is",Table_Material[(choice-1)][1]
        
#Table for insulating material.
    Table_Ins = [["Asbestos,loosely packed   ",0.154,520,180],
 ["Asbestos,cement           ",0.74,520,180],
 ["Balsam wood               ",0.04,35,30476],
 ["Cardboard,corrugated      ",0.064,240,45],
 ["Celotex                   ",0.048,30,1088],
 ["Corkboard                 ",0.043,160,167],
 ["Cork,regranulated         ",0.045,82.5,167],
 ["Diamond,Type IIa,insulator",2300,3500,1188443750],
 ["Diatomaceous earth        ",0.061,320,27],
 ["Felt,hair                 ",0.036,165,155],
 ["Felt,wool                 ",0.052,330,180],
 ["Fiber,insulating board    ",0.048,240,150],
 ["Glass wool                ",0.038,240.7,300],
 ["Glass fiber,duct liner    ",0.038,32,250],
 ["Glass fiber,loose blown   ",0.043,16,250],
 ["Ice                       ",2.22,910,30],
 ["Kapok                     ",0.035,290,250],
 ["Magnesia                  ",0.073,270,2500],
 ["Paper (avg)               ",0.12,900,285],
 ["Rock wool                 ",0.040,160,25],
 ["Sawdust                   ",0.059,210,6],
 ["Silica aerogel            ",0.024,140,125],
 ["Styrofoam                 ",0.033,50,160]]

#Printing the Table_Ins        
    print "\n\t\tINSULATING MATERIAL\t\tCONDUCTIVITY(SI)\tDENSITY(SI)\tCOST(Rs/kg)\n"
    for i in range(len(Table_Ins)):
        print i+1,"\t\t",Table_Ins[i][0],"\t\t",Table_Ins[i][1],"\t\t",Table_Ins[i][2],"\t\t",Table_Ins[i][3]

#Taking user input from Table_Ins
    choice1 = int(raw_input("\nPlease Select your insulating material from above list by entering its corresponding number: "))
    while(choice1>23):
        print "Please input correctly from list."
        choice1 = int(raw_input("Please Select your insulating material from above list by entering its corresponding number: "))
        
#Printing out user's choice
    print "\nSo, Your choice is",Table_Ins[(choice1-1)][0],"whose thermal conductivity is",Table_Ins[(choice1-1)][1],"W/m.K,\nwhose density is",Table_Ins[(choice1-1)][2],"kg per cubic metre and whose cost is Rs.",Table_Ins[(choice1-1)][3],"per kg."

    print '''\nWhat do you want to insulate ?
1. Wall
2. Tube
3. Sphere '''
    
#Taking input from user to specify which object to insulate
    choice2 = int(raw_input("\nSelect object from above list by entering its corresponding number: "))
    while(choice2>3):
        print "Please input correctly from list."
        choice2 = int(raw_input("Select object from above list by entering its corresponding number: "))
        
#Taking user inputs for inside Temprature, surrounding temprature, convective heat transfer coefficient.         
    Ti = float(raw_input("Enter the inside temprature of your material in kelvin: "))
    Ts = float(raw_input("Enter the surrounding temprature of your material in kelvin: "))
    h = float(raw_input("Enter the convective heat transfer coefficient(SI-units W/m2k): "))

#Taking values from Tables according to user's choice of material.
    k = Table_Material[(choice-1)][1]
    k_ins = Table_Ins[(choice1-1)][1]
    Density_Insulation = Table_Ins[(choice1-1)][2]
    Rate_Insulation = Table_Ins[(choice1-1)][3]

#Program if user chooses wall    
    if(choice2==1):
        #Taking dimensions from user
        Initial_Thickness = float(raw_input("Enter initial thickness of the wall in metres: "))
        Length = float(raw_input("Enter length of the wall in metres: "))
        Breadth = float(raw_input("Enter breadth of the wall in metres: "))

        #Heat loss per unit Area formula
        heat_loss_qbyA = abs((((Ti-Ts)*1.0))/((Initial_Thickness/(k*1.0))+(1/(h*1.0))))

        #Printing out current heat loss and user's expectation of heat loss(i.e 90% reduction in heat loss)
        print"\nNow heat lost by object is",round(heat_loss_qbyA,3),"W/m^2."
        print"By adding insulation we want to reduce heat loss to",round(((0.1)*(heat_loss_qbyA)),3),"W/m^2."

        #Calculating Insulation Thickness and printing it
        Insulation_Thickness = ((9.0*k_ins*1.0)*((Initial_Thickness/(k*1.0))+(1/(h*1.0))))
        print"\nThe thickness of insulating material required is",round(Insulation_Thickness,3),"m."

        #Calculating Weight and Total Cost and displaying it
        Weight_Insulation = Length*Breadth*Insulation_Thickness*Density_Insulation*1.0
        Total_Cost_Insulation = Rate_Insulation*Weight_Insulation*1.0
        print"\nTotal Weight of Insulation is",round(Weight_Insulation,3),"kg and total COST of Insulation is Rupees",round(Total_Cost_Insulation,3)

#Program if user chooses tube
    if(choice2==2):
        #Taking Dimensions of Tube from User
        Inner_Radius = float(raw_input("Enter the inner radius of the tube in metres: "))
        Outer_Radius = float(raw_input("Enter the outer radius of the tube in metres: "))
        Length = float(raw_input("Enter the length of tube in metres: "))

        #Heat loss per unit Area formula
        heat_loss_qbyA = abs((((2.0*(mt.pi))*((Ti-Ts)*1.0))/(((mt.log(Outer_Radius/(Inner_Radius*1.0)))/(k*1.0))+(1/(Outer_Radius*h*1.0)))))

        #Printing out current heat loss and user's expectation of heat loss(i.e 90% reduction in heat loss)  
        print"\nNow heat lost by object is",round(heat_loss_qbyA,3),"W/m^2."
        print"\nBy adding insulation we want to reduce heat loss to",round(((0.1)*(heat_loss_qbyA)),3),"W/m^2."

        #Critical Radius where heat loss is maximum 
        critical_radius = (k_ins/(h*1.0))
        print "\nThe critical radius of insulation is",critical_radius,"m."

        #There are warnings due to complex roots of lambert function which are needed to be ignored in Output so this loop has been started 
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore")

            #An equation is formed in terms of lnx and 1/x whixh is solved using lambert function, r1,r2 are solutions. 
            a = (h/(k_ins*1.0))
            b = Outer_Radius
            c = (k_ins)*((9.0*((mt.log(Outer_Radius/(Inner_Radius*1.0)))/(k*1.0)))+(10.0/(Outer_Radius*h*1.0)))
            z = -(1/(a*b*mt.exp(c)*1.0))
            w1 = lambertw(z,k=0)
            w2 = lambertw(z,k=-1)
            r1 = (b*(mt.exp(w1+c)))
            r2 = (b*(mt.exp(w2+c)))
            
        #print r1,r2
        
        #Function is called to check which is the appropriate insulation radius among the two r1,r2 and insulation radius is printed.
        Insulation_Radius = rad_check_condition(r1,r2,critical_radius)    
        print"\nThe radius of insulating material is",round(Insulation_Radius,3),"m, and the Thickness is",round((Insulation_Radius-Outer_Radius),3),"m."        

        #Weight and Total Cost of Insulation is calculated and printed.
        Weight_Insulation = (mt.pi)*(Length)*(((Insulation_Radius)**2)-(((Outer_Radius)**2)))*Density_Insulation*1.0
        Total_Cost_Insulation = Rate_Insulation*Weight_Insulation*1.0
        print"\nTotal Weight of Insulation is",round(Weight_Insulation,3),"kg and total COST of Insulation is Rupees",round(Total_Cost_Insulation)        

#Program if user chooses sphere
    if(choice2==3):
        
        #Taking Dimensions of Tube from User
        Inner_Radius = float(raw_input("Enter the inner radius of the sphere in metres: "))
        Outer_Radius = float(raw_input("Enter the outer radius of the sphere in metres: "))

        #Heat loss per unit Area formula
        heat_loss_qbyA = abs((((4.0*(mt.pi))*((Ti-Ts)*1.0))/(((((1.0/(Inner_Radius*1.0))-(1.0/(Outer_Radius*1.0)))/(k*1.0))+(1/(h*Outer_Radius*Outer_Radius*1.0)))*1.0)))

        #Printing out current heat loss and user's expectation of heat loss(i.e 90% reduction in heat loss)
        print"\nNow heat lost by object is",round(heat_loss_qbyA,3),"W/m^2."
        print"\nBy adding insulation we want to reduce heat loss to",round(((0.1)*(heat_loss_qbyA)),3),"W/m^2."

        #A quadratic equation a(1/r^2) +b(1/r) +c = 0 is formed according to given hypothesis which calculates the insulation radius.
        a = (1/(h*1.0))
        b = -(1/(k_ins*1.0))
        c = -((9/(k*1.0))*((1/(Inner_Radius*1.0))-(1/(Outer_Radius*1.0)))+((10)/(h*Outer_Radius*Outer_Radius*1.0))-(1/(k_ins*Outer_Radius*1.0)))
        delta = (b**2) - (4*a*c)
        if(delta<0):
            print "\nSome values are unreal since delta is negative."
        else:
            solution1 = (-b-mt.sqrt(delta))/(2*a*1.0)
            solution2 = (-b+mt.sqrt(delta))/(2*a*1.0)
            r1 = (1/(solution1*1.0))
            r2 = (1/(solution2*1.0))
            
        #print r1,r2

        #Critical Radius where heat loss is maximum
        critical_radius = ((2*k_ins)/(h*1.0))
        print "\nThe critical radius of insulation is",critical_radius,"m."

        #Function is called to check which is the appropriate insulation radius among the two r1,r2 and insulation radius is printed.
        Insulation_Radius =  rad_check_condition(r1,r2,critical_radius)           
        print"\nThe radius of insulating material is",round(Insulation_Radius,3),"m, and the Thickness is",round((Insulation_Radius-Outer_Radius),3),"m."

        #Weight and Total Cost of Insulation is calculated and printed.
        Weight_Insulation = (4.0/3.0)*(mt.pi)*(((Insulation_Radius)**3)-(((Outer_Radius)**3)))*Density_Insulation*1.0
        Total_Cost_Insulation = Rate_Insulation*Weight_Insulation*1.0
        print"\nTotal Weight of Insulation is",round(Weight_Insulation,3),"kg and total COST of Insulation is Rupees",round(Total_Cost_Insulation,3)
        
    #This block of code is written to allow user to decide whether to continue or not.
    while True:
        answer = raw_input("\nRun again? (Y/N): ")
        if answer in ("Y", "N","y","n"):
            break
        print "Invalid input."
    if answer == "Y" or answer == "y":
        continue
    else:
        print "\n--------------------------------------------------------THANK YOU--------------------------------------------------------"
        break


