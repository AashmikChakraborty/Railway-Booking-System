# ===================== RAILWAY BOOKING SYSTEM =====================

import random

# ===================== CLASSES =====================

class Passenger:

    def __init__(self, name, age, id_proof):

        self.name = name
        self.age = age
        self.id_proof = id_proof


class Train:

    def __init__(self, train_no, name, source, destination,
                 dep_time, arr_time, seats, price):

        self.train_no = train_no
        self.name = name
        self.source = source
        self.destination = destination
        self.dep_time = dep_time
        self.arr_time = arr_time
        self.__seats = seats
        self.price = price

    # Encapsulation
    def get_seats(self):

        return self.__seats

    def book_seats(self, total_seats):

        if self.__seats >= total_seats:

            self.__seats -= total_seats
            return True

        return False

    # Calculate Journey Duration
    def get_duration(self):

        dep_hour = int(self.dep_time.split(":")[0])
        dep_min = int(self.dep_time.split(":")[1])

        arr_hour = int(self.arr_time.split(":")[0])
        arr_min = int(self.arr_time.split(":")[1])

        dep_total = dep_hour * 60 + dep_min
        arr_total = arr_hour * 60 + arr_min

        # Overnight Train Handling
        if arr_total < dep_total:

            arr_total += 24 * 60

        duration_minutes = arr_total - dep_total

        hours = duration_minutes // 60
        minutes = duration_minutes % 60

        return str(hours) + "h " + str(minutes) + "m"


class Booking(Train):      # Inheritance

    # Polymorphism
    def display(self):

        print("\n================================================")

        print("Train Number     :", self.train_no)
        print("Train Name       :", self.name)
        print("Route            :", self.source, "→", self.destination)
        print("Departure Time   :", self.dep_time)
        print("Arrival Time     :", self.arr_time)
        print("Journey Duration :", self.get_duration())
        print("Ticket Price     : Rs.", self.price)
        print("Available Seats  :", self.get_seats())

        print("================================================")


# ===================== FILE HANDLING =====================

def save_booking(data):

    with open("bookings.txt", "a") as file:

        file.write(data + "\n")


def view_bookings():

    try:

        with open("bookings.txt", "r") as file:

            print("\n============= ALL BOOKINGS =============")
            print(file.read())

    except FileNotFoundError:

        print("\nNo bookings found!")


# ===================== TICKET FUNCTIONS =====================

def generate_pnr():

    return random.randint(1000000000, 9999999999)


def allocate_coach():

    coaches = ["A1", "A2", "B1", "B2", "S1", "S2"]

    return random.choice(coaches)


def allocate_seats(total_tickets):

    seat_numbers = []

    for i in range(total_tickets):

        seat_numbers.append(random.randint(1, 72))

    return seat_numbers


# ===================== PRINT TICKET =====================

def print_ticket(passenger, train, journey_date,
                 total_tickets, total_price,
                 pnr, coach, seats):

    ticket = """

========================================================
                    INDIAN RAILWAYS
========================================================

PNR Number        : """ + str(pnr) + """

Passenger Name    : """ + passenger.name + """
Passenger Age     : """ + str(passenger.age) + """
ID Proof          : """ + passenger.id_proof + """

--------------------------------------------------------

Train Number      : """ + str(train.train_no) + """
Train Name        : """ + train.name + """

From              : """ + train.source + """
To                : """ + train.destination + """

Journey Date      : """ + journey_date + """

Departure Time    : """ + train.dep_time + """
Arrival Time      : """ + train.arr_time + """
Journey Duration  : """ + train.get_duration() + """

--------------------------------------------------------

Coach Number      : """ + coach + """
Seat Numbers      : """ + str(seats) + """

Total Tickets     : """ + str(total_tickets) + """

Price Per Ticket  : Rs.""" + str(train.price) + """
Total Fare        : Rs.""" + str(total_price) + """

--------------------------------------------------------

Booking Status    : CONFIRMED

========================================================
          THANK YOU FOR BOOKING WITH US
========================================================
"""

    print(ticket)

    # Save Ticket To File
    with open("tickets.txt", "a") as file:

        file.write(ticket + "\n")


# ===================== TRAIN DATA =====================

