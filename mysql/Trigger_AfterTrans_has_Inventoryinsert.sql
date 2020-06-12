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