#!/usr/bin/python
import tkinter as tk
import calender as cal
import pttMapMaker as MM  # May need to remove
import datatest as dt
import math

LARGE_FONT = ("Verdana", 12)

lolList = []


# Last Updated : 12/20
# - UPDATESHIT (labels atleast)
# - Add errorchecking (if valid response from user)
# -

# Need Do
#   - Errorchecking on apply buttons
#   - Writing into and reading from text file


# Use these to help break up the code :
# SELECT ######## ________________________________________________________________________
# ________________________________________________________________________________________

# EXAMPLE :
# SELECT ######## ________________________________________________________________________
# ~~{Code here}~~
# ~~{Code here}~~
# ~~{Code here}~~
# ________________________________________________________________________________________





###################################################################################################################
#               ____Hello!___
# - If u want to ADD new page make sure you do these things!!!!
#   - in the controller class, in "for F in(....), MAKE SURE TO ADD YOUR CLASS!!!!!!!
# - MAKE SURE U HAVE THE calender and pttMapMaker files!!!!!
# - FOR NOW if u add a widget(label,button,etc) remeber to do widgetname.pack()
# - If u are making a class name it like this
#   - If Customer, then name ur class .... class CustomerFrame, class CustomerPayment, etc
#   - If Manager, then name ur class .... class ManagerFrame, class ManagerTheater, etc
# - BE AWARE of the import tkinter as tk!!!
#   - tk/cal/MM are shorthand versions of tkinter, calender, mapmaker
#   - calender.printdate() == cal.printdate()
#   - pttMapMaker.mapMaker() == MM.mapMaker()


# Want to access items/attributes/variables from other classes??????!!!??
# - Use container's get_page
# - self.What = get_page(Frame)
#   - self.What.attribute, Now you have it
# EXPLE__
#        self.controller = controller            # Help Access the controller + its methods
#        self.CustomerLocation = self.controller.get_page(CustomerLocation)  #Access to Frame CustomerLocation#
#
#        self.test = self.CustomerLocation.test
#
#
# FUNSTUFF____
# Code for buttons that can move around the frames!!!
# show_frame(aFrame) is a method in controller that will take the given frame and move it to the top
#
# button1 = tk.Button(self, text="Next",
#                     command=lambda: controller.show_frame(CustomerSeatMap))
# This button will go to frame CustomerSeatMap
# button1.pack()
#
# button2 = tk.Button(self, text="Back",
#                     command=lambda: controller.show_frame(CustomerPickDate))
# This Button will go to fram CusomerPickDate
# button2.pack()
#
#
#
# MAKING A NEW PAGE!!!
# Make sure to always have these
# class FRAMENAME(tk.Frame):
#    def __init__(self, parent, controller):
#        tk.Frame.__init__(self, parent)
#
# fun fact (from controller class)
# frame = F(container, self) -> __init__(self, parent, controller):
#   -self refers to controller
##############################################################################################################






# FOR THE SAKE OF DYNAMIC STUFF PLEASE USE THESE VARIABLES!!!
# FOR DAY : dayVar
# FOR MONTH : monthVar
# FOR LOCATION : locationVar
# FOR DURATION : durationVar
# ETC....





LocationList = []

with open('locations.txt','r') as f:
    LocationList = f.read().splitlines()

class controller(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.container = tk.Frame(self)
        self.minsize(width=300, height=300)
        # self.geometry("300x500")
        # container.grid(row = 200 , column = 200)
        # container.pack(side="top", fill="both", expand=True)
        self.container.grid()
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # Store all the frames
        for F in (StartPage, CustomerLocation, CustomerPickDate, CustomerPickMovie, CustomerSeatMap, CustomerPayment,
                  CustomerConfirmation,ManagerLogin,ManagerLocation, ManagerSelect, ManagerAddMovie, ManagerEditMovie, PageTwo):
            frame = F(self.container, self)  # F is the classes
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)  # Make Start Page on the top

        # Storing Stuff___________________________________________________________________________
        self.pickedlocation = ''
        self.pickedmonth = ''
        self.pickedday = ''
        self.pickedshowroom = ''
        self.pickedmovie = ''
        self.pickedtime = ' '
        self.pickedseat=''
        self.infofile = ''
        self.timesfile = ''
        self.seatsfile = ''
        self.allmovieinfo = []
        self.availablemovies = []
        self.movietimeslist = []
        self.takenseats = []

        self.MovieDic = {}
        # ________________________________________________________________________________________


    def show_frame(self, cont):  # Used to bring the given frame to the top/ show frame
        frame = self.frames[cont]  # Access the dic of all the frames
        frame.update()
        frame.tkraise()

    def get_page(self, page_class):  # Get access to the page and its attributes
        return self.frames[page_class]

    def combine_funcs(self, *funcs):  # Run multi funcs at one time (attach to a button!)
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)

        return combined_func

    # def updateDic(self,frame):
    #     print(self.availablemovies)
    #     #self.movieOptionMenu = tk.OptionMenu(self, self.movieVar, *self.MovieDic.keys())
    #     for i in range(0,len(self.availablemovies)):
    #        self.MovieDic[self.availablemovies[i]] = self.movietimeslist[i]
    #     print(self.MovieDic)
    #     holder = self.get_page(frame)
    #     holdermovieVar = holder.movieVar
    #     # self.movieVar = tk.StringVar()
    #     # self.movieVar.set("Select")
    #
    #     temp = tk.StringVar()
    #     temp.set("Select")
    #     self.get_page(frame).movieOptionMenu = tk.OptionMenu(frame, temp, *self.MovieDic.keys())
        # updatemovieVar = self.get_page(frame).movieVar
        # optionMenu = self.get_page(frame).movieOptionMenu
        # menu = optionMenu.children["menu"]
        # menu.delete(0,"end")


        # updatemovieVar = self.get_page(frame).movieVar
        # self.get_page(frame).movieOptionMenu =  tk.OptionMenu(frame, updatemovieVar, *self.MovieDic.keys())
        #updateOptionMenu = tk.OptionMenu(self, self.movieVar, *self.MovieDic.keys())

    # FUNCTIONS THAT WILL UPDATE DYNAMIC WIDGETS!!!!! ____________________________
    # Note, b/c widgets cant be parameters (like i cant set .dynamicLabel as a parameter), I have to make an
    # a func for each update
    # def CustomerPickDateDynamicLabel(self,variable): # CODE THAT UPDATES SHIT
    #     label = self.get_page(CustomerPickDate).dynamicLabel
    #     label['text'] = variable.get()
    # CODE THAT UPDATES SHIT

    def dynamicDate(self,frame): # FOR DATES ONLY
        # FRAME = THE FRAME U WILL BE EDITING
        # controller.dynamicDate(self.monthVar,self.dayVar,Frame)
        # VARS FROM OTHER FRAME ___________________________________________________________________
        # self.monthVar = controller.get_page(frame).variablemonth
        # self.dayVar = controller.get_page(CustomerPickDate).variableday
        # Uses vars above as parameters, stick it to button
        # ________________________________________________________________________________________

        self.monthVar = self.get_page(CustomerPickDate).variablemonth
        self.dayVar = self.get_page(CustomerPickDate).variableday

        monthStr = self.monthVar.get()
        dayStr = self.dayVar.get()
        wholedate = monthStr + "/" + dayStr
        label = self.get_page(frame).dateLabel
        label['text'] = "Date : " + wholedate

    def dynamicLocation(self,frame,user):
        if user == "c":
            self.locationVar = self.get_page(CustomerLocation).locationVar
        elif user =="m":
            self.locationVar = self.get_page(ManagerLocation).locationVar

        locationStr = self.locationVar.get()
        label = self.get_page(frame).locationLabel
        label['text'] = "Location : " + locationStr

    def dynamicShowroom(self,frame):
        self.showroomVar = self.get_page(ManagerLocation).variableShowroom
        showroomStr = self.showroomVar.get()
        label = self.get_page(frame).showroomLabel
        label['text'] = "Showroom : " + showroomStr


    def UpdateDynamicLabel(self,variable,frame): # UPDATE ONE LABEL
        label = self.get_page(frame).dynamicLabel
        label['text'] = variable.get()

    def UpdateTwoDynamicLabels(self,variableA,variableB,frame):
        labelA = self.get_page(frame).dynamicLabelA
        labelB = self.get_page(frame).dynamicLabelB

        labelA['text'] = variableA.get()
        labelB['text'] = variableB.get()

    def UpdateDynamicLabelsConfirm(self):
        pass