trains = [

    Booking(
        101,
        "Saraighat Express",
        "Guwahati",
        "New Bongaigaon",
        "06:00",
        "10:30",
        50,
        350
    ),

    Booking(
        102,
        "Kamrup Express",
        "Guwahati",
        "New Bongaigaon",
        "09:00",
        "13:45",
        40,
        400
    ),

    Booking(
        103,
        "Brahmaputra Mail",
        "Guwahati",
        "New Bongaigaon",
        "14:00",
        "18:20",
        35,
        450
    ),

    Booking(
        104,
        "North East Express",
        "Guwahati",
        "Delhi",
        "18:00",
        "10:00",
        60,
        2200
    ),

    Booking(
        105,
        "Rajdhani Express",
        "Delhi",
        "Kolkata",
        "06:00",
        "14:00",
        50,
        1500
    ),

    Booking(
        106,
        "Vande Bharat Express",
        "Kolkata",
        "Patna",
        "07:00",
        "12:30",
        45,
        1000
    )

]


# ===================== MAIN PROGRAM =====================

while True:

    print("\n================================================")
    print("            RAILWAY BOOKING SYSTEM")
    print("================================================")

    print("1. Book Ticket")
    print("2. View Bookings")
    print("3. Exit")

    choice = input("\nEnter Your Choice : ")

    try:

        # ================= BOOK TICKET =================

        if choice == '1':

            name = input("\nEnter Passenger Name : ")

            age = int(input("Enter Passenger Age  : "))

            id_proof = input("Enter ID Proof No    : ")

            source = input("Enter Source Station : ")

            destination = input("Enter Destination    : ")

            journey_date = input(
                "Enter Journey Date (YYYY-MM-DD) : "
            )

            total_tickets = int(
                input("Number Of Seats Needed : ")
            )

            passenger = Passenger(name, age, id_proof)

            available_trains = []

            # Find Matching Trains
            for train in trains:

                if (
                    train.source.lower() == source.lower()
                    and
                    train.destination.lower() == destination.lower()
                ):

                    available_trains.append(train)

            # No Train Found
            if len(available_trains) == 0:

                print("\n❌ No trains available!")
                continue

            # Automatically Select First Train
            selected_train = available_trains[0]

            print("\n=========== TRAIN ALLOTTED ===========")

            selected_train.display()

            # Total Fare Calculation
            total_price = (
                selected_train.price * total_tickets
            )

            print("\n=============== FARE DETAILS ===============")

            print("Tickets Needed   :", total_tickets)

            print(
                "Price Per Ticket : Rs.",
                selected_train.price
            )

            print("Total Fare       : Rs.", total_price)

            # Booking Confirmation
            confirm = input("\nConfirm Booking? (yes/no) : ")

            if confirm.lower() == "yes":

                booking_status = selected_train.book_seats(
                    total_tickets
                )

                if booking_status == True:

                    pnr = generate_pnr()

                    coach = allocate_coach()

                    seats = allocate_seats(total_tickets)

                    # Save Booking
                    booking_data = (
                        "PNR: " + str(pnr) +
                        ", Passenger: " + name +
                        ", Train: " + selected_train.name +
                        ", Route: " + source + " to " + destination +
                        ", Tickets: " + str(total_tickets) +
                        ", Coach: " + coach +
                        ", Seats: " + str(seats) +
                        ", Fare: Rs." + str(total_price)
                    )

                    save_booking(booking_data)

                    print("\n✅ THANK YOU! BOOKING CONFIRMED")

                    # Print Ticket
                    print_ticket(
                        passenger,
                        selected_train,
                        journey_date,
                        total_tickets,
                        total_price,
                        pnr,
                        coach,
                        seats
                    )

                else:

                    print("\n❌ Seats Not Available")

            else:

                print("\n❌ Booking Cancelled")

        # ================= VIEW BOOKINGS =================

        elif choice == '2':

            view_bookings()

        # ================= EXIT =================

        elif choice == '3':

            print(
                "\nThank You For Using Railway Booking System!"
            )

            break

        else:

            print("\n❌ Invalid Choice!")

    except Exception as e:

        print("\n❌ ERROR :", e)
