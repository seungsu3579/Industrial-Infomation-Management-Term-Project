use space;

INSERT INTO CUSTOMER
	(Customer_ID, Password, CustomerName, Email) 
    VALUES('ljh9625', 'ljh9625', 'ljh9625', 'ljh9625@gmail');
    
INSERT INTO CUSTOMER
	(Customer_ID, Password, CustomerName, Email) 
    VALUES('yss0410', 'yss0410', 'yss0410', 'yss0410@gmail');
    
INSERT INTO CUSTOMER
	(Customer_ID, Password, CustomerName, Email) 
    VALUES('kjh0710', 'kjh0710', 'kjh0710', 'kjh0710@gmail');
    
INSERT INTO CUS_ADDRESS
	(Address, CUSTOMER_Customer_ID) 
    VALUES('yonsei', 'ljh9625');
    
INSERT INTO CUS_ADDRESS
	(Address, CUSTOMER_Customer_ID) 
    VALUES('SNU', 'ljh9625');
    
INSERT INTO CUS_ADDRESS
	(Address, CUSTOMER_Customer_ID) 
    VALUES('Harvard', 'yss0410');
    
INSERT INTO CUS_ADDRESS
	(Address, CUSTOMER_Customer_ID) 
    VALUES('Cambridge', 'yss0410');
    
INSERT INTO CUS_ADDRESS
	(Address, CUSTOMER_Customer_ID) 
    VALUES('Oxford', 'kjh0710');
    
INSERT INTO CUS_ADDRESS
	(Address, CUSTOMER_Customer_ID) 
    VALUES('D407', 'kjh0710');
    
INSERT INTO CUS_COUPON
	(Coupon, CUSTOMER_Customer_ID) 
    VALUES('10percent', 'ljh9625');
    
INSERT INTO CUS_COUPON
	(Coupon, CUSTOMER_Customer_ID) 
    VALUES('50percent', 'ljh9625');
    
INSERT INTO CUS_COUPON
	(Coupon, CUSTOMER_Customer_ID) 
    VALUES('10percent', 'yss0410');
    
INSERT INTO CUS_COUPON
	(Coupon, CUSTOMER_Customer_ID) 
    VALUES('50percent', 'yss0410');
    
INSERT INTO CUS_COUPON
	(Coupon, CUSTOMER_Customer_ID) 
    VALUES('10percent', 'kjh0710');
    