class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  # Parent = controller class
        self.configure(background='#ED7D3B')

        tk.Label(self, text="HomePage - Select Account").pack(side=tk.BOTTOM)

        label = tk.Label(self, text="Select Acct", background='#ED7D3B',
                         foreground='#0F3A65', font="Verdana 14 bold")
        label.pack(pady=10, padx=10)

        # logo = tk.PhotoImage(file ="PrimeTicketTime.png")
        # w1 = tk.Label(self, image=logo).pack()

        Custbutton = tk.Button(self, text="Customer",
                               command=lambda: controller.show_frame(CustomerLocation))
        Custbutton.configure(highlightbackground='#ED7D3B')
        Custbutton.pack(pady=10, padx=10)
        Mangbutton2 = tk.Button(self, text="Manager",
                                command=lambda: controller.show_frame(ManagerLogin))
        Mangbutton2.configure(highlightbackground='#ED7D3B')
        Mangbutton2.pack(pady=10, padx=10)

#####################################################################################################################
#####################################################################################################################
#   CUSTOMER FRAMES!!!

class CustomerLocation(tk.Frame): # Error check: Y , Apply: Y , Write : N
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='#ED7D3B')

        tk.Label(self, text="Customer Frame 1 - Select Location").pack(side=tk.BOTTOM)
        selectLocationLabel = tk.Label(self, text="Select Location", background='#ED7D3B',
                         foreground='#0F3A65', font="Verdana 14 bold")
        selectLocationLabel.pack(pady=10, padx=10)


        # LOCATION OPTION MENU ___________________________________________________________________
        self.locationVar = tk.StringVar(self)
        self.locationVar.set("Select")
        locationList = ["Blackwood", "Camden", "Philadelphia"]      # HARD CODED
        locationOptionMenu = tk.OptionMenu(self, self.locationVar, *locationList)
        locationOptionMenu.configure(background='#ED7D3B')
        locationOptionMenu.pack()
        # ________________________________________________________________________________________



        # BUTTONS ________________________________________________________________________________
        nextButton = tk.Button(self, text="Next",
                               command=lambda: controller.combine_funcs(
                                   controller.dynamicLocation(CustomerPickDate,"c"),

                                   self.errorCheck(controller,self.locationVar),
                                   ))
        nextButton.configure(highlightbackground='#ED7D3B')
        nextButton.pack()

        backButton = tk.Button(self, text="Back",
                               command=lambda: controller.show_frame(StartPage))
        backButton.configure(highlightbackground='#ED7D3B')
        backButton.pack()
        # ________________________________________________________________________________________

    def apply(self,location):
        print(location)

    def errorCheck(self,controller,location):
        # Note optionMenu default is "select", that means they didnt select anything
        locationVar = location.get() # Get value
        Message = "None"
        if locationVar == "Select":
            Message = "Select a location"
        if Message == "None":
            self.apply(locationVar) # Show what user selected / probly write into/store
            controller.show_frame(CustomerPickDate)
        else: # Error!/Invalid!
            popup = tk.Toplevel()
            label1 = tk.Label(popup, text=Message, height=10, width=30)
            label1.pack()
            cancelButton = tk.Button(popup, text="OK",
                                     command=lambda: popup.destroy())
            cancelButton.pack(padx = 10,pady = 10)


