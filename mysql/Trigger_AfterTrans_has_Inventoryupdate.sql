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