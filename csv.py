import pandas as pd

ms=pd.read_csv("movie table.csv",index_col=0)
s=pd.read_csv("snacks table.csv",index_col=0)

ns=pd.read_csv("nowshowing.csv",index_col=0)
cs=pd.read_csv("comingsoon.csv",index_col=0)
"""
info= {"Num":[12,14,13,12,14,13,15], "NAME":['John','Camili','Rheana','Joseph','Amanti','Alexa','Siri']}
 
data = pd.DataFrame(info)
print("Original Data frame:\n")
print(data)
data.at[6,'NAME']='Safa'0
print(data)
"""
"""
print("UPDATING MOVIE NAME:")
a=int(input("Enter Movie ID to change its Name: "))
newname=input("Enter New Movie Name: ").upper()
print("*"*95)
print()
df=pd.DataFrame(ms)
df.at[a,"NAME"]=newname
print(df)
print()
print("*"*95)
"""

def updates():
    print()
    print("Which snack detail would you like to update? :")
    print("1. SNACKS \n2. AVAILIBILITY \n3. SIZE \n4. PRICE")
    ch=int(input("Enter your choice: "))
    print()
    if ch==1:
        print("UPDATE SNACK NAMES:")
        a=input("Enter Snack Name to change its Name: ").upper()
        newname=input("Enter New Snack Name: ").upper()
        print("*"*95)
        print()
        df=pd.DataFrame(s)
        df.at[a,"SNACKS"]=newname
        print(df)
        print()
        print("*"*95)
        print(updates())
    
    if ch==2:
        print("UPDATE SNACKS AVAILABILTY:")
        b=input("Enter Snack Name to change its Avilability: ").upper()
        newavail=input("Enter New Availabilty as 'YES' or 'NO': ").upper()
        print("*"*95)
        print()
        df=pd.DataFrame(s)
        df.at[b,"AVAILABILITY"]=newavail
        print(df)
        print()
        print("*"*95)
        print(updates())
        
    if ch==3:
        print("UPDATING SNACK SIZES:")
        c=input("Enter Snack to change its Sizes: ").upper()
        newsize=input("Enter New Sizez: ").upper()
        print("*"*95)
        print()
        df=pd.DataFrame(s)
        df.at[c,"SIZE"]=newsize
        print(df)
        print()
        print("*"*95)
        print(updates())
        
    if ch==4:
        print("UPDATING SNACK PRICES:")
        d=input("Enter Snack to change its Price: ").upper()
        newp=input("Enter New Price: ").upper()
        print("*"*95)
        print()
        df=pd.DataFrame(s)
        df.at[d,"PRICE"]=newp
        print(df)
        print()
        print("*"*95)
        print(updates())
        
    if ch!=1 and ch!=2 and ch!=3 and ch!=4:
        print("INCORRECT snacks INPUT !!!")
        
        
        
    
print(updates())