class CustomerPickDate(tk.Frame):  # Error check: Y , Apply:Y, Write : N
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#ED7D3B')
        self.controller = controller  # Help Access the controller + its methods
        self.CustomerLocation = self.controller.get_page(CustomerLocation)  # Access to Frame CustomerLocation
        self.variableLocation = self.CustomerLocation.locationVar

        tk.Label(self, text="Customer Frame 2 - Select Date").pack(side=tk.BOTTOM)

        label = tk.Label(self, text="Select Date", font=LARGE_FONT, background='#ED7D3B',
                         foreground='#0F3A65')
        label.pack(pady=10, padx=10)

        # DYNAMIC LABELS ________________________________________________________________________
        self.locationLabel = tk.Label(self, text="EMPTY", background='#ED7D3B',
                         foreground='#0F3A65', font="Verdana 14 bold")
        self.locationLabel.pack(pady=10, padx=10)
        # ________________________________________________________________________________________


        # DATE/MONTH/DAY _________________________________________________________________________
        monthLabel = tk.Label(self, text="Select Month", background='#ED7D3B',
                              foreground='#0F3A65', font="Verdana 14 bold")
        monthLabel.pack()
        self.variablemonth = tk.StringVar() # VAR!
        self.variablemonth.set("Select")
        alistmonth = ["01", "02", "03", "04", "05", "06", "07", "08",
                      "09", "10", "11", "12"]  # dynamica
        monthOptionMenu = tk.OptionMenu(self, self.variablemonth, *alistmonth)
        monthOptionMenu.configure(background='#ED7D3B')
        monthOptionMenu.pack()

        dayLabel = tk.Label(self, text="Select Day", background='#ED7D3B',
                            foreground='#0F3A65', font="Verdana 14 bold")
        dayLabel.pack()
        determonth = self.variablemonth.get()

        self.variableday = tk.StringVar()# VAR!
        self.variableday.set("Select")
        thirtydaylist = ['04', '06', '09', '11']
        thirtyonedaylist = ['01', '03', '05', '07', '08', '10', '11', '12']
        alistdays = ["01", "02", "03", "04", "05", "06", "07", "08",
                     "09", "10", "11", "12", "13", "14", "15", "16", "17",
                     "18", "19", "20", "21", "22", "23", "24", "25", "26",
                     "27", "28", "29", "30", "31"]
        dayOptionMenu = tk.OptionMenu(self, self.variableday, *alistdays)  # tHE OPTION MENU
        dayOptionMenu.configure(background='#ED7D3B')
        dayOptionMenu.pack()
        # ________________________________________________________________________________________


        # BUTTONS ________________________________________________________________________________
        NextButton = tk.Button(self, text="Next",
                               command=lambda: controller.combine_funcs(
                                   self.errorCheck(controller,self.variablemonth,
                                                                        self.variableday),
                                                                        self.storevalue(),
                               print(controller.availablemovies)))
        NextButton.pack()

        BackButton = tk.Button(self, text="Back",
                               command=lambda: controller.show_frame(CustomerLocation))
        BackButton.pack()
        # ________________________________________________________________________________________



    def storevalue(self):
        controller.pickedlocation= self.CustomerLocation.locationVar.get()
        controller.pickedmonth = self.variablemonth.get()
        controller.pickedday = self.variableday.get()

        #self.seatfile = 'locations/%s/%s/%s/%s/seats/%s.txt' % (controller.pickedlocation,
         #        controller.pickedmonth,controller.pickedday,
         #        controller.pickedshowroom,controller.pickedtime)

        #f = open(self.seatfile,'a+')
        #f.write(controller.pickedmovie+"\n")
        #f.close()
        templist = []
        templist2 = [[],[],[]]
        templist3 = []
        num =0
        x=0

        for i in ["A","B","C"]:
            movienames ='locations/%s/%s/%s/%s/MovieInfo.txt' % (controller.pickedlocation,controller.pickedmonth,controller.pickedday,i)

            with open(movienames,'r') as f:
                templist += f.read().splitlines()

            movietimes = 'locations/%s/%s/%s/%s/MovieTimes.txt' % (controller.pickedlocation,controller.pickedmonth,controller.pickedday,i)

            with open(movietimes,'r') as f:
                templist2[num] += f.read().splitlines()
            num += 1

        controller.allmovieinfo = templist
        controller.movietimeslist = templist2

        while x <9:
            templist3.append(controller.allmovieinfo[x])
            x+=3

        controller.availablemovies = templist3

        # print(controller.allmovieinfo)
        # print(controller.availablemovies)
        # print(controller.movietimeslist)

    def apply(self,month,day):
        print(month,day)
        controller.pickedlocation = self.CustomerLocation.locationVar.get()
        controller.pickedmonth = month
        controller.pickedday = day

    def errorCheck(self,controller,variablemonth,variableday):
        # Note optionMenu default is "select", that means they didnt select anything
        monthVar = variablemonth.get() # Get value
        dayVar = variableday.get()
        Message = ""
        if monthVar == "Select":
            Message = "Select a Month"
        if dayVar == "Select":
            Message += "Select a Day"
        if Message == "":
            self.apply(monthVar,dayVar) # Show what user selected / probly write into/store
            controller.show_frame(CustomerPickMovie)
        else: # Error!/Invalid!
            popup = tk.Toplevel()
            label1 = tk.Label(popup, text=Message, height=10, width=30)
            label1.pack()
            cancelButton = tk.Button(popup, text="OK",
                                     command=lambda: popup.destroy())
            cancelButton.pack(padx = 10,pady = 10)


