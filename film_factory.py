import pandas as pd
import matplotlib.pyplot as plt
import random
import datetime

sn=pd.read_csv("snacks table.csv")
s=pd.read_csv("snacks table.csv", index_col=0)
ns=pd.read_csv("nowshowing.csv",index_col=0)
cs=pd.read_csv("comingsoon.csv",index_col=0)
ms=pd.read_csv("movie table.csv",index_col=0)
m=pd.read_csv("movie table.csv")

#HOMEPAGE
def home():
    print()
    print("*"*95,"\n")
    print(" "*30,"HELLO! WELCOME TO FILM FACTORY! \n")
    print("*"*95)
    print("1. ADMIN \n2. BOOK A MOVIE")
    homepg=int(input("Enter your choice: "))
    print()
    
    #ADMIN PAGE
    if homepg==1:
        print(" "*23,"*"*17,"ADMIN LOGIN","*"*17)
        username=("filmfactoryadmin")
        password=("saditi")
        # LOGGING IN
        def log_in():
            x=input("Enter Username: ")
            y=input("Enter Password: ")
            if x==username and y==password:
                print()
                print(" "*35,"SUCCESFULLY LOGGED IN!!!","\n")
                print("*"*95,"\n")
                print(" "*40,"WELCOME, ADMIN \n")
                print("*"*95)
                def admin():
                    print("1. View Movies \n2. Update Movie Menu \n3. View Snacks \n4. Update Snacks Menu \n5. View Sales \n6. Return to Homepage")
                    menu=int(input("Enter your choice: "))
                    print()
                    
                    # VIEW MOVIES
                    if menu==1:
                        pd.set_option('display.expand_frame_repr',False)
                        pd.set_option('display.max_columns',None)
                        print(" "*41,"MOVIES MENU:")
                        print("*"*95,"\n")
                        print(ms,"\n") 
                        print("*"*95)
                        print("Do you wish to continue?:\n 1. YES \n 2. NO, RETURN TO HOMEPAGE")
                        a=int(input("Enter your choice:"))
                        print()
                        if a==1:
                            print(admin(),"\n")
                        else:
                            print("\n",home())
                            
                    # UPDATE MOVIES
                    if menu==2:
                        print("UPDATE MOVIES HERE: \n")
                        print("1. Add new movies \n2. Change movie details \n3. Delete movies \n4. Return to Admin" )
                        choice=int(input("Enter your choice:"))
                        print()
                        
                        # ADD MOVIES
                        if choice==1:
                            def add_movie():
                                mid=int(input("Enter Movie ID: "))
                                
                                for i in m["MOVIE_ID"]:
                                    if i==mid:
                                        print("Movie already exists !!!")
                                        print(add_movie())
                                              
                                        
                                print("\nMOVIE ID CREATED!!!")
                                name=input("\nEnter Movie Name: ").upper()
                                genre= input("\nEnter Genre Of The Movie: ").upper()
                                dur=input("\nEnter Duration In Minutes: ")
                                lan=input("\nEnter Language Of The Movie: ").upper()
                                pg=float(input("\nEnter The PG rating: "))
                                price=input("\nEnter Price Per Ticket: ")  
                                print("*"*95)
                                print("MOVIE DETAILS ENTERED ARE AS FOLLOWS:","\n")
                                print("Name:",name)
                                print("Genre:",genre)
                                print("Duration:",dur,"min")
                                print("Language:",lan)
                                print("PG Rating:",pg)
                                print("Ticket price:",price)
                                print("*"*95)
                                
                                print("Would you like confirm newly added movie details?\n 1. YES \n 2. NO")
                                c=int(input("Enter your choice:"))
                                
                                if c==1:
                                    m.loc[mid]=[mid,name,genre,dur,lan,pg,price]
                                    m.to_csv("movies table.csv",index=False)
                                    print("*"*33,"MOVIE SUCCESSFULLY ADDED !!!","*"*32,"\n")
                                    print(admin())
                                    
                                else:
                                    print()
                                    print(admin())
                            print(add_movie())
                            
                        # CHANGE MOVIE DETAILS
                        if choice==2:
                            def updatem():
                                print()
                                print("Which  movie detail would you like to update? :")
                                print("1. NAME \n2. GENRE \n3. DURATION \n4. LANGUAGE \n5. PRICES \n6. PG_RATING \n7. RETURN TO ADMIN")
                                ch=int(input("Enter your choice: "))
                                print()
                                if ch==1:
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
                                    print(updatem())
                                
                                if ch==2:
                                    print("UPDATING MOVIE GENRE:")
                                    a=int(input("Enter Movie ID to change its Genre: "))
                                    newgenre=input("Enter New Movie Genre: ").upper()
                                    print("*"*95)
                                    print()
                                    df=pd.DataFrame(ms)
                                    df.at[a,"GENRE"]=newgenre
                                    print(df)
                                    print()
                                    print("*"*95)
                                    print(updatem())
                                    
                                if ch==3:
                                    print("UPDATING MOVIE DURATION:")
                                    a=int(input("Enter Movie ID to change its Duration: "))
                                    newdur=int(input("Enter New Movie Duration in mins: "))
                                    print("*"*95)
                                    print()
                                    df=pd.DataFrame(ms)
                                    df.at[a,"DURATION"]=newdur
                                    print(df)
                                    print()
                                    print("*"*95)
                                    print(updatem())
                                    
                                if ch==4:
                                    print("UPDATING MOVIE LANGUAGE:")
                                    a=int(input("Enter Movie ID to change its language: "))
                                    newlang=input("Enter New Movie Language: ").upper()
                                    print("*"*95)
                                    print()
                                    df=pd.DataFrame(ms)
                                    df.at[a,"LANGUAGE"]=newlang
                                    print(df)
                                    print()
                                    print("*"*95)
                                    print(updatem())
                                    
                                if ch==5:
                                    print("UPDATING MOVIE PRICE:")
                                    a=int(input("Enter Movie ID to change its Price: "))
                                    newpri=int(input("Enter New Ticket Price: "))
                                    print("*"*95)
                                    print()
                                    df=pd.DataFrame(ms)
                                    df.at[a,"PRICES"]=newpri
                                    print(df)
                                    print()
                                    print("*"*95)
                                    print(updatem())
                                    
                                if ch==6:
                                    print("UPDATING MOVIE PG RATINGS:")
                                    a=int(input("Enter Movie ID to change its PGRatings: "))
                                    newpgr=float(input("Enter New Movie PG Ratings: "))
                                    print("*"*95)
                                    print()
                                    df=pd.DataFrame(ms)
                                    df.at[a,"PG_RATING"]=newpgr
                                    print(df)
                                    print()
                                    print("*"*95)
                                    print(updatem())
                                    
                                if ch==7:
                                    print(admin())
                                    
                                if ch!=[1,2,3,4,5,6,7]:
                                    print(" INCORRECT MOVIE INPUT !!!")
                                    print(updatem())
                                    
                            print(updatem())

                            
                        # DELETE MOVIES
                        if choice==3:
                            mid=int(input("Enter Movie ID to be Deleted: "))
                            df=ms.drop(mid,axis=0)
                            print()
                            print("*"*32,"MOVIE SUCCESFULLY DELETED !!!","*"*32)
                            print("\n",df)  
                            print()
                            print("*"*95)
                            print(admin())
                            
                        if choice==4:
                            print(admin())
                            
                        if choice!=[1,2,3,4]:
                            print("INCORRECT INPUT !!!")
                            print()
                            print(admin())

                            
                    # VIEW SNACKS
                    if menu==3:
                        pd.set_option('display.expand_frame_repr',False)
                        pd.set_option('display.max_columns',None)
                        print(" "*41,"SNACKS MENU:")
                        print("*"*95,"\n")
                        print(s,"\n") 
                        print("*"*95)
                        print("Do you wish to continue?:\n 1. YES \n 2. NO, RETURN TO HOMEPAGE")
                        a=int(input("Enter your choice:"))
                        print()
                        if a==1:
                            print("\n",admin())
                        else:
                            print("\n",home())
                    
                    # UPDATE SNACKS
                    if menu==4:
                        print("UPDATE SNACKS HERE:\n")
                        print("1. Add new snacks \n2. Change snacks details \n3. Delete snacks \n4. Return to Admin" )
                        choice=int(input("Enter your choice:"))
                        print()
                        
                        # ADD SNACKS
                        if choice==1:
                            def add_snacks():
                                name=input("Enter Snacks: ").upper()
                                avail=input("\nEnter Availibilty: ").upper()
                                size= input("\nEnter Sizes: ").upper()
                                price=input("\nEnter Prices: ").upper()
                                print("*"*95)
                                print("SNACK DETAILS ENTERED ARE AS FOLLOWS:","\n")
                                print("Snack:",name)
                                print("Avalibility:",avail)
                                print("Sizes:",size)
                                print("Prices:",price)
                                print("*"*95)
                                
                                print("Would you like confirm newly added snack details?\n 1. YES \n 2. NO")
                                c=int(input("Enter your choice:"))
                                
                                if c==1:
                                    sn.loc[name]=[name,avail,size,price]
                                    sn.to_csv("snacks table.csv",index=False)
                                    print("*"*33,"SNACK SUCCESSFULLY ADDED !!!","*"*32)
                                    print("\n",admin())
                        
                                else:
                                    print("\n",admin())
                            print(add_snacks())
                            
                        # CHANGE SNACKS DETAILS
                        if choice==2:
                            def updates():
                                print()
                                print("Which snack detail would you like to update? :")
                                print("1. AVAILIBILITY \n2. SIZE \n3. PRICE \n4. RETURN TO ADMIN")
                                ch=int(input("Enter your choice: "))
                                print()
                                
                                
                                if ch==1:
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
                                    
                                if ch==2:
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
                                    
                                if ch==3:
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
                                    
                                if ch==4:
                                    print(admin())
                                    
                                if ch!=1 and ch!=2 and ch!=3 and ch!=4:
                                    print("INCORRECT INPUT !!!")
                                    print(admin())
                                    
                                
                            print(updates())

                            
                        # DELETE SNACKS
                        if choice==3:
                            sname=input("Enter Snack Name to be Deleted: ").upper()
                            d=s.drop(sname,axis=0)
                            print()
                            print("*"*32,"SNACK SUCCESFULLY DELETED !!!","*"*32)
                            print("\n",d)  
                            print()
                            print("*"*95)
                            print(admin())
                            
                        # RETURN TO ADMIN
                        if choice==4:
                            print(admin())
                            
                        if choice!=[1,2,3,4]:
                            print()
                            print("INCORRECT INPUT !!!")
                            print()
                            print(admin())
                            
                    # VIEW SALES (GRAPHICALLY)
                    if menu==5:
                        def graphs():
                            print()
                            print("*"*44,"SALES","*"*44)
                            print()
                            print("1. YEARLY SALES \n2. MONTHLY SALES \n3. WEEKLY SALES \n4. DAILY SALES \n5. RETURN TO ADMIN PAGE")
                            sales=int(input("Enter your choice: "))
                            
                            #YEALY SALES
                            if sales==1:
                                year=[2015,2016,2017,2018,2019,2020,2021,2022]
                                amount=[10000,30000,20000,60000,40000,5000,25000,30000]
                                plt.xlabel("YEAR")
                                plt.ylabel("SALES")
                                plt.bar(year,amount,color=["r","b","g","c","y","m","tab:purple","tab:brown"])
                                plt.title("YEARLY SALES")
                                plt.show()
                                print(graphs())
                            
                            #MONTHLY SALES
                            if sales==2:
                                months=["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
                                amount=[20000,55000,34000,10000,15000,40000,50000,41000,34000,27000,20000,16000]
                                plt.xlabel("MONTHS")
                                plt.ylabel("SALES")
                                plt.bar(months,amount,color=["k","m","b","g","r","c","y"])
                                plt.title("MONTHLY SALES")
                                plt.show()
                                print(graphs())
                            
                            #WEEKLY SALES
                            if sales==3:
                                week=["Week1","Week2","Week3","Week4","Week5"]
                                amount=[5000,8000,7200,12000,4500]
                                plt.xlabel("WEEKS")
                                plt.ylabel("SALES")
                                plt.bar(week,amount,color=["tab:purple","tab:brown","r","c","g"])
                                plt.title("WEEKLY SALES")
                                plt.show()
                                print(graphs())
                                
                            #DAILY SALES
                            if sales==4:
                                day=["SUN","MON","TUE","WED","THU","FRI","SAT"]
                                amount=[2000,1250,640,200,2500,3000,2500]
                                plt.xlabel("DAYS")
                                plt.ylabel("SALES")
                                plt.bar(day,amount,color=["r","b","g"])
                                plt.title("DAILY SALES")
                                plt.show()
                                print(graphs())
                                
                            if sales==5:
                                print()
                                print(admin())
                                
                            if sales!=[1,2,3,4,5]:
                                print()
                                print("INCORRECT INPUT !!!")
                                print()
                                print(admin())
                                
                        print(graphs())
                    
                    # RETURN TO HOMEPAGE
                    if menu==6:
                        print(" "*41,"^_____^")
                        print(home())
                    
                    if menu!=[1,2,3,4,5,6]:
                        print("INCORRECT ADMIN INPUT !!!")
                        print()
                        print(admin())
                    
                
                        
                print(admin())
                
                
            else:
                print()
                print(" "*23,"*"*5,"INCORRECT USERNAME OR PASSWORD !!!","*"*5)
                print(" "*23,"*"*16,"TRY AGAIN !!!","*"*15)
                print()
                print(home())
            
       
        print(log_in())
    
    
    
    
    #CUSTOMER PAGE
    if homepg==2:
        def menuh():
            
            print(" "*40,"SELECT A MENU: ")
            print("*"*95)
            print("1. MOVIE MENU \n2. SNACKS MENU \n3. RETURN TO HOME PAGE")
            menu=int(input("Enter your choice: "))
            print()
    
            if menu==1:
                print(" "*33,"BOOK YOUR MOVIE TICKETS HERE: ")
                print("*"*95)
                print("Book your movie by: \n 1. NOW SHOWING \n 2. COMING SOON")
                print("\n       OR \n")
                print(" 3. RETURN TO MENU \n 4. RETURN TO HOMEPAGE")
                ch=int(input("Enter your choice: "))
                print()
    
            #random date generator
                start_date = datetime.date(2022, 11, 15)
                end_date = datetime.date(2022, 12, 31)
                
                time_between_dates = end_date - start_date
                days_between_dates = time_between_dates.days
                random_number_of_days = random.randrange(days_between_dates)
                random_date = start_date + datetime.timedelta(days=random_number_of_days)
            #random time generator
                st = pd.Series([9,10,11,12,13,14,15,16,17,18,19,20,21,22],index=None)
                et = pd.Series(["00",15,30,45],index=None)
                rst = random.choice(st)
                ret = random.choice(et)
                
                if ch==1:
    
                    def now_showing():
                        print()
                        print("NOW SHOWING: ")
                    
                        print("\n","1: ",ns.loc[101,"NAME"])
                        print("\n","2: ",ns.loc[102,"NAME"])
                        print("\n","3: ",ns.loc[103,"NAME"])
                        print("\n","4: ",ns.loc[104,"NAME"])
                        print("\n","5: ",ns.loc[105,"NAME"])
                        print()
                        m=int(input("Select movie to view details: "))
                        print()
                        print("*"*95)
                        if m==1:
                            print("MOVIE: ",ns.loc[101,"NAME"])
                            print("GENRE: ",ns.loc[101,"GENRE"])
                            print("DURATION: ",ns.loc[101,"DURATION"])
                            print("LANGUAGE: ",ns.loc[101,"LANGUAGE"])
                            print("PG RATING: ",ns.loc[101,"PG_RATING"])
                            print("PRICE PER TICKET: QR.",ns.loc[101,"PRICES"])
                            print("DATE & TIME: ", random_date,",",rst,":",ret)
                            print("*"*95)
                            print()
                        if m==2:
                            print("MOVIE: ",ns.loc[102,"NAME"])
                            print("GENRE: ",ns.loc[102,"GENRE"])
                            print("DURATION: ",ns.loc[102,"DURATION"])
                            print("LANGUAGE: ",ns.loc[102,"LANGUAGE"])
                            print("PG RATING: ",ns.loc[102,"PG_RATING"])
                            print("PRICE PER TICKET: QR.",ns.loc[102,"PRICES"])
                            print("DATE & TIME: ", random_date,",",rst,":",ret)
                            print("*"*95)
                            print()
                        if m==3:
                            print("MOVIE: ",ns.loc[103,"NAME"])
                            print("GENRE: ",ns.loc[103,"GENRE"])
                            print("DURATION: ",ns.loc[103,"DURATION"])
                            print("LANGUAGE: ",ns.loc[103,"LANGUAGE"])
                            print("PG RATING: ",ns.loc[103,"PG_RATING"])
                            print("PRICE PER TICKET: QR.",ns.loc[103,"PRICES"])
                            print("DATE & TIME: ", random_date,",",rst,":",ret)
                            print("*"*95)
                            print()
                        if m==4:
                            print("MOVIE: ",ns.loc[104,"NAME"])
                            print("GENRE: ",ns.loc[104,"GENRE"])
                            print("DURATION: ",ns.loc[104,"DURATION"])
                            print("LANGUAGE: ",ns.loc[104,"LANGUAGE"])
                            print("PG RATING: ",ns.loc[104,"PG_RATING"])
                            print("PRICE PER TICKET: QR.",ns.loc[104,"PRICES"])
                            print("DATE & TIME: ", random_date,",",rst,":",ret)
                            print("*"*95)
                            print()
                        if m==5:
                            print("MOVIE: ",ns.loc[105,"NAME"])
                            print("GENRE: ",ns.loc[105,"GENRE"])
                            print("DURATION: ",ns.loc[105,"DURATION"])
                            print("LANGUAGE: ",ns.loc[105,"LANGUAGE"])
                            print("PG RATING: ",ns.loc[105,"PG_RATING"])
                            print("PRICE PER TICKET: QR.",ns.loc[105,"PRICES"])
                            print("DATE & TIME: ", random_date,",",rst,":",ret)
                            print("*"*95)
                            print()
                            
                        print("WOULD YOU LIKE TO BOOK THIS MOVIE? \n 1. YES \n 2. NO, RETURN TO MOVIES")
                        yn=int(input("Enter your choice: "))
                        if yn==1: 
                            print()
                            print(" "*40,"CONTINUE BOOKING:")
                            print("*"*95)
                            tick=int(input("How many tickets would you like to book? : "))
                            
                            
                            
                            n1=ns.loc[101,"NAME"]
                            g1=ns.loc[101,"GENRE"]
                            d1=ns.loc[101,"DURATION"]
                            l1=ns.loc[101,"LANGUAGE"]
                            pg1=ns.loc[101,"PG_RATING"]
                            p1=ns.loc[101,"PRICES"]
                
                
                            n2=ns.loc[102,"NAME"]
                            g2=ns.loc[102,"GENRE"]
                            d2=ns.loc[102,"DURATION"]
                            l2=ns.loc[102,"LANGUAGE"]
                            pg2=ns.loc[102,"PG_RATING"]
                            p2=ns.loc[102,"PRICES"]
                            
                            n3=ns.loc[103,"NAME"]
                            g3=ns.loc[103,"GENRE"]
                            d3=ns.loc[103,"DURATION"]
                            l3=ns.loc[103,"LANGUAGE"]
                            pg3=ns.loc[103,"PG_RATING"]
                            p3=ns.loc[103,"PRICES"]
                            
                            n4=ns.loc[104,"NAME"]
                            g4=ns.loc[104,"GENRE"]
                            d4=ns.loc[104,"DURATION"]
                            l4=ns.loc[104,"LANGUAGE"]
                            pg4=ns.loc[104,"PG_RATING"]
                            p4=ns.loc[104,"PRICES"]
                            
                            n5=ns.loc[105,"NAME"]
                            g5=ns.loc[105,"GENRE"]
                            d5=ns.loc[105,"DURATION"]
                            l5=ns.loc[105,"LANGUAGE"]
                            pg5=ns.loc[105,"PG_RATING"]
                            p5=ns.loc[105,"PRICES"]
                            
                            
                        
                            
                            if m==1:
                                priceperticket=ns.loc[101,"PRICES"]
                                price=tick*priceperticket
                                print("Your Total Ticket Price: QR.",price)
                                print("\nAll viewers must match their age according to the movie's PG Ratings!!!\nAny viewer under the age limit will not be allowed to watch the movie!!!")
                                print()
                                print(" "*30,"BOOKING DETAILS & CONFIRMATION: ")
                                print("*"*95)
                                print("MOVIE: ",n1)
                                print("GENRE: ",g1)
                                print("DURATION: ",d1)
                                print("LANGUAGE: ",l1)
                                print("PG RATING: ",pg1)
                                print("PRICE PER TICKET: QR.",p1)
                                print("TOTAL PRICE: QR.",price)
                            if m==2:
                                priceperticket=ns.loc[102,"PRICES"]
                                price=tick*priceperticket
                                print("Your Total Ticket Price: QR.",price)
                                print("\nAll viewers must match their age according to the movie's PG Ratings!!!\nAny viewer under the age limit will not be allowed to watch the movie!!!")
                                print()
                                print(" "*30,"BOOKING DETAILS & CONFIRMATION: ")
                                print("*"*95)
                                print("MOVIE: ",n2)
                                print("GENRE: ",g2)
                                print("DURATION: ",d2)
                                print("LANGUAGE: ",l2)
                                print("PG RATING: ",pg2)
                                print("PRICE PER TICKET: QR.",p2)
                                print("TOTAL PRICE: QR.",price)
                            if m==3:
                                priceperticket=ns.loc[103,"PRICES"]
                                price=tick*priceperticket
                                print("Your Total Ticket Price: QR.",price)
                                print("\nAll viewers must match their age according to the movie's PG Ratings!!!\nAny viewer under the age limit will not be allowed to watch the movie!!!")
                                print()
                                print(" "*30,"BOOKING DETAILS & CONFIRMATION: ")
                                print("*"*95)
                                print("MOVIE: ",n3)
                                print("GENRE: ",g3)
                                print("DURATION: ",d3)
                                print("LANGUAGE: ",l3)
                                print("PG RATING: ",pg3)
                                print("PRICE PER TICKET: QR.",p3)
                                print("TOTAL PRICE: QR.",price)
                            if m==4:
                                priceperticket=ns.loc[104,"PRICES"]
                                price=tick*priceperticket
                                print("Your Total Ticket Price: QR.",price)
                                print("\nAll viewers must match their age according to the movie's PG Ratings!!!\nAny viewer under the age limit will not be allowed to watch the movie!!!")
                                print()
                                print(" "*30,"BOOKING DETAILS & CONFIRMATION: ")
                                print("*"*95)
                                print("MOVIE: ",n4)
                                print("GENRE: ",g4)
                                print("DURATION: ",d4)
                                print("LANGUAGE: ",l4)
                                print("PG RATING: ",pg4)
                                print("PRICE PER TICKET: QR.",p4)
                                print("TOTAL PRICE: QR.",price)
                            if m==5:
                                priceperticket=ns.loc[105,"PRICES"]
                                price=tick*priceperticket
                                print("Your Total Ticket Price: QR.",price)
                                print("\nAll viewers must match their age according to the movie's PG Ratings!!!\nAny viewer under the age limit will not be allowed to watch the movie!!!")
                                print()
                                print(" "*30,"BOOKING DETAILS & CONFIRMATION: ")
                                print("*"*95)
                                print("MOVIE: ",n5)
                                print("GENRE: ",g5)
                                print("DURATION: ",d5)
                                print("LANGUAGE: ",l5)
                                print("PG RATING: ",pg5)
                                print("PRICE PER TICKET: QR.",p5)
                                print("TOTAL PRICE: QR.",price)
                                
                                
                            def confirm():
                                print("\nWOULD YOU LIKE TO CONFIRM YOUR TICKET(S)?:\n 1. YES \n 2. NO, RETURN TO MOVIES")
                                confirmation=int(input("Enter your Choice: "))
                            
                                if confirmation==1:
                                    print()
                                    print()
                                    print(" "*22,"ALL PAYMENTS TO BE DONE UPON ARRIVAL AT THE THEATER")
                                    
                                    print(" "*36,"BOOKING SUCCESSFUL!!!")
                                    print("*"*95)
                                    print()
                                    print(" "*40,"THANK YOU!!!")
                                    print(" "*37,"ENJOY YOUR MOVIE:)")
                                    print(" "*41,"ヾ(⌐■_■)ノ♪")
                                else:
                                    print("\n",now_showing())
                                    
                            print(confirm())
                        else:
                            print()
                            print("\n",now_showing())
                    print(now_showing())
                                
    
                if ch==2:
                    
                    def coming_soon():
                        print()
                        print("COMING SOON: ")
                   
                        print("\n","1: ",cs.loc[116,"NAME"])
                        print("\n","2: ",cs.loc[117,"NAME"])
                        print("\n","3: ",cs.loc[118,"NAME"])
                        print("\n","4: ",cs.loc[119,"NAME"])
                        print("\n","5: ",cs.loc[120,"NAME"])
                        print()
                        m=int(input("Select movie to view details: "))
                        print()
                        print("*"*95)
                        if m==1:
                            print("MOVIE: ",cs.loc[116,"NAME"])
                            print("GENRE: ",cs.loc[116,"GENRE"])
                            print("DURATION: ",cs.loc[116,"DURATION"])
                            print("LANGUAGE: ",cs.loc[116,"LANGUAGE"])
                            print("PG RATING: ",cs.loc[116,"PG_RATING"])
                            print("PRICE PER TICKET: QR.",cs.loc[116,"PRICES"])
                            print("DATE & TIME: ", random_date,",",rst,":",ret)
                            print("*"*95)
                            print()
                        if m==2:
                            print("MOVIE: ",cs.loc[117,"NAME"])
                            print("GENRE: ",cs.loc[117,"GENRE"])
                            print("DURATION: ",cs.loc[117,"DURATION"])
                            print("LANGUAGE: ",cs.loc[117,"LANGUAGE"])
                            print("PG RATING: ",cs.loc[117,"PG_RATING"])
                            print("PRICE PER TICKET: QR.",cs.loc[117,"PRICES"])
                            print("DATE & TIME: ", random_date,",",rst,":",ret)
                            print("*"*95)
                            print()
                        if m==3:
                            print("MOVIE: ",cs.loc[118,"NAME"])
                            print("GENRE: ",cs.loc[118,"GENRE"])
                            print("DURATION: ",cs.loc[118,"DURATION"])
                            print("LANGUAGE: ",cs.loc[118,"LANGUAGE"])
                            print("PG RATING: ",cs.loc[118,"PG_RATING"])
                            print("PRICE PER TICKET: QR.",cs.loc[118,"PRICES"])
                            print("DATE & TIME: ", random_date,",",rst,":",ret)
                            print("*"*95)
                            print()
                        if m==4:
                            print("MOVIE: ",cs.loc[119,"NAME"])
                            print("GENRE: ",cs.loc[119,"GENRE"])
                            print("DURATION: ",cs.loc[119,"DURATION"])
                            print("LANGUAGE: ",cs.loc[119,"LANGUAGE"])
                            print("PG RATING: ",cs.loc[119,"PG_RATING"])
                            print("PRICE PER TICKET: QR.",cs.loc[119,"PRICES"])
                            print("DATE & TIME: ", random_date,",",rst,":",ret)
                            print("*"*95)
                            print()
                        if m==5:
                            print("MOVIE: ",cs.loc[120,"NAME"])
                            print("GENRE: ",cs.loc[120,"GENRE"])
                            print("DURATION: ",cs.loc[120,"DURATION"])
                            print("LANGUAGE: ",cs.loc[120,"LANGUAGE"])
                            print("PG RATING: ",cs.loc[120,"PG_RATING"])
                            print("PRICE PER TICKET: QR.",cs.loc[120,"PRICES"])
                            print("DATE & TIME: ", random_date,",",rst,":",ret)
                            print("*"*95)
                            print()
                            
                        print("WOULD YOU LIKE TO BOOK THIS MOVIE? \n 1. YES \n 2. NO, RETURN BACK TO MOVIES")
                        yn=int(input("Enter your choice: "))
                        if yn==1: 
                            print()
                            print(" "*40,"CONTINUE BOOKING:")
                            print("*"*95)
                            tick=int(input("How many tickets would you like to book? : "))
                            
                            
                            
                            n6=cs.loc[116,"NAME"]
                            g6=cs.loc[116,"GENRE"]
                            d6=cs.loc[116,"DURATION"]
                            l6=cs.loc[116,"LANGUAGE"]
                            pg6=cs.loc[116,"PG_RATING"]
                            p6=cs.loc[116,"PRICES"]
                
                
                            n7=cs.loc[117,"NAME"]
                            g7=cs.loc[117,"GENRE"]
                            d7=cs.loc[117,"DURATION"]
                            l7=cs.loc[117,"LANGUAGE"]
                            pg7=cs.loc[117,"PG_RATING"]
                            p7=cs.loc[117,"PRICES"]
                            
                            n8=cs.loc[118,"NAME"]
                            g8=cs.loc[118,"GENRE"]
                            d8=cs.loc[118,"DURATION"]
                            l8=cs.loc[118,"LANGUAGE"]
                            pg8=cs.loc[118,"PG_RATING"]
                            p8=cs.loc[118,"PRICES"]
                            
                            n9=cs.loc[119,"NAME"]
                            g9=cs.loc[119,"GENRE"]
                            d9=cs.loc[119,"DURATION"]
                            l9=cs.loc[119,"LANGUAGE"]
                            pg9=cs.loc[119,"PG_RATING"]
                            p9=cs.loc[119,"PRICES"]
                            
                            n10=cs.loc[120,"NAME"]
                            g10=cs.loc[120,"GENRE"]
                            d10=cs.loc[120,"DURATION"]
                            l10=cs.loc[120,"LANGUAGE"]
                            pg10=cs.loc[120,"PG_RATING"]
                            p10=cs.loc[120,"PRICES"]
                            
                            
                        
                            
                            if m==1:
                                priceperticket=cs.loc[116,"PRICES"]
                                price=tick*priceperticket
                                print("Your Total Ticket Price: QR.",price)
                                print("\nAll viewers must match their age according to the movie's PG Ratings!!!\nAny viewer under the age limit will not be allowed to watch the movie!!!")
                                print()
                                print(" "*30,"BOOKING DETAILS & CONFIRMATION: ")
                                print("*"*95)
                                print("MOVIE: ",n6)
                                print("GENRE: ",g6)
                                print("DURATION: ",d6)
                                print("LANGUAGE: ",l6)
                                print("PG RATING: ",pg6)
                                print("PRICE PER TICKET: QR.",p6)
                                print("TOTAL PRICE: QR.",price)
                            if m==2:
                                priceperticket=cs.loc[117,"PRICES"]
                                price=tick*priceperticket
                                print("Your Total Ticket Price: QR.",price)
                                print("\nAll viewers must match their age according to the movie's PG Ratings!!!\nAny viewer under the age limit will not be allowed to watch the movie!!!")
                                print()
                                print(" "*30,"BOOKING DETAILS & CONFIRMATION: ")
                                print("*"*95)
                                print("MOVIE: ",n7)
                                print("GENRE: ",g7)
                                print("DURATION: ",d7)
                                print("LANGUAGE: ",l7)
                                print("PG RATING: ",pg7)
                                print("PRICE PER TICKET: QR.",p7)
                                print("TOTAL PRICE: QR.",price)
                            if m==3:
                                priceperticket=cs.loc[118,"PRICES"]
                                price=tick*priceperticket
                                print("Your Total Ticket Price: QR.",price)
                                print("\nAll viewers must match their age according to the movie's PG Ratings!!!\nAny viewer under the age limit will not be allowed to watch the movie!!!")
                                print()
                                print(" "*30,"BOOKING DETAILS & CONFIRMATION: ")
                                print("*"*95)
                                print("MOVIE: ",n8)
                                print("GENRE: ",g8)
                                print("DURATION: ",d8)
                                print("LANGUAGE: ",l8)
                                print("PG RATING: ",pg8)
                                print("PRICE PER TICKET: ",p8)
                                print("TOTAL PRICE: QR.",price)
                            if m==4:
                                priceperticket=cs.loc[119,"PRICES"]
                                price=tick*priceperticket
                                print("Your Total Ticket Price: QR.",price)
                                print("\nAll viewers must match their age according to the movie's PG Ratings!!!\nAny viewer under the age limit will not be allowed to watch the movie!!!")
                                print()
                                print(" "*95,"BOOKING DETAILS & CONFIRMATION: ")
                                print("*"*30)
                                print("MOVIE: ",n9)
                                print("GENRE: ",g9)
                                print("DURATION: ",d9)
                                print("LANGUAGE: ",l9)
                                print("PG RATING: ",pg9)
                                print("PRICE PER TICKET: QR.",p9)
                                print("TOTAL PRICE: QR.",price)
                            if m==5:
                                priceperticket=cs.loc[120,"PRICES"]
                                price=tick*priceperticket
                                print("Your Total Ticket Price: QR.",price)
                                print("\nAll viewers must match their age according to the movie's PG Ratings!!!\nAny viewer under the age limit will not be allowed to watch the movie!!!")
                                print()
                                print(" "*30,"BOOKING DETAILS & CONFIRMATION: ")
                                print("*"*95)
                                print("MOVIE: ",n10)
                                print("GENRE: ",g10)
                                print("DURATION: ",d10)
                                print("LANGUAGE: ",l10)
                                print("PG RATING: ",pg10)
                                print("PRICE PER TICKET: QR.",p10)
                                print("TOTAL PRICE: QR.",price)
                                
                                
                            def confirm():
                                print("\nWOULD YOU LIKE TO CONFIRM YOUR TICKET(S)?:\n 1. YES \n 2. NO, RETURN TO MOVIES")
                                confirmation=int(input("Enter your Choice: "))
                            
                                if confirmation==1:
                                    print()
                                    print()
                                    print(" "*22,"ALL PAYMENTS TO BE DONE UPON ARRIVAL AT THE THEATER")
                                    print(" "*36,"BOOKING SUCCESSFUL!!!")
                                    print("*"*95)
                                    print()
                                    print(" "*40,"THANK YOU!!!")
                                    print(" "*37,"ENJOY YOUR MOVIE:)")
                                    print(" "*41,"ヾ(⌐■_■)ノ♪")
                                else:
                                    print("\n",coming_soon())
                                    
                            print(confirm())
                        else:
                            print()
                            print("\n",coming_soon())
                    print(coming_soon())
                
                if ch==3:
                    print(menuh())
                
                if ch==4:
                    print(home())
    
               
                    
                
            #SNACKS MENU    
            if menu==2:
                print(" "*27,"ENJOY AWESOME SNACKS WITH YOUR MOVIE :) \n")
                print(" "*20,"All food & beverages can be purchased upon arrival! \n")
                print(" "*40," SNACKS MENU:")
                print("*"*95)
                print(s,"\n")
                print("*"*95)
                
                print("Do you wish to continue?:\n 1. YES, RETURN TO HOMEPAGE \n 2. NO, EXIT")
                a=int(input("Enter your choice:"))
                if a==1:
                    print("\n",home())
                else:
                    print(" "*41,"(^_____^)") 
                
                    
            #RETURN TO HOMEPAGE
            if menu==3:
                print(home())
                
                
        print(menuh())

print(home())            