INSERT INTO CUS_COUPON
	(Coupon, CUSTOMER_Customer_ID) 
    VALUES('50percent', 'kjh0710');
    
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('CK M2M', 'CK', 'Sweater', 100000, '2019-12-06');
 
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('PLAC Jean', 'PLAC', 'Jean', 200000, '2019-12-06');
    
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('CKname Jacket', 'CK', 'Outer', 300000, '2019-12-06');
    
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Checkhoodover', 'Papercut', 'Shirts', 90000, '2019-12-18');
    
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Taperdeuropants', 'Halbkreis', 'Pants', 50000, '2019-12-10');
    
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Essential3Swind', 'Adidas', 'Training', 65000, '2019-11-07');
    
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Avotlopper', 'Dr.Martin', 'Shoes', 190000, '2019-10-02');
    
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Beanpoleback', 'Beanpole', 'Bag', 260000, '2019-09-30');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('c194sweat', 'A', 'Sweater', 19000, '2019-12-01');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Cherrytone', 'B', 'Sweater', 29000, '2019-12-02');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('HALFPOLA', 'C', 'Sweater', 39000, '2019-12-03');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Jellybean', 'D', 'Sweater', 49000, '2019-12-04');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Overknitfat', 'E', 'Sweater', 59000, '2019-12-05');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Softbasicturtleneck', 'F', 'Sweater', 69000, '2019-12-06');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Softcottoncrew', 'G', 'Sweater', 79000, '2019-12-07');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Softcottondropshoulder', 'H', 'Sweater', 89000, '2019-12-08');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('TWCknit', 'A', 'Sweater', 99000, '2019-12-09');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Vividpullover', 'C', 'Sweater', 119000, '2019-12-10');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('10willjacket', 'A', 'Outer', 13000, '2019-12-01');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Fishtailcoat', 'B', 'Outer', 233000, '2019-12-02');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Fishtailduffle', 'C', 'Outer', 44000, '2019-12-03');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Overfittrench', 'D', 'Outer', 52000, '2019-12-04');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Pontesinglecoat', 'E', 'Outer', 356000, '2019-12-05');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Trenchbeigecoat', 'F', 'Outer', 1146000, '2019-12-06');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Cottonfatigue', 'A', 'Pants', 29000, '2019-12-06');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Dailychino', 'B', 'Pants', 29000, '2019-12-07');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Musinsaslacks', 'C', 'Pants', 29000, '2019-12-08');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Objectpants', 'D', 'Pants', 29000, '2019-12-09');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Pinkcorduroy', 'E', 'Pants', 29000, '2019-12-10');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Taperedchino', 'F', 'Pants', 29000, '2019-12-11');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Widecorduroy', 'G', 'Pants', 29000, '2019-12-12');    
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Blakmessanger', 'A', 'Bag', 39000, '2019-12-12');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Covernantbag', 'B', 'Bag', 49000, '2019-12-13');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Covernatbbbag', 'C', 'Bag', 59000, '2019-12-14');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Fancybag', 'D', 'Bag', 69000, '2019-12-15');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Neikidnisbag', 'E', 'Bag', 79000, '2019-12-16');    
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('dknowdf', 'A', 'Jean', 89000, '2019-12-16');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Modifiedblack', 'A', 'Jean', 55000, '2019-12-17');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('patalblack', 'A', 'Jean', 53000, '2019-12-18');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Patalism', 'A', 'Jean', 544000, '2019-12-19');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Washingjean', 'A', 'Jean', 23000, '2019-12-20');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('Wideblue', 'A', 'Jean', 49000, '2019-12-21');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('beigeshirets', 'A', 'Shirts', 49000, '2019-11-21');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('bluecheck', 'B', 'Shirts', 49000, '2019-12-21');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('browncorduroy', 'C', 'Shirts', 49000, '2019-02-21');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('checkgurl', 'D', 'Shirts', 49000, '2019-04-21');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('yellowcheck', 'E', 'Shirts', 49000, '2019-05-21');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('3daemeot', 'A', 'Training', 49000, '2019-11-21');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('lashbae', 'B', 'Training', 39000, '2019-11-22');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('lashboy', 'C', 'Training', 29000, '2019-11-23');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('nikebaji', 'D', 'Training', 69000, '2019-11-22');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('warmhand', 'E', 'Training', 89000, '2019-11-23');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('yogagurl', 'F', 'Training', 119000, '2019-11-21');    
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('blackfancy', 'A', 'Shoes', 49000, '2019-11-21');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('bluegoodoo', 'B', 'Shoes', 59000, '2019-11-22');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('brownboots', 'C', 'Shoes', 119000, '2019-10-21');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('navymule', 'D', 'Shoes', 890000, '2019-12-21');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('sandle', 'E', 'Shoes', 498000, '2019-12-22');
INSERT INTO PRODUCT
	(ProductName, Brand, Category, Price, AcquiredDate) 
    VALUES('whitemul', 'F', 'Shoes', 65000, '2019-12-24');

INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Black', 33, 'CK M2M');

INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Black', 22, 'CK M2M');
    
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Blue', 34, 'PLAC Jean');
    
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Blue', 13, 'PLAC Jean');
    
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Black', 21, 'CKname Jacket');
    
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Black', 30, 'CKname Jacket');
    
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Gray', 109, 'Checkhoodover');
    
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Gray', 20, 'Checkhoodover'); 

INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Green', 39, 'Taperdeuropants'); 
    
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Green', 50, 'Taperdeuropants'); 
    
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Black', 40, 'Essential3Swind'); 
    
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Black', 30, 'Essential3Swind'); 
    
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Black', 50, 'Avotlopper'); 
    
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Black', 21, 'Avotlopper'); 
    
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Black', 28, 'Beanpoleback'); 
    
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Black', 36, 'Beanpoleback'); 

INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Black', 10, 'Blakmessanger');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Black', 12, 'Covernantbag');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Black', 11, 'Covernatbbbag');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Black', 8, 'Fancybag');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Black', 9, 'Neikidnisbag');
    
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Blue', 12, 'dknowdf');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Blue', 13, 'dknowdf');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Blue', 20, 'Wideblue');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Blue', 20, 'Wideblue');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Blue', 21, 'Washingjean');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Blue', 12, 'Washingjean');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Blue', 21, 'Patalism');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Blue', 17, 'Patalism');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Black', 14, 'Modifiedblack');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Black', 9, 'Modifiedblack');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Black', 11, 'patalblack');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Black', 12, 'patalblack');
    
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Red', 12, '10willjacket');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Green', 16, 'Fishtailcoat');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Green', 19, 'Fishtailduffle');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'White', 12, 'Overfittrench');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Brown', 17, 'Pontesinglecoat');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Blue', 23, 'Trenchbeigecoat');
    
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Brown', 11, 'Dailychino');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Brown', 12, 'Dailychino');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Brown', 12, 'Cottonfatigue');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Brown', 13, 'Cottonfatigue');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Black', 13, 'Musinsaslacks');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Black', 14, 'Musinsaslacks');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'White', 14, 'Objectpants');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'White', 15, 'Objectpants');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Pink', 15, 'Pinkcorduroy');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Pink', 16, 'Pinkcorduroy');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Brown', 16, 'Taperedchino');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Brown', 17, 'Taperedchino');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Black', 17, 'Widecorduroy');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Black', 18, 'Widecorduroy');
    
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Beige', 18, 'beigeshirets');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Blue', 10, 'bluecheck');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Brown', 8, 'browncorduroy');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Yellow', 14, 'checkgurl');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Yellow', 9, 'yellowcheck');
    
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Black', 9, 'blackfancy');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Blue', 8, 'bluegoodoo');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Brown', 11, 'brownboots');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'navy', 14, 'navymule');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Black', 13, 'sandle');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'White', 12, 'whitemul');
    
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', ' Black', 10, 'c194sweat');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Black', 13, 'Cherrytone');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Black', 15, 'HALFPOLA');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Colorful', 12, 'Jellybean');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Brown', 8, 'Overknitfat');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Black', 7, 'Softbasicturtleneck');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Brown', 10, 'Softcottoncrew');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Black', 14, 'Softcottondropshoulder');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Red', 15, 'TWCknit');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('L', 'Blue', 18, 'Vividpullover');
    
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Green', 18, '3daemeot');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Black', 13, 'lashbae');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Black', 16, 'lashboy');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Black', 22, 'nikebaji');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Brown', 25, 'warmhand');
INSERT INTO INVENTORY
	(Size, Color, Quantity, PRODUCT_ProductName) 
    VALUES('M', 'Blue', 17, 'yogagurl');
    
INSERT INTO INFLUENCER
	(AdminID, Password, Nickname, Height, Weight) 
    VALUES('woojoo123','woojoo123','woojoo', 180, 75);
    
INSERT INTO INFLUENCER
	(AdminID, Password, Nickname, Height, Weight) 
    VALUES('toybox505','toybox505','toybox', 185, 78);
    
INSERT INTO STYLE
	(ADMIN_AdminID, Description) 
    VALUES('woojoo123', 'Street Style you can be a hiphop');
    
INSERT INTO STYLE
	(ADMIN_AdminID, Description) 
    VALUES('woojoo123', 'great outfit for school opening day');
    
INSERT INTO STYLE
	(ADMIN_AdminID, Description) 
    VALUES('woojoo123', 'Today is dancing day, you can wear training outfit');
    
