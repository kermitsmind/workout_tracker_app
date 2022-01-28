#### importing libraries
from fileinput import hook_compressed
from timeit import repeat
from turtle import distance
import database_operations
import random

#### get root and superUser password from file
passwordFile_1 = open(
    "/Users/michal/Documents/Study/MSc/Semester II/Complex systems theory and practice/projectRootPassword"
)
passwordFile_2 = open(
    "/Users/michal/Documents/Study/MSc/Semester II/Complex systems theory and practice/projectSuperuserPassword"
)
rootPassword = passwordFile_1.readline()[:-1]
superUserPassword = passwordFile_2.readline()[:-1]


def main():

    dateList = [
        "2022-01-17",
        "2022-01-17",
        "2022-09-27",
        "2022-01-27",
        "2021-08-12",
        "2021-09-18",
        "2022-01-15",
        "2021-05-07",
        "2022-01-28",
        "2021-04-27",
        "2021-10-22",
        "2022-01-07",
        "2021-06-27",
        "2021-01-30",
        "2021-07-07",
        "2021-04-23",
        "2022-01-14",
        "2021-08-18",
        "2021-03-14",
    ]

    userList = [1, 2, 3, 4, 5, 6, 7, 8]

    typeList = ["sprint", "interval", "xD", "HAHA"]

    timeList = ["123", "5683", "2234", "1222", "0098", "1200"]

    distanceList = ["2233", "449", "3339", "9008", "209", "7800"]

    terrainList = ["outdoor", "indoor"]

    repeatsList = ["33", "12", "10", "8", "20"]

    weightList = ["90", "200", "100", "60", "80"]

    nameList = ["xd", "ppp", "wwww", "hahahah"]

    caloriesList = ["2000", "3000", "10000"]

    hoursList = ["12", "10", "9", "8", "7"]

    #### open connenction as super user
    connection = database_operations.openConnectionToDB(
        host="localhost",
        user="super_user",
        password=superUserPassword,
        database="WorkoutTrackerDB",
    )

    mycursor = connection.cursor(prepared=True)

    # ### add sample user
    # database_operations.createUser(firstName="Adam", lastName="Smith", birthDate="1998-03-12", phoneNumber=123456789, nationality="Polish", registrationDate="2011-12-12", userPassword="user_1_password", rootPassword=rootPassword)
    # database_operations.createUser(firstName="John", lastName="Wynn", birthDate="1997-09-11", phoneNumber=123456789, nationality="Polish", registrationDate="2011-12-12", userPassword="user_2_password", rootPassword=rootPassword)

    for i in range(30):
        ### add sample record to running
        database_operations.addRecordToRunningTable(
            connection=connection,
            cursor=mycursor,
            person_id=random.choice(userList),
            date=random.choice(dateList),
            type=random.choice(typeList),
            total_time=random.choice(timeList),
            total_distance=random.choice(distanceList),
            terrain=random.choice(terrainList),
        )

        ### add sample record to swimming
        database_operations.addRecordToSwimmingTable(
            connection=connection,
            cursor=mycursor,
            person_id=random.choice(userList),
            date=random.choice(dateList),
            type=random.choice(typeList),
            total_time=random.choice(timeList),
            total_distance=random.choice(distanceList),
            water=random.choice(terrainList),
        )

        ### add sample record to diet
        database_operations.addRecordToDietTable(
            connection=connection,
            cursor=mycursor,
            person_id=random.choice(userList),
            name=random.choice(nameList),
            start_date=random.choice(dateList),
            stop_date=random.choice(dateList),
            calories=random.choice(caloriesList),
        )

        ### add sample record to weight lifting
        database_operations.addRecordToWeightLiftingTable(
            connection=connection,
            cursor=mycursor,
            person_id=random.choice(userList),
            date=random.choice(dateList),
            type=random.choice(typeList),
            no_series=random.choice(repeatsList),
            repeats_per_series=random.choice(repeatsList),
            weight=random.choice(weightList),
        )

        ### add sample record to rest
        database_operations.addRecordToRestTable(
            connection=connection,
            cursor=mycursor,
            person_id=random.choice(userList),
            date=random.choice(dateList),
            night_sleep_hours=random.choice(hoursList),
            relax_hours=random.choice(hoursList),
        )

    database_operations.closeConnectionToDB(connection=connection)


if __name__ == "__main__":
    main()
