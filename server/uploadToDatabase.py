import credentials
import mysql.connector

def getHousingData():
    housingData = []
    # Note: You will need to replace this with the path to the dataset on your machine.
    file = open("./datasets/finalDataSet.csv", "r")
    for line in file:
        if line.split(",")[0] != "address":
            house = {}
            houseList = line.split(",")
            if len(houseList) == 12:
                house["address"] = houseList[0]
            else:
                house["address"] = ",".join(houseList[0:len(houseList) - 11]).replace('"', '')
            house["city"] = houseList[-11]
            house["state"] = houseList[-10]
            house["zipCode"] = int(houseList[-9])
            house["latitude"] = float(houseList[-8])
            house["longitude"] = float(houseList[-7])
            house["numberOfRooms"] = int(houseList[-6])
            house["squareFeet"] = int(houseList[-5])
            house["price"] = int(houseList[-4])
            house["distanceFromPublicTransportation"] = float(houseList[-3])
            house["distanceFromWholeFoods"] = float(houseList[-2])
            house["distanceFromParks"] = float(houseList[-1])
            housingData.append(house)
    return housingData

# This is to initialize the housing data and put it into a list of objects.
housingData = getHousingData()

cnx = mysql.connector.connect(user=credentials.mysqlUsername, password=credentials.mysqlPassword,
host=credentials.mysqlEndpoint,database="cmpe272")
cursor = cnx.cursor()

add_house = ("INSERT INTO cmpe272.housing "
            "(idhousing, address, city, state, zip_code, latitude, longitude, num_rooms, square_feet, price, "
            "transportation_distance, grocery_distance, parks_distance) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

i = 0
for house in housingData:
    print("Inserting row: {}".format(i))
    data_house = (i, house["address"], house["city"], house["state"], house["zipCode"], house["latitude"], 
    house["longitude"], house["numberOfRooms"], house["squareFeet"], house["price"], 
    house["distanceFromPublicTransportation"], house["distanceFromWholeFoods"], house["distanceFromParks"])
    print(data_house)
    cursor.execute(add_house, data_house)
    i += 1

cnx.commit()
cursor.close()
cnx.close()