INSERT INTO STYLE
	(ADMIN_AdminID, Description) 
    VALUES('toybox505', 'Street sytle can be FLEX BBAGGEU');
    
INSERT INTO STYLE
	(ADMIN_AdminID, Description) 
    VALUES('toybox505', 'Classic is the best fashion');

INSERT INTO STYLE
	(ADMIN_AdminID, Description) 
    VALUES('woojoo123', 'Ohmygod so fancy');
INSERT INTO STYLE
	(ADMIN_AdminID, Description) 
    VALUES('woojoo123', 'Fantastic beautiful');
INSERT INTO STYLE
	(ADMIN_AdminID, Description) 
    VALUES('woojoo123', 'Holy Joly Merry Christmas');
    
INSERT INTO STYLE
	(ADMIN_AdminID, Description) 
    VALUES('toybox505', 'Feliz Navidad');
INSERT INTO STYLE
	(ADMIN_AdminID, Description) 
    VALUES('toybox505', 'Classic is the only way');
INSERT INTO STYLE
	(ADMIN_AdminID, Description) 
    VALUES('toybox505', 'Seungsu so handsome');
INSERT INTO STYLE
	(ADMIN_AdminID, Description) 
    VALUES('toybox505', 'jeonghyun the cutest..');
    
INSERT INTO STYLE_has_Product
	(STYLE_StyleID, PRODUCT_ProductName) 
    VALUES(1, 'CK M2M');
    
INSERT INTO STYLE_has_Product
	(STYLE_StyleID, PRODUCT_ProductName) 
    VALUES(1, 'PLAC Jean');

INSERT INTO STYLE_has_Product
	(STYLE_StyleID, PRODUCT_ProductName) 
    VALUES(2, 'Checkhoodover');
    
INSERT INTO STYLE_has_Product
	(STYLE_StyleID, PRODUCT_ProductName) 
    VALUES(2, 'Taperdeuropants');
    
INSERT INTO STYLE_has_Product
	(STYLE_StyleID, PRODUCT_ProductName) 
    VALUES(2, 'Beanpoleback');
    
INSERT INTO STYLE_has_Product
	(STYLE_StyleID, PRODUCT_ProductName) 
    VALUES(3, 'CK M2M');
    
INSERT INTO STYLE_has_Product
	(STYLE_StyleID, PRODUCT_ProductName) 
    VALUES(3, 'Essential3Swind');
    
INSERT INTO STYLE_has_Product
	(STYLE_StyleID, PRODUCT_ProductName) 
    VALUES(4, 'Checkhoodover');
    
INSERT INTO STYLE_has_Product
	(STYLE_StyleID, PRODUCT_ProductName) 
    VALUES(4, 'PLAC Jean');
    
INSERT INTO STYLE_has_Product
	(STYLE_StyleID, PRODUCT_ProductName) 
    VALUES(5, 'Avotlopper');
    
INSERT INTO STYLE_has_Product
	(STYLE_StyleID, PRODUCT_ProductName) 
    VALUES(5, 'CK M2M');

INSERT INTO STYLE_has_Product
	(STYLE_StyleID, PRODUCT_ProductName) 
    VALUES(6, '3daemeot');
INSERT INTO STYLE_has_Product
	(STYLE_StyleID, PRODUCT_ProductName) 
    VALUES(6, 'nikebaji');
    
INSERT INTO STYLE_has_Product
	(STYLE_StyleID, PRODUCT_ProductName) 
    VALUES(7, 'Covernantbag');
INSERT INTO STYLE_has_Product
	(STYLE_StyleID, PRODUCT_ProductName) 
    VALUES(7, 'beigeshirets');
    
INSERT INTO STYLE_has_Product
	(STYLE_StyleID, PRODUCT_ProductName) 
    VALUES(8, 'Covernatbbbag');
INSERT INTO STYLE_has_Product
	(STYLE_StyleID, PRODUCT_ProductName) 
    VALUES(8, 'browncorduroy');
    
