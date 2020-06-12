#멤버십포인트가 자동으로 구매금액의 1%만큼 더해지게하는 trigger +trans table에 거래 내역이 추가될때마다 그 누적가격을 계산해서 해당 고객의 등급 update
DELIMITER //
CREATE TRIGGER AfterTransinsert
AFTER INSERT ON TRANS
FOR EACH ROW

BEGIN 
	DECLARE varTotalPrice	Int;
    DECLARE varMembership	Int;
    DECLARE varCustomerID	varchar(20);
    DECLARE varsumTotalprice	Int; #고객등급 update위한
    
    SET	 varCustomerID = NEW.CUSTOMER_Customer_ID;
    SET  varTotalPrice = NEW.TotalPrice;
    SET  varMembership = 0.01*varTotalPrice;
    
    UPDATE CUSTOMER
		SET  MembershipPoint = varMembership + MembershipPoint
		WHERE CUSTOMER_ID = varCustomerID;
	    
    SELECT SUM(TotalPrice) into varsumTotalprice
	FROM TRANS JOIN CUSTOMER AS C
	ON C.CUSTOMER_ID = CUSTOMER_Customer_ID
	WHERE C.CUSTOMER_ID = varCustomerID;
    
    IF varsumTotalprice <10000
    THEN
		UPDATE CUSTOMER
		SET  CustomerGrade = "Iron"
		WHERE CUSTOMER.CUSTOMER_ID = varCustomerID;
	
    ELSEIF varsumTotalprice <200000
    THEN
		UPDATE CUSTOMER
		SET  CustomerGrade = "Bronze"
		WHERE CUSTOMER.CUSTOMER_ID = varCustomerID;
	ELSEIF varsumTotalprice < 500000
	THEN
		UPDATE CUSTOMER
		SET  CustomerGrade = "Silver"
		WHERE CUSTOMER.CUSTOMER_ID = varCustomerID;
    ELSEIF varsumTotalprice < 1000000
	THEN
		UPDATE CUSTOMER
		SET  CustomerGrade = "Gold"
		WHERE CUSTOMER.CUSTOMER_ID = varCustomerID;
    ELSEIF varsumTotalprice < 2000000
	THEN
		UPDATE CUSTOMER
		SET  CustomerGrade = "Platinum"
		WHERE CUSTOMER.CUSTOMER_ID = varCustomerID;    
     ELSEIF varSUMTotalprice >= 2000000
    THEN
		UPDATE CUSTOMER
		SET  CustomerGrade = "Diamond"
		WHERE CUSTOMER.CUSTOMER_ID = varCustomerID;
    ELSE
		UPDATE CUSTOMER
		SET  CustomerGrade = "Iron"
		WHERE CUSTOMER.CUSTOMER_ID = varCustomerID;    
    
    END IF;        
    END //
    
DELIMITER ;