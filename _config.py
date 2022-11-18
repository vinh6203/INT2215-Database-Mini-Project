from tkinter import *
from tkinter import messagebox
from sqlTest import *

# Character = Champion
def openCharacterCreationWindow():
    def clearInput():
        nameInput.delete(0, 'end')
        typeInput.delete(0, 'end')
    def submitData():
        name = nameInput.get()
        charaterType = typeInput.get()
        try:
            name[0]
        except IndexError:
            return messagebox.showerror('Error', "Name can not be empty")
        return insertChampion(name, charaterType)
        return messagebox.showinfo('message', "name: %s, type: %s" % (name, charaterType))

    CharacterCreationWindow = Tk()
    CharacterCreationWindow.title("Character Creation Window")
    CharacterCreationWindow.geometry("500x250")

    title = Label(
        master=CharacterCreationWindow,
        text="Character Creation"
    )
    nameLabel = Label(
        CharacterCreationWindow,
        text="Character Name",
        font=('calibre', 10, 'bold')
    )
    nameInput = Entry(
        CharacterCreationWindow,
        width=50
    )
    typeLabel = Label(
        CharacterCreationWindow,
        text="Character Type",
        font=('calibre', 10, 'bold')
    )
    typeInput = Entry(
        CharacterCreationWindow,
        width=50
    )
    submitButton = Button(
        CharacterCreationWindow,
        text="Submit",
        width=25,
        height=5,
        bg="cyan",
        command=submitData
    )
    clearAll = Button(
        CharacterCreationWindow,
        text="Clear all",
        width=25,
        height=5,
        bg="red",
        command=clearInput
    )

    title.grid(row=0,column=1)
    nameLabel.grid(row=1,column=0)
    nameInput.grid(row=1,column=1)
    typeLabel.grid(row=2,column=0)
    typeInput.grid(row=2,column=1)
    submitButton.grid(row=3,column=1)
    clearAll.grid(row=4,column=1)
    CharacterCreationWindow.mainloop()


def openWeaponCreationWindow():
    def clearInput():
        nameInput.delete(0, 'end')
        attackInput.delete(0, 'end')
        defenseInput.delete(0, 'end')
        ChampionIDInput.delete(0, 'end')
    def submitData():
        name = nameInput.get()
        attack = attackInput.get()
        defense = defenseInput.get()
        championID = ChampionIDInput.get()
        try:
            name[0]
        except IndexError:
            return messagebox.showerror('Error', "Name can not be empty")
        try:
            int(attack)
        except ValueError:
            return messagebox.showerror('Error', "Attack must be integer")
        try:
            int(defense)
        except ValueError:
            return messagebox.showerror('Error', "Defense must be integer")
        try:
            int(championID)
        except ValueError:
            return messagebox.showerror('Error', "ChampionID must be integer")
        return insertWeapon(name, attack, defense, championID)
        return messagebox.showinfo('Message', name + " " + attack + " " + defense + " " + championID)

    WeaponCreationWindow = Tk()
    WeaponCreationWindow.title("Weapon Creation Window")
    WeaponCreationWindow.geometry("500x285")

    title = Label(
        master=WeaponCreationWindow,
        text="Weapon Creation"
    )
    nameLabel = Label(
        WeaponCreationWindow,
        text="Weapon Name",
        font=('calibre', 10, 'bold')
    )
    nameInput = Entry(
        WeaponCreationWindow,
        width=50
    )
    attackLabel = Label(
        WeaponCreationWindow,
        text="Attack Stats",
        font=('calibre', 10, 'bold')
    )
    attackInput = Entry(
        WeaponCreationWindow,
        width=50
    )
    defenseLabel = Label(
        WeaponCreationWindow,
        text="Defense Stats",
        font=('calibre', 10, 'bold')
    )
    defenseInput = Entry(
        WeaponCreationWindow,
        width=50
    )
    championIDLabel = Label(
        WeaponCreationWindow,
        text="ChampionID",
        font=('calibre', 10, 'bold')
    )
    ChampionIDInput = Entry(
        WeaponCreationWindow,
        width=50
    )
    submitButton = Button(
        WeaponCreationWindow,
        text="Submit",
        width=25,
        height=5,
        bg="cyan",
        command=submitData
    )
    clearAll = Button(
        WeaponCreationWindow,
        text="Clear all",
        width=25,
        height=5,
        bg="red",
        command=clearInput
    )
    title.grid(row=0,column=1)
    nameLabel.grid(row=1,column=0)
    nameInput.grid(row=1,column=1)
    attackLabel.grid(row=2,column=0)
    attackInput.grid(row=2,column=1)
    defenseLabel.grid(row=3,column=0)
    defenseInput.grid(row=3,column=1)
    championIDLabel.grid(row=4,column=0)
    ChampionIDInput.grid(row=4,column=1)
    submitButton.grid(row=5,column=1)
    clearAll.grid(row=6,column=1)
    WeaponCreationWindow.mainloop()