INSERT INTO STYLE_has_Product
	(STYLE_StyleID, PRODUCT_ProductName) 
    VALUES(9, 'checkgurl');
INSERT INTO STYLE_has_Product
	(STYLE_StyleID, PRODUCT_ProductName) 
    VALUES(9, 'Cottonfatigue');    
    
INSERT INTO STYLE_has_Product
	(STYLE_StyleID, PRODUCT_ProductName) 
    VALUES(10, 'Dailychino');
INSERT INTO STYLE_has_Product
	(STYLE_StyleID, PRODUCT_ProductName) 
    VALUES(10, '10willjacket');
    
INSERT INTO STYLE_has_Product
	(STYLE_StyleID, PRODUCT_ProductName) 
    VALUES(11, 'Fishtailcoat');
INSERT INTO STYLE_has_Product
	(STYLE_StyleID, PRODUCT_ProductName) 
    VALUES(11, 'whitemul');
    
INSERT INTO STYLE_has_Product
	(STYLE_StyleID, PRODUCT_ProductName) 
    VALUES(12, 'brownboots');
INSERT INTO STYLE_has_Product
	(STYLE_StyleID, PRODUCT_ProductName) 
    VALUES(12, 'Pontesinglecoat');
    
INSERT INTO TRANS
	(CUSTOMER_Customer_ID, Payment, TotalPrice, DateSold, DeliveryAddress) 
    VALUES('ljh9625', 'CreditCard', 300000, '2019-10-29', 'yonsei');
    
INSERT INTO TRANS
	(CUSTOMER_Customer_ID, Payment, TotalPrice, DateSold, DeliveryAddress) 
    VALUES('yss0410', 'DebtCard', 500000, '2019-11-03', 'Cambridge');

INSERT INTO TRANS
	(CUSTOMER_Customer_ID, Payment, TotalPrice, DateSold, DeliveryAddress) 
    VALUES('yss0410', 'DebitCard', 451000, '2019-11-05', 'Cambridge');
    
INSERT INTO TRANS
	(CUSTOMER_Customer_ID, Payment, TotalPrice, DateSold, DeliveryAddress) 
    VALUES('ljh9625', 'CreditCard', 217000, '2019-11-10', 'yonsei');
    
INSERT INTO TRANS
	(CUSTOMER_Customer_ID, Payment, TotalPrice, DateSold, DeliveryAddress) 
    VALUES('ljh9625', 'DebitCard', 368000, '2019-12-15', 'SNU');
    
INSERT INTO TRANS
	(CUSTOMER_Customer_ID, Payment, TotalPrice, DateSold, DeliveryAddress) 
    VALUES('yss0410', 'DebitCard', 365000, '2019-12-23', 'Harvard');
    
INSERT INTO TRANS
	(CUSTOMER_Customer_ID, Payment, TotalPrice, DateSold, DeliveryAddress) 
    VALUES('kjh0710', 'CreditCard', 347000, '2019-12-26', 'D407');
INSERT INTO TRANS
	(CUSTOMER_Customer_ID, Payment, TotalPrice, DateSold, DeliveryAddress) 
    VALUES('kjh0710', 'CreditCard', 185000, '2019-12-28', 'Oxford');
    
INSERT INTO TRANS_has_INVENTORY
	(TRANS_idTRANS, INVENTORY_idINVENTORY, Sellprice, Quantity, Review) 
    VALUES (1, 1, 100000, 1, 'Very Good');

INSERT INTO TRANS_has_INVENTORY
	(TRANS_idTRANS, INVENTORY_idINVENTORY, Sellprice, Quantity, Review) 
    VALUES (1, 3, 200000, 1, 'Good Enough');

INSERT INTO TRANS_has_INVENTORY
	(TRANS_idTRANS, INVENTORY_idINVENTORY, Sellprice, Quantity, Review) 
    VALUES (2, 4, 200000, 1, 'Awful');
    
