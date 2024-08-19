from tkinter import*
import tkinter.font as font
import tkinter.messagebox
import mysql.connector


#mysql DB details

global dbname
global dbuser
global dbpassword

#Change these values as per the mysql details in the machine where it is executed
dbname = "elections"
dbuser = "root"
dbpassword = "a1s2d#"

#Admin User details

global AdminUserName
global AdminPassword

AdminUserName = "a"
AdminPassword = "p"


#Screen Creation Function
def CreateScreen(Parent, Title, Geo, bgclr = 'grey'):

    Screen = Toplevel(Parent)
    Screen.geometry(Geo)
    Screen.title(Title)
    Screen.configure(bg=bgclr)
    return Screen

#Entry Creation Function
def CreateEntry(Parent, x, y, Pos, TxtVar):

    entry = Entry(Parent,textvariable=TxtVar)
    entry.place(relx=x, rely=y, anchor = Pos)

#Button Creation Function
def CreateButton(Parent, x, y, Pos, txt, cmd, btnwidth, btnheight, fnttype=1, bgclr = 'white', fgclr = 'black'):

    if fnttype==1:
        fnt = Font1
    elif fnttype==2:
        fnt = Font2
    else:
        fnt = Font1
        
    btn = Button(Parent, text=txt, font=fnt, bg=bgclr, fg=fgclr, width=btnwidth, height=btnheight, command=cmd)
    btn.place(relx = x, rely = y, anchor = Pos)
    return btn

#Label Creation Function
def CreateLabel(Parent, x, y, Pos, txt, fnttype=1, bgclr = 'grey', fgclr = 'white'):

    if fnttype==1:
        fnt = Font1
    elif fnttype==2:
        fnt = Font2
    else:
        fnt = Font1

    lbl = Label(Parent, text=txt, bg=bgclr, fg=fgclr, font = fnt)
    lbl.place(relx=x, rely=y, anchor=Pos)
    return lbl



#FUNCTION FOR VOTER REGISTRATION SUBMIT BUTTON
def submit_voter():

    if str(voter_username_verify.get()).strip()=="":

        tkinter.messagebox.showerror("Invalid Entry", "Please Enter A Valid Voter Name")

    else:

        voter_username=str(voter_username_verify.get())
    
        voter_list.append(voter_username)
        sql2 = "INSERT INTO v_details (v_name) VALUES ('" + voter_username  + "')"
        mycursor.execute(sql2)
        mydb.commit()
        
        voter_username_entry.delete(0,END)

        global vot
        displayv = "SELECT v_id FROM v_details WHERE v_name ='" + voter_username + "'"
        mycursor.execute(displayv)
        vot = mycursor.fetchone()

        tkinter.messagebox.showinfo("Registration Successful", "Your Voter ID Is: "+str(vot[0]))

    
   


#FUNCTION FOR OPENING VOTER REGISTRATION PAGE
def click_addvoter():
    global voter_reg
    voter_reg=Toplevel()
    voter_reg.title("VOTER REGISTRATION")
    voter_reg.geometry("500x500")
    voter_reg.configure(bg="grey")

   
    global voter_username_entry

    global voter_list
    voter_list=[]

    global voter_username_verify
    voter_username_verify=StringVar()

    Label(voter_reg,text="Enter Voter name:  ",font=Font2,fg="white",bg="grey").grid(row=0,column=0)
    voter_username_entry=Entry(voter_reg,textvariable=voter_username_verify)
    voter_username_entry.grid(row=0,column=1)
    
    Label(voter_reg,text="      ",bg="grey").grid(row=1,column=0)
    Button(voter_reg,text="SUBMIT",font=Font1,fg="black",bg="white",width=10,height=1,command=submit_voter).grid(row=2,column=1)

    

    voter_reg.mainloop()



