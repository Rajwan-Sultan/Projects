class Star_Cinema:
    __hall_list = []

    def entry_hall(self, obj):
        self.__hall_list.append(vars(obj))


class Hall(Star_Cinema):

    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        self.show_list.append((id, movie_name, time))
        # print(self.show_list)
        self.list_2D = [["empty" for i in range(self.cols)]
                        for j in range(self.rows)]
        self.seats[id] = self.list_2D
        # print('Seats-->', self.seats)

    def book_seats(self, customer_name, phone_no, id, tuple):
        for show in self.show_list:
            if show[0] == id:
                code = id+'_'+customer_name+'_'+phone_no + \
                    ':_seat->'+"row:"+str(tuple[0])+'_col:'+str(tuple[1])
                if tuple[0] < self.rows and tuple[1] < self.cols:
                    if (self.seats[id][tuple[0]][tuple[1]] == 'empty'):
                        self.seats[id][tuple[0]][tuple[1]] = code

                        print('Your seat is booked👍.Your customer code is:', code)
                    else:
                        print('Sorry the seat is already booked. 😓 ')
                else:
                    print(
                        f"Invalid input 🚫 .You need to enter row number ->from 0 to {self.rows-1} & column number ->from 0 to {self.cols-1} ")

            else:
                print('The ID of the show is not in the list 😞 ')
                break

    def view_show_list(self):
        print("#"*100)
        print()
        for id, movie, time in self.show_list:
            print("MOVIE NAME🎬 : ", movie, end="\t")
            print("SHOW ID 🪪 : ", id, end="\t")
            print("TIME ⏲️ : ", time)
        print("#"*100)
        print("\n")

    def view_available_seats(self, view_avail_seat_show_id):
        print("Available seats : ✅ .\nBooked seats: 🚫 .\n")
        for show in self.show_list:
            if show[0] == view_avail_seat_show_id:
                # print('Seats-->', self.seats)
                for i in range(self.rows):
                    for j in range(self.cols):
                        if self.seats[show[0]][i][j] == 'empty':
                            print(f"Seat No:{i}{j} ✅ ", end="\t")
                        else:
                            print(f"Seat No:{i}{j} 🚫 ", end="\t")
                    print()

                pass
            else:
                print('The ID of the show is not in the list 😞 ')
                break


class Counter(Hall):
    def __init__(self, obj):
        self.obj = vars(obj)

    def replica(self):
        while True:
            print("1. VIEW ALL SHOWS TODAY")
            print("2. VIEW AVAILABLE SEATS")
            print("3. BOOK TICKET")
            print("4. EXIT")

            option = int(input("ENTER OPTION: "))

            if option == 1:
                print()
                obj.view_show_list()
            elif option == 2:
                id = input("ENTER SHOW ID: ")
                print("\n")
                obj.view_available_seats(id)
            elif option == 3:
                obj.book_seats(customer_name=input('Enter your name: '), phone_no=input('Enter your phone number: '), id=input(
                    'Enter show ID: '), tuple=((int(input('Enter row number: '))), (int(input('Enter column number:')))))

            else:
                break


obj = Hall(2, 2, 101)
obj.entry_show('123', 'Sultan', '10:30PM')
c = Counter(obj)
c.replica()