def openGameCreationWindow():
    def clearInput():
        nameInput.delete(0, 'end')
        multiplayerInput.delete(0, 'end')
        priceInput.delete(0, 'end')
        publisherInput.delete(0, 'end')
    def submitData():
        name = nameInput.get()
        multiplayer = multiplayerInput.get()
        price = priceInput.get()
        publisher = publisherInput.get()
        try:
            name[0]
        except IndexError:
            return messagebox.showerror('Error', "Name can not be empty")
        try:
            float(price)
        except ValueError:
            return messagebox.showerror('Error', "Price must have integer or float value")
        if float(price) < 0:
            return messagebox.showerror('Error', "Price must be positive")
        if multiplayer not in ["Y", "y", "N", "n"]:
            return messagebox.showerror('Error', "Multiplayer input must be either Y, y, N, n")
        return insertGame(name, multiplayer, price, publisher)
        return messagebox.showinfo('message', name + " " + multiplayer + " " + price + " " + publisher)
        
    GameCreationWindow = Tk()
    GameCreationWindow.title("Game Creation Window")
    GameCreationWindow.geometry("500x285")

    title = Label(
        master=GameCreationWindow,
        text="Game Creation"
    )
    nameLabel = Label(
        GameCreationWindow,
        text="Game Name",
        font=('calibre', 10, 'bold')
    )
    nameInput = Entry(
        GameCreationWindow,
        width=50
    )
    multiplayerLabel = Label(
        GameCreationWindow,
        text="Is Multiplayer (Y/N)",
        font=('calibre', 10, 'bold')
    )
    multiplayerInput = Entry(
        GameCreationWindow,
        width=50
    )
    priceLabel = Label(
        GameCreationWindow,
        text="Price",
        font=('calibre', 10, 'bold')
    )
    priceInput = Entry(
        GameCreationWindow,
        width=50
    )
    publisherLabel = Label(
        GameCreationWindow,
        text="Publisher ID",
        font=('calibre', 10, 'bold')
    )
    publisherInput = Entry(
        GameCreationWindow,
        width=50
    )
    submitButton = Button(
        GameCreationWindow,
        text="Submit",
        width=25,
        height=5,
        bg="cyan",
        command=submitData
    )
    clearAll = Button(
        GameCreationWindow,
        text="Clear all",
        width=25,
        height=5,
        bg="red",
        command=clearInput
    )
    title.grid(row=0,column=1)
    nameLabel.grid(row=1,column=0)
    nameInput.grid(row=1,column=1)
    multiplayerLabel.grid(row=2,column=0)
    multiplayerInput.grid(row=2,column=1)
    priceLabel.grid(row=3,column=0)
    priceInput.grid(row=3,column=1)
    publisherLabel.grid(row=4,column=0)
    publisherInput.grid(row=4,column=1)
    submitButton.grid(row=5,column=1)
    clearAll.grid(row=6,column=1)
    GameCreationWindow.mainloop()


