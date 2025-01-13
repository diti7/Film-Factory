import pandas as pd
s=pd.read_csv("snacks table.csv", index_col=0)
ns=pd.read_csv("nowshowing.csv",index_col=0)
cs=pd.read_csv("comingsoon.csv",index_col=0)
m=pd.read_csv("movie table.csv")


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
        print("*"*41,"ADMIN LOGIN","*"*41)
        username=("fi")
        password=("sa")
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
            else:
                print("INCORRECT INPUT!!!")
                print()
                print(home())
            # ADMIN OPTIONS
            def admin():
                print("1. View Movies \n2. Update Movie Menu \n3. View Snacks \n4. Update Snacks Menu")
                menu=int(input("Enter your choice: "))
                print()
                
                # VIEW MOVIES
                if menu==1:
                    pd.set_option('display.expand_frame_repr',False)
                    pd.set_option('display.max_columns',None)
                    print(" "*41,"MOVIES MENU:")
                    print("*"*95,"\n")
                    print(m,"\n") 
                    print("*"*95)
                    print("Do you wish to continue?:\n 1. YES \n 2. NO, RETURN TO HOMEPAGE")
                    a=int(input("Enter your choice:"))
                    print()
                    if a==1:
                        print(admin())
                    else:
                        print("\n",home())
                        
                # UPDATE MOVIES
                if menu==2:
                    print("UPDATE MOVIES HERE: \n")
                    print("1.Add new movies \n2.Change movie details \n3.Delete movies" )
                    choice=int(input("Enter your choice:"))
                    print()
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
                        
                    # DELETE MOVIES
                    if choice==3:
                        mid=int(input("Enter Movie ID To Be Deleted: "))
                        print("*"*95,"\n")
                        mids=m.drop(mid,axis=0)
                        print(mids,"\n")
                        print("*"*32,"MOVIE SUCCESFULLY DELETED !!!","*"*32)
                        print("\n",admin())

                        
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
                    if a==1:
                        print("\n",admin())
                    else:
                        print("\n",home())
                
                # UPDATE SNACKS
                if menu==4:
                    print("1. Add new snacks \n2. Change snacks details \n3. Delete snacks" )
                    choice=int(input("Enter your choce:"))
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
                                s.loc[name]=[name,avail,size,price]
                                s.to_csv("snacks table.csv",index=False)
                                print("*"*33,"SNACK SUCCESSFULLY ADDED !!!","*"*32)
                                print("\n",admin())
                    
                            else:
                                print("\n",admin())
                        print(add_snacks())
                        
                    # DELETE SNACKS
                    if choice==3:
                        sn=input("Enter Snack To Be Deleted: ").upper()
                        print("*"*95,"\n")
                        sd=s.drop(sn,axis=0)
                        print(sd,"\n")
                        print("*"*32,"SNACK SUCCESFULLY DELETED !!!","*"*32)
                        print("\n",admin())
                    
            print(admin())
       
        print(log_in())
print(home())