INSERT INTO TRANS_has_INVENTORY
	(TRANS_idTRANS, INVENTORY_idINVENTORY, Sellprice, Quantity, Review) 
    VALUES (2, 6, 300000, 1, 'Super');

INSERT INTO TRANS_has_INVENTORY
	(TRANS_idTRANS, INVENTORY_idINVENTORY, Sellprice, Quantity, Review) 
    VALUES (3, 2, 300000, 3, 'Very Bad');
INSERT INTO TRANS_has_INVENTORY
	(TRANS_idTRANS, INVENTORY_idINVENTORY, Sellprice, Quantity, Review) 
    VALUES (3, 56, 98000, 2, 'Small For me');
INSERT INTO TRANS_has_INVENTORY
	(TRANS_idTRANS, INVENTORY_idINVENTORY, Sellprice, Quantity, Review) 
    VALUES (3, 32, 53000, 1, 'Fabulous');
    
INSERT INTO TRANS_has_INVENTORY
	(TRANS_idTRANS, INVENTORY_idINVENTORY, Sellprice, Quantity, Review) 
    VALUES (4, 23, 178000, 2, 'Very Good bbbbbb');
INSERT INTO TRANS_has_INVENTORY
	(TRANS_idTRANS, INVENTORY_idINVENTORY, Sellprice, Quantity, Review) 
    VALUES (4, 34, 39000, 3, 'NWTS');
    
    
INSERT INTO TRANS_has_INVENTORY
	(TRANS_idTRANS, INVENTORY_idINVENTORY, Sellprice, Quantity, Review) 
    VALUES (5, 43, 116000, 4, 'Lovely');
INSERT INTO TRANS_has_INVENTORY
	(TRANS_idTRANS, INVENTORY_idINVENTORY, Sellprice, Quantity, Review) 
    VALUES (5, 51, 174000, 6, 'Absolutely');
INSERT INTO TRANS_has_INVENTORY
	(TRANS_idTRANS, INVENTORY_idINVENTORY, Sellprice, Quantity, Review) 
    VALUES (5, 67, 78000, 2, 'Great');
    
INSERT INTO TRANS_has_INVENTORY
	(TRANS_idTRANS, INVENTORY_idINVENTORY, Sellprice, Quantity, Review) 
    VALUES (6, 4, 200000, 1, 'Sexy Mapsy');
INSERT INTO TRANS_has_INVENTORY
	(TRANS_idTRANS, INVENTORY_idINVENTORY, Sellprice, Quantity, Review) 
    VALUES (6, 26, 46000, 2, 'Nice Bro');
INSERT INTO TRANS_has_INVENTORY
	(TRANS_idTRANS, INVENTORY_idINVENTORY, Sellprice, Quantity, Review) 
    VALUES (6, 74, 119000, 1, 'Fancy You~');

INSERT INTO TRANS_has_INVENTORY
	(TRANS_idTRANS, INVENTORY_idINVENTORY, Sellprice, Quantity, Review) 
    VALUES (7, 54, 98000, 2, 'Feel Special');
INSERT INTO TRANS_has_INVENTORY
	(TRANS_idTRANS, INVENTORY_idINVENTORY, Sellprice, Quantity, Review) 
    VALUES (7, 80, 119000, 1, 'Ooh Ahh');
INSERT INTO TRANS_has_INVENTORY
	(TRANS_idTRANS, INVENTORY_idINVENTORY, Sellprice, Quantity, Review) 
    VALUES (7, 11, 130000, 2, 'Cheer up');
    
INSERT INTO TRANS_has_INVENTORY
	(TRANS_idTRANS, INVENTORY_idINVENTORY, Sellprice, Quantity, Review) 
    VALUES (8, 32, 106000, 2, 'Your love, my love babe');
INSERT INTO TRANS_has_INVENTORY
	(TRANS_idTRANS, INVENTORY_idINVENTORY, Sellprice, Quantity, Review) 
    VALUES (8, 21, 79000, 1, 'lose you to love myself');