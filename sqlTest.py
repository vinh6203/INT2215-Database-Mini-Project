import mysql.connector
import tkinter.messagebox as messagebox

def initializeDatabase(username="vscode_user_pass1234", password="1234", _host="localhost"):
    try:
        dataBase = mysql.connector.connect(
            host = _host,
            user = username,
            passwd = password
        )
    except mysql.connector.errors.DatabaseError:
        return messagebox.showerror('Error', 'Cannot connect to SQL database, please exit the program')
    return dataBase
    raise NotImplementedError

users = {"vscode_user_pass1234" : "1234"}
userCheck = False
database = initializeDatabase()
databaseCursor = database.cursor()
databaseCursor.execute("USE gamemanagementdb;")

def insertChampion(championName, championType):
    global database, databaseCursor
    try:
        insert_statement = (
          "INSERT INTO champion (championName, championType) "
          "VALUES (%s, %s)"
        )
        data = (championName, championType,)
        databaseCursor.execute(insert_statement, data)
        database.commit()
    except (mysql.connector.errors.ProgrammingError, mysql.connector.IntegrityError) as error:
        return messagebox.showwarning('Warning', error)
    return messagebox.showinfo('Info', 'Successfully insert Champion')
    raise NotImplementedError


def insertWeapon(weaponName, weaponAttack, weaponDefend, championID):
    global database, databaseCursor
    try:
        insert_statement = (
          "INSERT INTO weapon (weaponName, attackStats, defendStats, championID)"
          "VALUES (%s, %s, %s, %s)"
        )
        data = (weaponName, weaponAttack, weaponDefend, championID,)
        databaseCursor.execute(insert_statement, data)
        database.commit()
    except (mysql.connector.errors.ProgrammingError, mysql.connector.IntegrityError) as error:
        return messagebox.showwarning('Warning', error)
    return messagebox.showinfo('Info', 'Successfully insert Weapon')
    raise NotImplementedError


def insertGame(gameName, multiplayer, price, publisherID):
    global database, databaseCursor
    if multiplayer == "Y" or multiplayer == "y":
        multiplayer = 1
    else:
        multiplayer = 0
    try:
        insert_statement = (
          "INSERT INTO game (gameName, multiplayer, price, publisherID)"
          "VALUES (%s, %s, %s, %s)"
        )
        data = (gameName, multiplayer, price, publisherID,)
        databaseCursor.execute(insert_statement, data)
        database.commit()
    except (mysql.connector.errors.ProgrammingError, mysql.connector.IntegrityError) as error:
        return messagebox.showwarning('Warning', error)
    return messagebox.showinfo('Info', 'Successfully insert Game')
    raise NotImplementedError


def insertMap(mapName, height, width, gameID):
    global database, databaseCursor
    try:
        insert_statement = (
          "INSERT INTO map (gameID, mapName, width, height)"
          "VALUES (%s, %s, %s, %s)"
        )
        data = (gameID, mapName, width, height,)
        databaseCursor.execute(insert_statement, data)
        database.commit()
    except (mysql.connector.errors.ProgrammingError, mysql.connector.IntegrityError) as error:
        return messagebox.showwarning('Warning', error)
    return messagebox.showinfo('Info', 'Successfully insert Map')
    raise NotImplementedError


def insertItemIntoMap(itemName, itemType, stackable, mapID):
    global database, databaseCursor
    if stackable == "Y" or stackable == "y":
        stackable = 1
    else:
        stackable = 0
    try:
        insert_statement = (
          "INSERT INTO item (mapID, stackable, itemType, itemName)"
          "VALUES (%s, %s, %s, %s)"
        )
        data = (mapID, stackable, itemType, itemName,)
        databaseCursor.execute(insert_statement, data)
        database.commit()
    except (mysql.connector.errors.ProgrammingError, mysql.connector.IntegrityError) as error:
        return messagebox.showwarning('Warning', error)
    return messagebox.showinfo('Info', 'Successfully insert Item')
    raise NotImplementedError


def insertChampionIntoGame(championId, gameId):
    global database, databaseCursor
    try:
        insert_statement = (
          "INSERT INTO championlist (championID, gameID)"
          "VALUES (%s, %s)"
        )
        data = (championId, gameId,)
        databaseCursor.execute(insert_statement, data)
        database.commit()
    except (mysql.connector.errors.ProgrammingError, mysql.connector.IntegrityError) as error:
        return messagebox.showwarning('Warning', error)
    return messagebox.showinfo('Info', 'Successfully insert Champion into Game')
    raise NotImplementedError