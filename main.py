import asyncio
from typing import NoReturn
from control import command_string
from show import display_menu

async def phonebook_programm() -> None:
    # necessary for loop
    log: bool = False
    # -1 means termination of the loop
    while log != True:
        # display main menu
        display_menu()
        # wait for the command from user
        command: str = input("ВВЕДИТЕ КОММАНДУ:   ")
        # get log's number
        stop_program: bool = await command_string(command)
        # update log
        log = stop_program      


# start program
if __name__ == '__main__':
    asyncio.run(phonebook_programm())