class CustomerPickMovie(tk.Frame): # Error check: Y , Apply/Write : N
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='#ED7D3B')


        tk.Label(self, text="Customer Frame 3 - Select Movie").pack(side=tk.BOTTOM)

        tk.Label(self, text="Available Movies", background='#ED7D3B',
                         foreground='#0F3A65', font="Verdana 14 bold").pack(pady=10, padx=10)
        time = tk.StringVar()
        #self.MovieLabel1 = tk.Label(self, text="Dr. Strange") # Need to read from notepad / text file
        #self.MovieLabel1.pack(side="top")
        self.MovieDic = {"Dr.Strange ":["1:00","3:00","5:00","7:00","9:00"],
                     "Bee Movie ":["12:00-1:00","1:00-2:00","2:00-3:00"],
                          "Star Wars , Rouge One":["12:00-1:00","1:00-2:00","2:00-3:00"]}


        if len(self.MovieDic) < 1:
            self.MovieDic = {"Default": ["Null", "Null"]}
        self.movieVar = tk.StringVar()
        self.movieVar.set("Select")
        self.timeVar = tk.StringVar()
        self.timeVar.set("Select")

        #self.movieVar.trace('w', self.update_options)
        self.movieOptionMenu = tk.OptionMenu(self, self.movieVar, *self.MovieDic.keys())
        self.timeOptionMenu = tk.OptionMenu(self, self.timeVar, '')

        self.movieOptionMenu.configure(background='#ED7D3B')
        self.timeOptionMenu.configure(background='#ED7D3B')
        self.movieOptionMenu.pack()
        self.timeOptionMenu.pack()


        NextButton = tk.Button(self, text="Next",
                               command=lambda: controller.combine_funcs(
                                   self.errorCheck(controller,self.movieVar,self.timeVar)))
        NextButton.pack()

        BackButton = tk.Button(self, text="Back",
                               command=lambda: controller.show_frame(CustomerPickDate))
        BackButton.pack()



    def errorCheck(self,controller,movieVar,timeVar):  # Error if invalid, USED IN APPLYBUTTON
        # Note optionMenu default is "select", that means they didnt select anything
        LocationList = ["Blackwood", "Camden", "Philadelphia"]
        movieVariable = movieVar.get()
        timeVariable = timeVar.get()
        Message = ""
        if movieVariable == "Select":
            Message = "Select a movie"
        if timeVariable == "Select":
            Message = "Select a time"

        if Message == "":
            controller.show_frame(CustomerSeatMap)
        else:
            popup = tk.Toplevel()
            label1 = tk.Label(popup, text=Message, height=10, width=30)
            label1.pack()
            cancelButton = tk.Button(popup, text="OK",
                                     command=lambda: popup.destroy())
            cancelButton.pack()
    """
    def update_options(self):
        movies = self.MovieDic[self.movieVar.get()]
        self.timeVar.set(movies[0])

        menu = self.timeOptionMenu['menu']
        menu.delete(0, 'end')

        for movie in movies:
            menu.add_command(label=movie, command=lambda Movie=movie: self.timeVar.set(Movie))
    """

class CustomerSeatMap(tk.Frame): # Error check: N , Apply/Write : N
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#ED7D3B')

        row = 8
        column = 14
        buttonnumber = row * column
        buttonlist = [0] * buttonnumber
        currentbutton = 0

        rowlist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']
        columnlist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']

        self.selectedseat = tk.IntVar()
        rowlabels = [0] * row
        rowIter = 0
        columnlabels = [0] * column
        #colnum = 0
        colIter = 0

        purchasedseats = [8, 5, 1, 13]


        # ROW/COL PRINTING_________________________________________________________________________
        for r in range(0, row):
            rowlabels[rowIter] = tk.StringVar()
            label = tk.Label(self, textvariable=rowlabels[rowIter], background='#ED7D3B', foreground='#0F3A65',
                             font="Verdana 14 bold")

            rowlabels[rowIter].set(rowlist[rowIter])

            label.grid(row=rowIter + 1, column=0)
            rowIter += 1


        for c in range(0, column):
            columnlabels[colIter] = tk.StringVar()
            label = tk.Label(self, textvariable=columnlabels[colIter], background='#ED7D3B', foreground='#0F3A65',
                             font="Verdana 14 bold")

            columnlabels[colIter].set(columnlist[colIter])
            label.grid(row=0, column=colIter + 1)
            colIter += 1
        # ________________________________________________________________________________________


        # CREATING CHECKBUTTONS___________________________________________________________________
        for i in range(0 + 1, row + 1):
            for x in range(0 + 1, column + 1):

                if currentbutton in purchasedseats:
                    buttonlist[currentbutton] = tk.Checkbutton(self, text="", onvalue=currentbutton, state='disabled',
                                                               background='#ED7D3B')
                else:
                    buttonlist[currentbutton] = tk.Checkbutton(self, text="", onvalue=currentbutton, variable= self.selectedseat,
                                                               background='#ED7D3B')

                buttonlist[currentbutton].grid(row=i, column=x)
                currentbutton += 1
        # ________________________________________________________________________________________



        NextButton = tk.Button(self, text="Next",
                                       command=lambda: controller.combine_funcs(controller.show_frame(CustomerPayment),self.storevalue()))
        NextButton.grid(row=10, column=8)

        BackButton = tk.Button(self, text="Back",
                                       command=lambda: controller.show_frame(CustomerPickMovie))
        BackButton.grid(row=11, column=8)
        BackButton.configure(background='#ED7D3B')


        # tk.Label(self, text="Customer Frame 4 - Seating Map").pack(side=tk.BOTTOM)
        #
        # Seatinglabel = tk.Label(self, text="Seating", font=LARGE_FONT)
        # Seatinglabel.pack(pady=10, padx=10)
        # self.SeatingMap = MM.mapPrinter(5, 5, ["A1", "B2", "E4", "E5"]) # Probly need to be dynamic
        #
        # SeatingMaplabel = tk.Label(self, text=" " + self.SeatingMap, font=LARGE_FONT)
        # SeatingMaplabel.pack()
        #
        # Seatlabel = tk.Label(self, text="Select Seat")
        # Seatlabel.pack(pady=10, padx=10)
        #
        # SeatEntry = tk.Entry(self, bd=5)
        # SeatEntry.pack()
        #
        # NextButton = tk.Button(self, text="Next",
        #                        command=lambda: controller.show_frame(CustomerPayment))
        # NextButton.pack()
        #
        # BackButton = tk.Button(self, text="Back",
        #                        command=lambda: controller.show_frame(CustomerPickMovie))
        # BackButton.pack()
        # BackButton.configure(background='#ED7D3B')

    def storevalue(self):
       controller.pickedseat = self.selectedseat.get()
       print(controller.pickedseat)


