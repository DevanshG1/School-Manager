while(True):
	print("                         	Good Morning/Evening. Welcome To The New School Manager. I shall help you Add,Delete,Update and Display Records.")
#Creating Database Connectivity
	import mysql.connector as T
	Passwd=input("Enter the Password To continue")
	database=T.connect(host="localhost",user="root",passwd=Passwd)
	P=database.cursor()
#Creating the Database
	P.execute("CREATE DATABASE IF NOT EXISTS School_Records")
	P.execute("USE School_Records")
#Creating Requiered tables
	P.execute("CREATE TABLE IF NOT EXISTS Admin_Records(Admin_No int primary key, Name varchar(50), Section varchar(50), Address varchar(50))")
	P.execute("CREATE TABLE IF NOT EXISTS Class_Records(Admin_No int Primary Key, Roll_No int , Name varchar(50), Section varchar(50), Percentage float(2,2))")
	P.execute("CREATE TABLE IF NOT EXISTS Teacher_Records(Emp_ID int primary key, First_Name varchar(50), Last_Name varchar(50), Subject varchar(50))")
	P.execute("CREATE TABLE IF NOT EXISTS Sweepers_Records(Emp_ID int primary key, First_Name varchar(50), Last_Name varchar(50))")
	P.execute("CREATE TABLE IF NOT EXISTS Security_Records(Emp_ID int primary key, First_Name varchar(50), Last_name varchar(50))")
#Creating the First menu
    while True:
        print('Which set of data do you wanna view\n 1. Students (Admin Records)\n 2. Students (Class Records)\n 3. Teachers\n 4. Other Employees   ')
#The respnose to the above questions and creating a path
    	a1=int(input("Enter your Choice 1,2,3,4"))
    	if a1==1:
        	print('                         	You have Choosen Students Admin Records. If you wish to display the data press 1-\n If you wish to add data press 2-\n If you wish to delete data press 3-\n If you wish to update data press 4-\n If you wish to search for a specefic student press 5-')
#Respone to the above questio
        	a2=int(input("Enter your choice 1,2,3,4,5"))
        	if a2==1:
            	P.execute("SELECT * FROM Admin_Records")
            	z1=P.fetchall()
            	for x in z1:
                	print(x)
        	if a2==2:
            	a3='y'
            	while a3=='y':
                	ad1=input('Enter the Admission Number')
                	n1=input("Enter the name that you want to add")
                	sec1=input('Enter the Section')
                	add1=input('Enter the Address')
                	P.execute("INSERT INTO Admin_Records values('"+ad1+"','"+n1+"','"+sec1+"','"+add1+"')")
                	a3=input('Do You want to continue to keep adding records?(y/n)')
        	if a2==3:
            	a4='y'
            	while a4=='y':
                	ad2=input('Enter the Admission Number')
                	P.execute("DELETE FROM Admin_Records WHERE Admin_No='"+ad2+"'")
                	a4=input('Do You want to continue to keep adding records?(y/n)')
        	if a2==4:
            	a5='y'
            	while a5=='y':
                	up1=input("Enter the Admission No. of the students whose data is to be updated")
                	print("Do want to update the 1. Name\n 2. Section\n 3.Address")
                	a6=int(input("Enter your choice 1,2 or 3"))
                	if a6==1:
                    	n2=input("Enter the new Name")
                    	P.execute("UPDATE Admin_Records SET Name='"+n2+"' WHERE Admin_No= '"+up1+"'")
                	if a6==2:
                    	sec2=input("Enter the new Section")
                    	P.execute("UPDATE Admin_Records SET Section='"+sec2+"' WHERE Admin_No= '"+up1+"'")
                	if a6==3:
                    	add2=input('Enter the new Address')
                    	P.execute("UPDATE Admin_Records SET Address='"+add2+"' WHERE Admin_No= '"+up1+"'")
                	a5=input("Do you want to keep updating?(y/n)")
        	if a2==5:
            	a7='y'
            	while a7=='y':
                	s1=input("Enter the Admission No. of the student that you want to search for.")
                	P.execute("SELECT * FROM Admin_Records WHERE Admin_No='"+s1+"'")
                	dis1=P.fetchall()
                	print(dis1)
                	a7=input("Would you like to search for more Records?(y/n)")
#This concludes the display, adding, deleting and Updating of records from Admin tab
#This marks the commencement of the second Class Student Tab
    	if a1==2:
        	print('                         	You chosen Student Class Records. If you wish to display the data press 1\n If you wish to add data press 2\n If you wish to delete the data Press 3\n If you wish to update the data press 4\n If you wish to search for a particular student press 5\n If you wish to view the Record of an entire section press 6.')       	 
