'''So, I don't entirely know where to start, but I need to start with my 
own thoughts before just importing stuff since that's how i'll learn. 
I think i need to first figure out the structure of my items 
and stuff for classes and sub classes.

Class: LabConsumable - attributes: lot number and expiration date
    methods: check_expiration, get_lot_number
Subclass: LabReagent - attributes: reagent name, lot number, expiration date
Class: Lot2Lot - Attributes: Reagent name, lot number, expiration date, 
                            assigned person, assignment date, atellica 1 status, 
                            atellica 2 status, completion person completion date. 
            methods: assign_lot, complete_lot, check_status'''


'''Below is to define the super class of LabConsumables. Eventually 
reagents, calibrators, QC materials, supplies will all live within this 
program. All of these items share a name, lot number, experiation date 
and a purchase number. 
In this class there are methods to set and get/retrieve all variables.'''

from datetime import date

class LabConsumable() :
    def __init__(self, name, lotNumber, expDate, purchaseNum) :
        self.__name = name
        self.__lotNumber = lotNumber
        self.__expDate = expDate
        self.__purchaseNum = purchaseNum

    def set_name(self, value) :
        if not isinstance (value, str):
            raise ValueError("The name must be a string")
        self.__name = value 

    def get_name(self) :
        return self.__name

    def set_lot(self, value) :
        if not isinstance (value, int):
            raise ValueError("The name must be a integer (whole number)")
        self.__lotNumber = value

    def get_lot(self) :
        return self.__lotNumber
   
    def set_expiration(self, value) :
        if not isinstance (value, date) :
            raise ValueError("The expiration date must be a date (mm/dd/yyyy)")
        self.__expDate = value

    def get_expiration(self) :
        return self.__expDate

    def set_purchase_num(self, value) :
        if not isinstance (value, int) :
            raise ValueError("The name must be a integer (whole number)")
        self.__purchaseNum = value

    def get_purchase_num(self) :
        return self.__purchaseNum


'''Below is the LabReagent subclass, inheriting from the LabConsumable 
Class. The only addition is to add the lotStatus variable, 
and it inherits the rest. The lotStatus variable has associated 
set and get methods with it.'''
class LabReagent(LabConsumable) :
    def __init__(self, name, lotNumber, expDate, purchaseNum, lotStatus):
        super().__init__(name, lotNumber, expDate, purchaseNum)
        self.__lotStatus  = lotStatus

    def set_lot_status(self, value, statusType = "Not Complete") :
        statusTypes = ["Not Complete", "In progress", "Complete"]
        if statusType not in statusTypes : 
            raise ValueError ("Invalid lot to lot status. " 
                                "Expected values only: %s" % statusTypes)
        
    def get_lot_status(self) :
        return self.__lotStatus