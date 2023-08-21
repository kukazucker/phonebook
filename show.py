import pandas as pd
from typing import NoReturn
from typing import Final

# display main menu with a list with functions
def display_menu() -> None:
    print('\n********************ГЛАВНОЕ МЕНЮ********************\n\n' + 
          'Если вы хотите увидеть строки в справочнике, то введите /show\n' + 
          'Если вы хотите создать новую запись, введите /new\n' +
          'Если вы хотите отредактировать запись, введите /edit\n' + 
          'Если вы хотите найти запись(-и), введите /search\n' + 
          'Если вы хотите перезапустить программу - введите /exit\n')

# display phonebook profiles
async def display_rows() -> None:
    # required to complete the profile viewing
    exit: bool = False
    # get phonebook table
    data = pd.read_csv('data.csv')
    print("\nОТОБРАЖЕНИЕ ЗАПИСЕЙ В СПРАВОЧНИКЕ!\n")
    # how many rows to display
    rows_amount: Final = int(input('Сколько строк на странице вы хотите видеть? '))
    # start and stop row to display
    start: int = len(data) - rows_amount
    stop: int = len(data)
    # display the rows for first time
    print(data[start:stop].sort_index(ascending=False))
    # dont close window while the user wants to close
    while exit == False:
        # ask the user to continue or stop the viewing
        answer: str = input("\n ПРОДОЛЖИТЬ (enter) ИЛИ НЕТ (/exit)?     ")
        # if user will press exit from the window
        if answer == '/exit':
            exit = True
        
        else:
            # display another 'rows_amount' rows amount
            start -= rows_amount; stop -= rows_amount
            # if list is over
            if start <= 1:
                # show first profile in phonebook
                start = 0
                print(data[start:stop].sort_index(ascending=False))
                # notify the user
                print("\nСписок закончился!")
                return
            
            # display the table rows
            print(data[start:stop].sort_index(ascending=False))


# search the rows by any feature
async def search_rows() -> None:

    # get phonebook table
    data = pd.read_csv('data.csv')
    # search features
    properties: list = []
    print("\nПОИСКЗАПИСИ В СПРАВОЧНИКЕ!\n")

    # while user has the extra features
    while True:
        # input the feautre and value of this column
        row_feature: str = input("Введите наименование характеристики (Нажмите ENTER для окончания набора характеристик): ")
        value: str = input("Введите значение характеристики для поиска (Нажмите ENTER для окончания набора характеристик): ")

        # if user pressed ENTER to stop features collecting
        if row_feature == '' or value == '':
            # break the loop
            break
        
        # try to convert numeric features
        try:
            num_value: int = int(value)        
            # add feature to the search selector
            properties.append({row_feature : num_value})
        except:
            pass

        # add feature to the search selector
        properties.append({row_feature : value})

    # if user didnt select any feature
    if properties == []:
        # notify the user
        print("ВЫ НЕ ВВЕЛИ НИ ОДНОЙ ХАРАКТЕРИСТИКИ!")
        # close the program
        return
    
    # for every poverty to search
    for property in properties:
        # for table column and the corresponding value in the poverty
        for feature in property.items():
            # try to find rows by features
            data = data[data[feature[0]] == feature[1]]

    # if data is empty
    if data.empty == True:
        # notify the user
        print('\nПо запросу ничего не найдено!')
        return

    # display found rows
    print(data)