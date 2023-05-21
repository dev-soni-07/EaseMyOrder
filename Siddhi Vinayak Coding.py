from datetime import date

import pandas as pd

print("Date: ",date.today())

name=str(input("Enter Your Name :  "))

class   SiddhiVinayakRestaurant:
    
    def RestaurantBill(self,date,n):
        self.t=0
        self_1=0
        self_2=0
        self_3=0
        self_4=0
        self_5=0
        self_6=0
        self_7=0
        self_8=0
        self_9=0
        self_10=0
        self_11=0
        self_12=0
        self_13=0
        self_14=0
        self_15=0
        self_16=0
        self_17=0
        self_18=0
        self_19=0
        self_20=0
        self_21=0
        self_22=0
        self_23=0
        self_24=0
        self_25=0
        self_26=0
        self_27=0
        self_28=0
        self_29=0
        self_30=0
        self_31=0
        self_32=0
        self_33=0
        self_34=0
        self_35=0
        self_36=0
        self_37=0
        self_38=0
        self_39=0
        self_40=0
       
        
        
        print ("*************** RESTAURANT MENU **************")

        df=pd.read_csv("D:\Menu_Card.csv", index_col=("S.No."))
        
        print(df)
        
        print ("\n TO CALCULATE BILL- PRESS : {00}")
        
        while (1):
            

            e=int(input("Enter your choice:  "))

            if (e==1):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+80*f
                self_1=+f
                t=0
                t=t+80*f
                print("You have ordered Chilli Paneer :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==2):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+70*f
                self_2=+f
                t=0
                t=t+70*f
                print("You have ordered Veg.Manchurian :",'Qt.=',f,',','Rs.=',t)

            elif (e==3):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+70*f
                self_3=+f
                t=0
                t=t+70*f
                print("You have ordered Veg.Chaumeen :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==4):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+60*f
                self_4=+f
                t=0
                t=t+60*f
                print("You have ordered Chilli Potato :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==5):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+80*f
                self_5=+f
                t=0
                t=t+80*f
                print("You have ordered Chilli Garlic Chaumeen :",'Qt.=',f,',','Rs.=',t)
                                
            elif (e==6):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+60*f
                self_6=+f
                t=0
                t=t+60*f
                print("You have ordered Pav Bhaji :",'Qt.=',f,',','Rs.=',t)
                                
            elif (e==7):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+15*f
                self_7=+f
                t=0
                t=t+15*f
                print("You have ordered Extra Pav :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==8):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+80*f
                self_8=+f
                t=0
                t=t+80*f
                print("You have ordered Chole Bhature :",'Qt.=',f,',','Rs.=',t)

            elif (e==9):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+20*f
                self_9=+f
                t=0
                t=t+20*f
                print("You have ordered Extra Bhatura :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==10):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+70*f
                self_10=+f
                t=0
                t=t+70*f
                print("You have ordered Kabab :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==11):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+70*f
                self_11=+f
                t=0
                t=t+70*f
                print("You have ordered Tandoori Aloo :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==12):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+140*f
                self_12=+f
                t=0
                t=t+140*f
                print("You have ordered Paneer Tikka :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==13):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+90*f
                self_13=+f
                t=0
                t=t+90*f
                print("You have ordered Paneer Pakoda :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==14):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+80*f
                self_14=+f
                t=0
                t=t+80*f
                print("You have ordered French Fries :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==15):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+90*f
                self_15=+f
                t=0
                t=t+90*f
                print("You have ordered Paneer Fry :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==16):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+80*f
                self_16=+f
                t=0
                t=t+80*f
                print("You have ordered Chana Chat :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==17):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+80*f
                self_17=+f
                t=0
                t=t+80*f
                print("You have ordered Aloo Chat :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==18):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+70*f
                self_18=+f
                t=0
                t=t+70*f
                print("You have ordered Veg. Pakoda :",'Qt.=',f,',','Rs.=',t) 
                
            elif (e==19):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+80*f
                self_19=+f
                t=0
                t=t+80*f
                print("You have ordered Meggi :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==20):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+80*f
                self_20=+f
                t=0
                t=t+80*f
                print("You have ordered Pasta :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==21):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+90*f
                self_21=+f
                t=0
                t=t+90*f
                print("You have ordered White Pasta :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==22):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+70*f
                self_22=+f
                t=0
                t=t+70*f
                print("You have ordered Macroni :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==23):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+70*f
                self_23=+f
                t=0
                t=t+70*f
                print("You have ordered Plain Noodles :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==24):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+80*f
                self_24=+f
                t=0
                t=t+80*f
                print("You have ordered Chinese Noodles :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==25):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+100*f
                self_25=+f
                t=0
                t=t+100*f
                print("You have ordered Haka Noodles :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==26):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+60*f
                self_26=+f
                t=0
                t=t+60*f
                print("You have ordered Sandwich :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==27):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+90*f
                self_27=+f
                t=0
                t=t+90*f
                print("You have ordered Cheese Sandwich :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==28):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+90*f
                self_28=+f
                t=0
                t=t+90*f
                print("You have ordered Paneer Sandwich :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==29):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+100*f
                self_29=+f
                t=0
                t=t+100*f
                print("You have ordered Deluxe Sandwich :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==30):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+60*f
                self_30=+f
                t=0
                t=t+60*f
                print("You have ordered Malai Kofta :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==31):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+70*f
                self_31=+f
                t=0
                t=t+70*f
                print("You have ordered Veg. Kofta :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==32):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+50*f
                self_32=+f
                t=0
                t=t+50*f
                print("You have ordered Dum Aloo :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==33):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+30*f
                self_33=+f
                t=0
                t=t+30*f
                print("You have ordered Aloo Paratha :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==34):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+80*f
                self_34=+f
                t=0
                t=t+80*f
                print("You have ordered Spring Rolls :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==35):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+40*f
                self_35=+f
                t=0
                t=t+40*f
                print("You have ordered Mango Shake :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==36):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+50*f
                self_36=+f
                t=0
                t=t+50*f
                print("You have ordered Chocolate Shake :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==37):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+30*f
                self_37=+f
                t=0
                t=t+30*f
                print("You have ordered Soft Drink :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==38):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+40*f
                self_38=+f
                t=0
                t=t+40*f
                print("You have ordered Jeera Soda :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==39):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+40*f
                self_39=+f
                t=0
                t=t+40*f
                print("You have ordered Cold Coffee :",'Qt.=',f,',','Rs.=',t)
                
            elif (e==40):
                f=float(input("Enter the NO. of Plate:"))
                self.t=self.t+60*f
                self_40=+f
                t=0
                t=t+60*f
                print("You have ordered Cold Coffee With Ice-Cream :",'Qt.=',f,',','Rs.=',t)
                
                                                    
            elif (e==00):
                
                break
            else:
                print ("Invalid option")
        print()        
        print()
        print("Date :", date.today())
        print()
        print(name,"'s Bill:")
        print()
        print ("Total Amount = Rs",self.t,"\n")
        print()
        print("THANK YOU")
        print()
        print("Visit Again")
        print()
        print("Have a nice day ahead...")
        print()
        print()
         
        f=(" \n1.Chilli Paneer : " , str(self_1),"\n2.Veg. Manchurian : ", 
           str(self_2),"\n3.Veg. Chaumeen : ",
           str(self_3),"\n4.Chilli Potato : ", str(self_4),"\n5.Chilli Garlic Chaumeen : " ,
           str(self_5),"\n6.Pav Bhaji : ", str(self_6),"\n7.Extra Pav : ",
           str(self_7),"\n8.Chole Bhature : ", str(self_8),"\n9.Extra Bhatura : ",
           str(self_9),"\n10.Kabab : ", str(self_10), "\n11.Tandoori Aloo : ",
           str(self_11),"\n12.Paneer Tikka : ", str(self_12),"\n13.Paneer Pakoda : ", 
           str(self_13),"\n14.French Fries : ", str(self_14),"\n15.Paneer Fry : ", 
           str(self_15),"\n16.Chana Chat : ", str(self_16), "\n17.Aloo Chat : ", 
           str(self_17),"\n18.Veg. Pakoda : ", str(self_18), "\n19.Meggi : ", 
           str(self_19),"\n20.Pasta : ", str(self_20),"\n21.White Pasta : ", 
           str(self_21),"\n22.Macroni : ", str(self_22),"\n23.Plain Noodles : ", 
           str(self_23),"\n24.Chinese Noodles : ", str(self_24),"\n25.Haka Noodles : ", 
           str(self_25),"\n26.Sandwich : ", str(self_26),"\n27.Cheese Sandwich : ", 
           str(self_27),"\n28.Paneer Sandwich : ", str(self_28),"\n29.Deluxe Sandwich : ", 
           str(self_29),"\n30.Malai Kofta : ", str(self_30),"\n31.Veg. Kofta : ", 
           str(self_31),"\n32.Dum Aloo : ", str(self_32),"\n33.Aloo Paratha : ", 
           str(self_33),"\n34.Spring Rolls : ", str(self_34),"\n35.Mango Shake : ", 
           str(self_35),"\n36.Chocolate Shake : ", str(self_36),"\n37.Soft Drink : ", 
           str(self_37),"\n38.Jeera Soda : ", str(self_38),"\n39.Cold Coffee : ", 
           str(self_39),"\n40.Cold Coffee With Ice-Cream : ", str(self_40)) 
        
        d=str(date.today())
        
        e=("Date: ",d)
        
        u="Customer Name : "
        
        num=str(name)
        
        file=open("Restaurant.csv",'a')
        file.write('\n')
        file.writelines(e)        
        file.write('\n')        
        file.writelines(u)        
        file.writelines(num)        
        file.write('\n')        
        file.writelines(f)        
        file.write('\n')        
        file.close()
    
def main():
    
    a=SiddhiVinayakRestaurant()
    
    print("""   
 --------------------------------------------------------
 |======================================================| 
 |============ SIDDHI VINAYAK RESTAURANT ===============|
 |=============== [Family Restaurant] ==================|
 |================== Welcomes You ======================|
 -------------------------------------------------------- """)
        
    n=0
    
    while (1):
        
        n=n+1
        
        print("1.Menu Card")
        
        print("\n2.Place Order & Get Your Bill")
        
        print()
        
        print("3.EXIT")
        
        print()
        
        b=int(input("\nEnter your choice:  "))
        
        print()
        
        print()
        
        if (b==1):
            
            df=pd.read_csv("D:\Menu_Card.csv", index_col=("S.No."))
            
            print(df)
            
        if (b==2):
            
            a.RestaurantBill(date,n)
            
        if (b==3):
            
            break
        
main() 

         