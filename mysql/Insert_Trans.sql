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