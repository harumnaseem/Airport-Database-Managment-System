from PyInquirer import style_from_dict, Token, prompt
import mysql.connector
from examples import custom_style_2
import pyfiglet 
from datetime import date
from prettytable import PrettyTable

def main():
    print("""\n\n
                                                                                
:+ossssso+:-`                                               `hMNo                                   
NN//:://+oshmmy/`                                           yMMMM+                                  
oMo..........-+yNh/                                        .MMMMMN.                                 
 mN-............-omm:                                      +MMMMMMh                                 
 :Mhoo+/:-........-yMo                                     hMMMmhhM/                                
  .:/+osyhmNmo....-hN/                                     mN/-..-Nm`                               
         /mm/....:mm-                                      Md.....+Mo                               
       `dNo.....-dMo`                                     `Mh......dN`                              
        odmy+-..../dNs`                      `+mmmNd:/+oshdNy....../My                              
          `/yMdo++oodM+                     /Nm/::/dNso+/:-.........sdmhs/.                         
           .hMmhhhhmN/                    -dN+....-N/..................:+ymmy/`                     
          oMNdhhhhdMs                 `/ydNN:.....sd.......................-+yNhooooo+++/::-`       
         /MMmhhhhhhhNm/            `+dNmy---......do........./yhy:............-++++++++oyMMMMMmhs/` 
          .+dMNmdhhhhdNm+`      `/hMy/sh/.........:-.....::-:MMM:y....................../MMMMMMMMMMy
             .+dMMNdhhhhmNh+. -yNmdo..:y-...............shhy-yNMmo......................oMMMMMMMMMmo
                -dMMMNNNNNNNMNms-:y-...-................:+o:......................ohhhhhNMNmdhs+:`  
              -dNy/:-...-:sNs:....-.............................::...........:++-./My.```           
              yM/.............................................../m:...:my-..om:mM+.Nm               
              .ymdhyyyyhho.......................................yNdyyy+....oMMMM+.mM               
                 `..--..mN:......................................dmhhhdNs:/:.-+o/..dM               
                        `yNy:....................................sNdhhhmNso:.-hhh+.NN/`             
                          .oNm-.................................../shhyo-...../o+-/NoNm.            
                            +Ms..................................................-mo./Md            
                             /Nh:.............................................../mo.-oNm`           
                              .hMy-...........................................:hMyhmms:             
                             `yNhsdy:.....................................:+sdNho/-`                
                             dN:.../yhs/.............................-+ydmhs/-                      
                             /hmddddddNNmmhso+:--............--/+oydmds/.                           
                                          .:+oyhddddddddddddddhso/:.      


     """)
    ascii_banner = pyfiglet.figlet_format("Pikachu Airline Database")
    print(ascii_banner)
    
    options_prompt = {
        'type': 'list',
        'name': 'AdminOrReceptionist',
        'message': 'Do you want to login as Admin or Receptionist?',
        'choices': ['Admin', 'Receptionist']
    }

    answer = prompt(options_prompt,style = custom_style_2)
    if answer['AdminOrReceptionist'] == 'Admin':
        print('Welcome Admin, please enter your username and password to have access.\n')
        access = False
        while access == False:
            Admin_prompt1 = {
                'type' : 'input',
                'name' : 'ID',
                'message' : 'Enter your ID:'
            }
            answer1 = prompt(Admin_prompt1, style = custom_style_2)
            AdminIDAnswer = answer1['ID']
            try:
                IntAdminID = int(AdminIDAnswer)
            except:
                print('ID cannot have characters. Try again. \n')
                continue

            Admin_prompt2 = {
                'type' : 'password',
                'name' : 'Pass',
                'message': 'Enter your password'
            }

            answer2 = prompt(Admin_prompt2, style = custom_style_2)
            AdminPasswordAnswer = answer2['Pass']

            mydb = mysql.connector.connect(
               host = "localhost",
                user = "root",
                passwd = "dumbshit"
            )

            mycursor = mydb.cursor()
            mycursor.execute("Use Airline")
            mycursor.execute("Select * from Admins")
            

            for data in mycursor:
                if data[0] == int(AdminIDAnswer):
                    if data[2] == AdminPasswordAnswer:
                        access = True
                        print(data[1], ', you have been granted access.\n')
                        

            if access == False:
                print('Access denied. Incorrect ID/Password.\n')
                continue


            Admin_Display_Prompt = {
                'type' : 'list',
                'name' : 'choice',
                'message' : 'What do you want to do?',
                'choices' : ['Add a new flight record.','Update details of an exisiting flight record.', 'Cancel a particular flight record.', 'View all flights landing and taking off for a particular airport today.', 'View every table of the database in tabular form.', 'Exit the Airline Database Management System.']
            }


            while 1:
                answer = prompt(Admin_Display_Prompt, style = custom_style_2)
                answer = answer['choice']
                if answer == 'Exit the Airline Database Management System.':
                    print('Exiting...\n')
                    break
                elif answer == 'View all flights landing and taking off for a particular airport today.':
                    prompt_airport = {
                        'type' : 'input',
                        'name' : 'airport',
                        'message' : 'Enter the name of the airport: '
                    }

                    airportname = prompt(prompt_airport, style = custom_style_2)
                    airportname = airportname['airport']

                    dateToday = date.today()
                    dateToday = dateToday.strftime('%Y-%m-%d')

                    query = 'Select * from Flights where (Source = \'' + airportname + '\' or Destination = \'' + airportname + '\') and DepartureDate = \'' + dateToday + '\''
                    
                    mycursor.execute(query)
                    
                    table = PrettyTable()
                    table.field_names = ["Flight ID", "Source", "Destination", "Departure Time", "Arrival Time", "Departure Date", "Arrival Date", "Aircraft", "Fare"]
                    count = 0
                    for x in mycursor:
                        table.add_row(x)
                        count = count + 1
                    if count == 0:
                        print('No flight is landing/leaving this airport today.')
                    else:
                        print(table)
                elif answer == 'Cancel a particular flight record.':
                    prompt_updateFlight1 = {
                        'type' : 'input', 
                        'name' :'FID',
                        'message' : 'Enter the flight ID: '
                    }

                    flightID = prompt(prompt_updateFlight1, style = custom_style_2)
                    flightID = flightID['FID']

                    query = 'Select * from Flights'
                    mycursor.execute(query)
                    u = False
                    for x in mycursor:
                        if x[0] == flightID:
                            u = True
                    if u == False:
                        print('No flight with this ID exists. \n')
                        continue

                    query = 'Delete from Flights where FlightID = \'' + flightID + '\''
                    mycursor.execute(query)
                    mydb.commit()
                    print('Flight has been deleted from the database. \n')
                elif answer == 'Add a new flight record.':
                    prompt_newFlight1 = {
                        'type' : 'input',
                        'name' : 'FID',
                        'message' : 'Enter the flight ID: '
                    }
                    while True:
                        flightID = prompt(prompt_newFlight1, style = custom_style_2)
                        flightID = flightID['FID']
                        query = ("Select * from Flights")
                        mycursor.execute(query)
                        chk = True
                        for x in mycursor:
                            if x[0] == flightID:
                                print('A flight with this ID already exists. \n')
                                chk = False
                        if chk == True:
                            break
                    k = False
                    flightSource = ''
                    while k == False:
                        prompt_newFlight2 = {
                            'type' : 'input', 
                            'name' : 'S',
                            'message' : 'Enter the source location: '
                        }

                        flightSource = prompt(prompt_newFlight2, style = custom_style_2)
                        flightSource = flightSource['S']
                        u = False
                        for x in flightSource:
                            try:
                                int(x)
                                print('Source location cannot have a digit. \n')
                                u = True
                                break
                            except:
                                continue
                        if u == True:
                            continue
                        else:
                            break
                    k = False
                    flightDestination = ''
                    while k == False:
                        prompt_newFlight3 = {
                            'type' : 'input', 
                            'name' : 'D',
                            'message' : 'Enter the destination location: '
                        }

                        flightDestination = prompt(prompt_newFlight3, style = custom_style_2)
                        flightDestination = flightDestination['D']
                        u = False
                        for x in flightDestination:
                            try:
                                int(x)
                                print('Destination location cannot have a digit. \n')
                                u = True
                                break
                            except:
                                continue
                        if u == True:
                            continue
                        else:
                            break
                    departureTime = ''
                    k = False
                    while k == False:
                        print('Format must be hh:mm:ss')
                        prompt_newFlight4 = {
                            'type' : 'input', 
                            'name' : 'DT',
                            'message' : 'Enter the departure time: '
                        }

                        departureTime = prompt(prompt_newFlight4, style = custom_style_2)
                        departureTime = departureTime['DT']
                        if len(departureTime) != 8:
                            print('Incorrect format. \n')
                            continue
                        count = 0
                        u = False
                        for x in departureTime:
                            if count == 2 or count == 5:
                                if x != ':':
                                    print('Incorrect format. \n')
                                    u = True
                                    break
                            else:
                                try:
                                    int(x)
                                except:
                                    print('Incorrect format. \n')
                                    u = True
                                    break
                            count = count + 1
                        if u == True:
                            continue
                        else:
                            break
                    k = False
                    arrivalTime = ''
                    while k == False:
                        print('Format must be hh:mm:ss')
                        prompt_newFlight5 = {
                            'type' : 'input', 
                            'name' : 'AT',
                            'message' : 'Enter the arrival time: '
                        }

                        arrivalTime = prompt(prompt_newFlight5, style = custom_style_2)
                        arrivalTime = arrivalTime['AT']
                        if len(arrivalTime) != 8:
                            print('Incorrect format. \n')
                            continue
                        count = 0
                        u = False
                        for x in arrivalTime:
                            if count == 2 or count == 5:
                                if x != ':':
                                    print('Incorrect formattt. \n')
                                    u = True
                                    break
                            else:
                                try:
                                    int(x)
                                except:
                                    print('Incorrect format. \n')
                                    u = True
                                    break
                            count = count + 1
                        if u == True:
                            continue
                        else:
                            break

                    k = False
                    departureDate = ''
                    while k == False:
                        print('Format must be yyyy-mm-dd')
                        prompt_newFlight6 = {
                            'type' : 'input',
                            'name' : 'DD',
                            'message' : 'Enter the departure date: '
                        }

                        departureDate = prompt(prompt_newFlight6, style = custom_style_2)
                        departureDate = departureDate['DD']
                        if len(departureDate) != 10:
                            print('Incorrect format. \n')
                            continue
                        count = 0
                        u = False
                        for x in departureDate:
                            if count == 4 or count == 7:
                                if x != '-':
                                    print('Incorrect format. \n')
                                    u = True
                                    break
                            else: 
                                try:
                                    int(x)
                                except:
                                    print('Incorrect format. \n')
                                    u = True
                                    break
                            
                            count = count + 1
                        if u == True:
                            continue
                        else:
                            break
                    k = False
                    arrivalDate = ''
                    while k == False:
                        print('Format must be yyyy-mm-dd')
                        prompt_newFlight7 = {
                            'type' : 'input',
                            'name' : 'AD',
                            'message' : 'Enter the arrival date: '
                        }

                        arrivalDate  = prompt(prompt_newFlight7, style = custom_style_2)
                        arrivalDate  = arrivalDate['AD']
                        if len(arrivalDate) != 10:
                            print('Incorrect format. \n')
                            continue
                        count = 0
                        u = False
                        for x in arrivalDate:
                            if count == 4 or count == 7:
                                if x != '-':
                                    print('Incorrect format. \n')
                                    u = True
                                    break
                            else: 
                                try:
                                    int(x)
                                except:
                                    print('Incorrect format. \n')
                                    u = True
                                    break
                            
                            count = count + 1
                        if u == True:
                            continue
                        else:
                            break
                    prompt_newFlight8 = {
                        'type' : 'input',
                        'name' : 'AC',
                        'message' : 'AirCraft: '
                    }

                    aircraft = prompt(prompt_newFlight8, style = custom_style_2)
                    aircraft = aircraft['AC']
                    fare = ''
                    k = False
                    while k == False:
                        prompt_newFlight9 = {
                            'type' : 'input',
                            'name' : 'FC',
                            'message' : 'Fare: '
                        }

                        fare = prompt(prompt_newFlight9, style = custom_style_2)
                        fare = fare['FC']
                        u = False
                        for x in fare:
                            try:
                                int(x)
                            except:
                                print('Fare cannot have characters. \n')
                                u = True
                                break
                        if u == True:
                            continue
                        else:
                            fare = int(fare)
                            break
                    y = (flightID, flightSource, flightDestination, departureTime, arrivalTime, departureDate, arrivalDate, aircraft, fare)
                    query = 'Insert into Flights values ' + str(y)

                    mycursor.execute(query)
                    mydb.commit()

                    print('Flight record has been added.') 
                elif answer == 'Update details of an exisiting flight record.':
                    prompt_updateFlight1 = {
                        'type' : 'input', 
                        'name' :'FID',
                        'message' : 'Enter the flight ID: '
                    }

                    flightID = prompt(prompt_updateFlight1, style = custom_style_2)
                    flightID = flightID['FID']

                    query = 'Select * from Flights'
                    mycursor.execute(query)
                    u = False
                    for x in mycursor:
                        if x[0] == flightID:
                            u = True
                    if u == False:
                        print('No flight with this ID exists. \n')
                        continue

                    while 1:
                        promptChoice = {
                            'type' : 'list',
                            'name' : 'updateChoice',
                            'message' : 'What do you want to update?',
                            'choices' : ['Source Airport', 'Destination Airport', 'Departure Time', 'Arrival Time', 'Departure Date', 'Arrival Date', 'Aircraft', 'Fare', 'Nothing/Exit']
                        }

                        choice = prompt(promptChoice, style = custom_style_2)
                        choice = choice['updateChoice']
                        if choice == 'Nothing/Exit':
                            break
                        elif choice == 'Source Airport':
                            k = False
                            flightSource = ''
                            while k == False:
                                prompt_newFlight2 = {
                                    'type' : 'input', 
                                    'name' : 'S',
                                    'message' : 'Enter the new source location: '
                                }

                                flightSource = prompt(prompt_newFlight2, style = custom_style_2)
                                flightSource = flightSource['S']
                                u = False
                                for x in flightSource:
                                    try:
                                        int(x)
                                        print('Source location cannot have a digit. \n')
                                        u = True
                                        break
                                    except:
                                        continue
                                if u == True:
                                    continue
                                else:
                                    break
                            query = 'Update Flights set Source = \'' + flightSource + '\' where FlightID = \'' + flightID + '\''
                            mycursor.execute(query)
                            mydb.commit()
                        elif choice == 'Destination Airport':
                            k = False
                            flightDestination = ''
                            while k == False:
                                prompt_newFlight2 = {
                                    'type' : 'input', 
                                    'name' : 'D',
                                    'message' : 'Enter the new destination location: '
                                }

                                flightDestination = prompt(prompt_newFlight2, style = custom_style_2)
                                flightDestination = flightDestination['D']
                                u = False
                                for x in flightDestination:
                                    try:
                                        int(x)
                                        print('Destination location cannot have a digit. \n')
                                        u = True
                                        break
                                    except:
                                        continue
                                if u == True:
                                    continue
                                else:
                                    break
                            query = 'Update Flights set Destination = \'' + flightDestination + '\' where FlightID = \'' + flightID + '\''
                            mycursor.execute(query)
                            mydb.commit()
                        elif choice == 'Departure Time':
                            departureTime = ''
                            k = False
                            while k == False:
                                print('Format must be hh:mm:ss')
                                prompt_newFlight4 = {
                                    'type' : 'input', 
                                    'name' : 'DT',
                                    'message' : 'Enter the new departure time: '
                                }

                                departureTime = prompt(prompt_newFlight4, style = custom_style_2)
                                departureTime = departureTime['DT']
                                if len(departureTime) != 8:
                                    print('Incorrect format. \n')
                                    continue
                                count = 0
                                u = False
                                for x in departureTime:
                                    if count == 2 or count == 5:
                                        if x != ':':
                                            print('Incorrect format. \n')
                                            u = True
                                            break
                                    else:
                                        try:
                                            int(x)
                                        except:
                                            print('Incorrect format. \n')
                                            u = True
                                            break
                                    count = count + 1
                                if u == True:
                                    continue
                                else:
                                    break
                            query = 'Update Flights set DepartureTime = \'' + departureTime + '\' where FlightID = \'' + flightID + '\''
                            mycursor.execute(query)
                            mydb.commit()
                        elif choice == 'Arrival Time':
                            arrivalTime = ''
                            k = False
                            while k == False:
                                print('Format must be hh:mm:ss')
                                prompt_newFlight4 = {
                                    'type' : 'input', 
                                    'name' : 'DT',
                                    'message' : 'Enter the new arrival time: '
                                }

                                arrivalTime = prompt(prompt_newFlight4, style = custom_style_2)
                                arrivalTime = arrivalTime['DT']
                                if len(arrivalTime) != 8:
                                    print('Incorrect format. \n')
                                    continue
                                count = 0
                                u = False
                                for x in arrivalTime:
                                    if count == 2 or count == 5:
                                        if x != ':':
                                            print('Incorrect format. \n')
                                            u = True
                                            break
                                    else:
                                        try:
                                            int(x)
                                        except:
                                            print('Incorrect format. \n')
                                            u = True
                                            break
                                    count = count + 1
                                if u == True:
                                    continue
                                else:
                                    break  
                            query = 'Update Flights set ArrivalTime = \'' + arrivalTime + '\' where FlightID = \'' + flightID + '\''
                            mycursor.execute(query)
                            mydb.commit()
                        elif choice == 'Departure Date':
                            k = False
                            departureDate = ''
                            while k == False:
                                print('Format must be yyyy-mm-dd')
                                prompt_newFlight6 = {
                                    'type' : 'input',
                                    'name' : 'DD',
                                    'message' : 'Enter the new departure date: '
                                }

                                departureDate = prompt(prompt_newFlight6, style = custom_style_2)
                                departureDate = departureDate['DD']
                                if len(departureDate) != 10:
                                    print('Incorrect format. \n')
                                    continue
                                count = 0
                                u = False
                                for x in departureDate:
                                    if count == 4 or count == 7:
                                        if x != '-':
                                            print('Incorrect format. \n')
                                            u = True
                                            break
                                    else: 
                                        try:
                                            int(x)
                                        except:
                                            print('Incorrect format. \n')
                                            u = True
                                            break
                            
                                    count = count + 1
                                if u == True:
                                    continue
                                else:
                                    break
                            query = 'Update Flights set DepartureDate = \'' + departureDate + '\' where FlightID = \'' + flightID + '\''
                            mycursor.execute(query)
                            mydb.commit()
                        elif choice == 'Arrival Date':
                            k = False
                            arrivalDate = ''
                            while k == False:
                                print('Format must be yyyy-mm-dd')
                                prompt_newFlight6 = {
                                    'type' : 'input',
                                    'name' : 'DD',
                                    'message' : 'Enter the new arrival date: '
                                }

                                arrivalDate = prompt(prompt_newFlight6, style = custom_style_2)
                                arrivalDate = arrivalDate['DD']
                                if len(arrivalDate) != 10:
                                    print('Incorrect format. \n')
                                    continue
                                count = 0
                                u = False
                                for x in arrivalDate:
                                    if count == 4 or count == 7:
                                        if x != '-':
                                            print('Incorrect format. \n')
                                            u = True
                                            break
                                    else: 
                                        try:
                                            int(x)
                                        except:
                                            print('Incorrect format. \n')
                                            u = True
                                            break
                            
                                    count = count + 1
                                if u == True:
                                    continue
                                else:
                                    break
                            query = 'Update Flights set ArrivalDate = \'' + arrivalDate + '\' where FlightID = \'' + flightID + '\''
                            mycursor.execute(query)
                            mydb.commit()
                        elif choice == 'Aircraft':
                            prompt_newFlight8 = {
                                'type' : 'input',
                                'name' : 'AC',
                                'message' : 'AirCraft: '
                            }

                            aircraft = prompt(prompt_newFlight8, style = custom_style_2)
                            aircraft = aircraft['AC']
                            query = 'Update Flights set AirCraft = \'' + aircraft + '\' where FlightID = \'' + flightID + '\''
                            mycursor.execute(query)
                            mydb.commit()
                        elif choice == 'Fare':
                            k = False
                            while k == False:
                                prompt_newFlight9 = {
                                    'type' : 'input',
                                    'name' : 'FC',
                                    'message' : 'Fare: '
                                }

                                fare = prompt(prompt_newFlight9, style = custom_style_2)
                                fare = fare['FC']
                                u = False
                                for x in fare:
                                    try:
                                        int(x)
                                    except:
                                        print('Fare cannot have characters. \n')
                                        u = True
                                        break
                                if u == True:
                                    continue
                                else:
                                    fare = int(fare)
                                    break
                            query = 'Update Flights set FareCharges =' + str(fare) + ' where FlightID = \'' + flightID + '\''
                            mycursor.execute(query)
                            mydb.commit()
                        print('Database has been updated. \n')
                elif answer == 'View every table of the database in tabular form.':
                    table1 = PrettyTable()
                    table1.field_names = ["Admin ID", "Admin Name", "Admin Password"]

                    query = 'Select * from Admins'
                    mycursor.execute(query) 

                    for x in mycursor:
                        table1.add_row(x)
                    print(table1)

                    table2 = PrettyTable()
                    table2.field_names = ["Receptionist ID", "Receptionist Name", "Receptionist password"]
                    query = 'Select * from Receptionists'
                    mycursor.execute(query) 

                    for x in mycursor:
                        table2.add_row(x)
                    print(table2)

                    table3 = PrettyTable()
                    table3.field_names = [ 'CNIC', 'Passenger Name', 'Address', 'Phone Number', 'Age', 'Gender', 'Nationality']

                    query = 'Select * from Passengers'
                    mycursor.execute(query) 

                    for x in mycursor:
                        table3.add_row(x)
                    print(table3)

                    table4 = PrettyTable()
                    table4.field_names = ['Flight ID', 'Source', 'Destination', 'Departure Time', 'Arrival Time', 'Departure Date', 'Arrival Date', 'AirCraft', 'Fare Charges']

                    query = 'Select * from Flights'
                    mycursor.execute(query) 

                    for x in mycursor:
                        table4.add_row(x)
                    print(table4)

                    table5 = PrettyTable()
                    table5.field_names = ['Ticket ID', 'Flight ID', 'CNIC', 'Seat Number', 'Registeration Date']

                    query = 'Select * from HistoryRecord'
                    mycursor.execute(query) 

                    for x in mycursor:
                        table5.add_row(x)
                    print(table5)
    else:
        print('Welcome Receptionist, please enter your username and password to have access.\n')
        access = False
        while access == False:
            Receptionist_prompt1 = {
                'type' : 'input',
                'name' : 'ID',
                'message' : 'Enter your ID:'
            }
            answer1 = prompt(Receptionist_prompt1, style = custom_style_2)
            ReceptionistIDAnswer = answer1['ID']
            try:
                IntReceptionistID = int(ReceptionistIDAnswer)
            except:
                print('ID cannot have characters. Try again. \n')
                continue

            Receptionist_prompt2 = {
                'type' : 'password',
                'name' : 'Pass',
                'message': 'Enter your password'
            }

            answer2 = prompt(Receptionist_prompt2, style = custom_style_2)
            ReceptionistPasswordAnswer = answer2['Pass']

            mydb = mysql.connector.connect(
               host = "localhost",
                user = "root",
                passwd = "dumbshit"
            )

            mycursor = mydb.cursor()
            mycursor.execute("Use Airline")
            mycursor.execute("Select * from Receptionists")
            

            for data in mycursor:
                if data[0] == int(ReceptionistIDAnswer):
                    if data[2] == ReceptionistPasswordAnswer:
                        access = True
                        print(data[1], ', you have been granted access.\n')
        

            if access == False:
                print('Access denied. Incorrect ID/Password.\n')
                continue

            Receptionist_Display_Prompt = {
                'type' : 'list',
                'name' : 'choice',
                'message' : 'What do you want to do?',
                'choices' : ['Create new passenger record.', 'Update details of an exisiting passenger record.', 'View all available flights in a particular time period using the departure airport IATA and arrival airport IATA.', 'Generate ticket record of a particular passenger for a particular flight.', 'View the cheapest flight given the departure and arrival airport IATA code.', 'View flight history of a particular passenger.', 'Cancel a particular ticket record.', 'Exit the Airline Database Management System.']
            }

            while 1:
                ans = prompt(Receptionist_Display_Prompt, style = custom_style_2)
                answer = ans['choice']
                if answer == 'Exit the Airline Database Management System.':
                    print('Exiting...')
                    break
                elif answer == 'Create new passenger record.':
                    newPassengerName = ''
                    newPassengerNumber = ''
                    newPassengerCNIC = ''
                    newPassengerAddress = ''
                    newPassengerNationality = ''
                    newPassengerAge = ''
                    newPassengerGender = ''
                    correctNAME = False
                    while correctNAME == False:
                        prompt_NEW_name = {
                            'type' : 'input',
                            'name' : 'fullname',
                            'message' : 'Enter full name:'
                        }

                        newPassengerName = prompt(prompt_NEW_name, style = custom_style_2)
                        newPassengerName = newPassengerName['fullname']
                        k = False
                        for x in newPassengerName:
                            try:
                                int(x)
                                print('Name cannot contain numbers.\n')
                                k = True
                                break
                            except:
                                continue
                        if k == True:
                            continue
                        correctNAME = True
                    correctCNIC = False
                    while correctCNIC == False:
                        prompt_NEW_CNIC = {
                            'type' : 'input',
                            'name' : 'CNIC',
                            'message' : 'Enter CNIC:'
                        }

                        newPassengerCNIC = prompt(prompt_NEW_CNIC, style = custom_style_2)
                        newPassengerCNIC = newPassengerCNIC['CNIC']

                        try:
                            int(newPassengerCNIC)
                        except:
                            print('CNIC cannot have letters in it.\n')
                            continue

                        if len(newPassengerCNIC) !=13:
                            print('CNIC must have 13 digits.\n')
                            continue
                        query = ('Select * from Passengers')
                        mycursor.execute(query)
                        c = False
                        for x in mycursor:
                            if x[0] == newPassengerCNIC:
                                c = True
                        if c == False:
                            correctCNIC = True
                        else:
                            print('A passenger with this CNIC already exists. \n')

                    correctPhoneNumber = False
                    while correctPhoneNumber == False:
                        prompt_NEW_PhoneNumber = {
                            'type' : 'input',
                            'name' : 'Number',
                            'message' : 'Enter Phone Number:'
                        }

                        newPassengerNumber = prompt(prompt_NEW_PhoneNumber, style = custom_style_2)
                        newPassengerNumber = newPassengerNumber['Number']

                        try:
                            int(newPassengerNumber)
                        except:
                            print('Phone number cannot contain characters.\n')
                            continue

                        if len(newPassengerNumber) != 11:
                            print('Phone number must have 11 characters.\n')
                            continue

                        correctPhoneNumber = True

                    prompt_NEW_Address = {
                        'type' : 'input',
                        'name' : 'Address',
                        'message' : 'Enter Address:'
                    }

                    newPassengerAddress = prompt(prompt_NEW_Address, style = custom_style_2)
                    newPassengerAddress = newPassengerAddress['Address']

                    correctNATIONALITY = False
                    while correctNATIONALITY == False:
                        prompt_NEW_Nationality = {
                            'type' : 'input',
                            'name' : 'Nationality',
                            'message' : 'Enter Nationality:'
                        }

                        newPassengerNationality = prompt(prompt_NEW_Nationality, style = custom_style_2)
                        newPassengerNationality = newPassengerNationality['Nationality']
                        k = False
                        for x in newPassengerNationality:
                            try:
                                int(x)
                                print('Nationality cannot contain numbers.\n')
                                k = True
                                break
                            except:
                                continue
                        if k == True:
                            continue
                        correctNATIONALITY = True

                    correctAGE = False
                    while correctAGE == False:
                        prompt_NEW_Age = {
                            'type' : 'input',
                            'name' : 'Age',
                            'message' : 'Enter Age:'
                        }

                        newPassengerAge = prompt(prompt_NEW_Age, style = custom_style_2)
                        newPassengerAge = newPassengerAge['Age']

                        try:
                            int(newPassengerAge)
                        except:
                            print('Age cannot contain characters.\n')
                            continue

                        if len(newPassengerAge) > 3:
                            print('How can you be this old? :o \n')
                            continue
                        correctAGE = True

                    
                    prompt_NEW_Gender = {
                        'type' : 'list', 
                        'name' : 'Gender',
                        'message' : 'Enter Gender:',
                        'choices' : ['Female', 'Male']
                    } 

                    newPassengerGender = prompt(prompt_NEW_Gender, style = custom_style_2)
                    newPassengerGender = newPassengerGender['Gender']
                    x = 'Insert into Passengers (CNIC, PassengerName, Address, PhoneNumber, Age, Gender, Nationality) values'
                    y = (newPassengerCNIC, newPassengerName, newPassengerAddress, newPassengerNumber, newPassengerAge, newPassengerGender, newPassengerNationality)
                    y = str(y)
                    x = x + y
                    mycursor.execute(x)
                    mydb.commit()

                    print('Passenger created successfully!\n\n')
                elif answer == 'Update details of an exisiting passenger record.':
                    k = False
                    cnicInfo = ''
                    while k == False:
                        prompt_update_info = {
                            'type' : 'input',
                            'name' : 'CNICinfo',
                            'message' : "Enter the CNIC of the passenger: "
                        }

                        cnicInfo = prompt(prompt_update_info, style = custom_style_2)
                        cnicInfo = cnicInfo['CNICinfo']
                        try:
                            int(cnicInfo)
                        except:
                            print('CNIC cannot have letters in it.\n')
                            continue

                        if len(cnicInfo) !=13:
                            print('CNIC must have 13 digits.\n')
                            continue

                        query = 'Select * from Passengers'
                        mycursor.execute(query)
                   
                        for x in mycursor:
                            if x[0] == cnicInfo:
                                k = True
                        if k == False:
                            print('No passenger with this CNIC is present in the database. \n')
                            continue


                    prompt_Update_Menu = {
                        'type' : 'list',
                        'name' : 'UpdateAttributeChoice',
                        'message' : 'What do you want to update?',
                        'choices' : ['Passenger Name', 'Address', 'Phone Number', 'Age', 'Gender', 'Nationality', 'Nothing/Exit']
                    }
                    while 1:
                        changeChoice = prompt(prompt_Update_Menu, style = custom_style_2)
                        changeChoice = changeChoice['UpdateAttributeChoice']
                        newPassengerName = ''
                        if changeChoice == 'Nothing/Exit':
                            break
                        elif changeChoice == 'Passenger Name':
                            correctNAME = False
                            while correctNAME == False:
                                prompt_NEW_name = {
                                    'type' : 'input',
                                    'name' : 'fullname',
                                    'message' : 'Enter full name:'
                                }

                                newPassengerName = prompt(prompt_NEW_name, style = custom_style_2)
                                newPassengerName = newPassengerName['fullname']
                                k = False
                                for x in newPassengerName:
                                    try:
                                        int(x)
                                        print('Name cannot contain numbers.\n')
                                        k = True
                                        break
                                    except:
                                        continue
                                if k == True:
                                    continue
                                correctNAME = True

                            query = 'Update Passengers Set PassengerName = \'' + newPassengerName +'\' where CNIC = \'' + cnicInfo +'\'' 
                    
                            mycursor.execute(query)
                            mydb.commit()
                        elif changeChoice == 'Address':
                            prompt_NEW_Address = {
                                'type' : 'input',
                                'name' : 'Address',
                                'message' : 'Enter Address:'
                            }

                            newPassengerAddress = prompt(prompt_NEW_Address, style = custom_style_2)
                            newPassengerAddress = newPassengerAddress['Address']
                            query = 'Update Passengers Set Address = \'' + newPassengerAddress +'\' where CNIC = \'' + cnicInfo +'\'' 
                    
                            mycursor.execute(query)
                            mydb.commit()
                        elif changeChoice == 'Phone Number':
                            correctPhoneNumber = False
                            newPassengerNumber = ''
                            while correctPhoneNumber == False:
                                prompt_NEW_PhoneNumber = {
                                    'type' : 'input',
                                    'name' : 'Number',
                                    'message' : 'Enter Phone Number:'
                                }

                                newPassengerNumber = prompt(prompt_NEW_PhoneNumber, style = custom_style_2)
                                newPassengerNumber = newPassengerNumber['Number']

                                try:
                                    int(newPassengerNumber)
                                except:
                                    print('Phone number cannot contain characters.\n')
                                    continue

                                if len(newPassengerNumber) != 11:
                                    print('Phone number must have 11 characters.\n')
                                    continue

                                correctPhoneNumber = True
                            query = 'Update Passengers Set PhoneNumber = \'' + newPassengerNumber +'\' where CNIC = \'' + cnicInfo +'\'' 
                    
                            mycursor.execute(query)
                            mydb.commit()
                        elif changeChoice == 'Age':
                            correctAGE = False
                            newPassengerAge = ''
                            while correctAGE == False:
                                prompt_NEW_Age = {
                                    'type' : 'input',
                                    'name' : 'Age',
                                    'message' : 'Enter Age:'
                                }

                                newPassengerAge = prompt(prompt_NEW_Age, style = custom_style_2)
                                newPassengerAge = newPassengerAge['Age']

                                try:
                                    int(newPassengerAge)
                                except:
                                    print('Age cannot contain characters.\n')
                                    continue

                                if len(newPassengerAge) > 3:
                                    print('How can you be this old? :o \n')
                                    continue
                                correctAGE = True
                            query = 'Update Passengers Set Age = \'' + newPassengerAge +'\' where CNIC = \'' + cnicInfo +'\'' 
                    
                            mycursor.execute(query)
                            mydb.commit()
                        elif changeChoice == 'Gender':
                            prompt_NEW_Gender = {
                            'type' : 'list', 
                            'name' : 'Gender',
                            'message' : 'Enter Gender:',
                            'choices' : ['Female', 'Male']
                            } 

                            newPassengerGender = prompt(prompt_NEW_Gender, style = custom_style_2)
                            newPassengerGender = newPassengerGender['Gender']
                            query = 'Update Passengers Set Gender = \'' + newPassengerGender +'\' where CNIC = \'' + cnicInfo +'\'' 
                    
                            mycursor.execute(query)
                            mydb.commit()
                        elif changeChoice == 'Nationality':
                            correctNATIONALITY = False
                            newPassengerNationality = ''
                            while correctNATIONALITY == False:
                                prompt_NEW_Nationality = {
                                    'type' : 'input',
                                    'name' : 'Nationality',
                                    'message' : 'Enter Nationality:'
                                }

                                newPassengerNationality = prompt(prompt_NEW_Nationality, style = custom_style_2)
                                newPassengerNationality = newPassengerNationality['Nationality']
                                k = False
                                for x in newPassengerNationality:
                                    try:
                                        int(x)
                                        print('Nationality cannot contain numbers.\n')
                                        k = True
                                        break
                                    except:
                                        continue
                                if k == True:
                                    continue
                                correctNATIONALITY = True
                            query = 'Update Passengers Set Nationality = \'' + newPassengerNationality +'\' where CNIC = \'' + cnicInfo +'\'' 
                    
                            mycursor.execute(query)
                            mydb.commit()

                        print('Database has been updated. \n \n')
                elif answer == 'View all available flights in a particular time period using the departure airport IATA and arrival airport IATA.':
                   
                    exit = False
                    k = False
                    departure = ''
                    while k == False:
                        prompt_showAvailable1 = {
                            'type' : 'input',
                            'name' : 'DepartureAIRPORT',
                            'message' : 'Departure:'
                        }

                        departure = prompt(prompt_showAvailable1, style = custom_style_2)
                        departure = departure['DepartureAIRPORT']
                        u = False
                        for x in departure:
                            try:
                                int(x)
                                print('Cannot contain numbers.')
                                u = True
                                break
                            except:
                                continue
                        if u == True:
                            continue

                        

                        query = 'Select * from Flights'
                        mycursor.execute(query)
                   
                        for x in mycursor:
                            if x[1] == departure:
                                k = True
                        if k == False:
                            print('No flight is leaving from this airport. \n')
                            exit = True
                            break
                    if exit == True:
                        continue

                    arrival = ''
                    k = False
                    while k == False:
                        prompt_showAvailable2 = {
                            'type' : 'input',
                            'name' : 'ArrivalAIRPORT',
                            'message' : 'Arrival: '
                        }

                        arrival = prompt(prompt_showAvailable2, style = custom_style_2)
                        arrival = arrival['ArrivalAIRPORT']
                        u = False
                        for x in arrival:
                            try:
                                int(x)
                                print('Cannot contain numbers.')
                                u = True
                                break
                            except:
                                continue
                        if u == True:
                            continue

                        

                        query = 'Select * from Flights'
                        mycursor.execute(query)
                   
                        for x in mycursor:
                            if x[2] == arrival:
                                k = True
                        if k == False:
                            print('No flight is arriving at this airport. \n')
                            exit = True
                            break
                    if exit == True:
                        continue

                    Date = ''
                    k = False
                    while k == False:
                        print('Date format must be yyyy-mm-dd.')
                        prompt_showAvailable3 = {
                            'type' : 'input',
                            'name' : 'DepartureDATE',
                            'message' : 'Departure date: '
                        }

                        Date = prompt(prompt_showAvailable3, style = custom_style_2)
                        Date = Date['DepartureDATE']
                        if len(Date) != 10:
                            print('Incorrect format. \n')
                            continue
                        count = 0
                        u = False
                        for x in Date:
                            if count == 4 or count == 7:
                                if x != '-':
                                    print('Incorrect format. \n')
                                    u = True
                                    break
                            else: 
                                try:
                                    int(x)
                                except:
                                    print('Incorrect format. \n')
                                    u = True
                                    break
                            
                            count = count + 1
                        if u == True:
                            continue

                        query = 'Select * from Flights'
                        mycursor.execute(query)

                        for x in mycursor:
                            if x[5] == Date:
                                k = True
                        if k == False:
                            print('No flight is leaving from the airport on this date. \n')
                            exit = True
                            break
                    if exit == True:
                        continue

                    query = 'Select * from Flights where DepartureDate = \'' + Date + '\' and Source = \'' + departure + '\' and Destination  = \'' + arrival + '\''
                    mycursor.execute(query)
                    table = PrettyTable()
                    table.field_names = ['FlightID','Source', 'Destination', 'Departure Time', 'Arrival Time', 'Departure Date', 'Arrival Date', 'AirCraft', 'Fare charges']

                    for x in mycursor:
                        table.add_row(x)
                    print(table)
                        
                elif answer == 'Generate ticket record of a particular passenger for a particular flight.':
                    correctFlightID = False
                    flightID = ''
                    while correctFlightID == False:
                        prompt_generate1 = {
                            'type' : 'input',
                            'name' : 'FlightID',
                            'message' : 'Enter Flight ID: '
                        }

                        flightID = prompt(prompt_generate1, style = custom_style_2)
                        flightID = flightID['FlightID']
                        query = 'Select * from Flights'
                        mycursor.execute(query)
                    
                        for x in mycursor:
                            if x[0] == flightID:
                                correctFlightID = True

                        if correctFlightID == False:
                            print('No Flight with this ID. \n')

                    k = False
                    CNIC = ''
                    while k == False:
                        prompt_update_info = {
                            'type' : 'input',
                            'name' : 'CNICinfo',
                            'message' : "Enter the CNIC of the passenger: "
                        }

                        cnicInfo = prompt(prompt_update_info, style = custom_style_2)
                        cnicInfo = cnicInfo['CNICinfo']
                        try:
                            int(cnicInfo)
                        except:
                            print('CNIC cannot have letters in it.\n')
                            continue

                        if len(cnicInfo) !=13:
                            print('CNIC must have 13 digits.\n')
                            continue

                        query = 'Select * from Passengers'
                        mycursor.execute(query)
                   
                        for x in mycursor:
                            if x[0] == cnicInfo:
                                k = True
                        if k == False:
                            print('No passenger with this CNIC is present in the database. \n')
                            continue
                        CNIC = cnicInfo
                    bookingDate = date.today()
                    bookingDate = bookingDate.strftime("%Y-%m-%d")
                    
                    seatNumber = ''
                    foundSeat = False
                    for x in range(6):
                        if x == 0:
                            for y in range(10):
                                seatNumber = 'A' + str(y+1)
                                query = 'Select * from HistoryRecord where SeatNumber = \'' + seatNumber +'\'' 
                                mycursor.execute(query)
                                count = 0
                                for x in mycursor:
                                    count = count + 1
                                if count == 0:
                                    foundSeat = True
                                    break
                        elif x == 1:
                            for y in range(10):
                                seatNumber = 'B' + str(y+1)
                                query = 'Select * from HistoryRecord where SeatNumber = \'' + seatNumber +'\'' 
                                mycursor.execute(query)
                                count = 0
                                for x in mycursor:
                                    count = count + 1
                                if count == 0:
                                    foundSeat = True
                                    break
                        elif x == 2:
                            for y in range(10):
                                seatNumber = 'C' + str(y+1)
                                query = 'Select * from HistoryRecord where SeatNumber = \'' + seatNumber +'\'' 
                                mycursor.execute(query)
                                count = 0
                                for x in mycursor:
                                    count = count + 1
                                if count == 0:
                                    foundSeat = True
                                    break
                        elif x == 3:
                            for y in range(10):
                                seatNumber = 'D' + str(y+1)
                                query = 'Select * from HistoryRecord where SeatNumber = \'' + seatNumber +'\'' 
                                mycursor.execute(query)
                                count = 0
                                for x in mycursor:
                                    count = count + 1
                                if count == 0:
                                    foundSeat = True
                                    break
                        elif x == 4:
                            for y in range(10):
                                seatNumber = 'E' + str(y+1)
                                query = 'Select * from HistoryRecord where SeatNumber = \'' + seatNumber +'\'' 
                                mycursor.execute(query)
                                count = 0
                                for x in mycursor:
                                    count = count + 1
                                if count == 0:
                                    foundSeat = True
                                    break
                        elif x == 5:
                            for y in range(10):
                                seatNumber = 'F' + str(y+1)
                                query = 'Select * from HistoryRecord where SeatNumber = \'' + seatNumber +'\'' 
                                mycursor.execute(query)
                                count = 0
                                for x in mycursor:
                                    count = count + 1
                                if count == 0:
                                    foundSeat = True
                                    break
                        if foundSeat == True:
                            break
                    if foundSeat == False:
                        print('Flight is full.')
                        continue
                    x = 'Insert into HistoryRecord (FlightID, CNIC, SeatNumber, RegisteringDate) values'
                    y = (flightID, passengerID, seatNumber, bookingDate)
                    y = str(y)
                    x = x + y
                    mycursor.execute(x)
                    mydb.commit()

                    print('Ticket has been generated successfully!')
                elif answer == 'View flight history of a particular passenger.':
                    k = False
                    CNIC = ''
                    while k == False:
                        prompt_update_info = {
                            'type' : 'input',
                            'name' : 'CNICinfo',
                            'message' : "Enter the CNIC of the passenger: "
                        }

                        cnicInfo = prompt(prompt_update_info, style = custom_style_2)
                        cnicInfo = cnicInfo['CNICinfo']
                        try:
                            int(cnicInfo)
                        except:
                            print('CNIC cannot have letters in it.\n')
                            continue

                        if len(cnicInfo) !=13:
                            print('CNIC must have 13 digits.\n')
                            continue

                        query = 'Select * from Passengers'
                        mycursor.execute(query)
                        u = False
                        for x in mycursor:
                            if x[0] == cnicInfo:
                                k = True
                        CNIC = cnicInfo
                        if k == False:
                            print('No passenger with this CNIC is present in the database. \n')
                            u = True
                            break

                    if u == True:
                        continue

                    query = 'Select * from HistoryRecord where CNIC =' + CNIC
                    mycursor.execute(query)

                    table = PrettyTable()
                    table.field_names=['Ticket ID', 'Flight ID', 'CNIC', 'Seat Number', 'Registeration Date']
                    count = 0
                    for x in mycursor:
                        table.add_row(x)
                        count = count + 1
                    if count == 0:
                        print('No flight history of this passenger.')
                    else:
                        print(table)
                elif answer == 'Cancel a particular ticket record.':
                    k = False
                    while k == False:
                        prompt_cancel_info = {
                            'type' : 'input',
                            'name' : 'ticket',
                            'message' : "Enter the ticket ID: "
                        }

                        ticketID = prompt(prompt_cancel_info, style = custom_style_2)
                        ticketID = ticketID['ticket']
                        u = False
                        for x in ticketID:
                            try:
                                int(x)
                            except:
                                print('Ticket ID cannot have characters in it. \n')
                                u = True
                                break
                        if u == True:
                            continue
                        else:
                            break
                    query = 'Select * from HistoryRecord'
                    mycursor.execute(query)
                    u = False
                    for x in mycursor:
                        if x[0] == int(ticketID):
                            u = True

                    if u == False:
                        print('No ticket record of this ticket ID exists. \n')
                        continue

                    query = 'Delete from HistoryRecord where TicketID = ' + ticketID
                    mycursor.execute(query)
                    mydb.commit()
                    print('Ticket record has been deleted. \n')
                elif answer == 'View the cheapest flight given the departure and arrival airport IATA code.':
                    departure = ''
                    k = False
                    exit = False
                    while k == False:
                        prompt_showAvailable1 = {
                            'type' : 'input',
                            'name' : 'DepartureAIRPORT',
                            'message' : 'Departure:'
                        }

                        departure = prompt(prompt_showAvailable1, style = custom_style_2)
                        departure = departure['DepartureAIRPORT']
                        u = False
                        for x in departure:
                            try:
                                int(x)
                                print('Cannot contain numbers.')
                                u = True
                                break
                            except:
                                continue
                        if u == True:
                            continue

                        

                        query = 'Select * from Flights'
                        mycursor.execute(query)
                   
                        for x in mycursor:
                            if x[1] == departure:
                                k = True
                        if k == False:
                            print('No flight is leaving from this airport. \n')
                            exit = True
                            break
                    if exit == True:
                        continue

                    arrival = ''
                    k = False
                    while k == False:
                        prompt_showAvailable2 = {
                            'type' : 'input',
                            'name' : 'ArrivalAIRPORT',
                            'message' : 'Arrival: '
                        }

                        arrival = prompt(prompt_showAvailable2, style = custom_style_2)
                        arrival = arrival['ArrivalAIRPORT']
                        u = False
                        for x in arrival:
                            try:
                                int(x)
                                print('Cannot contain numbers.')
                                u = True
                                break
                            except:
                                continue
                        if u == True:
                            continue

                        

                        query = 'Select * from Flights'
                        mycursor.execute(query)
                   
                        for x in mycursor:
                            if x[2] == arrival:
                                k = True
                        if k == False:
                            print('No flight is arriving at this airport. \n')
                            exit = True
                            break
                    if exit == True:
                        continue
                    query = 'Select * from Flights where Destination = \'' + departure + '\' and Source = \'' + arrival + '\' order by FareCharges asc'
                    mycursor.execute(query)
                    count = 0
                    table1 = PrettyTable()
                    table1.field_names = ["Flight ID", "Source", "Destination", "Departure Time", "Arrival Time", "Departure Date", "Arrival Date", "AirCraft", "Fare Charges"]

                

        
                    for x in mycursor:
                        if count != 1:
                            table1.add_row(x)
                            count = count + 1
                    if count == 0:
                        print('No such flight. \n')
                    else:
                        print(table1)
main()