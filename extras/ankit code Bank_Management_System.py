from tkinter import *
accounts = {}

class Transaction:
    def __init__(self,master):
        self.master=master
        self.balance=0
        self.master.title("Banking Management System")
        self.master.geometry('500x500')
    def login(self):
        name=Label(text="Customer Name")
        user_name=Entry(self.master)
        password=Label(text="Password")
        user_password=Entry(self.master)
        name.grid(row=0,column=0,padx=20,pady=10)
        password.grid(row=1,column=0,padx=20,pady=10)
        user_name.grid(row=0,column=1,padx=20,pady=10)
        user_password.grid(row=1,column=1,padx=20,pady=10)
        submit=Button(self.master,text="Submit",command=self.main_page)
        submit.grid(row=2,column=4)
        self.master.mainloop() 

    def insert_data(self):
        global entry
        string = entry.get()
        
    def main_page(self):
        self.master1=Toplevel(self.master)
        self.master1.geometry('500x500')
        self.master1.title("Main Window")
        self.master1.resizable(False,False)
        # self.master.destroy()
        # self.master1=Tk()
        # self.master1.geometry('500x500')
        create_Account=Button(self.master1,text="Create Account",command=self.creating_account)
        Withdraw_Amount=Button(self.master1,text="Withdraw Amount",command=self.withdrawl)
        Deposit_Amount=Button(self.master1,text="Deposit Amount",command=self.deposit)
        Transfer_Amount=Button(self.master1,text="Transfer Amount",command=self.transfer)
        Account_Details=Button(self.master1,text="Account Details",command=self.details)
        create_Account.grid(row=0,column=0,pady=50,padx=70)
        Withdraw_Amount.grid(row=0,column=1,pady=50)
        Transfer_Amount.grid(row=1,column=0,pady=50,padx=70)
        Deposit_Amount.grid(row=1,column=1)
        Account_Details.grid(row=2,column=0,pady=40)
        self.master1.mainloop()

    def creating_account(self):
        self.master2=Toplevel(self.master)
        self.master2.geometry('500x500')
        self.master2.title("Create Account")
        self.master2.resizable(False,False)
        # self.master1.destroy()
        # self.master2=Tk()
        # self.master2.geometry('500x500')
        name=Label(self.master2,text="Customer Name:")
        id=Label(self.master2,text="Customer ID:")
        mno=Label(self.master2,text="Customer Mobile No:")
        acc_no=Label(self.master2,text="Account No:")
        name_entry=Entry(self.master2)
        id_entry=Entry(self.master2)
        mobileno_entry=Entry(self.master2)
        acc_no_entry=Entry(self.master2)
        name_entry.grid(row=0,column=1,padx=10,pady=5)
        id_entry.grid(row=1,column=1,padx=10,pady=5)
        mobileno_entry.grid(row=2,column=1,padx=10,pady=5)
        acc_no_entry.grid(row=3,column=1,padx=10,pady=5)
        name.grid(row=0,column=0,padx=10,pady=5)
        id.grid(row=1,column=0,padx=10,pady=5)
        mno.grid(row=2,column=0,padx=10,pady=5)
        acc_no.grid(row=3,column=0,padx=10,pady=5)
        submit=Button(self.master2,text="Submit",command=self.insert_data)
        submit.grid(row=4,column=1,padx=10,pady=10)
        self.master2.mainloop()
        # acc_no=acc_no_entry.get()
        
    def withdrawl(self):
        self.master3=Toplevel(self.master)
        self.master3.geometry('500x500')
        self.master3.title("Create Withdrawl")
        self.master3.resizable(False,False)
        # self.master2.destroy()
        # self.master3=Tk()
        acc_no_label=Label(self.master3,text="Enter Your Account No:")
        amount_label=Label(self.master3,text="Enter Your Amount:")
        acc_no_label.grid(row=0,column=0,padx=50,pady=10)
        amount_label.grid(row=1,column=0,padx=50,pady=10)
        acc_no_entry=Entry(self.master3)
        amount_entry=Entry(self.master3)
        acc_no_entry.grid(row=0,column=1,padx=10,pady=10)
        amount_entry.grid(row=1,column=1,padx=10,pady=10)

        if amount_entry > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount_entry
            print(f"{amount_entry} withdrawn from account {acc_no_entry}. New balance: {self.balance}")
        
        submit=Button(self.master3,text="Submit")
        submit.grid(row=3,column=1,padx=10,pady=10)
        self.master3.mainloop() 

    def deposit(self):
        self.master4=Toplevel(self.master)
        self.master4.geometry('500x500')
        self.master4.title("Create deposited")
        self.master4.resizable(False,False)
        # self.master3.destroy()
        # self.master4=Tk()
        # self.master4.geometry('500x500')
        acc_no_label=Label(self.master4,text="Enter Your Account No:")
        amount_label=Label(self.master4,text="Enter Your Amount:")
        acc_no_label.grid(row=0,column=0,padx=50,pady=10)
        amount_label.grid(row=1,column=0,padx=50,pady=10)
        acc_no_entry=Entry(self.master4)
        amount_entry=Entry(self.master4)

        self.balance += amount_entry.get()
        print(f"{amount_entry} deposited into account {acc_no_entry}. New balance: {self.balance}")

        acc_no_entry.grid(row=0,column=1,padx=10,pady=10)
        amount_entry.grid(row=1,column=1,padx=10,pady=10)
        submit=Button(self.master4,text="Submit")
        submit.grid(row=3,column=1,padx=10,pady=10)
        self.master4.mainloop()

    def transfer(self):
        self.master5=Toplevel(self.master)
        self.master5.geometry('500x500')
        self.master5.title("create transfer")
        self.master5.resizable(False,False)
        # self.master4.destroy()
        # self.master5=Tk()
        # self.master5.geometry('500x500')
        sender_acc_label=Label(self.master5,text="Enter Sender Account No:")
        rece_acc_label=Label(self.master5,text="Enter Receiver Account No:")
        money_label=Label(self.master5,text="Enter Amount:")
        sender_acc_label.grid(row=0,column=0,padx=50,pady=10)
        rece_acc_label.grid(row=1,column=0,padx=50,pady=10)
        money_label.grid(row=2,column=0,padx=50,pady=10)
        sender_acc_entry=Entry(self.master5)
        rece_acc_entry=Entry(self.master5)
        money_entry=Entry(self.master5)
        sender_acc_entry.grid(row=0,column=1,padx=10,pady=10)
        rece_acc_entry.grid(row=1,column=1,padx=10,pady=10)
        money_entry.grid(row=2,column=1,padx=10,pady=10)
        submit=Button(self.master5,text="Submit")
        submit.grid(row=3,column=1,padx=10,pady=10)
        self.master5.mainloop()

    def details(self):
        self.master6=Toplevel(self.master)
        self.master6.geometry('500x500')
        self.master6.title("Create details")
        self.master6.resizable(False,False)
        # self.master5.destroy()
        # self.master6=Tk()
        # self.master6.geometry('500x500')
        name=Label(self.master6,text="Customer Name:")
        id=Label(self.master6,text="Customer ID:")
        mno=Label(self.master6,text="Customer Mobile No:")
        acc_type=Label(self.master6,text="Account Type:")
        balance=Label(self.master6,text="Customer Account Balance:")
        name.grid(row=0,column=0,padx=50,pady=10)
        id.grid(row=1,column=0,padx=50,pady=10)
        mno.grid(row=2,column=0,padx=50,pady=10)
        acc_type.grid(row=3,column=0,padx=50,pady=10)
        self.master6.mainloop()
# obj=Transaction()

def main():
    root=Tk()
    app=Transaction(root)
    root.title("phoneBook")
    root.geometry("500x500")
    root.resizable(False,False)
    app.login()
    root.mainloop()
   
if __name__=='__main__':   # this code runs main method
    main()