def openMapCreationWindow():
    def clearInput():
        nameInput.delete(0, 'end')
        mapWidthInput.delete(0, 'end')
        mapHeightInput.delete(0, 'end')
        belongGameInput.delete(0, 'end')
    def submitData():
        name = nameInput.get()
        mapWidth = mapWidthInput.get()
        mapHeight = mapHeightInput.get()
        belongGame = belongGameInput.get()
        try:
            name[0]
        except IndexError:
            return messagebox.showerror('Error', "Name can not be empty")
        try:
            int(mapWidth)
        except ValueError:
            return messagebox.showerror('Error', "Map Width must be integer")
        try:
            int(mapHeight)
        except ValueError:
            return messagebox.showerror('Error', "Map Height must be integer")
        try:
            int(belongGame)
        except ValueError:
            return messagebox.showerror('Error', "GameID must be integer")
        return insertMap(name, mapHeight, mapWidth, belongGame)
        return messagebox.showinfo('message', name + " " + mapWidth + " " + mapHeight + " " + belongGame)

    MapCreationWindow = Tk()
    MapCreationWindow.title("Map Creation Window")
    MapCreationWindow.geometry("450x290")

    title = Label(
        master=MapCreationWindow,
        text="Map Creation"
    )
    nameLabel = Label(
        MapCreationWindow,
        text="Map Name",
        font=('calibre', 10, 'bold')
    )
    nameInput = Entry(
        MapCreationWindow,
        width=50
    )
    mapWidthLabel = Label(
        MapCreationWindow,
        text="Map Width",
        font=('calibre', 10, 'bold')
    )
    mapWidthInput = Entry(
        MapCreationWindow,
        width=50
    )
    mapHeightLabel = Label(
        MapCreationWindow,
        text="Map Height",
        font=('calibre', 10, 'bold')
    )
    mapHeightInput = Entry(
        MapCreationWindow,
        width=50
    )
    belongGameLabel = Label(
        MapCreationWindow,
        text="Game ID",
        font=('calibre', 10, 'bold')
    )
    belongGameInput = Entry(
        MapCreationWindow,
        width=50
    )
    submitButton = Button(
        MapCreationWindow,
        text="Submit",
        width=25,
        height=5,
        bg="cyan",
        command=submitData
    )
    clearAll = Button(
        MapCreationWindow,
        text="Clear all",
        width=25,
        height=5,
        bg="red",
        command=clearInput
    )

    title.grid(row=0,column=1)
    nameLabel.grid(row=1,column=0)
    nameInput.grid(row=1,column=1)
    mapWidthLabel.grid(row=2,column=0)
    mapWidthInput.grid(row=2,column=1)
    mapHeightLabel.grid(row=3,column=0)
    mapHeightInput.grid(row=3,column=1)
    belongGameLabel.grid(row=4,column=0)
    belongGameInput.grid(row=4,column=1)
    submitButton.grid(row=5,column=1)
    clearAll.grid(row=6,column=1)
    MapCreationWindow.mainloop()


def openItemCreationWindow():
    def clearInput():
        nameInput.delete(0, 'end')
        itemTypeInput.delete(0, 'end')
        stackableInput.delete(0, 'end')
        belongMapInput.delete(0, 'end')
    def submitData():
        itemName = nameInput.get()
        itemType = itemTypeInput.get()
        stackable = stackableInput.get()
        belongMap = belongMapInput.get()
        try:
            itemName[0]
        except IndexError:
            return messagebox.showerror('Error', "Name can not be empty")
        try:
            int(belongMap)
        except ValueError:
            return messagebox.showerror('Error', "MapID must be integer")
        if stackable not in ["Y", "y", "N", "n"]:
            return messagebox.showerror('Error', "Stackable input must be either Y, y, N, n")
        return insertItemIntoMap(itemName, itemType, stackable, belongMap)
        return messagebox.showinfo('message', itemName + " " + itemType + " " + stackable + " " + belongMap)

    ItemCreationWindow = Tk()
    ItemCreationWindow.title("Item Creation Window")
    ItemCreationWindow.geometry("450x290")

    title = Label(
        master=ItemCreationWindow,
        text="Item Creation"
    )
    nameLabel = Label(
        ItemCreationWindow,
        text="Item Name",
        font=('calibre', 10, 'bold')
    )
    nameInput = Entry(
        ItemCreationWindow,
        width=50
    )
    itemTypeLabel = Label(
        ItemCreationWindow,
        text="Item Type",
        font=('calibre', 10, 'bold')
    )
    itemTypeInput = Entry(
        ItemCreationWindow,
        width=50
    )
    stackableLabel = Label(
        ItemCreationWindow,
        text="Stackable (Y/N)",
        font=('calibre', 10, 'bold')
    )
    stackableInput = Entry(
        ItemCreationWindow,
        width=50
    )
    belongMapLabel = Label(
        ItemCreationWindow,
        text="Game ID",
        font=('calibre', 10, 'bold')
    )
    belongMapInput = Entry(
        ItemCreationWindow,
        width=50
    )
    submitButton = Button(
        ItemCreationWindow,
        text="Submit",
        width=25,
        height=5,
        bg="cyan",
        command=submitData
    )
    clearAll = Button(
        ItemCreationWindow,
        text="Clear all",
        width=25,
        height=5,
        bg="red",
        command=clearInput
    )

    title.grid(row=0,column=1)
    nameLabel.grid(row=1,column=0)
    nameInput.grid(row=1,column=1)
    itemTypeLabel.grid(row=2,column=0)
    itemTypeInput.grid(row=2,column=1)
    stackableLabel.grid(row=3,column=0)
    stackableInput.grid(row=3,column=1)
    belongMapLabel.grid(row=4,column=0)
    belongMapInput.grid(row=4,column=1)
    submitButton.grid(row=5,column=1)
    clearAll.grid(row=6,column=1)
    ItemCreationWindow.mainloop()