#Respone to the above questions
        	b1=int(input("Enter your choice 1,2,3,4"))
        	if b1==1:
            	P.execute("SELECT * FROM Class_Records")
            	z2=P.fetchall()
            	for x in z2:
                	print(x)
        	if b1==2:
            	b2='y'
            	while b2=='y':
                	ad3=input('Enter the Role Number')
                	rno1=int(input('Enter the Role Number'))
                	n3=input("Enter the name that you want to add")
                	sec3=input('Enter the Section')
                	per1=input('Enter the Address')
                	P.execute("INSERT INTO Class_Records values('"+ad3+"','"+rno1+"','"+n3+"','"+sec3+"','"+per1+"')")
                	b2=input('Do You want to continue to keep adding records?(y/n)')
        	if b1==3:
            	b3='y'
            	while b3=='y':
                	rno2=input('Enter the Role Number')
                	sec4=input("Enter the Class in which the student is.")
                	P.execute("DELETE FROM Class_Records WHERE Roll_No='"+rno2+"' Section='"+sec4+"'")
                	b3=input('Do You want to continue to keep adding records?(y/n)')
        	if b1==4:
            	b4='y'
            	while b4=='y':
                	up2=input("Enter the Admission No. of the students whose data is to be updated")
                	print("Do want to update the 1. Name\n 2. Section\n 3.Percentage")
                	b5=int(input("Enter your choice 1,2 or 3"))
                	if b5==1:
                    	n4=input("Enter the new Name")
                    	P.execute("UPDATE Class_Records SET Name='"+n4+"' WHERE Admin_No= '"+up2+"'")
                	if b5==2:
                    	sec5=input("Enter the new Section")
                    	P.execute("UPDATE Class_Records SET Section='"+sec5+"' WHERE Admin_No= '"+up2+"'")
                	if b5==3:
                    	per2=float(input('Enter the new Percentage'))
                    	P.execute("UPDATE Class_Records SET Percentage='"+per2+"' WHERE Admin_No= '"+up2+"'")
                	b4=input("Do you want to keep updating the Records?(y/n)")
        	if b1==5:
            	b6='y'
            	while b6=='y':
                	s2=input("Enter the Admission No. of the student that you want to search for.")
                	P.execute("SELECT * FROM Class_Records WHERE Admin_No='"+s2+"'")
                	dis2=P.fetchone()
                	print(dis2)
                	b6=input("Would you like to search for more Records?(y/n)")
       	 
        	if b1==6:
            	b7='y'
            	while b7=='y':
                	sec6=input("Enter the Class Name")
                	P.execute("SLECT * FROM Class_Records WHERE Section='"+sec6+"'")
                	dis3=P.fetchall()
                	print(dis3)
                	b7=input("Would you like to see Records of another class?(y/n)")
#The segment for Class Records end here
#The segment for Teacher Records start here
    	if a1==3:
        	print('You have chosen the Teachers table. To display Records press 1\n To add Records press 2\n To delete records press 3\n To update records press 4\n To Search for a Specefic Record press 5')
#Response to the above question
        	c1=int(input("Enter your choice 1,2,3,4 or 5"))
        	if c1==1:
            	P.execute("SELECT * FROM Teacher_Records")
            	z3=P.fetchall()
            	for x in z3:
                 	print(x)
        	if c1==2:
            	c2='y'
            	while c2=='y':
                	emp1=input('Enter the Role Number')
                	fname1=input('Enter the First Name')
                	lname1=input('Enter the Last Name')
                	sub1=input('Enter the Subject taught')
                	P.execute("INSERT INTO Teacher_Records values('"+emp1+"','"+fname1+"','"+lname1+"','"+sub1+"')")
                	c2=input("Do you wish to add more records?(y/n)")
        	if c1==3:
            	c3='y'
            	while c3=='y':
                	emp2=input("Enter the Employee Id")
                	P.execute("DELETE FROM Teacher_Records WHERE Emp_ID='"+emp2+"'")
        	if c1==4:
            	c4='y'
            	while c4=='y':
                	up3=input("Enter the Employee Id of the Teachers whose data is to be updated")
                	print("Do want to update the 1. First Name\n 2. Last Name\n 3.Subject")
                	c5=int(input("Enter your choice 1,2 or 3"))
                	if c5==1:
                    	fname2=input("Enter the First Name")
                    	P.execute("UPDATE Teacher_Records SET First_Name='"+fname2+"' WHERE Emp_ID= '"+up3+"'")
                	if c5==2:
                    	lname2=input("Enter the new Last Name")
                    	P.execute("UPDATE Teacher_Records SET Last_Name='"+lname2+"' WHERE Emp_ID= '"+up3+"'")
                	if c5==3:
                    	sub2=input('Enter the new Subject')
                    	P.execute("UPDATE Teacher_Records SET Subject='"+sub2+"' WHERE Emp_ID= '"+up3+"'")
                	c4=input("Do you want to keep updating the Records?(y/n)")
        	if c1==5:
            	c6='y'
            	while c6=='y':
                	s3=input("Enter the Employee ID")
                	P.execute("SELECT * FROM Teacher_Records WHERE Emp_ID='"+s3+"'")
                	dis3=p.fetchall()
                	print(dis3)
            	c6=input("Would you like to search for more records?(y/n)")
    	if a1==4:
        	print("You have selected the Other employess option. For Maid and Sweeper Records press 1\n For Security Staff Records Press 2")
        	a10=int(input("Enter your choice 1 or 2."))
        	if a10==1:
            	print('You have chosen the Maid and Sweeper table. To display Records press 1\n To add Records press 2\n To delete records press 3\n To update records press 4\n To Search for a Specefic Record press 5')
