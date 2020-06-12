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