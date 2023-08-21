from show import display_rows, search_rows
from row_actions import add_row, edit_row

# the core of the program
async def command_string(kk) -> bool:
        # which command has been selected by the user
        match(kk):
            # display the phonebook rows
            case '/show':
                await display_rows()
                # return False to dont close the program
                return False
            # find the phonebook rows
            case '/search':
                await search_rows()
                # return False to dont close the program
                return False
            # create a new profile
            case '/new':
                await add_row()
                # return False to dont close the program
                return False
            # edit a profile
            case '/edit':
                await edit_row()
                # return False to dont close the program
                return False
            # stop the program
            case '/exit':
                print('ПРОГРАММА ЗАКРЫТА!')
                # return True to close the program
                return True
            # undefined command
            case _ : 
                print("ОШИБКА: НЕОПОЗНАННАЯ КОММАНДА!")
                # return False to dont close the program
                return False