class CustomerPayment(tk.Frame): # Error check: Y , Apply/Write : N
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#ED7D3B')

        tk.Label(self, text="Customer Frame 5 - Payment").pack(side=tk.BOTTOM)
        # CREDITCARD STUFF ________________________________________________________________________
        Paymentlabel = tk.Label(self, text="Payment", background='#ED7D3B',
                                foreground='#0F3A65', font="Verdana 14 bold")
        Paymentlabel.pack()
        PriceLabel = tk.Label(self, text="Your cost is $10", background='#ED7D3B',
                              foreground='#0F3A65', font="Verdana 14 bold")
        PriceLabel.pack()
        CreditCardLabel = tk.Label(self, text="Credit Card", background='#ED7D3B',
                                   foreground='#0F3A65', font="Verdana 14 bold")
        CreditCardLabel.pack()
        CreditCardEntry = tk.Entry(self, bd=5)
        CreditCardEntry.configure(highlightbackground='#ED7D3B')
        CreditCardEntry.pack()
        # ________________________________________________________________________________________

        NextButton = tk.Button(self, text="Next",
                               command=lambda: controller.combine_funcs(self.errorCheck(controller,CreditCardEntry),
                                                                        controller.dynamicDate(CustomerConfirmation),
                                                                        controller.dynamicLocation(CustomerConfirmation,"c")))

        NextButton.pack()
        NextButton.configure(highlightbackground='#ED7D3B')

        BackButton = tk.Button(self, text="Back",
                               command=lambda: controller.show_frame(CustomerSeatMap))
        BackButton.pack()
        BackButton.configure(highlightbackground='#ED7D3B')

    def apply(self,CC):
        print(CC)
    def errorCheck(self, controller, CreditCard):
        # Note optionMenu default is "select", that means they didnt select anything
        CCVar = CreditCard.get() # Get value
        Message = ""
        if CCVar == "":
            Message = "Insert Credit Card "
        if Message == "":
            self.apply(CCVar) # Show what user selected / probly write into/store
            controller.show_frame(CustomerConfirmation)
        else: # Error!/Invalid!
            popup = tk.Toplevel()
            label1 = tk.Label(popup, text=Message, height=10, width=30)
            label1.pack()
            cancelButton = tk.Button(popup, text="OK",
                                     command=lambda: popup.destroy())
            cancelButton.pack(padx = 10,pady = 10)




class CustomerConfirmation(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.configure(background='#ED7D3B')
        self.movieVar = controller.get_page(CustomerPickMovie).movieVar

        # VARS FROM OTHER FRAME ___________________________________________________________________
        self.locationVar = controller.get_page(CustomerLocation).locationVar
        # ________________________________________________________________________________________

        # DYNAMIC LABELS _________________________________________________________________________
        self.locationLabel = tk.Label(self, text="EMPTY" ,
                                      background='#ED7D3B',
                                      foreground='#0F3A65', font="Verdana 14 bold")
        self.locationLabel.pack(padx=5, pady=5)

        self.dateLabel =tk.Label(self, text="EMPTY" ,
                                      background='#ED7D3B',
                                      foreground='#0F3A65', font="Verdana 14 bold")
        self.dateLabel.pack()


        # ________________________________________________________________________________________



        label = tk.Label(self, text="Payed!", background='#ED7D3B',
                         foreground='#0F3A65', font="Verdana 14 bold")
        label.pack(pady=10, padx=10)

        # self.movieVar = tk.StringVar()
        # self.movieVar.set("Select")
        # self.timeVar = tk.StringVar()
        # self.timeVar.set("Select")






        movieTitle = "Bee movie" # Dynamic label
        seatNum = "C4" # Gotta grab
        rateT = "R" # Gotta read from file
        priceP= "10"
        titleLable = tk.Label(self,text = movieTitle,font = LARGE_FONT)
        titleLable.pack()
        seatLable = tk.Label(self,text = seatNum,font = LARGE_FONT)
        seatLable.pack()
        rateLable = tk.Label(self,text = rateT,font = LARGE_FONT)
        rateLable.pack()
        priceLable = tk.Label(self,text = priceP,font = LARGE_FONT)
        priceLable.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button1.configure(highlightbackground='#ED7D3B')

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#ED7D3B')

        label = tk.Label(self, text="Payed!", background='#ED7D3B',
                         foreground='#0F3A65', font="Verdana 14 bold")
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button1.configure(highlightbackground='#ED7D3B')

################################################################################################
################################################################################################
#   MANAGER FRAMES!



class ManagerLogin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#ED7D3B')
        tk.Label(self, text="Manager Frame 0 - login").pack(side=tk.BOTTOM)
        label = tk.Label(self, text="Manager Login", background='#ED7D3B',
                         foreground='#0F3A65', font="Verdana 14 bold")
        label.pack(pady=10, padx=10)

        tk.Label(self, text="Username",background='#ED7D3B',
                         foreground='#0F3A65', font="Verdana 8 bold").pack()
        self.username = tk.Entry(self)
        self.username.configure(highlightbackground='#ED7D3B')
        self.username.pack()

        tk.Label(self, text="Password", background='#ED7D3B',
                 foreground='#0F3A65', font="Verdana 8 bold").pack()
        self.password = tk.Entry(self,show= "*")
        self.password.configure(highlightbackground='#ED7D3B')
        self.password.pack()


        applyButton = tk.Button(self, text="Login",
                                command=lambda:
                                self.errorCheck(self.username,self.password,controller))
        applyButton.configure(highlightbackground='#ED7D3B')
        applyButton.pack(pady=5, padx=5)

        backButton = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame(StartPage))
        backButton.configure(highlightbackground='#ED7D3B')
        backButton.pack(pady=5, padx=5)

    def errorCheck(self,username,password,controller):
        validUsername = "petersux"
        validPassword = "petersux"
        usernameStr = username.get()
        passwordStr = password.get()
        Message = ""
        if usernameStr != validUsername or passwordStr != validPassword:
            Message = "Invalid Login"

        if Message == "":
            controller.show_frame(ManagerLocation)
        else:
            popup = tk.Toplevel()
            label1 = tk.Label(popup, text=Message, height=10, width=30)
            label1.pack()
            cancelButton = tk.Button(popup, text="OK",
                                     command=lambda: popup.destroy())
            cancelButton.pack()