def loop_next_click_headprefect():

    if str(candidate_name_headprefect.get()).strip()=="":

        tkinter.messagebox.showerror("Invalid Registration", "Please Enter A Valid Candidate Name ")


    else:   

        candidate_name=str(candidate_name_headprefect.get())
        HPlist.append(candidate_name)
        Candidatelist.append(candidate_name)
        candidate_post="HP"

        sql1 = "INSERT INTO c_details (c_name,c_post) VALUES ('" + candidate_name  + "' , '" + candidate_post + "')"
        mycursor.execute(sql1)
        mydb.commit()

        displayc = "SELECT c_id FROM c_details WHERE c_name ='" + candidate_name + "'"
        mycursor.execute(displayc)
        global cand
        cand = mycursor.fetchone()

        candidate_name_headprefect_entry.delete(0,END)

        tkinter.messagebox.showinfo("Candidate ID", "The Candidate's ID Is: "+str(cand[0]))



def loop_next_click_sportscaptain():

    if str(candidate_name_sportscaptain.get()).strip()=="":

        tkinter.messagebox.showerror("Invalid Registration", "Please Enter A Valid Candidate Name ")



    else:   

        candidate_name=str(candidate_name_sportscaptain.get())
        SClist.append(candidate_name)
        Candidatelist.append(candidate_name)
        candidate_post="SC"

        sql1 = "INSERT INTO c_details (c_name,c_post) VALUES ('" + candidate_name  + "' , '" + candidate_post + "')"
        mycursor.execute(sql1)
        mydb.commit()

        displayc = "SELECT c_id FROM c_details WHERE c_name ='" + candidate_name + "'"
        mycursor.execute(displayc)
        global cand
        cand = mycursor.fetchone()
     
        candidate_name_sportscaptain_entry.delete(0,END)

        tkinter.messagebox.showinfo("Candidate ID", "The Candidate's ID Is: "+str(cand[0]))
        


def submit_candidate_hp():

    if str(candidate_name_headprefect.get()).strip()=="":

        tkinter.messagebox.showerror("Invalid Registration", "Please Enter A Valid Candidate Name ")


    else:   

        candidate_name=str(candidate_name_headprefect.get())
        HPlist.append(candidate_name)
        Candidatelist.append(candidate_name)
        candidate_post="HP"

        sql1 = "INSERT INTO c_details (c_name,c_post) VALUES ('" + candidate_name  + "' , '" + candidate_post + "')"
        mycursor.execute(sql1)
        mydb.commit()

        displayc = "SELECT c_id FROM c_details WHERE c_name ='" + candidate_name + "'"
        mycursor.execute(displayc)
        global cand
        cand = mycursor.fetchone()

        candidate_name_headprefect_entry.delete(0,END)

        tkinter.messagebox.showinfo("Candidate ID", "The Candidate's ID Is: "+str(cand[0]))


    ElectionDetails.destroy()


def submit_candidate_sc():

    if str(candidate_name_sportscaptain.get()).strip()=="":

        tkinter.messagebox.showerror("Invalid Registration", "Please Enter A Valid Candidate Name ")



    else:   

        candidate_name=str(candidate_name_sportscaptain.get())
        SClist.append(candidate_name)
        Candidatelist.append(candidate_name)
        candidate_post="SC"

        sql1 = "INSERT INTO c_details (c_name,c_post) VALUES ('" + candidate_name  + "' , '" + candidate_post + "')"
        mycursor.execute(sql1)
        mydb.commit()

        displayc = "SELECT c_id FROM c_details WHERE c_name ='" + candidate_name + "'"
        mycursor.execute(displayc)
        global cand
        cand = mycursor.fetchone()
        
        candidate_name_sportscaptain_entry.delete(0,END)

        tkinter.messagebox.showinfo("Candidate ID", "The Candidate's ID Is: "+str(cand[0]))



    ElectionDetails.destroy()
  

    
    
