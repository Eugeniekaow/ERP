"""
==== 1. =====
請參考 73-tkinter-label-2文字擺放place.py

使用tkinter 建立
一個視窗
上面顯示label
產品的資料
"""
"""
import tkinter as tk # 在Python 3.x 匯入該tkinter 函式庫
win = tk.Tk()        # 步驟2：建立GUI 應用程式的主視窗
win.wm_title("主視窗標題")                  #設定主視窗
win.resizable(width=False,height=False)    #設定主視窗不可以被調整大小
win.minsize(width=640,height=480)          #最小尺寸
win.maxsize(width=640,height=480)          #最大尺寸

label13=tk.Label(win,text="產品名稱:上衣")      #建立文字
label13.place(x=50,y=70)                      #指定元件位置

label14=tk.Label(win,text="價錢:350")         #建立文件
label14.place(x=60,y=120)                    #指定元件位置

win.mainloop()       # 最後步驟：程式做無限循環
"""
"""
==== 2. ======


使用 class 建立
一個class
儲存

產品的相關資料
"""
"""
class commodityItem(object):  # 繼承Python 最上層的object 類別
   commodityName = "上衣"
   commodityMaterial = "雪紡"
   commoditySize = "F"
   commodityClotheslength = 62
   commodityChestwidth = 110
   commodityOrigin = "台灣"
   commodityColor = "白色"
   commodityCost = 200
   commodityPricing = 350
   commodityQuantity = 10


   def __init__(self,Name,Material,Size,Clotheslength,Chestwidth,Origin,Color,Cost,Pricing,Quantity):    # 類別初始化的函數 initialize 一開始要做的函數
         self.commodityName = Name
         self.commodityMaterial = Material
         self.commoditySize = Size
         self.commodityClotheslength =Clotheslength
         self.commodityChestwidth = Chestwidth
         self.commodityOrigin = Origin
         self.commodityColor = Color
         self.commodityCost = Cost
         self.commodityPricing = Pricing
         self.commodityQuantity = Quantity

   def info(self):                                #  Method 方法
       print("商品名稱:",self.commodityName)
       print("商品材質:",self.commodityMaterial)
       print("商品尺寸:", self.commoditySize)
       print("商品衣長:", self.commodityClotheslength)
       print("商品胸寬:", self.commodityChestwidth )
       print("商品產地:", self.commodityOrigin)
       print("商品顏色:", self.commodityColor)
       print("商品成本:", self.commodityCost)
       print("商品價錢:", self.commodityPricing)
       print("商品數量:", self.commodityQuantity)

commodityItem1=commodityItem(Name="上衣",Material="雪紡",Size="F",Clotheslength=62,Chestwidth=110,Origin="台灣",Color="白色",
                             Cost=200,Pricing=350,Quantity=10)
commodityItem1.info()

"""

"""
==== 3. ======
請參考
65-class-properties.py

把第一題的Label 上的文字
改成讀取 class properties
"""
from PIL import ImageTk, Image
import tkinter as tk # 在Python 3.x 匯入該tkinter 函式庫

class commodityItem(object):  # 繼承Python 最上層的object 類別
   commodityName = "上衣"
   commodityMaterial = "雪紡"
   commoditySize = "F"
   commodityClotheslength = 62
   commodityChestwidth = 110
   commodityOrigin = "台灣"
   commodityColor = "白色"
   commodityCost = 200
   commodityPricing = 350
   commodityQuantity = 10


   def __init__(self,Name,Material,Size,Clotheslength,Chestwidth,Origin,Color,Cost,Pricing,Quantity):    # 類別初始化的函數 initialize 一開始要做的函數
         self.commodityName = Name
         self.commodityMaterial = Material
         self.commoditySize = Size
         self.commodityClotheslength =Clotheslength
         self.commodityChestwidth = Chestwidth
         self.commodityOrigin = Origin
         self.commodityColor = Color
         self.commodityCost = Cost
         self.commodityPricing = Pricing
         self.commodityQuantity = Quantity

   def info(self):                                #  Method 方法
       print("商品名稱:",self.commodityName)
       print("商品材質:",self.commodityMaterial)
       print("商品尺寸:", self.commoditySize)
       print("商品衣長:", self.commodityClotheslength)
       print("商品胸寬:", self.commodityChestwidth )
       print("商品產地:", self.commodityOrigin)
       print("商品顏色:", self.commodityColor)
       print("商品成本:", self.commodityCost)
       print("商品價錢:", self.commodityPricing)
       print("商品數量:", self.commodityQuantity)

commodityItem1=commodityItem(Name="上衣",Material="雪紡",Size="F",Clotheslength=62,Chestwidth=110,Origin="台灣",Color="白色",
                             Cost=200,Pricing=350,Quantity=10)
commodityItem1.info()

import tkinter as tk # 在Python 3.x 匯入該tkinter 函式庫
win = tk.Tk()        # 步驟2：建立GUI 應用程式的主視窗
win.wm_title("主視窗標題")                  #設定主視窗
win.resizable(width=False,height=False)    #設定主視窗不可以被調整大小
win.minsize(width=640,height=480)          #最小尺寸
win.maxsize(width=640,height=480)          #最大尺寸

# 背景圖片
x=Image.open("background-image.jpg")                     # 讀取圖片
img = ImageTk.PhotoImage(x)                    # 轉換成PhotoImage
label1 =tk.Label(win, image = img)             # 建立Label物件 顯示圖片
label1.pack()

label21=tk.Label(win,text="商品名稱:上衣",font=("Helvetica", 16),fg="#ffaa64",bg='#fff5a5')      #建立文字
label21.place(x=50,y=100)                      #指定元件位置

label22=tk.Label(win,text="商品材質:雪紡")         #建立文件
label22.place(x=50,y=120)                    #指定元件位置

label23=tk.Label(win,text="商品尺寸:F")         #建立文件
label23.place(x=50,y=140)                    #指定元件位置

label21=tk.Label(win,text="商品衣長:62")      #建立文字
label21.place(x=50,y=160)                      #指定元件位置

label21=tk.Label(win,text="商品胸寬:110")      #建立文字
label21.place(x=50,y=180)                      #指定元件位置

label21=tk.Label(win,text="商品產地:台灣")      #建立文字
label21.place(x=50,y=200)                      #指定元件位置

label21=tk.Label(win,text="商品顏色:白色")      #建立文字
label21.place(x=50,y=220)                      #指定元件位置

label21=tk.Label(win,text="商品成本:200")      #建立文字
label21.place(x=50,y=240)                      #指定元件位置

label21=tk.Label(win,text="商品價錢:350")      #建立文字
label21.place(x=50,y=260)                      #指定元件位置

label21=tk.Label(win,text="商品數量:10")      #建立文字
label21.place(x=50,y=280)                      #指定元件位置




"""
label1 =tk.Label(win,text="產品",font=("Helvetica", 16),fg="#ffaa64",bg='#fff5a5')  # 建立文字
label1.place(x=20, y=0)

label1 =tk.Label(win,text="產品名稱:"+productClass1.productName )  # 建立文字
label1.place(x=20, y=60)                 # 指定元件位置 x=20, y=60 的位置
label2 =tk.Label(win,text="價格:"+str(productClass1.productPrice))  # 建立文字
label2.place(x=20, y=80)                 # 指定元件位置 x=20, y=80 的位置
label3 =tk.Label(win,text="庫存:"+str(productClass1.productItems))  # 建立文字
label3.place(x=20, y=100)                 # 指定元件位置 x=20, y=100 的位置


win.mainloop()       # 最後步驟：程式做無限循環

"""