class ManagerLocation(tk.Frame): # Error check: Y , Apply/Write : N
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#ED7D3B')
        tk.Label(self, text="Manager Frame 1 - Select Location").pack(side=tk.BOTTOM)

        # SELECT LOCATION ________________________________________________________________________
        label = tk.Label(self, text="Select Location", background='#ED7D3B',
                         foreground='#0F3A65', font="Verdana 14 bold")
        label.pack(pady=10, padx=10)

        locationList = ["Blackwood", "Camden", "Philadelphia"]      # HARD CODED
        self.locationVar = tk.StringVar()
        self.locationVar.set("Select")

        locationOptionMenu = tk.OptionMenu(self,self.locationVar,*locationList)
        locationOptionMenu.pack()
        # ________________________________________________________________________________________



        # SELECT SHOWROOM ________________________________________________________________________
        self.showroomLabel = tk.Label(self, text="Select Showroom for Location", background='#ED7D3B',
                                 foreground='#0F3A65', font="Verdana 14 bold")
        self.showroomLabel.pack()
        self.variableShowroom = tk.StringVar()
        self.variableShowroom.set("Select")
        alistShowroom = ["A", "B", "C"]
        showroomOptionMenu = tk.OptionMenu(self, self.variableShowroom, *alistShowroom)
        showroomOptionMenu.configure(background='#ED7D3B')
        showroomOptionMenu.pack()
        # ________________________________________________________________________________________


        # SELECT DATE ________________________________________________________________________
        monthLabel = tk.Label(self, text="Select Month", background='#ED7D3B',
                              foreground='#0F3A65', font="Verdana 14 bold")
        monthLabel.pack()
        self.variablemonth = tk.StringVar()
        self.variablemonth.set("Select")
        alistmonth = ["01", "02", "03", "04", "05", "06", "07", "08",
                      "09", "10", "11", "12"]  # dynamic
        monthOptionMenu = tk.OptionMenu(self, self.variablemonth, *alistmonth)
        monthOptionMenu.configure(background='#ED7D3B')
        monthOptionMenu.pack()

        dayLabel = tk.Label(self, text="Select Day", background='#ED7D3B',
                            foreground='#0F3A65', font="Verdana 14 bold")
        dayLabel.pack()
        determonth = self.variablemonth.get()
        self.variableday = tk.StringVar()
        self.variableday.set("Select")
        thirtydaylist = ['04', '06', '09', '11']
        thirtyonedaylist = ['01', '03', '05', '07', '08', '10', '11', '12']
        alistdays = ["01", "02", "03", "04", "05", "06", "07", "08",
                     "09", "10", "11", "12", "13", "14", "15", "16", "17",
                     "18", "19", "20", "21", "22", "23", "24", "25", "26",
                     "27", "28", "29", "30", "31"]
        dayOptionMenu = tk.OptionMenu(self, self.variableday, *alistdays)
        dayOptionMenu.configure(background='#ED7D3B')
        dayOptionMenu.pack()

        # ________________________________________________________________________________________

        ApplyButton = tk.Button(self, text="Apply",
                                command=lambda: controller.combine_funcs(
                                    controller.dynamicShowroom(ManagerSelect),
                                    controller.dynamicLocation(ManagerSelect,"m"),
                                                                         self.storevalue(),
                                                                         self.errorCheckLocation(controller,
                                                                                            self.locationVar,
                                                                                            self.variableShowroom,
                                                                                            self.variablemonth,
                                                                                            self.variableday)))
        ApplyButton.configure(highlightbackground='#ED7D3B')
        ApplyButton.pack(pady=10, padx=10)

        BackButton = tk.Button(self, text="Back",
                               command=lambda: controller.show_frame(StartPage))
        BackButton.configure(highlightbackground='#ED7D3B')
        BackButton.pack(pady=10, padx=10)

    def storevalue(self):
        controller.pickedlocation = self.locationVar.get()
        controller.pickedmonth = self.variablemonth.get()
        controller.pickedday = self.variableday.get()
        controller.pickedshowroom = self.variableShowroom.get()

    def errorCheckLocation(self,controller,location, showroom, month, day):  # Error if invalid, USED IN APPLYBUTTON
        # Note optionMenu default is "select", that means they didnt select anything
        LocationList = ["Blackwood", "Camden", "Philadelphia"]
        locationValue = location.get()
        showroomValue = showroom.get()
        monthvalue = month.get()
        dayvalue = day.get()
        Message = ""
        thirtydaylist = ['04', '06', '09', '11']
        if locationValue not in LocationList:
            Message = "Select location \n"
        if showroomValue == "Select":
            Message += "Select a Showroom\n"

        if monthvalue == "02":
            if int(dayvalue) > 28:
                Message += "Select a Valid Date\n"

        if monthvalue in thirtydaylist:
            if int(dayvalue) > 30:
                Message += "Select a Valid Date\n"

        if monthvalue == "Select":
            Message += "Select a Valid Month\n"

        if dayvalue == "Select":
            Message += "Select a Valid Day\n"

        if Message == "":
            Message = "None"

        if Message == "None":
            controller.show_frame(ManagerSelect)
        else:
            popup = tk.Toplevel()
            label1 = tk.Label(popup, text=Message, height=10, width=30)
            label1.pack()
            cancelButton = tk.Button(popup, text="OK",
                                     command=lambda: popup.destroy())
            cancelButton.pack()