def next_click():

    global ElectionDetails
    global candidate_name_headprefect_entry
    global candidate_name_headprefect
    

    global candidate_name_sportscaptain_entry
    global candidate_name_sportscaptain
    global candidate_name
    
    candidate_name_headprefect=StringVar()
    candidate_name_sportscaptain=StringVar()

    global Candidatelist
    Candidatelist=[]

    global HPlist
    HPlist=[]

    global SClist
    SClist=[]
    
    if election_no.get()==1:
        
        ElectionDetails=Toplevel(AddElection)
        ElectionDetails.geometry("750x500")
        ElectionDetails.configure(bg="grey")
        ElectionDetails.title("HEAD PREFECT CANDIDATE ENTRY")

            
        Label(ElectionDetails,text="Enter Head Prefect candidate name:",font=Font2,fg="white",bg="grey").grid(row=0,column=0)
        candidate_name_headprefect_entry=Entry(ElectionDetails,textvariable=candidate_name_headprefect)
        candidate_name_headprefect_entry.grid(row=0,column=2)
        Label(ElectionDetails,text="   ",font=Font2,fg="white",bg="grey").grid(row=1,column=0)
        Button(ElectionDetails,text="ADD NEXT",font=Font1,fg="black",bg="white",command=loop_next_click_headprefect).grid(row=2,column=0)
        Button(ElectionDetails,text="SUBMIT",font=Font1,fg="black",bg="white",command=submit_candidate_hp).grid(row=2,column=1)


        ElectionDetails.mainloop()
        
        

    elif election_no.get()==2:
        
        ElectionDetails=Toplevel(AddElection)
        ElectionDetails.geometry("750x500")
        ElectionDetails.configure(bg="grey")
        ElectionDetails.title("SPORTS CAPTAIN CANDIDATE ENTRY")

            
        Label(ElectionDetails,text="Enter Sports Captain candidate name:",font=Font2,fg="white",bg="grey").grid(row=0,column=0)
        candidate_name_sportscaptain_entry=Entry(ElectionDetails,textvariable=candidate_name_sportscaptain)
        candidate_name_sportscaptain_entry.grid(row=0,column=2)
        Label(ElectionDetails,text="   ",font=Font2,fg="white",bg="grey").grid(row=1,column=0)
        Button(ElectionDetails,text="ADD NEXT",font=Font1,fg="black",bg="white",command=loop_next_click_sportscaptain).grid(row=2,column=0)
        Button(ElectionDetails,text="SUBMIT",font=Font1,fg="black",bg="white",command=submit_candidate_sc).grid(row=2,column=1)


        ElectionDetails.mainloop()



    else:

        tkinter.messagebox.showerror("No Option Selected", "Please Select A Post")
            
               

        
            
     
#FUNCTION FOR CANDIDATE REGISTRATION
def click_addelection():
    global AddElection
    AddElection=Toplevel()
    AddElection.geometry=("500x500")
    AddElection.title("CHOOSE ELECTION")
    AddElection.configure(bg="grey")

    
    global election_no
    election_no=IntVar()

    
    
    Label(AddElection,text="Choose election to add candidates: ",font=Font2,bg="grey",fg="white").grid(row=0,column=0) 
    Radiobutton(AddElection,text="Head  Prefect  ",font=Font1,variable=election_no,value=1).grid(row=1,column=0,sticky=W)
    Radiobutton(AddElection,text="Sports Captain",font=Font1,variable=election_no,value=2).grid(row=2,column=0,sticky=W)
    Label(AddElection,text="  ",font=Font2,bg="grey").grid(row=3,column=0)
    Button(AddElection,text="NEXT",font=Font1,bg="white",fg="black",command=next_click).grid(row=4,column=0)
    
    
    
    


    AddElection.mainloop()

    

#FUNCTION FOR ADMIN LOGIN BUTTON
def login_click():

    if(username_verify.get() == AdminUserName and password_verify.get() == AdminPassword):
        AdminScreen = CreateScreen(AdminLogin, "Admin", "500x300")

        CreateButton(AdminScreen, 0.5, 0.2, CENTER, "Add Voter", click_addvoter, 30, 3, 1, 'white', 'black')
        CreateButton(AdminScreen, 0.5, 0.5, CENTER, "Add Candidate", click_addelection, 30, 3, 1, 'white', 'black')

        AdminScreen.mainloop()
    else:
        tkinter.messagebox.showerror("Invalid Login", "Authentication Failed!")
        


