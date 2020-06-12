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