class ManagerSelect(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#ED7D3B')
        self.controller = controller
        tk.Label(self, text="Manager Frame 2 - Select Option").pack(side=tk.BOTTOM)


        # VARS FROM PREV FRAME ___________________________________________________________________
        self.locationVar = controller.get_page(ManagerLocation).locationVar
        self.showroomVar = controller.get_page(ManagerLocation).variableShowroom
        # ________________________________________________________________________________________




        # DYNAMIC LABELS _________________________________________________________________________
        self.locationLabel = tk.Label(self,text = "EMPTY",background='#ED7D3B',
                         foreground='#0F3A65', font="Verdana 14 bold")
        self.locationLabel.pack()
        self.showroomLabel = tk.Label(self, text="EMPTY", background='#ED7D3B',
                                      foreground='#0F3A65', font="Verdana 14 bold")
        self.showroomLabel.pack()
        # ________________________________________________________________________________________


        label = tk.Label(self, text="Select Option", background='#ED7D3B',
                         foreground='#0F3A65', font="Verdana 14 bold")
        label.pack(pady=10, padx=10)


        # BUTTONS LABELS _________________________________________________________________________
        AddMovieButton = tk.Button(self, text="Add Movie",
                                   command=lambda: controller.show_frame(ManagerAddMovie))
        AddMovieButton.configure(highlightbackground='#ED7D3B')
        AddMovieButton.pack()

        EditMovieButton = tk.Button(self, text="Edit Movie",
                                    command=lambda: controller.combine_funcs(
                                        controller.dynamicShowroom(ManagerEditMovie),
                                        controller.dynamicLocation(ManagerEditMovie,"m"),
                                        controller.show_frame(ManagerEditMovie)))
        EditMovieButton.configure(highlightbackground='#ED7D3B')
        EditMovieButton.pack()

        homeButton = tk.Button(self, text="Back to Home",
                               command=lambda: controller.show_frame(StartPage))
        homeButton.configure(highlightbackground='#ED7D3B')
        homeButton.pack()
        # ________________________________________________________________________________________




class ManagerAddMovie(tk.Frame): # Error check:Y , Apply/Write : N
    # Note may need to make vars into attributes (self.variableTime)
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#ED7D3B')


        tk.Label(self, text="Manager Frame 3 - Add Movie").pack(side=tk.BOTTOM)

        # Use lists to add into dropdown menu -> *list
        # SET NAME _______________________________________________________________________________
        tk.Label(self, text="Name of Movie", background='#ED7D3B',
                 foreground='#0F3A65', font="Verdana 14 bold").pack(pady=10, padx=10)
        self.movieVar = tk.Entry(self)
        self.movieVar.configure(highlightbackground='#ED7D3B')
        self.movieVar.pack()
        # moviename.bind('<Return>', return_entry)
        # ________________________________________________________________________________________



        # SELECT TIME ____________________________________________________________________________
        tk.Label(self, text="Select First Showing Time", background='#ED7D3B',
                 foreground='#0F3A65', font="Verdana 14 bold").pack(pady=10, padx=10)
        self.timeVar = tk.StringVar()
        self.timeVar.set("Select")
        alistTime = ["12:00 P.M.", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00",
                     "08:00", "09:00", "10:00", "11:00", "12:00 A.M."]  # dynamic
        timeOptionMenu = tk.OptionMenu(self, self.timeVar, *alistTime)
        timeOptionMenu.configure(background='#ED7D3B')
        timeOptionMenu.pack()

        tk.Label(self, text="Select Last Showing Time", background='#ED7D3B',
                 foreground='#0F3A65', font="Verdana 14 bold").pack(pady=10, padx=10)
        self.variableLastTime = tk.StringVar()
        self.variableLastTime.set("Select")
        alistTime = ["12:00 P.M.", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00",
                     "08:00", "09:00", "10:00", "11:00", "12:00 A.M."]  # dynamic
        LasttimeOptionMenu = tk.OptionMenu(self, self.variableLastTime, *alistTime)
        LasttimeOptionMenu.configure(background='#ED7D3B')
        LasttimeOptionMenu.pack()

        # ________________________________________________________________________________________



        # SELECT DURATION ________________________________________________________________________
        tk.Label(self, text="Movie Duration", background='#ED7D3B',
                 foreground='#0F3A65', font="Verdana 14 bold").pack(pady=10, padx=10)
        self.durationVar = tk.StringVar(self)
        # durationVar.set("Enter # of Minutes")  # default value
        durationEntry = tk.Entry(self, textvariable=self.durationVar)
        durationEntry.pack(side='top')
        durationEntry.configure(highlightbackground='#ED7D3B')
        tk.Label(self, text="(minutes)", background='#ED7D3B',
                 foreground='#0F3A65', font="Verdana 9 bold").pack(side='top')
        # ________________________________________________________________________________________



        # SELECT RATING __________________________________________________________________________
        tk.Label(self, text="Movie Rating", background='#ED7D3B',
                 foreground='#0F3A65', font="Verdana 14 bold").pack(pady=10, padx=10)

        self.ratingVar = tk.StringVar(self)
        self.ratingVar.set("Select")  # default value

        ratingOptionMenu = tk.OptionMenu(self, self.ratingVar, "G", "PG", "PG13", "R", "NC17")
        ratingOptionMenu.configure(background='#ED7D3B')
        ratingOptionMenu.pack(pady=20, padx=20)

        # ________________________________________________________________________________________


        # BUTTONS ________________________________________________________________________________
        applyButton = tk.Button(self, text="Apply",
                                command=lambda:
                                controller.combine_funcs(
                                    self.storevalue(),
                                    self.errorCheckAddMovie(
                                        controller,self.movieVar, self.durationVar,self.ratingVar)
                                ))
        # apply(moviename, variableTime, durationVar, ratingVar)
        applyButton.configure(highlightbackground='#ED7D3B')
        applyButton.pack()

        cancelButton = tk.Button(self, text="Cancel",
                                 command=lambda: controller.show_frame(ManagerSelect))
        cancelButton.configure(highlightbackground='#ED7D3B')
        cancelButton.pack()
        # ________________________________________________________________________________________

    def apply(self, name, duration, rating):  # NOTE NAME IS THE ENTRYBOX
        # n = name.get()
        # d = duration.get()
        # r = rating.get()
        data = dt.makeMovie(name, duration, rating)
        outfile = open("anthonysucks.txt", "w")
        outfile.write("Name: {}".format(data.name))
        outfile.close()
        print(lolList)

    def errorCheckAddMovie(self,controller,name, duration, rating):  # Error if invalid
        # Note optionMenu default is "select", that means they didnt select anything
        nameVar = name.get()
        durationVar = duration.get()
        ratingVar = rating.get()
        Message = ""
        if durationVar == "":
            Message = "Invalid duration \n"
        if nameVar == "":
            Message += "Invalid Name\n"
        if ratingVar == "Select":
            Message += "Invalid Rating\n"
        if Message == "":
            Message = "Success!"
        popup = tk.Toplevel()
        label1 = tk.Label(popup, text=Message, height=10, width=30)
        label1.pack()

        if Message == "Success!":
            self.storevalue()
            cancelButton = tk.Button(popup, text="OK",
                                     command=lambda: controller.combine_funcs(controller.show_frame(ManagerSelect),
                                                                              popup.destroy()))
        else:
            cancelButton = tk.Button(popup, text="OK",
                                     command=lambda: popup.destroy())
        cancelButton.pack()

    def storevalue(self):
        controller.pickedmovie = self.movieVar.get()
        movietime = self.timeVar.get()
        lastmovietime = self.variableLastTime.get()
        duration = self.durationVar.get()
        rating = self.ratingVar.get()

        LocationList = []

        self.infofile = 'locations/%s/%s/%s/%s/%s.txt' % (
        controller.pickedlocation, controller.pickedmonth, controller.pickedday, controller.pickedshowroom, 'MovieInfo')

        print(self.infofile)

        f = open(self.infofile, 'w+')
        f.write(controller.pickedmovie + "\n")
        f.write(duration + "\n")
        f.write(rating + "\n")
        f.close()

        durint = int(duration)
        firsttimeint = int(movietime[:2])
        lasttimeint = int(lastmovietime[:2])

        hourlength = math.ceil(durint / 60)

        self.timesfile = 'locations/%s/%s/%s/%s/%s.txt' % (
        controller.pickedlocation, controller.pickedmonth, controller.pickedday, controller.pickedshowroom,
        'MovieTimes')

        f = open(self.timesfile, 'w+')
        f.write(movietime + "\n")

        setmovieint = 0
        while setmovieint <= lasttimeint:
            setmovieint += hourlength
            if setmovieint <= lasttimeint:
                timestring = '%d:00\n' % (setmovieint)
                f.write(timestring)
            else:
                f.close()

class ManagerEditMovie(tk.Frame): # Error check: N , Apply/Write : N
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#ED7D3B')
        self.controller = controller
        tk.Label(self, text="Manager Frame 4 - Edit Movie").pack(side=tk.BOTTOM)


        # VARS FROM OTHER FRAME ___________________________________________________________________
        self.locationVar = controller.get_page(ManagerLocation).locationVar
        self.showroomVar = controller.get_page(ManagerLocation).variableShowroom
        # ________________________________________________________________________________________


        # DYNAMIC LABELS _________________________________________________________________________
        self.locationLabel = tk.Label(self, text="EMPTY",
                                      background='#ED7D3B',
                                      foreground='#0F3A65', font="Verdana 14 bold")
        self.locationLabel.pack(padx = 5,pady = 5)
        self.showroomLabel = tk.Label(self,
                                      text="EMPTY" ,
                                      background='#ED7D3B',
                                      foreground='#0F3A65', font="Verdana 14 bold")
        self.showroomLabel.pack()
        # ________________________________________________________________________________________


        whichlabel = tk.Label(self, text="Current Movie:", background='#ED7D3B',
                              foreground='#0F3A65', font="Verdana 10 bold")
        whichlabel.pack()

        self.dynamicLabelC = tk.Label(self,
                                      text= "No Movie Showing Currently",
                                      background='#ED7D3B',
                                      foreground='#0F3A65', font="Verdana 14 bold")
        self.dynamicLabelC.pack()


        renameEntry = tk.Entry(self,bd = 5)
        renameEntry.pack()


        tk.Label(self, text="Movie Duration", background='#ED7D3B',
                 foreground='#0F3A65', font="Verdana 14 bold").pack(pady=10, padx=10)
        self.durationVar = tk.StringVar(self)
        # durationVar.set("Enter # of Minutes")  # default value
        durationEntry = tk.Entry(self, textvariable=self.durationVar)
        durationEntry.pack(side='top')
        durationEntry.configure(highlightbackground='#ED7D3B')
        tk.Label(self, text="(minutes)", background='#ED7D3B',
                 foreground='#0F3A65', font="Verdana 9 bold").pack(side='top')


        RatingLabel = tk.Label(self, text="Movie Rating", background='#ED7D3B', foreground='#0F3A65',
                               font="Verdana 14 bold")

        RatingLabel.pack()

        ratingvar = tk.StringVar(self)
        ratingvar.set("Select")

        ratinglist = ["G", "PG", "PG13", "R", "NC17"]

        RatingMenu = tk.OptionMenu(self, ratingvar, *ratinglist)
        RatingMenu.configure(background='#ED7D3B')
        RatingMenu.pack()

        # Apply = tk.Button(self, text="Apply",
        #                       command=lambda: controller.show_frame(ManagerSelect))
        # Apply.pack()

        backButton = tk.Button(self, text="Back",
                               command=lambda: controller.show_frame(ManagerSelect))
        backButton.configure(highlightbackground='#ED7D3B')
        backButton.pack(side='bottom')

class ManagerDeleteMovie(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Manager Frame 5 - Remove Movie").pack(side=tk.BOTTOM)

        tk.Label(self,text = "Movie in Current Showroom:")




        applyButton = tk.Button(self, text="Apply",
                               command=lambda: controller.show_frame(ManagerSelect))


        backButton = tk.Button(self, text="Back",
                               command=lambda: controller.show_frame(ManagerSelect))
        backButton.configure(highlightbackground='#ED7D3B')
        backButton.pack(side='bottom')
app = controller()
app.title("Prime Ticket Time")
app.mainloop()
# print(lolList)


