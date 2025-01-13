import matplotlib.pyplot as plt
def graphs():
    print()
    print("*"*26,"SALES","*"*26)
    print()
    print("1. YEARLY SALES \n2. MONTHLY SALES \n3. WEEKLY SALES \n4. DAILY SALES")
    sales=int(input("Enter your choice: "))
    
    #YEALY SALES
    if sales==1:
        year=[2015,2016,2017,2018,2019,2020,2021,2022]
        amount=[10000,30000,20000,60000,40000,5000,25000,30000]
        plt.xlabel("YEAR")
        plt.ylabel("SALES")
        plt.bar(year,amount,color=["r","b","g","c","y","m","tab:purple","tab:brown"])
        plt.title("YEARLY SALES")
        plt.savefig("Yearly Sales.png")
        plt.show()
        print(graphs())
    
    #MONTHLY SALES
    if sales==2:
        months=["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
        amount=[20000,55000,34000,10000,15000,40000,50000,41000,34000,27000,20000,16000]
        plt.xlabel("MONTHS")
        plt.ylabel("SALES")
        #plt.bar(month,amount,color=["tab:purple","tab:blue","k","m","tab:brown","g","c","y"]
        plt.bar(months,amount,color=["k","m","b","g","r","c","y"])
        plt.title("MONTHLY SALES")
        plt.savefig("Monthly Sales.png")
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
        plt.savefig("Weekly Sales.png")
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
        plt.savefig("Daily Sales.png")
        plt.show()
        print(graphs())
        
print(graphs())