#FUNCTIONS FOR ADMIN AND VOTER BUTTONS i.e IN FIRST PAGE
def admin_click():

    global username_verify
    global password_verify
    global AdminLogin

    username_verify=StringVar()
    password_verify=StringVar()

    AdminLogin = CreateScreen(Home, "Admin Login", "400x200")

    CreateLabel(AdminLogin, 0.1, 0.15, "nw", "User Name ", 2)
    CreateLabel(AdminLogin, 0.1, 0.35, "nw", "Password  ", 2)

    CreateEntry(AdminLogin, 0.5, 0.17, "nw", username_verify)
    CreateEntry(AdminLogin, 0.5, 0.37, "nw", password_verify)

    CreateButton(AdminLogin, 0.3, 0.65, "nw", "Login", login_click, 20, 2)

    AdminLogin.mainloop()
    

def vote_click():
    
    sql3 = "INSERT INTO v_rec (v_id, HP_id, SC_id ) VALUES ('" + str(voter_ID.get())  + "', " + str(voteHP.get())  + ", '" + str(voteSC.get()) + "')"
    print(sql3)
    mycursor.execute(sql3)
    mydb.commit()

    ElectionPage.destroy()
    

    

            
def voter_login_click():

    global ElectionPage

    global HeadPrefect_ID
    HeadPrefect_ID=StringVar()

    global SportsCaptain_ID
    SportsCaptain_ID=StringVar()


    global VoterID_List
    mycursor.execute("SELECT v_id FROM v_details")
    VoterID_List = [row[0] for row in mycursor.fetchall()]

    global VoterName_List
    mycursor.execute("SELECT v_name FROM v_details")
    VoterName_List = [row[0] for row in mycursor.fetchall()]

    Match = False
    Idx = 0

    if ( str(voter_ID.get()).strip() != "" and str(voter_username.get()).strip() != "" ):
    
        vID = voter_ID.get()

        for Id in VoterID_List:
            if Id == int(vID) and VoterName_List[Idx] == voter_username.get():
                Match = True
                break
            Idx = Idx+1

    if Match == False:
        tkinter.messagebox.showerror("Invalid Login", "Please Enter A Valid Username Or ID")

    else:
        global CandidatePost_List
        mycursor.execute("SELECT c_post FROM c_details")
        CandidatePost_List = [row[0] for row in mycursor.fetchall()]
        
        
        global CandidateID_List
        mycursor.execute("SELECT c_id FROM c_details")
        CandidateID_List = [row[0] for row in mycursor.fetchall()]
        


        global CandidateName_List
        mycursor.execute("SELECT c_name FROM c_details")
        CandidateName_List = [row[0] for row in mycursor.fetchall()]
        


        global ln
        ln=len(CandidateID_List)

        global SC_Candidate_List
        SC_Candidate_List=[]

        global HP_Candidate_List
        HP_Candidate_List=[]


        
        sql4="SELECT c_name,c_id FROM c_details WHERE c_post='HP'"
        mycursor.execute(sql4)
        HP_Candidate_List=mycursor.fetchall()
        lnHP=len(HP_Candidate_List)
        


        sql5="SELECT c_name,c_id FROM c_details WHERE c_post='SC'"
        mycursor.execute(sql5)
        SC_Candidate_List=mycursor.fetchall()
        lnSC=len(SC_Candidate_List)

        
        ElectionPage=Toplevel(VoterLogin)
        ElectionPage.title("ELECTIONS SCREEN")
        ElectionPage.geometry("500x500")
        ElectionPage.configure(bg="grey")
        
        Label(ElectionPage,text="Select the Head Prefect candidate :",font=Font1,bg="grey",fg="white").grid(row=0,column=0)

        global voteHP
        voteHP=StringVar()
        voteHP.set("0")
        

        for i in range(lnHP):
               Radiobutton(ElectionPage,text=HP_Candidate_List[i][0]+"  "+str(HP_Candidate_List[i][1]),variable=voteHP,value=HP_Candidate_List[i][1],width=20).grid(row=i+2,column=0)
               
        


        Label(ElectionPage,text="Select the Sports Captain candidate :",font=Font1,bg="grey",fg="white").grid(row=0,column=1)
        
        global voteSC
        voteSC=StringVar()
        voteSC.set("0")

        for j in range(lnSC):
               Radiobutton(ElectionPage,text=SC_Candidate_List[j][0]+"  "+str(SC_Candidate_List[j][1]),variable=voteSC,value=SC_Candidate_List[j][1],width=20).grid(row=j+2,column=1)
               

        

        Label(ElectionPage,text="   ",bg="grey").grid(row=6,column=0)
        Button(ElectionPage,text="VOTE",font=Font1,bg="white",fg="black",command=vote_click).grid(row=20,column=0,sticky=W)



        ElectionPage.mainloop()

    
