# 1. Create add item function
def add_item(myTempList, item):    
    myTempList.append(item)
# 2. create find item function
def find_index_item(myTempList, item_name):
    result = -1
    length = len(myTempList)
    for i in range(length):
        if myTempList[i]['name'] == item_name:
            result = i
    return result
# 3. Create delete item function
def remove_item(myTempList, item_name):
    if find_index_item(myTempList, item_name) > -1:
        del myTempList[find_index_item(myTempList, item_name)]
    else:
        print(item_name + " not in list")
# 4. interfrace with user
expenses = []
check = True
while check:
  print("Your expenses:", expenses)
  print("What do you want to do? -\n"\
          "1. Add\n" \
          "2. Remove\n" \
          "3. Quit")
  option = int(input("Select option 1 or 2 or 3: "))

  if option == 1:
      name_input = input("Item name: ")
      cost_input = int(input("Item cost: "))
      date_input = input("Date: ")
      item = {'name': name_input, 'cost':cost_input, 'date':date_input}
      add_item(expenses, item)

  elif option == 2:
      name_input = input("Item name: ")
      remove_item(expenses, name_input)

  elif option == 3:
      print("Thank you for using our app")
      check = False
      
  else:
      print("Invalid input")