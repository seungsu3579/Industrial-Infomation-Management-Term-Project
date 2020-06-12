#Trans_has_inventory에 추가된 주문 개수만큼 INVENTORY 테이블 해당 제품의 재고에서 차감해주는 Trigger
DELIMITER //
CREATE TRIGGER AfterTrans_has_Inventoryinsert
AFTER INSERT ON TRANS_has_INVENTORY
FOR EACH ROW

BEGIN 
	DECLARE varQuantity INT;
    DECLARE varInventoryID INT; 
    
    SET varQuantity = NEW.Quantity;
    SET varInventoryID = NEW.INVENTORY_idINVENTORY;
    
    UPDATE INVENTORY
		SET INVENTORY.Quantity = INVENTORY.Quantity - varQuantity
		WHERE  idINVENTORY = varInventoryID;
    
 END //
    
DELIMITER ;

#환불시 재고 원래대로 돌려놓음
DELIMITER //
CREATE TRIGGER AfterTrans_has_Inventoryupdate
AFTER UPDATE ON TRANS_has_INVENTORY
FOR EACH ROW

BEGIN 
	DECLARE varQuantity INT;
    DECLARE varInventoryID INT; 
    
    SET varQuantity = NEW.Quantity;
    SET varInventoryID = NEW.INVENTORY_idINVENTORY;
    
    UPDATE INVENTORY
		SET INVENTORY.Quantity = INVENTORY.Quantity + varQuantity
		WHERE  idINVENTORY = varInventoryID;
    
 END //
    
DELIMITER ;

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

#TRANS의 Cancellation col이 바뀌고 나서(환불되고 나서) 고객등급, 포인트 재업데이트, 재고 UPDATE
DELIMITER //

CREATE TRIGGER AfterTransUpdateTrigger
AFTER UPDATE ON TRANS
FOR EACH ROW

BEGIN
	DECLARE varTotalPrice INT;
    DECLARE varSUMTotalPrice INT;
    DECLARE varCustomerID	varchar(20);
    DECLARE varMemberShip  INT;
    DECLARE varTransID INT;
    
    SET	  varTotalPrice = NEW.TotalPrice;
	SET   varMemberShip = 0.01*varTotalPrice;  #환불 금액의 1%만큼 멤버십포인트에서 차감하기위해 설정
    SET	  varCustomerID = OLD.CUSTOMER_Customer_ID;
    SET varTransID = OLD.idTrans;
    #T_h_I 테이블에서 해당 Transid와 같은 id를 가지는 주문내역의 quantity를 같은 값으로 update
    UPDATE TRANS_has_INVENTORY
		SET Quantity = Quantity
		WHERE TRANS_idTRANS = varTransID;
    #환불 금액만큼 비례해서 멤버십포인트 차감
    UPDATE CUSTOMER
		SET  MembershipPoint = -varMembership + MembershipPoint
		WHERE CUSTOMER_ID = varCustomerID;
    
    -- 환불된 금액을 제외한 누적합계금액 구함
    
    SELECT SUM(Totalprice) into varSUMTotalprice   #환불된 금액만큼 차감된 누적합계금액 구함
    FROM TRANS
    WHERE CUSTOMER_Customer_ID = varCustomerID AND Cancellation = 'No';
    
    
    
    -- 환불 후 고객등급 업데이트해주는 쿼리
    IF varSUMTotalprice <10000 OR varSUMTotalprice = NULL
    THEN
		UPDATE CUSTOMER
		SET  CustomerGrade = "Iron"
		WHERE CUSTOMER.CUSTOMER_ID = varCustomerID;
	
    ELSEIF varSUMTotalprice <200000
    THEN
		UPDATE CUSTOMER
		SET  CustomerGrade = "Bronze"
		WHERE CUSTOMER.CUSTOMER_ID = varCustomerID;
	ELSEIF varSUMTotalprice < 500000
	THEN
		UPDATE CUSTOMER
		SET  CustomerGrade = "Silver"
		WHERE CUSTOMER.CUSTOMER_ID = varCustomerID;
	ELSEIF varSUMTotalprice < 1000000
	THEN
		UPDATE CUSTOMER
		SET  CustomerGrade = "Gold"
		WHERE CUSTOMER.CUSTOMER_ID = varCustomerID;
	ELSEIF varSUMTotalprice < 2000000
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
    
    
END//

DELIMITER ;