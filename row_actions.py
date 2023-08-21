import pandas as pd
from typing import NoReturn, List, Any

# add new user to phonebook
async def add_row() -> None:
    # get phonebook table
    data: pd.DataFrame = pd.read_csv('data.csv')
    # new user row
    person : List[Any] = []
    print("\nСОЗДАНИЕ НОВОЙ ЗАПИСИ В СПРАВОЧНИКЕ!\n")
    # for every column in phonebook
    for column in data.columns:
        # input a value for every column
        new_value = input(f"Новое значение в колонке '{column}': ")
        # add column value to the new user row
        person.append(new_value)
    # add new user to phonebook
    pd.concat([data, pd.Series(person)], axis=1)
    # data.loc[len(data)] = person
    # notify the user
    print("\nНовая запись сохранена!")

# edit an existing profile
async def edit_row() -> None:
    # get phonebook table
    data: pd.DataFrame = pd.read_csv('data.csv')
    # new user row
    person = []
    print("\nРЕДАКТИРОВАНИЕ ЗАПИСИ В СПРАВОЧНИКЕ!\n")
    # try to find row by ID
    try:
        # input ID
        row_id = int(input('Пожалуйста, введите ID строки, которую хотите изменить (ID вы увидите при поиске строки или при отображении списка - число перед фамилией): '))
        # get profile row
        row = data.iloc[row_id]
    except:
        # or notify the user about failure
        print("Запись не найдена!")
        return 
    
    # pair of column and value
    for column, value in row.items():
        # display the last value for the column
        print(f"\n{column} в записи: {value}\nЕсли вы не хотите менять значение, нажмите ENTER!\n")
        # input new value
        edited_value = input(f"Новое значение: ")
        # if user did input a value
        if edited_value != '':
            # insert an edited value
            person.append(edited_value)
        else:
            # inser an existing value
            person.append(value)

    # rewrite the row
    data.iloc[row_id] = pd.Series(person)
    # save the file
    data.to_csv('data.csv', index=False)
    # notify the user
    print("\nЗапись отредактирована!")
