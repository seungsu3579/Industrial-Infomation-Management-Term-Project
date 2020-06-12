import tkinter as tk
from tkinter import ttk
import tkinter.font
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import dbModel
from datetime import date

############################
## 2016147014 seungsu yoo ##
############################
##   산.정.관   final 과제 ##
############################



class SpaceProgram():
    def __init__(self, db):
        self.window = tk.Tk()
        self.window.title("space space")
        self.window.geometry("860x1000")
        self.db = db
        self.Basket = []
        self.productWindow = None
        self.styleWindow = None
        self.createWidgets()
        self.confirmLogin()



    def confirmLogin(self):
        # - - - - - - - - - - - - - - - - - - - - -
        # The Login frame
        self.loginWindow = tk.Tk()
        self.loginWindow.title("Login Page")
        self.loginWindow.geometry("350x100")
        self.loginWindow['padx'] = 10
        self.loginWindow['pady'] = 10

        self.Log_frame = ttk.LabelFrame(self.loginWindow, text="Log-In", relief=tk.RIDGE)
        self.Log_frame.grid(row=1, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

        ID_label = ttk.Label(self.Log_frame, width=12, text="CustomerID")
        ID_label.grid(row=1, column=1, sticky=tk.W, pady=3)

        PW_label = ttk.Label(self.Log_frame, width=12, text="CustomerPW")
        PW_label.grid(row=2, column=1, sticky=tk.W, pady=3)
        
        self.ID_entry = ttk.Entry(self.Log_frame, width=20)
        self.ID_entry.grid(row=1, column=2, sticky=tk.W, pady=3, ipady=3, ipadx=3)

        self.PW_entry = ttk.Entry(self.Log_frame, width=20)
        self.PW_entry.grid(row=2, column=2, sticky=tk.W, pady=3, ipady=3, ipadx=3)

        Login_button = ttk.Button(self.Log_frame, text="Log-In",  command=self.login)
        Login_button.grid(row=1, column=3)

    
    def createMypage(self):
        self.mypageWindow = tk.Tk()
        self.mypageWindow.title("MyPage")
        self.mypageWindow.geometry("870x500")
        self.mypageWindow['padx'] = 10
        self.mypageWindow['pady'] = 10

        # title
        self.Mypage_Title_frame = ttk.LabelFrame(self.mypageWindow, relief=tk.RIDGE)
        self.Mypage_Title_frame.grid(row=1, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

        self.Mypage_Title_label = ttk.Label(self.Mypage_Title_frame, text="마이페이지", font=tk.font.Font(size=40))
        self.Mypage_Title_label.grid(row=1, column=1)


        # user_Info
        self.Mypage_User_frame = ttk.LabelFrame(self.mypageWindow, text="User-Info", relief=tk.RIDGE)
        self.Mypage_User_frame.grid(row=1, column=2, sticky=tk.E + tk.W + tk.N + tk.S)

        self.Mypage_Name_label = ttk.Label(self.Mypage_User_frame, text="이름")
        self.Mypage_Name_label.grid(row=1, column=1)

        self.Mypage_Grade_label = ttk.Label(self.Mypage_User_frame, text="등급")
        self.Mypage_Grade_label.grid(row=2, column=1)

        self.Mypage_Point_label = ttk.Label(self.Mypage_User_frame, text="포인트")
        self.Mypage_Point_label.grid(row=3, column=1)
        

        # User Chart
        self.User_Menu_Frame = ttk.LabelFrame(self.mypageWindow, text="Category", relief=tk.RIDGE)
        self.User_Menu_Frame.grid(row=2, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

        self.CusInfoButton = tk.Button(self.User_Menu_Frame, text="개인정보", width=20, command = self.showCustomerInfo)
        self.CusInfoButton.grid(row=1, column=1)
        self.CouponButton = tk.Button(self.User_Menu_Frame, text="쿠폰", width=20, command = self.showCouponlist)
        self.CouponButton.grid(row=2, column=1)
        self.AddressButton = tk.Button(self.User_Menu_Frame, text="배송지", width=20, command = self.showAddresslist)
        self.AddressButton.grid(row=3, column=1)
        self.TransListButton = tk.Button(self.User_Menu_Frame, text="거래내역", width=20, command = self.showTranslist)
        self.TransListButton.grid(row=4, column=1)

        # User Info detail
        self.Mypage_Detail_frame = ttk.LabelFrame(self.mypageWindow, text="Detail Information", relief=tk.RIDGE)
        self.Mypage_Detail_frame.grid(row=2, column=2, sticky=tk.E + tk.W + tk.N + tk.S)

        self.refresh_mypage()


    def createWidgets(self):
        self.window['padx'] = 10
        self.window['pady'] = 10

        
        # title
        self.Title_frame = ttk.LabelFrame(self.window, relief=tk.RIDGE)
        self.Title_frame.grid(row=1, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

        self.Title_label = ttk.Label(self.Title_frame, text="우주공간", font=tk.font.Font(size=40))
        self.Title_label.grid(row=1, column=1)


        # user_Info
        self.User_frame = ttk.LabelFrame(self.window, text="User-Info", relief=tk.RIDGE)
        self.User_frame.grid(row=1, column=2, sticky=tk.E + tk.W + tk.N + tk.S)

        self.Name_label = ttk.Label(self.User_frame, text="이름", font=tk.font.Font(size=10))
        self.Name_label.grid(row=1, column=1)

        self.Grade_label = ttk.Label(self.User_frame, text="등급", font=tk.font.Font(size=10))
        self.Grade_label.grid(row=2, column=1)

        self.Point_label = ttk.Label(self.User_frame, text="포인트", font=tk.font.Font(size=10))
        self.Point_label.grid(row=3, column=1)

        self.blank1 = ttk.Label(self.User_frame, width=39, text=" ")
        self.blank1.grid(row=2, column=2)

        self.Mypage_button = ttk.Button(self.User_frame, width=13, text="마이페이지", command=self.createMypage)
        self.Mypage_button.grid(row=1, column=3, rowspan=3, ipadx=5 , ipady=15)



        # Category
        self.Category_frame = ttk.LabelFrame(self.window, text="Category", relief=tk.RIDGE)
        self.Category_frame.grid(row=2, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

        # categories=["Outer", "Sweater", "Shirts", "Pants", "Jean", "Training", "Shoes", "Bag"]

        self.outerCategoryButton = tk.Button(self.Category_frame, text="Outer", width=30, command = lambda : self.showCategoryProduct("Outer"))
        self.outerCategoryButton.grid(row=1, column=1)
        self.sweaterCategoryButton = tk.Button(self.Category_frame, text="Sweater", width=30, command = lambda : self.showCategoryProduct("Sweater"))
        self.sweaterCategoryButton.grid(row=2, column=1)
        self.shirtsCategoryButton = tk.Button(self.Category_frame, text="Shirts", width=30, command = lambda : self.showCategoryProduct("Shirts"))
        self.shirtsCategoryButton.grid(row=3, column=1)
        self.pantsCategoryButton = tk.Button(self.Category_frame, text="Pants", width=30, command = lambda : self.showCategoryProduct("Pants"))
        self.pantsCategoryButton.grid(row=4, column=1)
        self.jeanCategoryButton = tk.Button(self.Category_frame, text="Jean", width=30, command = lambda : self.showCategoryProduct("Jean"))
        self.jeanCategoryButton.grid(row=5, column=1)
        self.trainingCategoryButton = tk.Button(self.Category_frame, text="Training", width=30, command = lambda : self.showCategoryProduct("Training"))
        self.trainingCategoryButton.grid(row=6, column=1)
        self.shoesCategoryButton = tk.Button(self.Category_frame, text="Shoes", width=30, command = lambda : self.showCategoryProduct("Shoes"))
        self.shoesCategoryButton.grid(row=7, column=1)
        self.bagCategoryButton = tk.Button(self.Category_frame, text="bag", width=30, command = lambda : self.showCategoryProduct("bag"))
        self.bagCategoryButton.grid(row=8, column=1)



        # Product
        self.Product_frame = ttk.LabelFrame(self.window, relief=tk.RIDGE)
        self.Product_frame.grid(row=2, column=2, sticky=tk.E + tk.W + tk.N + tk.S)

        self.productOrder_frame = ttk.LabelFrame(self.Product_frame, text="Sort")
        self.productOrder_frame.grid(row=1, column=1)
        self.newOrderButton = tk.Button(self.productOrder_frame, text="신상품순", width=13, command = lambda : self.showOrderProduct("AcquiredDate", "DESC"))
        self.newOrderButton.grid(row=1,column=1)
        self.highPriceOrderButton = tk.Button(self.productOrder_frame, text="높은가격순", width=13, command = lambda : self.showOrderProduct("Price", "DESC"))
        self.highPriceOrderButton.grid(row=1,column=2)
        self.lowPriceOrderButton = tk.Button(self.productOrder_frame, text="낮은가격순", width=13, command = lambda : self.showOrderProduct("Price", "ASC"))
        self.lowPriceOrderButton.grid(row=1,column=3)
        self.brandOrderButton = tk.Button(self.productOrder_frame, text="브랜드순", width=13, command = lambda : self.showOrderProduct("Brand", "ASC"))
        self.brandOrderButton.grid(row=1,column=4)


        self.item_frame = ttk.LabelFrame(self.Product_frame, text="item list")
        self.item_frame.grid(row=2, column=1)

        self.itemTree = ttk.Treeview(self.item_frame, columns=["브랜드", "제품명", "가격"])
        self.itemTree.pack()

        self.itemTree.column("#0", width=10)
        self.itemTree.heading("#0", text="")

        self.itemTree.column("브랜드", width=100, anchor="w")
        self.itemTree.heading("브랜드", text="브랜드", anchor="center")

        self.itemTree.column("제품명", width=200, anchor="w")
        self.itemTree.heading("제품명", text="제품명", anchor="center")

        self.itemTree.column("가격", width=100, anchor="w")
        self.itemTree.heading("가격", text="가격", anchor="center")

        self.itemTree.bind("<Double-1>", self.showItemInfo)

        # Influencer Category
        self.Category_Influencer_frame = ttk.LabelFrame(self.window, text="Influencer", relief=tk.RIDGE)
        self.Category_Influencer_frame.grid(row=3, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

        self.influencerButton1 = tk.Button(self.Category_Influencer_frame, text="Show All", width=30, command = lambda : self.showCategoryInfluencer("refresh"))
        self.influencerButton1.grid(row=1, column=1)
        self.influencerButton2 = tk.Button(self.Category_Influencer_frame, text="toybox505", width=30, command = lambda : self.showCategoryInfluencer("toybox505"))
        self.influencerButton2.grid(row=2, column=1)
        self.influencerButton3 = tk.Button(self.Category_Influencer_frame, text="woojoo123", width=30, command = lambda : self.showCategoryInfluencer("woojoo123"))
        self.influencerButton3.grid(row=3, column=1)

        # Style
        self.Style_frame = ttk.LabelFrame(self.window, text="Style Advice", relief=tk.RIDGE)
        self.Style_frame.grid(row=3, column=2, sticky=tk.E + tk.W + tk.N + tk.S)

        self.styleTree = ttk.Treeview(self.Style_frame, columns=["스타일 작성자", "스타일 설명"])
        self.styleTree.pack()

        self.styleTree.column("#0", width=10)
        self.styleTree.heading("#0", text="")

        self.styleTree.column("스타일 작성자", width=100, anchor="w")
        self.styleTree.heading("스타일 작성자", text="스타일 작성자", anchor="center")

        self.styleTree.column("스타일 설명", width=300, anchor="w")
        self.styleTree.heading("스타일 설명", text="스타일 설명", anchor="center")

        self.styleTree.bind("<Double-1>", self.showStyleInfo)


        # Basket
        self.Basket_frame = ttk.LabelFrame(self.window, text="장바구니", relief=tk.RIDGE)
        self.Basket_frame.grid(row=2, column=3, sticky=tk.E + tk.W + tk.N + tk.S)
        self.Basket_listbox = tk.Listbox(self.Basket_frame, width=25, selectmode = MULTIPLE, height=8)
        self.Basket_listbox.grid(row=1, column=1, columnspan=2)

        self.blank2 = tk.Label(self.Basket_frame, height=1, text=" ")
        self.blank2.grid(row=2, column=2)

        self.basket_buy_Button = tk.Button(self.Basket_frame, width=10, text="구매", command = self.selectOption)
        self.basket_buy_Button.grid(row=3, column=1)

        self.basket_delete_Button = tk.Button(self.Basket_frame, width=10, text="장바구니 삭제", command = lambda : self.deleteBasket(self.Basket_listbox.curselection()))
        self.basket_delete_Button.grid(row=3, column=2)


    def selectOption(self):
        self.selectWindow = tk.Tk()
        self.selectWindow.title("Select Option")
        self.selectWindow.geometry("600x600")
        self.selectWindow['padx'] = 10
        self.selectWindow['pady'] = 10

        # 상품정보, 판매자, 배송비, 수량, 할인, 주문금액
        self.buy_Item_frame = ttk.LabelFrame(self.selectWindow, relief=tk.RIDGE)
        self.buy_Item_frame.grid(row=1, column=1, columnspan=2, sticky=tk.E + tk.W + tk.N + tk.S)

        self.buy_item_column_frame = ttk.LabelFrame(self.buy_Item_frame)
        self.buy_item_column_frame.grid(row=1, column=1, columnspan=2, sticky=tk.E + tk.W + tk.N + tk.S)

        
        self.MyPage_Detail_Label1 = ttk.Label(self.buy_item_column_frame, width=28, text="상품정보")
        self.MyPage_Detail_Label1.grid(row=1, column=1, padx=10,pady=10)

        self.MyPage_Detail_Label2 = ttk.Label(self.buy_item_column_frame, width=17, text="색상")
        self.MyPage_Detail_Label2.grid(row=1, column=2, padx=5, pady=5)

        self.MyPage_Detail_Label3 = ttk.Label(self.buy_item_column_frame, width=17, text="사이즈")
        self.MyPage_Detail_Label3.grid(row=1, column=3, padx=5, pady=5)

        self.MyPage_Detail_Label4 = ttk.Label(self.buy_item_column_frame, width=17, text="수량")
        self.MyPage_Detail_Label4.grid(row=1, column=4, padx=5, pady=5)

        num, self.buyitemList = db.showItemOrder("AcquiredDate", "DESC")

        self.buy_Item_frame_list = []

        for i in range(num):
            if self.buyitemList[i]['ProductName'] in self.Basket:

                self.buy_Item_frame_list.append({})

                self.buy_Item_frame_list[len(self.buy_Item_frame_list)-1]['frame'] = ttk.LabelFrame(self.buy_Item_frame)
                self.buy_Item_frame_list[len(self.buy_Item_frame_list)-1]['frame'].grid(row=i+2, column=1, columnspan=2, sticky=tk.E + tk.W + tk.N + tk.S)

                self.buy_Item_frame_list[len(self.buy_Item_frame_list)-1]['ProductName'] = ttk.Label(self.buy_Item_frame_list[len(self.buy_Item_frame_list)-1]['frame'], width=25, text=self.buyitemList[i]['ProductName'])
                self.buy_Item_frame_list[len(self.buy_Item_frame_list)-1]['ProductName'].grid(row=1, column=1, padx=10, pady=10)

                self.selection_Item_Name_label = ttk.Label(self.buy_Item_frame_list[len(self.buy_Item_frame_list)-1]['frame'], width=25, text="+ 옵션을 선택해주세요")
                self.selection_Item_Name_label.grid(row=2, column=1, padx=10, pady=10)


                self.selection_Item_Color_List = tk.Listbox(self.buy_Item_frame_list[len(self.buy_Item_frame_list)-1]['frame'], width=10, height=2)
                self.selection_Item_Color_List.grid(row=1, column=2, padx=30)
                numColor, inventoryColorItem = db.getInventoryItem("Color", self.buyitemList[i]['ProductName'])

                for m in range(numColor):
                    self.selection_Item_Color_List.insert(tk.END, inventoryColorItem[m]['Color'])

                self.buy_Item_frame_list[len(self.buy_Item_frame_list)-1]['Color'] = ttk.Entry(self.buy_Item_frame_list[len(self.buy_Item_frame_list)-1]['frame'], width=9)
                self.buy_Item_frame_list[len(self.buy_Item_frame_list)-1]['Color'].grid(row=2, column=2, padx=30, sticky=tk.W, pady=10, ipady=3, ipadx=3)
                self.buy_Item_frame_list[len(self.buy_Item_frame_list)-1]['Color'].insert(tk.END, inventoryColorItem[0]['Color'])


                self.selection_Item_Size_List = tk.Listbox(self.buy_Item_frame_list[len(self.buy_Item_frame_list)-1]['frame'], width=10, height=2)
                self.selection_Item_Size_List.grid(row=1, column=3, padx=30)
                numSize, inventorySizeItem = db.getInventoryItem("Size", self.buyitemList[i]['ProductName'])

                for n in range(numSize):
                    self.selection_Item_Size_List.insert(tk.END, inventorySizeItem[n]['Size'])

                self.buy_Item_frame_list[len(self.buy_Item_frame_list)-1]['Size'] = ttk.Entry(self.buy_Item_frame_list[len(self.buy_Item_frame_list)-1]['frame'], width=9)
                self.buy_Item_frame_list[len(self.buy_Item_frame_list)-1]['Size'].grid(row=2, column=3, padx=30, sticky=tk.W, pady=10, ipady=3, ipadx=3)
                self.buy_Item_frame_list[len(self.buy_Item_frame_list)-1]['Size'].insert(tk.END, inventorySizeItem[0]['Size'])

                self.buy_Item_frame_list[len(self.buy_Item_frame_list)-1]['Quantity'] = ttk.Entry(self.buy_Item_frame_list[len(self.buy_Item_frame_list)-1]['frame'], width=1)
                self.buy_Item_frame_list[len(self.buy_Item_frame_list)-1]['Quantity'].grid(row=2, column=4, padx=30, sticky=tk.W, pady=10, ipady=3, ipadx=3)
                self.buy_Item_frame_list[len(self.buy_Item_frame_list)-1]['Quantity'].insert(tk.END, "1")

        self.paymentbutton = tk.Button(self.selectWindow, width=13, text="구매확정", command = self.payment)
        self.paymentbutton.grid(row=4, column=1, columnspan=2, ipadx=10, ipady=10)



    def payment(self):

        self.paymentWindow = tk.Tk()
        self.paymentWindow.title("Payment")
        self.paymentWindow.geometry("600x580")
        self.paymentWindow['padx'] = 10
        self.paymentWindow['pady'] = 10

        self.priceList = []
        
        self.payment_frame0 = ttk.LabelFrame(self.paymentWindow)
        self.payment_frame0.grid(row=1, column=1, columnspan=2, sticky=tk.E + tk.W + tk.N + tk.S)

        
        self.MyPage_Detail_Label1 = ttk.Label(self.payment_frame0, width=19, text="상품정보")
        self.MyPage_Detail_Label1.grid(row=1, column=1, padx=10,pady=10)

        self.MyPage_Detail_Label2 = ttk.Label(self.payment_frame0, width=15, text="색상")
        self.MyPage_Detail_Label2.grid(row=1, column=2, padx=5, pady=5)

        self.MyPage_Detail_Label3 = ttk.Label(self.payment_frame0, width=18, text="사이즈")
        self.MyPage_Detail_Label3.grid(row=1, column=3, padx=5, pady=5)

        self.MyPage_Detail_Label4 = ttk.Label(self.payment_frame0, width=15, text="주문금액")
        self.MyPage_Detail_Label4.grid(row=1, column=4, padx=5, pady=5)


        # 상품 나열
        self.payment_frame1 = ttk.LabelFrame(self.paymentWindow, text="Products", relief=tk.RIDGE)
        self.payment_frame1.grid(row=2, column=1, columnspan=2, sticky=tk.E + tk.W + tk.N + tk.S)

        for i in range(len(self.buy_Item_frame_list)):
            self.buy_item_small_frame = ttk.LabelFrame(self.payment_frame1)
            self.buy_item_small_frame.grid(row=i, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

            self.buy_Item_Name_label = ttk.Label(self.buy_item_small_frame, width=15, text=self.buy_Item_frame_list[i]['ProductName']['text'])
            self.buy_Item_Name_label.grid(row=1, column=1, padx=10, pady=10)
            self.buy_Item_frame_list[i]['ProductName'] = str(self.buy_Item_frame_list[i]['ProductName']['text'])

            self.buy_Item_Color_label = ttk.Label(self.buy_item_small_frame, width=9, text=self.buy_Item_frame_list[i]['Color'].get())
            self.buy_Item_Color_label.grid(row=1, column=2, padx=30, sticky=tk.W, pady=10, ipady=3, ipadx=3)
            self.buy_Item_frame_list[i]['Color'] = str(self.buy_Item_frame_list[i]['Color'].get())

            self.buy_Item_Size_label = ttk.Label(self.buy_item_small_frame, width=9, text=self.buy_Item_frame_list[i]['Size'].get())
            self.buy_Item_Size_label.grid(row=1, column=3, padx=30, sticky=tk.W, pady=10, ipady=3, ipadx=3)
            self.buy_Item_frame_list[i]['Size'] = str(self.buy_Item_frame_list[i]['Size'].get())

            self.buy_Item_Quantity_label = ttk.Label(self.buy_item_small_frame, width=1, text=self.buy_Item_frame_list[i]['Quantity'].get())
            self.buy_Item_Quantity_label.grid(row=1, column=4, padx=30, sticky=tk.W, pady=10, ipady=3, ipadx=3)
            self.buy_Item_frame_list[i]['Quantity'] = str(self.buy_Item_frame_list[i]['Quantity'].get())

            num, buyItem = db.getProductInfo(self.buy_Item_frame_list[i]['ProductName'])
            price = int(buyItem['Price'])*int(self.buy_Item_frame_list[i]['Quantity'])
            self.priceList.append(price)

            self.buy_Item_Price_label = ttk.Label(self.buy_item_small_frame, width=10, text= price)
            self.buy_Item_Price_label.grid(row=1, column=4, padx=30, sticky=tk.W, pady=10, ipady=3, ipadx=3)


        # 배송지
        self.payment_frame2 = ttk.LabelFrame(self.paymentWindow, text="Address", relief=tk.RIDGE)
        self.payment_frame2.grid(row=3, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

        self.paymentAddressTree = ttk.Treeview(self.payment_frame2, columns=["주소지"])
        self.paymentAddressTree.grid(row=1, column=1)
        self.paymentAddressTree['height'] = 5

        self.paymentAddressTree.column("#0", width=20)
        self.paymentAddressTree.heading("#0", text="")

        self.paymentAddressTree.column("주소지", width=240, anchor="w")
        self.paymentAddressTree.heading("주소지", text="주소지", anchor="center")

        self.paymentAddressTree.bind("<Double-1>", self.refresh_payment)

        num, self.paymentAddressList = db.getAddress(self.ID_str)
        for i in range(num):
            self.paymentAddressTree.insert('', 'end', values=tuple(self.paymentAddressList[i].values()), iid=str(i))


        # 쿠폰
        self.payment_frame3 = ttk.LabelFrame(self.paymentWindow, text="Coupon", relief=tk.RIDGE)
        self.payment_frame3.grid(row=3, column=2, rowspan=2, sticky=tk.E + tk.W + tk.N + tk.S)

        self.paymentCouponTree = ttk.Treeview(self.payment_frame3, columns=["목록", "할인률"])
        self.paymentCouponTree.grid(row=1, column=1)
        self.paymentCouponTree['height'] = 5

        self.paymentCouponTree.column("#0", width=20)
        self.paymentCouponTree.heading("#0", text="")

        self.paymentCouponTree.column("목록", width=130, anchor="w")
        self.paymentCouponTree.heading("목록", text="목록", anchor="center")

        self.paymentCouponTree.column("할인률", width=110, anchor="w")
        self.paymentCouponTree.heading("할인률", text="할인률", anchor="center")

        self.paymentCouponTree.bind("<Double-1>", self.refresh_payment)
        self.paymentCouponTree.bind("<Double-3>", self.cancelSelectCoupon)
        

        num, self.paymentCouponList = db.getCoupon(self.ID_str)
        for i in range(num):
            coupon = self.paymentCouponList[i]['Coupon']
            self.paymentCouponTree.insert('', 'end', values=(coupon, coupon[0:2]+"%"), iid=str(i))



        # 결제방식
        self.payment_frame4 = ttk.LabelFrame(self.paymentWindow, text="Payment", relief=tk.RIDGE)
        self.payment_frame4.grid(row=4, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

        self.paymentList = ["무통장입금", "카드결제", "실시간계좌이체", "가상계좌", "휴대폰결제", "문화상품권", "카카오페이", "제로페이", "페이코"]

        self.paymentTree = ttk.Treeview(self.payment_frame4, columns=["결제방식"])
        self.paymentTree.grid(row=1, column=1)
        self.paymentTree['height'] = 9

        self.paymentTree.column("#0", width=20)
        self.paymentTree.heading("#0", text="")

        self.paymentTree.column("결제방식", width=240, anchor="w")
        self.paymentTree.heading("결제방식", text="결제방식", anchor="center")

        self.paymentTree.bind("<Double-1>", self.refresh_payment)

        for i in range(len(self.paymentList)):
            self.paymentTree.insert('', 'end', values=(self.paymentList[i]), iid=str(i))


        # 결제정보 프레임
        self.payment_frame5 = ttk.LabelFrame(self.paymentWindow, relief=tk.RIDGE)
        self.payment_frame5.grid(row=4, column=2, sticky=tk.E + tk.W + tk.N + tk.S)

        self.payment_select_Address_label = ttk.Label(self.payment_frame5, width =10 ,text="▶ Address")
        self.payment_select_Address_label.grid(row=1,column=1, padx=10, pady=10)
        self.payment_select_Address = ttk.Label(self.payment_frame5, width =20 ,text="배송지를 선택해주세요")
        self.payment_select_Address.grid(row=1,column=2, padx=10, pady=10)

        self.payment_select_Coupon_label = ttk.Label(self.payment_frame5, width =10 ,text="▶ Coupon")
        self.payment_select_Coupon_label.grid(row=2,column=1, padx=10, pady=10)
        self.payment_select_Coupon = ttk.Label(self.payment_frame5, width =20 ,text="쿠폰을 선택해주세요")
        self.payment_select_Coupon.grid(row=2,column=2, padx=10, pady=10)

        self.payment_select_Payment_label = ttk.Label(self.payment_frame5, width =10 ,text="▶ Payment")
        self.payment_select_Payment_label.grid(row=3,column=1, padx=10, pady=10)
        self.payment_select_Payment = ttk.Label(self.payment_frame5, width =20 ,text="결제방식을 선택해주세요")
        self.payment_select_Payment.grid(row=3,column=2, padx=10, pady=10)

        price = sum(self.priceList)
        self.payment_select_Price_label = ttk.Label(self.payment_frame5, width =10 ,text="▶ Price")
        self.payment_select_Price_label.grid(row=4,column=1, padx=10, pady=10)
        self.payment_select_Price = ttk.Label(self.payment_frame5, width =20 ,text=price)
        self.payment_select_Price.grid(row=4,column=2, padx=10, pady=10)

        self.payment_confirm_button = ttk.Button(self.payment_frame5, text="구매", command = self.confirmPayment)
        self.payment_confirm_button.grid(row=5,column=1,columnspan=2, padx=10, pady=10)

        self.selectWindow.destroy()

    def cancelSelectCoupon(self, event):
        if len(self.paymentCouponTree.selection()) != 0:
            price = sum(self.priceList)
            self.payment_select_Price = ttk.Label(self.payment_frame5, width =20 ,text=price)
            self.payment_select_Price.grid(row=4,column=2, padx=10, pady=10)
            self.payment_select_Coupon = ttk.Label(self.payment_frame5, width =20 ,text="적용할 쿠폰을 선택해주세요")
            self.payment_select_Coupon.grid(row=2,column=2, padx=10, pady=10)
            k = self.paymentCouponTree.selection()[0]
            self.paymentCouponTree.selection_remove(k)

    def confirmPayment(self):
        if len(self.paymentAddressTree.selection()) == 0 and len(self.paymentTree.selection()) == 0:
            failorder = tkinter.messagebox.showerror("메세지 상자", "주소와 결제방식이 입력되지 않았습니다.")
        elif len(self.paymentAddressTree.selection()) == 0:
            failorder = tkinter.messagebox.showerror("메세지 상자", "주소가 입력되지 않았습니다.")
        elif len(self.paymentTree.selection()) == 0:
            failorder = tkinter.messagebox.showerror("메세지 상자", "결제방식이 입력되지 않았습니다.")
        elif len(self.paymentAddressTree.selection()) != 0 and len(self.paymentTree.selection()) != 0:
            # Trans data insert
            db.insertTrans(self.total_payment_Info['User'], self.total_payment_Info['Payment'], self.total_payment_Info['Price'], str(date.today()), self.total_payment_Info['DeliveryAddress'])
            trans_id = db.getTransID(self.total_payment_Info['User'], self.total_payment_Info['Payment'], self.total_payment_Info['Price'], str(date.today()), self.total_payment_Info['DeliveryAddress'])

            # T_h_I data insert
            for item in self.buy_Item_frame_list:
                invenItem = db.getInvenID(item['Size'], item['Color'], item['ProductName'])
                num, buyItem = db.getProductInfo(item['ProductName'])
                if "Coupon" in self.total_payment_Info:
                    price = int(buyItem['Price'])*int(item['Quantity'])*(100 - int(self.total_payment_Info['Coupon'][0:2]))*0.01
                    db.deleteCoupon(self.total_payment_Info['Coupon'], self.ID_str)
                else:
                    price = int(buyItem['Price'])*int(item['Quantity'])
                db.insertT_h_I(trans_id[1]['idTRANS'], invenItem[1]['idINVENTORY'], int(price), item['Quantity'])
            
            self.Basket = []
            self.refresh_table()

            self.order()

    def order(self):
        self.orderWindow = tk.Tk()
        self.orderWindow.title("Order Complete")
        self.orderWindow.geometry("370x120")
        self.orderWindow['padx'] = 10
        self.orderWindow['pady'] = 10

        self.order_frame1 = ttk.LabelFrame(self.orderWindow, relief=tk.RIDGE)
        self.order_frame1.grid(row=1, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

        self.orderCompleteMessage = ttk.Label(self.order_frame1, width =35 ,text="구매가 완료되었습니다.", font=tk.font.Font(size=10))
        self.orderCompleteMessage.grid(row=1,column=1, padx=30, pady=10)
        self.orderCompleteMessage = ttk.Label(self.order_frame1, width =35 ,text="빠르고 안전하게 배송해드리겠습니다.", font=tk.font.Font(size=10))
        self.orderCompleteMessage.grid(row=2,column=1, padx=30, pady=10)
        
        self.paymentWindow.destroy()
    
    def refresh_payment(self, event):
        self.total_payment_Info = {'User':self.ID_str}

        price = sum(self.priceList)
        self.total_payment_Info['Price'] = price

        if len(self.paymentAddressTree.selection()) != 0:
            address = self.paymentAddressList[int(self.paymentAddressTree.selection()[0])]['Address']
            self.payment_select_Address = ttk.Label(self.payment_frame5, width =20 ,text=address)
            self.payment_select_Address.grid(row=1,column=2, padx=10, pady=10)
            self.total_payment_Info['DeliveryAddress'] = address

        if len(self.paymentCouponTree.selection()) != 0:
            coupon = self.paymentCouponList[int(self.paymentCouponTree.selection()[0])]['Coupon']
            price = sum(self.priceList)*(100 - int(coupon[0:2]))*0.01
            self.payment_select_Coupon = ttk.Label(self.payment_frame5, width =20 ,text=coupon)
            self.payment_select_Coupon.grid(row=2,column=2, padx=10, pady=10)
            self.payment_select_Price = ttk.Label(self.payment_frame5, width =20 ,text=int(price))
            self.payment_select_Price.grid(row=4,column=2, padx=10, pady=10)
            self.total_payment_Info['Coupon'] = coupon
            self.total_payment_Info['Price'] = int(price)

        if len(self.paymentTree.selection()) != 0:
            payment = self.paymentList[int(self.paymentTree.selection()[0])]
            self.payment_select_Payment = ttk.Label(self.payment_frame5, width =20 ,text=payment)
            self.payment_select_Payment.grid(row=3,column=2, padx=10, pady=10)
            self.total_payment_Info['Payment'] = payment



    def deleteBasket(self, deletelist):
        deletelist = list(deletelist)
        deletelist2 = []
        for i in deletelist:
            deletelist2.append(self.Basket_listbox.get(i))
        for item in deletelist2:
            self.Basket.remove(item)

        self.refresh_table()


    def addBasket(self, addlist):
        for item in addlist:
            self.Basket.append(item)

        self.refresh_table()


    def closeClickProduct(self):
        self.productWindow.destroy()
        self.productWindow = None

    def closeClickStyle(self):
        self.styleWindow.destroy()
        self.styleWindow = None
    
    def showItemInfo(self, event):
        num = self.itemTree.selection()[0]
        item = self.itemList[int(num)]['ProductName']
        count = db.countCumSold(item)[1][0]['sum']
        if count == None:
            count = 0       #누적 판매량 없으면 0이라고 count에 할당

        if self.productWindow != None:
            self.productWindow.destroy()
            self.productWindow = None

        self.productWindow = tk.Tk()
        self.productWindow.title("Product")
        self.productWindow.geometry("460x700")
        self.productWindow['padx'] = 10
        self.productWindow['pady'] = 10

        self.productWindow.protocol("WM_DELETE_WINDOW", self.closeClickProduct)

        #제품사진
        self.product_picture_frame = ttk.LabelFrame(self.productWindow ,text="product image")
        self.product_picture_frame.width = 50
        self.product_picture_frame.grid(row=1, column=1, sticky=tk.E + tk.W + tk.N + tk.S)
        self.product_image = ttk.Label(self.product_picture_frame, text="제품 이미지")
        self.product_image.grid(row=1,column=1)

        #사진 넣기, 사진 저장형태는 png,gif등 가능
        # pic's upper left corner (NW) on the canvas is at x=50 y=10
        self.canvas = Canvas(self.product_picture_frame, width = 420,height =400)
        self.canvas.grid(row=1,column=1)
        self.image_name = item + ".png"
        self.img = PhotoImage(master = self.canvas, file=self.image_name)
        self.canvas.create_image(10,10,anchor =NW, image=self.img)


        #제품정보
        self.product_info_frame = ttk.LabelFrame(self.productWindow, text="product Info")
        self.product_info_frame.grid(row=2, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

        product_name1 = ttk.Label(self.product_info_frame,width =20 ,text="제품명")
        product_name1.grid(row=1,column=1)
        product_name2 = ttk.Label(self.product_info_frame,width =20 ,text=self.itemList[int(num)]['ProductName'])
        product_name2.grid(row=1,column=2)
        product_price1 = ttk.Label(self.product_info_frame,width =20,text="가격")
        product_price1.grid(row=2,column=1)
        product_price2 = ttk.Label(self.product_info_frame,width =20,text=self.itemList[int(num)]['Price'])
        product_price2.grid(row=2,column=2)
        product_brand1 = ttk.Label(self.product_info_frame,width =20, text = "브랜드")
        product_brand1.grid(row=3,column=1)
        product_brand2 = ttk.Label(self.product_info_frame,width =20, text =self.itemList[int(num)]['Brand'])
        product_brand2.grid(row=3,column=2)
        product_soldquantity1 = ttk.Label(self.product_info_frame,width =20, text = "누적 판매량")
        product_soldquantity1.grid(row=4,column=1)
        product_soldquantity2 = ttk.Label(self.product_info_frame,width =20, text = str(count))
        product_soldquantity2.grid(row=4,column=2)

        # 장바구니 프레임, 버튼
        itembasket = []
        itembasket.append(item)
        self.productWindow.cart_button = ttk.Button(self.product_info_frame, text="장바구니에 추가", command = lambda : self.addBasket(itembasket))
        self.productWindow.cart_button.grid(row=1, column=4)
        #리뷰 프레임 라벨
        self.product_review_frame = ttk.LabelFrame(self.productWindow, text="review")
        self.product_review_frame.grid(row=3, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

        num, self.ReviewList = db.getReview(item)
        self.cus_reivewlist = []
        self.customerLabellist = []
        self.reivewLabellist =[]
        if num == 0:
            self.cus_reivewlist.append(["No Review",""])   #밑에 애랑 형식 맞춰주려고 넣음
        else:
            for i in range(num):
                self.cus_reivewlist.insert(i,[self.ReviewList[i]["CUSTOMER_Customer_ID"], self.ReviewList[i]["Review"]])
        #작성자 리스트
        for k in range(len(self.cus_reivewlist)):
            self.customerLabellist.append(ttk.Label(self.product_review_frame,text =self.cus_reivewlist[k][0], width = 50 ))
            self.customerLabellist[k].grid(row=k, column=1)
        for k in range(len(self.cus_reivewlist)):
            self.reivewLabellist.append(ttk.Label(self.product_review_frame,text =self.cus_reivewlist[k][1] ))
            self.reivewLabellist[k].grid(row=k, column=1)
        # UserMenuList = []
        #         # UserMenu = ["쿠폰", "배송지", "거래내역", "반품신청"]
        #         # for k in range(len(UserMenu)):
        #         #     UserMenuList.append(tk.Button(self.User_Menu_Frame, text=UserMenu[k], width=20))
        #         #     UserMenuList[k].grid(row=k, column=1)
        # product_name1 = ttk.Label(self.product_info_frame, width=20, text="제품명")
        #         # product_name1.grid(row=1, column=1)

        # 제품 해당하는 스타일 보여주는 frame,Treeview
        self.style_frame = ttk.LabelFrame(self.productWindow)
        self.style_frame.grid(row=4, column=1)

        self.productstyleTree = ttk.Treeview(self.style_frame, height=4, columns=["스타일 작성자", "스타일 설명"])
        self.productstyleTree.pack()

        self.productstyleTree.column("#0", width=10)
        self.productstyleTree.heading("#0", text="")

        self.productstyleTree.column("스타일 작성자", width=100, anchor="w")
        self.productstyleTree.heading("스타일 작성자", text="스타일 작성자", anchor="center")

        self.productstyleTree.column("스타일 설명", width=300, anchor="w")
        self.productstyleTree.heading("스타일 설명", text="스타일 설명", anchor="center")


        num, self.style_productList = db.PRODUCT_StyleID(item)

        for i in range(num):
            self.productstyleTree.insert('', 'end', values=(self.style_productList[i]['ADMIN_AdminID'], self.style_productList[i]['Description']), iid=str(i))


    def showStyleInfo(self, event):
        num = self.styleTree.selection()[0]
        style = self.styleList[int(num)]['StyleID']
        influencer = self.styleList[int(num)]['ADMIN_AdminID']

        if self.styleWindow != None:
            self.styleWindow.destroy()
            self.styleWindow = None

        self.styleWindow = tk.Tk()
        self.styleWindow.title("Style")
        self.styleWindow.geometry("470x700")
        self.styleWindow['padx'] = 10
        self.styleWindow['pady'] = 10

        self.styleWindow.protocol("WM_DELETE_WINDOW", self.closeClickStyle)

        #스타일사진
        self.style_picture_frame = ttk.LabelFrame(self.styleWindow ,text="style image")
        self.style_picture_frame.width = 50
        self.style_picture_frame.grid(row=1, column=1, columnspan=2, sticky=tk.E + tk.W + tk.N + tk.S)
        self.style_image = ttk.Label(self.style_picture_frame, text="스타일 이미지")
        self.style_image.grid(row=1,column=1)

        #사진 넣기, 사진 저장형태는 png,gif등 가능
        # pic's upper left corner (NW) on the canvas is at x=50 y=10
        self.style_canvas = Canvas(self.style_picture_frame, width = 420,height =420)
        self.style_canvas.grid(row=1,column=1)
        self.style_image_name = str(style) + ".png"
        self.style_img = PhotoImage(master = self.style_canvas, file=self.style_image_name)
        self.style_canvas.create_image(10,20,anchor =NW, image=self.style_img)

        # 스타일정보(스타일 자체 정보)
        self.style_info_frame1 = ttk.LabelFrame(self.styleWindow, text="Style Info")
        self.style_info_frame1.grid(row=2, column=1, columnspan=2, sticky=tk.E + tk.W + tk.N + tk.S)

        style_description1 = ttk.Label(self.style_info_frame1,width =15 ,text="스타일 설명")
        style_description1.grid(row=1,column=1)
        style_description2 = ttk.Label(self.style_info_frame1,width =50 ,text=self.styleList[int(num)]['Description'])
        style_description2.grid(row=1,column=2)



        #스타일정보(스타일안에 들어가는 제품 정보)
        self.style_info_frame2 = ttk.LabelFrame(self.styleWindow, text="Style Product")
        self.style_info_frame2.grid(row=3, column=1, columnspan=2, sticky=tk.E + tk.W + tk.N + tk.S)

        self.styleitemTree = ttk.Treeview(self.style_info_frame2, height = 4, columns=["제품명", "브랜드", "가격"])
        self.styleitemTree.pack()

        self.styleitemTree.column("#0", width=10)
        self.styleitemTree.heading("#0", text="")

        self.styleitemTree.column("제품명", width=100, anchor="w")
        self.styleitemTree.heading("제품명", text="제품명", anchor="center")

        self.styleitemTree.column("브랜드", width=200, anchor="w")
        self.styleitemTree.heading("브랜드", text="브랜드", anchor="center")

        self.styleitemTree.column("가격", width=100, anchor="w")
        self.styleitemTree.heading("가격", text="가격", anchor="center")

        # style
        itembasket = []
        num, self.styleitemList = db.Style_PRODUCT(style)
        for i in range(num):
            itembasket.append(self.styleitemList[i]["ProductName"])
            self.styleitemTree.insert('', 'end', values=tuple(self.styleitemList[i].values()), iid=str(i))

        # 인플루언서 정보
        numInfluencer, infdata = db.getinfluencer(influencer)
        self.style_influencer_frame = ttk.LabelFrame(self.styleWindow, text="Influencer Info")
        self.style_influencer_frame.grid(row=4, column=1)

        style_Influencer_Name_label = ttk.Label(self.style_influencer_frame,width =15 ,text="모델이름")
        style_Influencer_Name_label.grid(row=1,column=1)
        style_Influencer_Name = ttk.Label(self.style_influencer_frame,width =30 ,text=infdata['NickName'])
        style_Influencer_Name.grid(row=1,column=2)

        style_Influencer_Height_label = ttk.Label(self.style_influencer_frame,width =15 ,text="모델 키")
        style_Influencer_Height_label.grid(row=2,column=1)
        style_Influencer_Height = ttk.Label(self.style_influencer_frame,width =30 ,text=infdata['Height'])
        style_Influencer_Height.grid(row=2,column=2)

        style_Influencer_Weight_label = ttk.Label(self.style_influencer_frame,width =15 ,text="모델 몸무게")
        style_Influencer_Weight_label.grid(row=3,column=1)
        style_Influencer_Weight = ttk.Label(self.style_influencer_frame,width =30 ,text=infdata['Weight'])
        style_Influencer_Weight.grid(row=3,column=2)



        #장바구니 프레임, 버튼
        self.style_cart_frame = ttk.LabelFrame(self.styleWindow, text = "add to cart")
        self.style_cart_frame.grid(row =4, column= 2)
        
        self.styleWindow.cart_button = ttk.Button(self.style_cart_frame, text="장바구니에 추가", command = lambda : self.addBasket(itembasket))
        self.styleWindow.cart_button.grid(row=1, column=3)


    def showOrderProduct(self, index, order):
        # if len(self.itemTree.selection()) > 0:
        #     self.itemTree.selection_remove(self.itemTree.selection()[0])
        x = self.itemTree.get_children()
        for item in x:
            self.itemTree.delete(item)
        num, self.itemList = db.showItemOrder(index, order)
        for i in range(num):
            self.itemTree.insert('', 'end', values=tuple(self.itemList[i].values()), iid=str(i))
        

    def showCategoryProduct(self, index):
        x = self.itemTree.get_children()
        for item in x:
            self.itemTree.delete(item)

        num, self.itemList = db.getCategory(index)
        for i in range(num):
            self.itemTree.insert('', 'end', values=tuple(self.itemList[i].values()), iid=str(i))

    def showCategoryInfluencer(self, id):
        x = self.styleTree.get_children()
        for style in x:
            self.styleTree.delete(style)

        if id == "refresh":
            num, self.styleList = db.showStyleOrder("ADMIN_AdminID", "ASC")
        else:
            num, self.styleList = db.getinfluencer_Style(id)
        
        for i in range(num):
            self.styleTree.insert('', 'end', values=(self.styleList[i]['ADMIN_AdminID'], self.styleList[i]['Description']), iid=str(i))


    def refresh_mypage(self):
        # userinfo
        user_Data = db.getCusInfo(self.ID_str)

        self.Mypage_Name_label_Data = ttk.Label(self.Mypage_User_frame, text=user_Data["CustomerName"])
        self.Mypage_Name_label_Data.grid(row=1, column=2)

        self.Mypage_Grade_label_Data = ttk.Label(self.Mypage_User_frame, text="         ")
        self.Mypage_Grade_label_Data.grid(row=2, column=2)
        self.Mypage_Grade_label_Data = ttk.Label(self.Mypage_User_frame, text=user_Data["CustomerGrade"])
        self.Mypage_Grade_label_Data.grid(row=2, column=2)

        self.Mypage_Point_label_Data = ttk.Label(self.Mypage_User_frame, text="         ")
        self.Mypage_Point_label_Data.grid(row=3, column=2)
        self.Mypage_Point_label_Data = ttk.Label(self.Mypage_User_frame, text=user_Data["MembershipPoint"])
        self.Mypage_Point_label_Data.grid(row=3, column=2)


    def refresh_table(self):
        # userinfo
        user_Data = db.getCusInfo(self.ID_str)

        self.Name_label_Data = ttk.Label(self.User_frame, text=user_Data["CustomerName"], font=tk.font.Font(size=10))
        self.Name_label_Data.grid(row=1, column=2)

        self.Grade_label_Data = ttk.Label(self.User_frame, text="         ", font=tk.font.Font(size=10))
        self.Grade_label_Data.grid(row=2, column=2)
        self.Grade_label_Data = ttk.Label(self.User_frame, text=user_Data["CustomerGrade"], font=tk.font.Font(size=10))
        self.Grade_label_Data.grid(row=2, column=2)

        self.Point_label_Data = ttk.Label(self.User_frame, text="         ", font=tk.font.Font(size=10))
        self.Point_label_Data.grid(row=3, column=2)
        self.Point_label_Data = ttk.Label(self.User_frame, text=user_Data["MembershipPoint"], font=tk.font.Font(size=10))
        self.Point_label_Data.grid(row=3, column=2)

        x = self.itemTree.get_children()
        for item in x:
            self.itemTree.delete(item)

        x = self.styleTree.get_children()
        for style in x:
            self.styleTree.delete(style)

        # inventory
        num, self.itemList = db.showItemOrder("AcquiredDate", "DESC")
        for i in range(num):
            self.itemTree.insert('', 'end', values=tuple(self.itemList[i].values()), iid=str(i))

        # style
        num, self.styleList = db.showStyleOrder("ADMIN_AdminID", "ASC")
        for i in range(num):
            self.styleTree.insert('', 'end', values=(self.styleList[i]['ADMIN_AdminID'], self.styleList[i]['Description']), iid=str(i))

        # inven
        # item = self.itemTree.selection()[0]

        # style
        # style = self.styleTree.selection()[0]

        # basket
        self.Basket_listbox.delete(0,self.Basket_listbox.size()-1)
        for item in self.Basket:
            self.Basket_listbox.insert(tk.END, item)


    def login(self):
        self.ID_str = self.ID_entry.get()
        Password_str = self.PW_entry.get()
        self.ID_entry.delete(0,tk.END)
        self.PW_entry.delete(0,tk.END)
        check,name = self.db.logcheck(self.ID_str,Password_str)

        print("login" + str(check))
        if check:
            self.refresh_table()
            self.loginWindow.destroy()
        else:
            failLogin = tkinter.messagebox.showerror("메세지 상자", "잘못된 정보입력입니다.")

    def showCouponlist(self):

        self.Mypage_Detail_frame = ttk.LabelFrame(self.mypageWindow, text="Coupon List", relief=tk.RIDGE)
        self.Mypage_Detail_frame.grid(row=2, column=2, sticky=tk.E + tk.W + tk.N + tk.S)
        
        self.MyPageDetailTree = ttk.Treeview(self.Mypage_Detail_frame, columns=["목록"])
        self.MyPageDetailTree.grid(row=1, column=1)

        self.MyPageDetailTree.column("#0", width=10)
        self.MyPageDetailTree.heading("#0", text="")

        self.MyPageDetailTree.column("목록", width=200, anchor="w")
        self.MyPageDetailTree.heading("목록", text="목록", anchor="center")

        num, self.DetailList = db.getCoupon(self.ID_str)
        for i in range(num):
            self.MyPageDetailTree.insert('', 'end', values=tuple(self.DetailList[i].values()), iid=str(i))

    def showAddresslist(self):

        self.Mypage_Detail_frame = ttk.LabelFrame(self.mypageWindow, text="Coupon List", relief=tk.RIDGE)
        self.Mypage_Detail_frame.grid(row=2, column=2, sticky=tk.E + tk.W + tk.N + tk.S)

        num, self.DetailList = db.getAddress(self.ID_str)
        self.addressList1 = []

        for i in range(num):
            self.Mypage_Detail_Name_Label = ttk.Label(self.Mypage_Detail_frame, width=20, text="▶ 주소지 " + str(i+1))
            self.Mypage_Detail_Name_Label.grid(row=i+1, column=1, padx=10 ,pady=10)
            self.Mypage_Detail_Name = ttk.Label(self.Mypage_Detail_frame, width=20, text=self.DetailList[i]['Address'])
            self.Mypage_Detail_Name.grid(row=i+1, column=2, padx=10 ,pady=10)
            self.addressList1.append((self.Mypage_Detail_Name_Label, self.Mypage_Detail_Name))
        
        self.Mypage_Detail_Update_Button = tk.Button(self.Mypage_Detail_frame, width=10, text="주소지 수정", command = self.updateAddresslist)
        self.Mypage_Detail_Update_Button.grid(row=5, column=1, pady=20, ipady=10)

        self.Mypage_Detail_Update_Button = tk.Button(self.Mypage_Detail_frame, width=10, text="주소지 추가", command = self.insertAddresslist)
        self.Mypage_Detail_Update_Button.grid(row=5, column=2, pady=20, ipady=10)


    def insertAddresslist(self):

        self.insertAddressWindow = tk.Tk()
        self.insertAddressWindow.title("Insert Address")
        self.insertAddressWindow.geometry("360x100")
        self.insertAddress_frame = ttk.LabelFrame(self.insertAddressWindow, text="Log-In", relief=tk.RIDGE)
        self.insertAddress_frame.grid(row=1, column=1, pady=5, sticky=tk.E + tk.W + tk.N + tk.S)

        insertAddress_Label = ttk.Label(self.insertAddress_frame, text="+ 주소 ")
        insertAddress_Label.grid(row=1, column=1, sticky=tk.W, pady=10, ipady=3)
    
        self.insertAddress_Entry = ttk.Entry(self.insertAddress_frame, width=30)
        self.insertAddress_Entry.grid(row=1, column=2, sticky=tk.W, pady=10, ipady=3, ipadx=3)
        self.insertAddress_Entry.insert(tk.END, "주소를 입력해주세요")

        insert_Address_button = ttk.Button(self.insertAddress_frame, text="추가하기",  command=self.insertAddress)
        insert_Address_button.grid(row=1, column=3)


    def insertAddress(self):

        if self.insertAddress_Entry.get() != "주소를 입력해주세요":
            db.insertAddress(self.ID_str, self.insertAddress_Entry.get())

        self.insertAddressWindow.destroy()
        self.showAddresslist()


    def updateAddresslist(self):

        self.Mypage_Detail_frame = ttk.LabelFrame(self.mypageWindow, text="Address List", relief=tk.RIDGE)
        self.Mypage_Detail_frame.grid(row=2, column=2, sticky=tk.E + tk.W + tk.N + tk.S)

        num, self.DetailList = db.getAddress(self.ID_str)
        self.addressList2 = []

        for i in range(num):
            self.Mypage_Detail_Name_Label = ttk.Label(self.Mypage_Detail_frame, width=20, text="▶ 주소지 " + str(i+1))
            self.Mypage_Detail_Name_Label.grid(row=i+1, column=1, padx=10 ,pady=10)
            self.Mypage_Detail_Name = ttk.Entry(self.Mypage_Detail_frame, width=20)
            self.Mypage_Detail_Name.grid(row=i+1, column=2, padx=10 ,pady=10)
            self.Mypage_Detail_Name.insert(tk.END, self.DetailList[i]['Address'])

            self.addressList2.append((self.Mypage_Detail_Name_Label, self.Mypage_Detail_Name))

        self.Mypage_Detail_Update_Button = tk.Button(self.Mypage_Detail_frame, width=10, text="수정하기", command = self.refreshAddresslist)
        self.Mypage_Detail_Update_Button.grid(row=5, column=1, pady=20, ipady=10, columnspan=2)

        self.Mypage_Detail_Alter_Label = ttk.Label(self.Mypage_Detail_frame, text="+ 아무것도 입력하지 않으면 주소지가 삭제됩니다.")
        self.Mypage_Detail_Alter_Label.grid(row=6, column=1, padx=10 ,pady=10, columnspan=2)
        

    def refreshAddresslist(self):
    
        for i in range(len(self.addressList2)):
            if self.addressList2[i][1].get() == "":
                db.deleteAddress(self.DetailList[i]['Address'], self.ID_str)
            else:
                db.updateAddress(self.addressList2[i][1].get(), self.ID_str, self.DetailList[i]['Address'])
        
        self.showAddresslist()

    #재홍 
    def showTranslist(self):

        self.Mypage_Detail_frame = ttk.LabelFrame(self.mypageWindow, text="Trans List", relief=tk.RIDGE)
        self.Mypage_Detail_frame.grid(row=2, column=2, sticky=tk.E + tk.W + tk.N + tk.S)

        self.MyPage_Detail_Label1 = ttk.Label(self.Mypage_Detail_frame, width=20, text="상품정보/사이즈/색상")
        self.MyPage_Detail_Label1.grid(row=1, column=1, padx=10,pady=10)

        self.MyPage_Detail_Label2 = ttk.Label(self.Mypage_Detail_frame, width=10, text="주문일자")
        self.MyPage_Detail_Label2.grid(row=1, column=2, padx=5, pady=5)

        self.MyPage_Detail_Label3 = ttk.Label(self.Mypage_Detail_frame, width=10, text="주문번호")
        self.MyPage_Detail_Label3.grid(row=1, column=3, padx=5, pady=5)

        self.MyPage_Detail_Label4 = ttk.Label(self.Mypage_Detail_frame, width=10, text="주문금액")
        self.MyPage_Detail_Label4.grid(row=1, column=4, padx=5, pady=5)

        self.MyPage_Detail_Label5 = ttk.Label(self.Mypage_Detail_frame, width=10, text="주문수량")
        self.MyPage_Detail_Label5.grid(row=1, column=5, padx=5, pady=5)
        #trans에서 idTrans, DateSold 가져오기
        num, self.TransDetailList = db.getCUS_TRANS(self.ID_str)
        self.MyPageDetailLabelList = []
        for i in range(num):        #i= 0,1,...num-1
            self.MyPageDateSoldLabel = ttk.Label(self.Mypage_Detail_frame, width=10, text=self.TransDetailList[i]['DateSold'])
            self.MyPageDateSoldLabel.grid(row=i + 2, column=2, padx=5, pady=5)
            self.MyPageDetailLabelList.append(self.MyPageDateSoldLabel)

            self.MyPageidtransLabel = ttk.Label(self.Mypage_Detail_frame, width=10, text=self.TransDetailList[i]['idTRANS'])
            self.MyPageidtransLabel.grid(row=i+2, column=3, padx=5, pady=5)
            self.MyPageDetailLabelList.append(self.MyPageidtransLabel)

            self.MyPageSellPriceLabel = ttk.Label(self.Mypage_Detail_frame, width=10, text=self.TransDetailList[i]['SellPrice'])
            self.MyPageSellPriceLabel.grid(row=i + 2, column=4, padx=5, pady=5)
            self.MyPageDetailLabelList.append(self.MyPageSellPriceLabel)

            self.MyPageQuantityLabel = ttk.Label(self.Mypage_Detail_frame, width=10, text=self.TransDetailList[i]['Quantity'])
            self.MyPageQuantityLabel.grid(row=i + 2, column=5, padx=5, pady=5)
            self.MyPageDetailLabelList.append(self.MyPageQuantityLabel)

        self.MypageidInventorylist = []   #idinventory 담는 list
        for i in range(num):
            self.MypageidInventorylist.append(self.TransDetailList[i]['INVENTORY_idINVENTORY'])
        #idinventory 해당하는 상품정보
        self.ProductInfoList = []
        for i in range(len(self.MypageidInventorylist)):
            num, self.ProductDetailList = db.getPRODUCT_INVENTORY(self.MypageidInventorylist[i])
            self.ProductInfoList.append(self.ProductDetailList)

        #상품정보(제품명, 색,사이즈) 하나의 텍스트로 만들기
        self.textlist = []
        for i in range(len(self.ProductInfoList)):  #상품정보 형식 바꾸고싶으면 밑에줄 조작
            self.textlist.append( '%s, %s, %s' %(self.ProductInfoList[i][0]['ProductName'],self.ProductInfoList[i][0]['Size'],self.ProductInfoList[i][0]['Color']))

        for i in range(len(self.textlist)):
            self.MyPageProductInfoLabel = ttk.Label(self.Mypage_Detail_frame, width=20, text=self.textlist[i])
            self.MyPageProductInfoLabel.grid(row=i + 2, column=1, padx=10, pady=10)
            self.MyPageDetailLabelList.append(self.MyPageProductInfoLabel)

        # 반품하기 버튼
        self.RefundButtonList = []
        for i in range(len(self.TransDetailList)):
            self.Mypage_Detail_Refund_Button = tk.Button(self.Mypage_Detail_frame, width=10, text="환불하기", command= lambda k=i: self.RefundUpdateTrans(k))
            self.Mypage_Detail_Refund_Button.grid(row=i+2, column=6, padx=10, pady=10)
            self.RefundButtonList.append(self.Mypage_Detail_Refund_Button)
        self.ReviewButtonList =[]
        for i in range(len(self.TransDetailList)):
            self.Mypage_Detail_Review_Button = tk.Button(self.Mypage_Detail_frame, width=10, text="리뷰쓰기", command=lambda k=i: self.UpdateReviewList(k))
            self.Mypage_Detail_Review_Button.grid(row=i + 2, column=7, padx=10, pady=10)
            self.ReviewButtonList.append(self.Mypage_Detail_Review_Button)


    def UpdateReviewList(self,i):

        self.UpdateReviewWindow = tk.Tk()
        self.UpdateReviewWindow.title("Update Review")
        self.UpdateReviewWindow.geometry("360x100")
        self.UpdateReview_frame = ttk.LabelFrame(self.UpdateReviewWindow, text= 'Review', relief=tk.RIDGE)
        self.UpdateReview_frame.grid(row=1, column=1, padx=5, pady=5, sticky=tk.E + tk.W + tk.N + tk.S)

        self.UpdateReview_Entry = ttk.Entry(self.UpdateReview_frame, width=30)
        self.UpdateReview_Entry.grid(row=1, column=2, sticky=tk.W, pady=10, ipady=3, ipadx=3)
        self.UpdateReview_Entry.insert(tk.END, "상품에 대한 리뷰를 작성해주세요")
        # db.Update_T_h_IReview(Review, self.TransDetailList[i]['idTRANS'], self.MypageidInventorylist[i])

        Login_button = ttk.Button(self.UpdateReview_frame, text="완료", command= lambda k=i: self.UpdateReview(self.TransDetailList[k]['idTRANS'], self.MypageidInventorylist[k]))
        Login_button.grid(row=1, column=3)


    def UpdateReview(self,idtrans,idinventory):

        if self.UpdateReview_Entry.get() != "상품에 대한 리뷰를 작성해주세요":
            db.Update_T_h_IReview(self.UpdateReview_Entry.get(),idtrans,idinventory)

        self.refresh_table()
        self.refresh_mypage()
        self.UpdateReviewWindow.destroy()


    def RefundUpdateTrans(self,i):  #i는 지워질(update될) idtrans의 index
        self.yesorno = tkinter.messagebox.askquestion("메세지 상자", "정말 환불하시겠습니까?")
        if self.yesorno == "yes":
            db.Update_TRANS(self.TransDetailList[i]['idTRANS'])
        self.refresh_table()
        self.refresh_mypage()
        self.showTranslist()
    # 재홍

    def showCustomerInfo(self):

        self.DetailList = db.getCusInfo(self.ID_str)

        self.Mypage_Detail_frame = ttk.LabelFrame(self.mypageWindow, text="Trans List", relief=tk.RIDGE)
        self.Mypage_Detail_frame.grid(row=2, column=2, sticky=tk.E + tk.W + tk.N + tk.S)

        self.Mypage_Detail_Name_Label = ttk.Label(self.Mypage_Detail_frame, width=20, text="▶ 이름")
        self.Mypage_Detail_Name_Label.grid(row=1, column=1, padx=10 ,pady=10)
        self.Mypage_Detail_Name = ttk.Label(self.Mypage_Detail_frame, width=20, text=self.DetailList['CustomerName'])
        self.Mypage_Detail_Name.grid(row=1, column=2, padx=10 ,pady=10)

        self.Mypage_Detail_CusID_Label = ttk.Label(self.Mypage_Detail_frame, width=20, text="▶ 아이디")
        self.Mypage_Detail_CusID_Label.grid(row=2, column=1, padx=10 ,pady=10)
        self.Mypage_Detail_CusID = ttk.Label(self.Mypage_Detail_frame, width=20, text=self.DetailList['Customer_ID'])
        self.Mypage_Detail_CusID.grid(row=2, column=2, padx=10 ,pady=10)

        # self.Mypage_Detail_PW_Label = ttk.Label(self.Mypage_Detail_frame, width=20, text="▶ 비밀번호")
        # self.Mypage_Detail_PW_Label.grid(row=3, column=1, padx=10 ,pady=10)
        # self.Mypage_Detail_PW = ttk.Label(self.Mypage_Detail_frame, width=20, text=self.DetailList['Password'])
        # self.Mypage_Detail_PW.grid(row=3, column=2, padx=10 ,pady=10)

        self.Mypage_Detail_Email_Label = ttk.Label(self.Mypage_Detail_frame, width=20, text="▶ 이메일")
        self.Mypage_Detail_Email_Label.grid(row=4, column=1, padx=10 ,pady=10)
        self.Mypage_Detail_Email = ttk.Label(self.Mypage_Detail_frame, width=20, text=self.DetailList['Email'])
        self.Mypage_Detail_Email.grid(row=4, column=2, padx=10 ,pady=10)

        self.Mypage_Detail_Update_Button = tk.Button(self.Mypage_Detail_frame, width=10, text="개인정보 수정", command = self.updateCustomerInfo)
        self.Mypage_Detail_Update_Button.grid(row=5, column=1, pady=20, ipady=10)
        self.Mypage_Detail_Update_Button = tk.Button(self.Mypage_Detail_frame, width=10, text="회원탈퇴", command = self.withdrawlCustomer)
        self.Mypage_Detail_Update_Button.grid(row=5, column=2, pady=20, ipady=10)

        # Cutomer_ID, Password, CustomerName, Email, MembershipPoint, Customergrade

    def withdrawlCustomer(self):
        self.withdrawlConfirmWindow = tk.Tk()
        self.withdrawlConfirmWindow.title("Withdrawl")
        self.withdrawlConfirmWindow.geometry("360x100")
        self.withdrawl_frame = ttk.LabelFrame(self.withdrawlConfirmWindow, text= 'Withdrawl', relief=tk.RIDGE)
        self.withdrawl_frame.grid(row=1, column=1, padx=5, pady=5, sticky=tk.E + tk.W + tk.N + tk.S)

        self.confirmPassword = ttk.Entry(self.withdrawl_frame, width=30)
        self.confirmPassword.grid(row=1, column=2, sticky=tk.W, pady=10, ipady=3, ipadx=3)
        self.confirmPassword.insert(tk.END, "패스워드를 입력해주세요")

        withdrawlButton = ttk.Button(self.withdrawlConfirmWindow, text="탈퇴", command= self.withdrawlConfirm)
        withdrawlButton.grid(row=1, column=3)

    def withdrawlConfirm(self):
        result = db.withdrawlCus(self.ID_str, self.confirmPassword.get())
        if result:
            showWithdrawl = tkinter.messagebox.showinfo("메세지상자", "회원탈퇴가 완료되었습니다.\n다음엔 더 나은 서비스로 보답하겠습니다.")
            self.withdrawlConfirmWindow.destroy()
            self.mypageWindow.destroy()
            self.window.quit()
        else:
            showWithdrawl = tkinter.messagebox.showerror("메세지상자", "패스워드가 틀렸습니다.")

    def updateCustomerInfo(self):

        self.DetailList = db.getCusInfo(self.ID_str)

        self.Mypage_Detail_frame = ttk.LabelFrame(self.mypageWindow, text="Trans List", relief=tk.RIDGE)
        self.Mypage_Detail_frame.grid(row=2, column=2, sticky=tk.E + tk.W + tk.N + tk.S)

        self.Mypage_Detail_Name_Label = ttk.Label(self.Mypage_Detail_frame, width=20, text="▶ 이름")
        self.Mypage_Detail_Name_Label.grid(row=1, column=1, padx=10 ,pady=10)
        self.Mypage_Detail_Name = ttk.Label(self.Mypage_Detail_frame, width=20, text=self.DetailList['CustomerName'])
        self.Mypage_Detail_Name.grid(row=1, column=2, padx=10 ,pady=10)

        self.Mypage_Detail_CusID_Label = ttk.Label(self.Mypage_Detail_frame, width=20, text="▶ 아이디")
        self.Mypage_Detail_CusID_Label.grid(row=2, column=1, padx=10 ,pady=10)
        self.Mypage_Detail_CusID = ttk.Label(self.Mypage_Detail_frame, width=20, text=self.DetailList['Customer_ID'])
        self.Mypage_Detail_CusID.grid(row=2, column=2, padx=10 ,pady=10)

        self.Mypage_Detail_PW_Label = ttk.Label(self.Mypage_Detail_frame, width=20, text="▶ 비밀번호")
        self.Mypage_Detail_PW_Label.grid(row=3, column=1, padx=10 ,pady=10)
        self.Mypage_Detail_PW = ttk.Entry(self.Mypage_Detail_frame, width=20)
        self.Mypage_Detail_PW.grid(row=3, column=2, padx=10 ,pady=10, ipadx=3, ipady=3)
        self.Mypage_Detail_PW.insert(tk.END, self.DetailList['Password'])

        self.Mypage_Detail_Email_Label = ttk.Label(self.Mypage_Detail_frame, width=20, text="▶ 이메일")
        self.Mypage_Detail_Email_Label.grid(row=4, column=1, padx=10 ,pady=10)
        self.Mypage_Detail_Email = ttk.Entry(self.Mypage_Detail_frame, width=20)
        self.Mypage_Detail_Email.grid(row=4, column=2, padx=10 ,pady=10, ipadx=3, ipady=3)
        self.Mypage_Detail_Email.insert(tk.END, self.DetailList['Email'])

        self.Mypage_Detail_Update_Button = tk.Button(self.Mypage_Detail_frame, width=10, text="수정하기", command = self.refreshCustomerInfo)
        self.Mypage_Detail_Update_Button.grid(row=5, column=1, pady=20, ipady=10, columnspan=2)

        # Cutomer_ID, Password, CustomerName, Email, MembershipPoint, Customergrade

    def refreshCustomerInfo(self):

        db.update_Customer(self.Mypage_Detail_PW.get(), self.Mypage_Detail_Email.get(), self.ID_str)

        self.showCustomerInfo()
        


# Create the entire GUI program
db = dbModel.Database()
program = SpaceProgram(db)

# Start the GUI event loop
program.window.mainloop()