#Response to the above question
            	d1=int(input("Enter your choice 1,2,3,4 or 5"))
            	if d1==1:
                	P.execute("SELECT * FROM Sweepers_Records")
                	z4=P.fetchall
                	for x in z4:
                     	print(x)
            	if d1==2:
                	d2='y'
                	while d2=='y':
                    	Emp1=input('Enter the Employee ID')
                    	Fname1=input('Enter the First Name')
                    	Lname1=input('Enter the Last Name')
                    	P.execute("INSERT INTO Sweepers_Records values('"+Emp1+"','"+Fname1+"','"+Lname1+"')")
                	d2=input("Do you wish to add more records?(y/n)")
            	if d1==3:
                	d3='y'
                	while d3=='y':
                    	Emp2=input("Enter the Employee Id")
                    	P.execute("DELETE FROM Sweepers_Records WHERE Emp_ID='"+Emp2+"'")
                    	d3=input('Would you like to delete more records?(y/n)')
            	if d1==4:
                	d4='y'
                	while d4=='y':
                    	up4=input("Enter the Employee Id of the Maid/Sweepers whose data is to be updated")
                    	print("Do want to update the 1. First Name\n 2. Last Name")
                    	d5=int(input("Enter your choice 1,2 or 3"))
                    	if d5==1:
                        	Fname2=input("Enter the First Name")
                        	P.execute("UPDATE Sweepers_Records SET First_Name='"+Fname2+"' WHERE Emp_ID= '"+up4+"'")
                    	if d5==2:
                        	Lname2=input("Enter the new Last Name")
                        	P.execute("UPDATE Sweepers_Records SET Last_Name='"+Lname2+"' WHERE Emp_ID= '"+up4+"'")
                    	d4=input("Do you want to keep updating the Records?(y/n)")
            	if d1==5:
                	d6='y'
                	while d6=='y':
                    	s4=input("Enter the Employee ID")
                    	P.execute("SELECT * FROM Sweepers_Records WHERE Emp_ID='"+s4+"'")
                    	dis4=p.fetchall()
                    	print(dis4)
                	d6=input("Would you like to search for more records?(y/n)")
        	if a10==2:
            	print('You have chosen the Maid and Sweeper table. To display Records press 1\n To add Records press 2\n To delete records press 3\n To update records press 4\n To Search for a Specefic Record press 5')
#Response to the above question
            	e1=int(input("Enter your choice 1,2,3,4 or 5"))
            	if e1==1:
                	P.execute("SELECT * FROM Sweepers_Records")
                	z5=P.fetchall()
                	for x in z5:
                     	print(x)
            	if e1==2:
                	e2='y'
                	while e2=='y':
                    	EMp1=input('Enter the Employee ID')
                    	FName1=input('Enter the First Name')
                    	LName1=input('Enter the Last Name')
                    	P.execute("INSERT INTO Security_Records values('"+emp1+"','"+fname1+"','"+lname1+"')")
                	e2=input("Do you wish to add more records?(y/n)")
            	if e1==3:
                	e3='y'
                	while e3=='y':
                    	EMp2=input("Enter the Employee Id")
                    	P.execute("DELETE FROM Security_Records WHERE Emp_ID='"+emp2+"'")
            	if e1==4:
                	e4='y'
                	while d4=='y':
                    	up5=input("Enter the Employee Id of the Security Staff whose data is to be updated")
                    	print("Do want to update the 1. First Name\n 2. Last Name")
                    	e5=int(input("Enter your choice 1,2 or 3"))
                    	if e5==1:
                        	FName2=input("Enter the First Name")
                        	P.execute("UPDATE Security_Records SET First_Name='"+FName2+"' WHERE Emp_ID= '"+up5+"'")
                    	if e5==2:
                        	LName2=input("Enter the new Last Name")
                        	P.execute("UPDATE Security_Records SET Last_Name='"+LName2+"' WHERE Emp_ID= '"+up5+"'")
                    	e4=input("Do you want to keep updating the Records?(y/n)")
            	if e1==5:
                	e6='y'
                	while e6=='y':
                    	s5=input("Enter the Employee ID")
                    	P.execute("SELECT * FROM Security_Records WHERE Emp_ID='"+s5+"'")
                    	dis5=P.fetchall()
                    	print(dis5)
                    	e6=input("Would you like to search for more records?(y/n)")       	 
	print("                                                    	Thank you for you Patience.")