def openInsertCharacterGameWindow():
    def clearInput():
        championIdInput.delete(0, 'end')
        gameIdInput.delete(0, 'end')
    def submitData():
        championId = championIdInput.get()
        gameId = gameIdInput.get()
        try:
            int(championId)
        except ValueError:
            return messagebox.showerror('Error', "Champion ID must have integer value")
        try:
            int(gameId)
        except ValueError:
            return messagebox.showerror('Error', "Game ID must have integer value")
        return insertChampionIntoGame(championId, gameId)
        return messagebox.showinfo('message', "name: %s, type: %s" % (championId, gameId))

    insertCharacterGameWindow = Tk()
    insertCharacterGameWindow.title("Insert Character into Game Window")
    insertCharacterGameWindow.geometry("400x250")

    title = Label(
        master=insertCharacterGameWindow,
        text="Character Creation"
    )
    championIdLabel = Label(
        insertCharacterGameWindow,
        text="Champion ID",
        font=('calibre', 10, 'bold')
    )
    championIdInput = Entry(
        insertCharacterGameWindow,
        width=50
    )
    gameIdLabel = Label(
        insertCharacterGameWindow,
        text="Game ID",
        font=('calibre', 10, 'bold')
    )
    gameIdInput = Entry(
        insertCharacterGameWindow,
        width=50
    )
    submitButton = Button(
        insertCharacterGameWindow,
        text="Submit",
        width=25,
        height=5,
        bg="cyan",
        command=submitData
    )
    clearAll = Button(
        insertCharacterGameWindow,
        text="Clear all",
        width=25,
        height=5,
        bg="red",
        command=clearInput
    )

    title.grid(row=0,column=1)
    championIdLabel.grid(row=1,column=0)
    championIdInput.grid(row=1,column=1)
    gameIdLabel.grid(row=2,column=0)
    gameIdInput.grid(row=2,column=1)
    submitButton.grid(row=3,column=1)
    clearAll.grid(row=4,column=1)
    insertCharacterGameWindow.mainloop()


def openDisplayTableInput():
    global databaseCursor
    displayTableInputWindow = Tk()
    displayTableInputWindow.title("Find Table")
    def clearInput():
        tableInput.delete(0, 'end')
    def showTable():
        displayTableWindow = Tk()
        displayTableWindow.geometry("1300x1080")
        displayTableWindow.title("Result")
        tableName = (tableInput.get(),)
        command = (
            "DESCRIBE %s;" % (tableName)
        )
        try:
            databaseCursor.execute(command)
        except mysql.connector.errors.ProgrammingError as error:
            return messagebox.showwarning("Warning", error)
        
        att = []
        for i in [*databaseCursor]:
            att.extend([i[0]])
        for j in range(len(att)):
            e=Label(displayTableWindow,width=30,text=att[j],borderwidth=2, relief='ridge',anchor='w',bg='yellow')
            e.grid(row=0,column=j)

        command = (
            "SELECT * from %s;" % (tableName)
        )
        try:
            databaseCursor.execute(command)
        except mysql.connector.errors.ProgrammingError as error:
            return messagebox.showwarning("Warning", error)
        i = 1
        for _publisher in databaseCursor:
            for j in range(len(_publisher)):
                e = Entry( displayTableWindow, width=35, fg='blue')
                e.grid(row=i, column=j)
                if _publisher[j] == None:
                    e.insert('end', "NULL")
                    continue
                e.insert('end', _publisher[j])
            i = i + 1
        displayTableWindow.mainloop()

    tableLabel = Label(
        displayTableInputWindow,
        text="Table Name",
        font=('calibre', 10, 'bold')
    )
    tableInput = Entry(
        displayTableInputWindow,
        width=50
    )
    showTableButton = Button(
        displayTableInputWindow,
        text="Show Table",
        width=25,
        height=5,
        bg="cyan",
        command=showTable
    )
    clearAll = Button(
        displayTableInputWindow,
        text="Clear all",
        width=25,
        height=5,
        bg="red",
        command=clearInput
    )
    tableLabel.grid(row=0, column=0)
    tableInput.grid(row=0, column=1)
    showTableButton.grid(row=1, column=1)
    clearAll.grid(row=2,column=1)
    displayTableInputWindow.mainloop()