def voter_click():
    global VoterLogin
    VoterLogin=Toplevel(Home)
    VoterLogin.title("VOTER LOGIN")
    VoterLogin.geometry("430x150")
    VoterLogin.configure(bg="grey")

    global voter_username
    voter_username=StringVar()

    global voter_ID
    voter_ID=StringVar()
 
    Label(VoterLogin,text="   Enter Voter Name:  ",font=Font2,fg="white",bg="grey").grid(row=0,column=0)
    voter_username_login=Entry(VoterLogin,textvariable=voter_username)
    voter_username_login.grid(row=0,column=1)

    Label(VoterLogin,text="Enter Voter ID:     ",font=Font2,fg="white",bg="grey").grid(row=1,column=0)
    voter_ID_login=Entry(VoterLogin,textvariable=voter_ID)
    voter_ID_login.grid(row=1,column=1)


    Label(VoterLogin,text="      ",bg="grey").grid(row=2,column=0)

    Button(VoterLogin,text="LOGIN",font=Font1,fg="black",bg="white",width=10,height=1,command=voter_login_click).grid(row=3,column=1)

    VoterLogin.mainloop()


def PrintHPResults(ResultPage):

    sql="SELECT c_name,c_id FROM c_details WHERE c_post='HP'"
    mycursor.execute(sql)
    HP_CandidateID_List=mycursor.fetchall()

    HPWinnerName = "None"
    HPWinnerId = 0
    HPWinnerVotes = 0
    HPCandidateId = 0
    HPCandidateName = "None"
    HPCandidateVotes = 0
    HPResultsList = []

    counter = 0

    #lbl = Label(ResultPage, text="HP CandidateId")
    #lbl.place(relx=0.1, rely=0.1, anchor="nw")


    CreateLabel(ResultPage, 0.1, 0.03, "nw","Head Prefect Election Results", 2, "grey", "red")
    CreateLabel(ResultPage, 0.1, 0.1, "nw", "Id            ")
    CreateLabel(ResultPage, 0.15, 0.1, "nw", "Name                            ")
    CreateLabel(ResultPage, 0.3, 0.1, "nw", "Votes ")

    HP_No_Of_Votes_List=[]
    
    for c in HP_CandidateID_List:
        filter2 = "SELECT * FROM v_rec WHERE HP_id = " + str(c[1])
        mycursor.execute(filter2)  
        mycursor.fetchall()

        HPCandidateId = c[1]
        HPCandidateName = c[0]
        HPCandidateVotes = mycursor.rowcount
        HP_No_Of_Votes_List.append(HPCandidateVotes)

        #Update Winner data, if the vote is high
        if HPCandidateVotes > HPWinnerVotes:
            HPWinnerName = HPCandidateName
            HPWinnerId = HPCandidateId
            HPWinnerVotes = HPCandidateVotes
            
        counter = counter+1
        CreateLabel(ResultPage, 0.1, 0.1+(counter*0.05), "nw", str(HPCandidateId))
        CreateLabel(ResultPage, 0.15, 0.1+(counter*0.05), "nw", HPCandidateName)
        CreateLabel(ResultPage, 0.3, 0.1+(counter*0.05), "nw", str(HPCandidateVotes))

    counter=counter+1

    if HP_No_Of_Votes_List.count(HPWinnerVotes)>1:

         CreateLabel(ResultPage, 0.1, 0.1+(counter*0.05), "nw", "There is a draw", 2, "grey", "blue")

    else:

        CreateLabel(ResultPage, 0.1, 0.1+(counter*0.05), "nw", "The Head Prefect Is: " + HPWinnerName, 2, "grey", "blue")
    
    
    


