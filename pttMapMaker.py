# Hello

# import curses
# stdscr = curses.initscr()


# LAST UPDATED : 11/30/16
# TO RUN/TEST, IMPORT THEN CALL MAIN()

# Add a "Mode" to the mapMaker
# Return the string or print out in console

class seating():
    def __init__(self, initV="Empty"):
        self.name = initV
        self.cardInfo = initV
        self.seatID = initV
        self.test = ["A1", "B2", "C1"]

    def editname(self, name):
        self.name = name

    def editCardInfo(self, card):
        self.cardInfo = card

    def editSeatID(self, seat):
        self.seatID = seat

    def seatInfo(self):  # Will be used outside of this class
        infoList = [self.name, self.cardInfo, self.seatID]
        return infoList

    def clear(self):
        self.name = "Empty"
        self.cardInfo = "Empty"
        self.seatID = "Empty"

    def find(self, name):
        for x in self.test:
            if x == name:
                return 0
        return 1

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.name + " " + self.cardInfo + " " + self.seatID)


def mapPrinter(colSize, rowSize, seatsTaken):
    # This function will return the large string of the map instead of printing it out
    # colSize : an int, how many columns
    # rowSize : an int, how many rows
    # seatsTaken : a list of sorted strings, all the seats taken

    cols = ["A", "B", "C", "D", "E", "F"]  # All avaliable columns (may add more if needed)
    rows = [1, 2, 3, 4, 5, 6]  # All avaliable rows (may add more if needed)

    col = cols[:colSize]  # parameter colSize/rowsize
    row = rows[:rowSize]  # will break up the list that we need

    # All possible seats
    seatRowA = ["A1", "A2", "A3", "A4", "A5", "A6"]
    seatRowB = ["B1", "B2", "B3", "B4", "B5", "B6"]
    seatRowC = ["C1", "C2", "C3", "C4", "C5", "C6"]
    seatRowD = ["D1", "D2", "D3", "D4", "D5", "D6"]
    seatRowE = ["E1", "E2", "E3", "E4", "E5", "E6"]
    seatRowF = ["F1", "F2", "F3", "F4", "F5", "F6"]

    # List of all seats, index breaks are in place for error checking later
    seatRows = [seatRowA[:rowSize], seatRowB[:rowSize], seatRowC[:rowSize], seatRowD[:rowSize], seatRowE[:rowSize],
                seatRowF[:rowSize]]

    # Will be used to error check
    flattened_list = [y for x in seatRows for y in x]

    # Counters that will be used to walk through the taken seats
    seatCounter = 0
    colCounter = 0


    all = ""


    # ____ ROW PRINTING ____#
    all += "     "
    for x in row:
        all +="%d    " % x
    all += "\n"

    # ____ COLUMN / SEAT PRINTING ____#

    taken = "X"
    free = "0"
    for x in range(0, int(colSize)):  # Columns
        all += "%s  " % (col[colCounter])
        for j in range(0, rowSize):  # Rows
            try:
                if seatsTaken[seatCounter] == seatRows[x][j]:
                    all += " |%s| " % (taken)
                    seatCounter += 1  # Iterate through the list of taken seats
                else:
                    all +=" |%s| " % (free)
            except:  # If it ever goes out of index
                all+=" |%s| " % (free)
        colCounter += 1  # Go to next column
        all+= "\n"
    return all

def mapMaker(colSize, rowSize, seatsTaken):
    # colSize : an int, how many columns
    # rowSize : an int, how many rows
    # seatsTaken : a list of sorted strings, all the seats taken


    cols = ["A", "B", "C", "D", "E", "F"]  # All avaliable columns (may add more if needed)
    rows = [1, 2, 3, 4, 5, 6]  # All avaliable rows (may add more if needed)

    col = cols[:colSize]  # parameter colSize/rowsize
    row = rows[:rowSize]  # will break up the list that we need

    # All possible seats
    seatRowA = ["A1", "A2", "A3", "A4", "A5", "A6"]
    seatRowB = ["B1", "B2", "B3", "B4", "B5", "B6"]
    seatRowC = ["C1", "C2", "C3", "C4", "C5", "C6"]
    seatRowD = ["D1", "D2", "D3", "D4", "D5", "D6"]
    seatRowE = ["E1", "E2", "E3", "E4", "E5", "E6"]
    seatRowF = ["F1", "F2", "F3", "F4", "F5", "F6"]

    # List of all seats, index breaks are in place for error checking later
    seatRows = [seatRowA[:rowSize], seatRowB[:rowSize], seatRowC[:rowSize], seatRowD[:rowSize], seatRowE[:rowSize],
                seatRowF[:rowSize]]

    # Will be used to error check
    flattened_list = [y for x in seatRows for y in x]

    # Counters that will be used to walk through the taken seats
    seatCounter = 0
    colCounter = 0

    # ____ ROW PRINTING ____#
    print("     ", end="")
    for x in row:
        print("%d    " % x, end="")
    print("")

    # ____ COLUMN / SEAT PRINTING ____#
    taken = "X"
    free = "0"
    for x in range(0, int(colSize)):  # Columns
        print("%s  " % (col[colCounter]), end="")
        for j in range(0, rowSize):  # Rows
            try:
                if seatsTaken[seatCounter] == seatRows[x][j]:
                    print(" |%s| " % (taken), end="")
                    seatCounter += 1  # Iterate through the list of taken seats
                else:
                    print(" |%s| " % (free), end="")
            except:  # If it ever goes out of index
                print(" |%s| " % (free), end="")
        colCounter += 1  # Go to next column
        print("")
    return flattened_list


# Note this will be a showroom obj at some point. This is for demonstration
seatsTaken = ["A1", "A3", "B1", "B3", "B4", "D1", "E5", "F6"]
#seatsTaken = ["A1", "B1", "B3", "B4", "D1", "E5", "F6"]

# NOTES_____
# - Remeber the showroom obj needs to be created FIRST. THEN inserted
#   - If (col,row) is 2,2 and the seatsTaken is ["A1", "A3", "B1", "B3", "B4", "D1", "E5", "F6"]
#   it will not work correctly. (Note A3 will cause mess it up due to being out of the map)
#   - Under assumption that every seat in seatsTaken is ALREADY valid
# - Seats need to be SORTED
# - Cool idea:
#   - Grab multiple seats at once



def main():
    global seatsTaken

    # The manager user will need to do something like this to the showroom obj
    rowSize = int(input("Insert Row Size"))
    colSize = int(input("Insert Col Size"))

    currentMap = mapMaker(rowSize, colSize, seatsTaken)

    # While loop for demonstration
    cont = True
    while (cont):
        seatSelect = input("Select Seat")

        if seatSelect in seatsTaken:  # If the seat is already taken
            print("Seat taken / Unavaliable")
        elif seatSelect not in currentMap:  # If invalid seat
            print("Seat out of range")
        else:
            sortIter = 0
            for n in seatsTaken:  # INSERT SORT
                # print("COMPAREING : %s < %s" % (seatSelect,n)) : #Code to see what is happening inside
                if seatSelect < n:
                    print("Added!")
                    seatsTaken.insert(sortIter, seatSelect)
                    break  # Need to break or forever loop
                sortIter += 1

        mapMaker(rowSize, colSize, seatsTaken)

        selectAgain = input("Want to select another seat Y/N?")
        if selectAgain == "N":
            cont = False