#==========Main===================

# Master window function
def master():
    if not userCheck: #userCheck == False means not login yet!
        return
        
    window = Tk()
    window.title("Main Window")
    window.geometry("700x630")

    title = Label(
        text="Game Management",
    )
    newCharacterButton = Button(
        window,
        text="Create New Character",
        width=25,
        height=5,
        bg="lime",
        command=openCharacterCreationWindow
    )
    newWeaponButton = Button(
        window,
        text="Create New Weapon",
        width=25,
        height=5,
        bg="pink",
        command=openWeaponCreationWindow
    )
    newGameButton = Button(
        window,
        text="Create New Game",
        width=25,
        height=5,
        bg="yellow",
        command=openGameCreationWindow
    )
    newMapButton = Button(
        window,
        text="Create New Map",
        width=25,
        height=5,
        bg="#28B463",
        command=openMapCreationWindow
    )
    insertItem = Button(
        window,
        text="Insert Item Into Map",
        width=25,
        height=5,
        bg="#F39C12",
        command=openItemCreationWindow
    )
    insertCharacterInGameButton = Button(
        window,
        text="Insert Champion Into Game",
        width=25,
        height=5,
        bg="orchid",
        command=openInsertCharacterGameWindow
    )
    displayPublisherButton = Button(
        window,
        text="Find Table",
        width=25,
        height=5,
        bg="#33FFC1",
        command=openDisplayTableInput
    )

    #==== Pack site ====
    title.pack()
    newGameButton.pack(fill=X)
    newMapButton.pack(fill=X)
    newCharacterButton.pack(fill=X)
    newWeaponButton.pack(fill=X)
    insertItem.pack(fill=X)
    insertCharacterInGameButton.pack(fill=X)
    displayPublisherButton.pack(fill=X)

    #==== End of pack site ====
    window.mainloop()
    database.close()
    databaseCursor.close()

#========END OF MAIN=========


#========LOGIN===============
def loginWindowFunction():
    def existUser(username, password):
        return username in users and users[username] == password
    def getInput():
        global users, database, databaseCursor, userCheck
        username = usernameInput.get()
        password = passwordInput.get()
        if existUser(username, password):
            database = initializeDatabase(username, password)
            databaseCursor = database.cursor()
            logWindow.destroy()
            userCheck = True
            return messagebox.showinfo("Infomation", "Successfully login!")
        return messagebox.showwarning("Warning", "Username or Password is not correct!")

    logWindow = Tk()
    logWindow.title("Login Window")
    usernameLabel = Label(
        logWindow,
        text="Username",
        font=('calibre', 10, 'bold')
    )
    usernameInput = Entry(
        logWindow,
        width=50
    )
    passwordLabel = Label(
        logWindow,
        text="Password",
        font=('calibre', 10, 'bold')
    )
    passwordInput = Entry(
        logWindow,
        show="*",
        width=50
    )
    submitButton = Button(
        logWindow,
        text="Submit",
        width=25,
        height=5,
        bg="cyan",
        command=getInput
    )
    usernameLabel.grid(row=0,column=0)
    usernameInput.grid(row=0,column=1)
    passwordLabel.grid(row=1,column=0)
    passwordInput.grid(row=1,column=1)
    submitButton.grid(row=2,column=1)
    logWindow.mainloop()
#========END OF LOGIN==========