def PrintSCResults(ResultPage):
    
    sql="SELECT c_name,c_id FROM c_details WHERE c_post='SC'"
    mycursor.execute(sql)
    SC_CandidateID_List=mycursor.fetchall()

    SCWinnerName = "None"
    SCWinnerId = 0
    SCWinnerVotes = 0
    SCCandidateId = 0
    SCCandidateName = "None"
    SCCandidateVotes = 0
    SCResultsList = []

    counter = 0

    CreateLabel(ResultPage, 0.6, 0.03, "nw","Sports Captain Election Results", 2, "grey", "red")
    CreateLabel(ResultPage, 0.6, 0.1, "nw", "Id            ")
    CreateLabel(ResultPage, 0.75, 0.1, "nw", "Name                            ")
    CreateLabel(ResultPage, 0.9, 0.1, "nw", "Votes ")

    SC_No_Of_Votes_List=[]
    
    for c in SC_CandidateID_List:
        filter2 = "SELECT * FROM v_rec WHERE SC_id = " + str(c[1])
        mycursor.execute(filter2)  
        mycursor.fetchall()

        SCCandidateId = c[1]
        SCCandidateName = c[0]
        SCCandidateVotes = mycursor.rowcount
        SC_No_Of_Votes_List.append(SCCandidateVotes)

        #Update Winner data, if the vote is high
        if SCCandidateVotes > SCWinnerVotes:
            SCWinnerName = SCCandidateName
            SCWinnerId = SCCandidateId
            SCWinnerVotes = SCCandidateVotes
            
        counter = counter+1
        CreateLabel(ResultPage, 0.6, 0.1+(counter*0.05), "nw", str(SCCandidateId))
        CreateLabel(ResultPage, 0.75, 0.1+(counter*0.05), "nw", SCCandidateName)
        CreateLabel(ResultPage, 0.9, 0.1+(counter*0.05), "nw", str(SCCandidateVotes))

    counter=counter+1

    if SC_No_Of_Votes_List.count(SCWinnerVotes)>1:

        CreateLabel(ResultPage, 0.6, 0.1+(counter*0.05), "nw", "There is a draw", 2, "grey", "blue")

    else:

        CreateLabel(ResultPage, 0.6, 0.1+(counter*0.05), "nw", "The Sports Captain Is: " + SCWinnerName, 2, "grey", "blue")


#FUNCTION FOR SEE RESULT BUTTON
def results_click():

    ResultPage=Tk()
    ResultPage.title("RESULT PAGE")
    ResultPage.geometry("1200x600")
    ResultPage.configure(bg="grey")

    PrintHPResults(ResultPage)
    PrintSCResults(ResultPage)
    
    ResultPage.mainloop()
    ResultPage=Toplevel(Home)
    
 

#Main Function Starts here       

Home=Tk()
Home.title("Elections")
Home.geometry("1000x500")
Home.configure(bg="grey")


#Connect to DB
mydb = mysql.connector.connect(
  host="localhost",
  user=dbuser,
  password=dbpassword,
  database=dbname
)
mycursor=mydb.cursor()

#Create Fonts
global Font1
Font1=font.Font(family="Helvetica",weight="bold",size=10)
global Font2
Font2=font.Font(family="Helvetica",weight="bold",size=20)


#BUTTON FOR ADMIN AND VOTER AND SEE RESULTS

CreateButton(Home, 0.5, 0.2, CENTER, "ADMIN", admin_click, 30, 3, 1, 'white', 'black')
CreateButton(Home, 0.5, 0.4, CENTER, "VOTER", voter_click, 30, 3, 1, 'white', 'black')
CreateButton(Home, 0.5, 0.6, CENTER, "RESULTS", results_click, 30, 3, 1, 'white', 'black')
CreateButton(Home, 0.5, 0.8, CENTER, "EXIT", Home.destroy, 20, 2, 1, 'white', 'red')

Home.mainloop()



