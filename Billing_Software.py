from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
import random,os
from tkinter import messagebox
import tempfile
from time import *
import tkinter.font


class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")

#===============================Variable=========================
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z = random.randint(1000,10000)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_Total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        


        #Product Categories List
        self.Category=["Select Option","Clothing","LifeStyle","Mobile"]
       
        #SubCatClothing
        self.SubCatClothing=["Pant","T-Shirt","Shirt"]
        self.Pant=["Levis","Mufti","Spykar"]
        self.Price_Levis=5000
        self.Price_Mufti=6000 
        self.Price_Spykar=2000

        self.T_shirt=['Polo','Roadster','3Bros','HRX']
        self.Price_polo=900
        self.Price_roadster=500
        self.Price_3bros=600
        self.Price_HRX=1500

        self.Shirt=['Peter England','Lius Phillipe','Park Avanue','Netplay','JackJones']
        self.Price_Peter=900
        self.Price_Lius=2000
        self.Price_ParkAvanue=3000
        self.Price_Netplay=680
        self.Price_JackJones=850

        #SubCatStyle
        self.SubCatLifeStyle =["Bath_Soap","Face_Cream","Hair_Oil","Perfume"]
        
        self.Bath_Soap=['Dove','Dettol','Cinthol','Lux','Santoor','Pearl']
        self.Price_Dove=50
        self.Price_Dettol=20
        self.Price_Cinthol=25
        self.Price_Lux=30
        self.Price_Santoor=60
        self.Price_Pearl=40

        self.Face_Cream=['Fair And Handsome', ' Himalaya','Mamaearth','Ponds']
        self.Price_Fair=200
        self.Price_Himalaya=250
        self.Price_Mamaearth=300
        self.Price_Ponds=400

        self.Hair_Oil=['Dabur','Kesh_king','Parachute','Bajaj']
        self.Price_Dabur=150
        self.Price_Keshking=250
        self.Price_Parachute=100
        self.Price_Bajaj=200

        self.Perfume=['Gucci','Beardo','Engage','Fogg','Wild Stone']
        self.Price_Gucci=1000
        self.Price_Beardo=1500
        self.Price_Engage=1200
        self.Price_Fogg=500
        self.Price_WildStone=700

        #SubcatMobiles
        self.SubCatMobiles=["Iphone","Samsung","Redmi","RealMe","OnePlus","Oppo","Vivo"]

        self.Iphone=['Iphone_X','Iphone_XI','Iphone_XII','Iphone_XIII','Iphone_XIV']
        self.Price_IphoneX=60000
        self.Price_IphoneXI=120000
        self.Price_IphoneXII=160000
        self.Price_IphoneXIII=200000
        self.Price_IphoneXIV=100000

        self.Samsung=['Galaxy_S1','Galaxy_S2','Samsung_M2_Pro','Samsung_M5_Pro']
        self.Price_S1=60000
        self.Price_S2=80000
        self.Price_M2=12000
        self.Price_M5=25000

        self.Redmi=['Note_7 ','Note_9','Note_11','Note_13','Note_15']
        self.Price_Note7=12000
        self.Price_Note9=16000
        self.Price_Note11=20000
        self.Price_Note13=18000
        self.Price_Note15=15000

        self.RealMe=['Realme_6','Realme_7','Realme_8','Realme_9','Realme_10']
        self.Price_RealM6=10000
        self.Price_RealM7=15000
        self.Price_RealM8=18000
        self.Price_RealM9=20000
        self.Price_RealM10=25000

        self.OnePlus=['OnePlus7','OnePlus8','OnePlus9','OnePlus10','OnePlus11']
        self.Price_OnePlus7=25000
        self.Price_OnePlus8=35000
        self.Price_OnePlus9=30000
        self.Price_OnePlus10=45000
        self.Price_OnePlus11=50000

        self.Oppo=['Reno_7','Reno_8','Oppo_A7','Oppo_A8','Oppo_A55']
        self.Price_Reno7=35000
        self.Price_Reno8=45000
        self.Price_A7=35000
        self.Price_A8=60000
        self.Price_A55=50000

        self.Vivo=['Vivo_V23','Vivo_V25','Vivo_V27','Vivo_V29','Vivo_S1']
        self.Price_V23=60000
        self.Price_V25=55000
        self.Price_V27=45000
        self.Price_V29=35000
        self.Price_VS1=15000


        # image_1
        img = Image.open("image/deepak photo.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        lb1_img=Label(self.root,image=self.photoimg)
        lb1_img.place(x=0,y=0,width=500,height=130)

        #  image_2
        img_1 = Image.open("image/girls.jpg")
        img_1=img_1.resize((500,130),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        lb1_img_1=Label(self.root,image=self.photoimg_1)
        lb1_img_1.place(x=500,y=0,width=500,height=130)

        # image_3
        img_2 = Image.open("image/girl1.jpg")
        img_2 =img_2.resize((500,130),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lb1_img_2=Label(self.root,image=self.photoimg_2)
        lb1_img_2.place(x=1000,y=0,width=520,height=130)
        
        lbl_title=Label(self.root,text="BILLING SOFTWARE USING PYTHON", font=("DFKai-SB",35,"bold"),bg="white",fg="blue")
        lbl_title.place(x=0,y=130,width=1530,height=45)
        # Time Zone
        def time():
             string=strftime('%H:%M:%S %p')
             lbl.config(text=string)
             lbl.after(1000,time)

        lbl=Label(lbl_title,font=('Comic Sans MS', 16,'bold'),background='white',foreground='green')
        lbl.place(x=0,y=0,width=120,height=45)
        time() 
      #Main frame
        Main_Frame= Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1530,height=620)


        #Customer Label Frame
        Cust_Frame = LabelFrame(Main_Frame, text="Customer",font=("Comic Sans MS",12,"bold"),bg="white",fg="deeppink3")
        Cust_Frame.place(x=10,y=5,width=350,height=150)

        self.lbl_mob = Label(Cust_Frame, text="Mobile No.",font=("Comic Sans MS",12,"bold"),bg="white",fg="black")
        self.lbl_mob.grid(row=0,column=0 ,sticky=W,padx=5,pady=2)
          
        self.entry_mob = ttk.Entry(Cust_Frame,textvariable=self.c_phone ,font=("Comic Sans MS",12,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)
         
        self.lblCustName = Label(Cust_Frame,font=("Comic Sans MS",10,"bold"),bg="white",text="Customer Name",bd=4)
        self.lblCustName.grid(row=1,column=0 ,sticky=W,padx=5,pady=2)

        self.txtCustName = ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("Comic Sans MS",10,"bold"),width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblEmail = Label(Cust_Frame,font=("Comic Sans MS",12,"bold"),bg="white",text="Email",bd=4)
        self.lblEmail.grid(row=2,column=0 ,stick=W,padx=5,pady=2)

        self.txtEmail = ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("Comic Sans MS",12,"bold"),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2) 
        
        #Product Label Frame
        Product_Frame = LabelFrame(Main_Frame, text="Product",font=("Comic Sans MS",12,"bold"),bg="white",fg="deeppink3")
        Product_Frame.place(x=370,y=5,width=620,height=140)

        #Category
        self.lblCategory = Label(Product_Frame,font=("Comic Sans MS",10,"bold"),bg="white",text="Select Categories",bd=4)
        self.lblCategory.grid(row=0,column=0 ,sticky=W,padx=5,pady=2)
        
        self.Combo_Category = ttk.Combobox(Product_Frame,value=self.Category,font=("Comic Sans MS",10,"bold"),width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)


        # SubCategory
        self.lblSubCategory = Label(Product_Frame,font=("Comic Sans MS",12,"bold"),bg="white",text="Subcategory",bd=4)
        self.lblSubCategory.grid(row=1,column=0 ,sticky=W,padx=5,pady=2)
        
        self.ComboSubCategory = ttk.Combobox(Product_Frame,value=[" "],font=("Comic Sans MS",10,"bold"),width=24,state="readonly")
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_Add)
        # Product Name
        self.lblProduct = Label(Product_Frame,font=("Comic Sans MS",10,"bold"),bg="white",text="Product Name",bd=4)
        self.lblProduct.grid(row=2,column=0 ,sticky=W,padx=5,pady=2)
        
        self.ComboProduct = ttk.Combobox(Product_Frame,textvariable=self.product,font=("Comic Sans MS",10,"bold"),width=24,state="readonly")
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)
       #Price
        self.lblPrice = Label(Product_Frame,font=("Comic Sans MS",10,"bold"),bg="white",text="Price",bd=4)
        self.lblPrice.grid(row=0,column=2 ,sticky=W,padx=5,pady=2)
       
        self.ComboPrice = ttk.Combobox(Product_Frame,textvariable=self.prices,font=("Comic Sans MS",10,"bold"),width=24,state="readonly")
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)
        
       #Qty
        self.lblQty = Label(Product_Frame,font=("Comic Sans MS",10,"bold"),bg="white",text="Qty",bd=4)
        self.lblQty.grid(row=1,column=2 ,sticky=W,padx=5,pady=2)
        
        self.ComboQty = ttk.Entry(Product_Frame,textvariable=self.qty,font=("Comic Sans MS",10,"bold"),width=26)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)
 

       #Middle_Frame
        Middle_Frame=Frame(Main_Frame,bd=18)
        Middle_Frame.place(x=10,y=150,width=980,height=340)

       #image_2
        img_12 = Image.open("image/deepak photo.jpg")
        img_12=img_2.resize((490,340),Image.ANTIALIAS)
        self.photoimg_12=ImageTk.PhotoImage(img_12)

        lb1_img_12=Label(Middle_Frame,image=self.photoimg_12)
        lb1_img_12.place(x=0,y=0,width=490,height=340)

        #image_3
        img_13 = Image.open("image/mall.jpg")
        img_13 =img_13.resize((490,340),Image.ANTIALIAS)
        self.photoimg_13=ImageTk.PhotoImage(img_13)

        lb1_img_13=Label(Middle_Frame,image=self.photoimg_13)
        lb1_img_13.place(x=490,y=0,width=500,height=340)



        #Search
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=1020,y=10,width=500,height=40)

        self.lblBill = Label(Search_Frame ,font=("Comic Sans MS",12,"bold"),bg="magenta",fg="white",text="Bill Number")
        self.lblBill.grid(row=0,column=0 ,sticky=W,padx=1,pady=2)
        
        self.txt_Entry_Search = ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("Comic Sans MS",10,"bold"),width=24)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2) 

        self.BtnSearch = Button(Search_Frame, command=self.find_bill,text="Search",font=("Comic Sans MS",10,"bold"),bg="hotpink",fg="white",width=10,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2 ,sticky=W,padx=2)

       #Right Frame Bill Area
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("Times New Roman Baltic",11,"bold"),bg="white",fg="hotpink")
        RightLabelFrame.place(x=1000,y=45,width=480,height=440)

        scroll_y = Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="hotpink",font=("Times New Roman Baltic",11,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #Bill Counter Label Frame
        Bottom_Frame = LabelFrame(Main_Frame, text="Bill Counter",font=("Comic Sans MS",12,"bold"),bg="white",fg="hotpink")
        Bottom_Frame.place(x=0,y=485,width=1520,height=125)

        self.lblSubTotal = Label(Bottom_Frame  ,font=("Comic Sans MS",10,"bold"),bg="white",text="Sub Total",bd=4)
        self.lblSubTotal.grid(row=0,column=0 ,sticky=W,padx=5,pady=2)
        
        self.EntrySubTotal = ttk.Entry(Bottom_Frame,font=("Comic Sans MS",10,"bold"),width=24)
        self.EntrySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2) 

        self.lbl_tax = Label(Bottom_Frame  ,font=("Comic Sans MS",10,"bold"),bg="white",text=" Gov tax",bd=4)
        self.lbl_tax.grid(row=1,column=0 ,sticky=W,padx=5,pady=2)
        
        self.txt_tax = ttk.Entry(Bottom_Frame,font=("Comic Sans MS",10,"bold"),width=24)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblAmountTotal = Label(Bottom_Frame  ,font=("Comic Sans MS",10,"bold"),bg="white",text="Total",bd=4)
        self.lblAmountTotal.grid(row=2,column=0 ,sticky=W,padx=5,pady=2)
        
        self.EntryAmountTotal = ttk.Entry(Bottom_Frame,font=("Comic Sans MS",10,"bold"),width=24)
        self.EntryAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        # Button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart = Button(Btn_Frame,command=self.AddItem,height=2,text="Add To Cart",font=("Comic Sans MS",15,"bold"),bg="royalblue3",fg="white",width=16,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.BtnGenerateBill = Button(Btn_Frame,command=self.Gen_bill, height=2,text="Generate Bill",font=("Comic Sans MS",15,"bold"),bg="magenta",fg="white",width=16,cursor="hand2")
        self.BtnGenerateBill.grid(row=0,column=1)
        
        self.BtnSave = Button(Btn_Frame,command=self.save_bill, height=2,text="Save Bill ",font=("Comic Sans MS",15,"bold"),bg="turquoise1",fg="white",width=16,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

        self.BtnPrint= Button(Btn_Frame,command=self.iprint, height=2,text="Print Bill",font=("Comic Sans MS",15,"bold"),bg="red4",fg="white",width=16,cursor="hand2")
        self.BtnPrint .grid(row=0,column=3)

        self.BtnClear = Button(Btn_Frame,command=self.clear, height=2,text="Clear",font=("Comic Sans MS",15,"bold"),bg="mediumturquoise",fg="white",width=16,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit = Button(Btn_Frame,command=self.root.destroy, height=2,text="Exit",font=("Comic Sans MS",15,"bold"),bg="maroon1",fg="white",width=16,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
       
        self.welcome()     
        self.l=[] 

      # welcome Page
    def welcome(self):
         self.textarea.delete(1.0,END)
         self.textarea.insert(END,"Welcome To Mini Value And Veriety Mart")
         self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
         self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
         self.textarea.insert(END,f"\n Mobile number:{self.c_phone.get()}")
         self.textarea.insert(END,f"\n Email Id :{self.c_email.get()}")

         self.textarea.insert(END,f"\n==================================================")
         self.textarea.insert(END,f"\n PRODUCTS\t\t\tQTY\t\t\tPRICE")
         self.textarea.insert(END,f"\n==================================================\n") 

# ===================================Funciton ==============================================


    def AddItem(self):
         Tax=1
         self.n=self.prices.get()
         self.m=self.qty.get()*self.n
         self.l.append(self.m)
         if self.product.get()=="":
              messagebox.showerror("Error","Please select the Product Name")
         else:
              self.textarea.insert(END,f"\n {self.product.get()}\t\t\t{self.qty.get()}\t\t\t{self.m}")     
              self.sub_Total.set(str('Rs.%.2f'%(sum(self.l))))
              self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
              self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))       
 
  
    def Gen_bill(self):
         if self.product.get()=="":
              messagebox.showerror("Error","Please Add to cart Product")
         else:
              text=self.textarea.get(10.0,+(10.0+float(len(self.l))))      
              self.welcome()
              self.textarea.insert(END,text)
              self.textarea.insert(END,"\n==================================================")
              self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_Total.get()}")
              self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
              self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
              self.textarea.insert(END,"\n==================================================")
    
    # Save_Bills
    def save_bill(self):
         op=messagebox.askyesno("Save Bill ", "Do You Want To Save The Bill..")
         if op>0:
              self.bill_data=self.textarea.get(1.0,END)
              f1=open('Bills/'+str(self.bill_no.get())+".txt",'w')
              op=messagebox.showinfo("Saved ",f"Bill No:{self.bill_no.get()} saved Sucessfully")
         
              f1.write(self.bill_data)
              f1.close()

      # Print The bill

    def iprint(self):
         q = self.textarea.get(1.0,"end-1c")
         filename=tempfile.mktemp('.txt')
         open(filename,'w').write(q)
         os.startfile(filename,"print")

   # Find Bills 
    def find_bill(self):
         found="no"
         for i in os.listdir("Bills/"):
              if i.split('.')[0]==self.search_bill.get():
                   f1=open(f'Bills/{i}','r')
                   self.textarea.delete(1.0,END)
                   for d in f1:
                        self.textarea.insert(END,d)
                   f1.close()
                   found="yes"
         if found=="no":
              messagebox.showerror("Error","Invalid Bill No.. ")
                   
                   
       # Clear data
    def clear(self):  
        self.textarea.delete(1.0,END) 
        self.c_name.set("")
        self.c_phone.set("")
        self.c_email.set("")
        x = random.randint(1000,10000)
        self.bill_no.set(str(x))        
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_Total.set("")
        self.tax_input.set('')
        self.welcome()

    # Category Define
   
    def Categories(self,event=""):
          if self.Combo_Category.get()=="Clothing":
               self.ComboSubCategory.config(value=self.SubCatClothing)
               self.ComboSubCategory.current(0)

          if self.Combo_Category.get()=="LifeStyle":
               self.ComboSubCategory.config(value=self.SubCatLifeStyle)
               self.ComboSubCategory.current(0)

          if self.Combo_Category.get()=="Mobile":
               self.ComboSubCategory.config(value=self.SubCatMobiles)
               self.ComboSubCategory.current(0)


         # Product adding
    def Product_Add(self,event=""):
           #Clothing
           if self.ComboSubCategory.get()=="Pant":
                self.ComboProduct.config(value=self.Pant)
                self.ComboProduct.current(0)
            
           if self.ComboSubCategory.get()=="T-Shirt":
                self.ComboProduct.config(value=self.T_shirt)
                self.ComboProduct.current(0)
             
           if self.ComboSubCategory.get()=="Shirt":
                self.ComboProduct.config(value=self.Shirt)
                self.ComboProduct.current(0)

         # LifeStyle
           
           if self.ComboSubCategory.get()=="Bath_Soap":
                self.ComboProduct.config(value=self.Bath_Soap)
                self.ComboProduct.current(0)
           
           if self.ComboSubCategory.get()=="Face_Cream":
                self.ComboProduct.config(value=self.Face_Cream)
                self.ComboProduct.current(0)
           
           if self.ComboSubCategory.get()=="Hair_Oil":
                self.ComboProduct.config(value=self.Hair_Oil)
                self.ComboProduct.current(0)  
                                    
           if self.ComboSubCategory.get()=="Perfume":
                self.ComboProduct.config(value=self.Perfume)
                self.ComboProduct.current(0)

               #Mobile

           if self.ComboSubCategory.get()=="Iphone":
                self.ComboProduct.config(value=self.Iphone)
                self.ComboProduct.current(0)     

           if self.ComboSubCategory.get()=="Samsung":
                self.ComboProduct.config(value=self.Samsung)
                self.ComboProduct.current(0)


           if self.ComboSubCategory.get()=="Redmi":
                self.ComboProduct.config(value=self.Redmi)
                self.ComboProduct.current(0)

           if self.ComboSubCategory.get()=="RealMe":
                self.ComboProduct.config(value=self.RealMe)
                self.ComboProduct.current(0)

           if self.ComboSubCategory.get()=="OnePlus":
                self.ComboProduct.config(value=self.OnePlus)
                self.ComboProduct.current(0)

           if self.ComboSubCategory.get()=="Oppo":
                self.ComboProduct.config(value=self.Oppo)
                self.ComboProduct.current(0)

           if self.ComboSubCategory.get()=="Vivo":
                self.ComboProduct.config(value=self.Vivo)
                self.ComboProduct.current(0)
 
        #  Price Of The Product
    def price(self,event=""):
         #pant
         if self.ComboProduct.get()=="Levis":
              self.ComboPrice.config(value=self.Price_Levis)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Mufti":
              self.ComboPrice.config(value=self.Price_Mufti)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Spykar":
              self.ComboPrice.config(value=self.Price_Spykar)
              self.ComboProduct.current(0)
              self.qty.set(1)         
      
         #T-Shirt

         if self.ComboProduct.get()=="Polo":
              self.ComboPrice.config(value=self.Price_polo)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Roadster":
              self.ComboPrice.config(value=self.Price_roadster)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="3bros":
              self.ComboPrice.config(value=self.Price_3bros)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="HRX":
              self.ComboPrice.config(value=self.Price_HRX)
              self.ComboProduct.current(0)
              self.qty.set(1)

        # Shirt

         if self.ComboProduct.get()=="Peter England ":
              self.ComboPrice.config(value=self.Price_Peter)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Lius Phillipe":
              self.ComboPrice.config(value=self.Price_Lius)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Park Avanue":
              self.ComboPrice.config(value=self.Price_ParkAvanue)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Netplay":
              self.ComboPrice.config(value=self.Price_Netplay)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="JackJones":
              self.ComboPrice.config(value=self.Price_JackJones)
              self.ComboProduct.current(0)
              self.qty.set(1)

       # Bath_Soap    

         if self.ComboProduct.get()=="Dove":
              self.ComboPrice.config(value=self.Price_Dove)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Dettol":
              self.ComboPrice.config(value=self.Price_Dettol)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Cinthol":
              self.ComboPrice.config(value=self.Price_Cinthol)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Lux":
              self.ComboPrice.config(value=self.Price_Lux)
              self.ComboProduct.current(0)
              self.qty.set(1)
              
         if self.ComboProduct.get()=="Santoor":
              self.ComboPrice.config(value=self.Price_Santoor)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Pearl":
              self.ComboPrice.config(value=self.Price_Pearl)
              self.ComboProduct.current(0)
              self.qty.set(1)

       #Face_Cream   
         if self.ComboProduct.get()=="Fair And Handsome":
              self.ComboPrice.config(value=self.Price_Fair)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Himalaya":
              self.ComboPrice.config(value=self.Price_Himalaya)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Mamaearth":
              self.ComboPrice.config(value=self.Price_Mamaearth)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Ponds":
              self.ComboPrice.config(value=self.Price_Ponds)
              self.ComboProduct.current(0)
              self.qty.set(1)

         # Hair_Oil

         if self.ComboProduct.get()=="Dabur":
              self.ComboPrice.config(value=self.Price_Dabur)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Kesh_King":
              self.ComboPrice.config(value=self.Price_Keshking)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Parachute":
              self.ComboPrice.config(value=self.Price_Parachute)
              self.ComboProduct.current(0)
              self.qty.set(1) 

         if self.ComboProduct.get()=="Bajaj":
              self.ComboPrice.config(value=self.Price_Bajaj)
              self.ComboProduct.current(0)
              self.qty.set(1)
           
            #Perfume

         if self.ComboProduct.get()=="Gucci":
              self.ComboPrice.config(value=self.Price_Gucci)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Beardo":
              self.ComboPrice.config(value=self.Price_Beardo)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Engage":
              self.ComboPrice.config(value=self.Price_Engage)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Fogg":
              self.ComboPrice.config(value=self.Price_Fogg)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Wild Stone":
              self.ComboPrice.config(value=self.Price_WildStone)
              self.ComboProduct.current(0)
              self.qty.set(1)

       # Iphone  
         if self.ComboProduct.get()=="Iphone_X":
              self.ComboPrice.config(value=self.Price_IphoneX)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Iphone_XI":
              self.ComboPrice.config(value=self.Price_IphoneXI)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Iphone_XII":
              self.ComboPrice.config(value=self.Price_IphoneXII)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Iphone_XIII":
              self.ComboPrice.config(value=self.Price_IphoneXIII)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Iphone_XIV":
              self.ComboPrice.config(value=self.Price_IphoneXIV)
              self.ComboProduct.current(0)
              self.qty.set(1)

        
         # Samsung  
        
         if self.ComboProduct.get()=="Galaxy_S1":
              self.ComboPrice.config(value=self.Price_S1)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Galaxy_S2":
              self.ComboPrice.config(value=self.Price_S2)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Samsung_M2_Pro":
              self.ComboPrice.config(value=self.Price_M2)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Samsung_M5_Pro":
              self.ComboPrice.config(value=self.Price_M5)
              self.ComboProduct.current(0)
              self.qty.set(1)

       # Redmi

         if self.ComboProduct.get()=="Note_7":
              self.ComboPrice.config(value=self.Price_Note7)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Note_9":
              self.ComboPrice.config(value=self.Price_Note9)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Note_11":
              self.ComboPrice.config(value=self.Price_Note11)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Note_13":
              self.ComboPrice.config(value=self.Price_Note13)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Note_15":
              self.ComboPrice.config(value=self.Price_Note15)
              self.ComboProduct.current(0)
              self.qty.set(1)

         # RealMe  

         if self.ComboProduct.get()=="Realme_6":
              self.ComboPrice.config(value=self.Price_RealM6)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Realme_7":
              self.ComboPrice.config(value=self.Price_RealM7)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Realme_8":
              self.ComboPrice.config(value=self.Price_RealM8)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Realme_9":
              self.ComboPrice.config(value=self.Price_RealM9)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Realme_10":
              self.ComboPrice.config(value=self.Price_RealM10)
              self.ComboProduct.current(0)
              self.qty.set(1)

      # OnePLus  

         if self.ComboProduct.get()=="OnePlus7":
              self.ComboPrice.config(value=self.Price_OnePlus7)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="OnePlus8":
              self.ComboPrice.config(value=self.Price_OnePlus8)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="OnePlus9":
              self.ComboPrice.config(value=self.Price_OnePlus9)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="OnePlus10":
              self.ComboPrice.config(value=self.Price_OnePlus10)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="OnePlus11":
              self.ComboPrice.config(value=self.Price_OnePlus11)
              self.ComboProduct.current(0)
              self.qty.set(1)
       
       # Oppo 

         if self.ComboProduct.get()=="Reno_7":
              self.ComboPrice.config(value=self.Price_Reno7)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Reno_8":
              self.ComboPrice.config(value=self.Price_Reno8)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Oppo_A7":
              self.ComboPrice.config(value=self.Price_A7)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Oppo_A8":
              self.ComboPrice.config(value=self.Price_A8)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Oppo_A55":
              self.ComboPrice.config(value=self.Price_A55)
              self.ComboProduct.current(0)
              self.qty.set(1)
      
      # Vivo 

         if self.ComboProduct.get()=="Vivo_V23":
              self.ComboPrice.config(value=self.Price_V23)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Vivo_V25":
              self.ComboPrice.config(value=self.Price_V25)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Vivo_V27":
              self.ComboPrice.config(value=self.Price_V27)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Vivo_V29":
              self.ComboPrice.config(value=self.Price_V29)
              self.ComboProduct.current(0)
              self.qty.set(1)

         if self.ComboProduct.get()=="Vivo_S1":
              self.ComboPrice.config(value=self.Price_VS1)
              self.ComboProduct.current(0)
              self.qty.set(1)
      
      # End 

if __name__=='__main__':
    root = Tk()
    obj = Bill_App(root)
    root.mainloop()