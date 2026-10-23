import LabItems

#This is to test the LabConsumable.py classes see below for tests

#Testing the methods of the lab consumable class
ctest_1 = LabItems.LabConsumable("Chol_2","1234","10/2/2026","1")

print(ctest_1.get_name(), ctest_1.get_lot(), ctest_1.get_expiration(), ctest_1.get_purchase_num())

ctest_1.set_name(123)

print(ctest_1.get_name(), ctest_1.get_lot(), ctest_1.get_expiration(), ctest_1.get_purchase_num())