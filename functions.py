from datetime import date
import read_data as rd
import sys

"""
This bloc contains the admin functions
"""

# 1
def displayStat():
    """This function display how many jobs are to be printed today """
    timestamp = date.today().strftime('%Y%m%d')
    job_counter = 0
    current = rd.pq.head
    while current: # O(n)
        if current.priority[0] == int(timestamp):
            job_counter+=1
        current = current.next
    print()
    print("You have", job_counter, "job to be printed today.")

#####################################################################
# 2
def addJob():
    """This function is used to add a new job"""
    print()
    username = input("Enter the username:")
    priority = input("Enter the priority:")
    job_id = "job"+str(rd.pq.max_job_id+1)
    timestamp = date.today().strftime('%Y%m%d')

    rd.pq.enqueue([job_id, username] ,[int(timestamp), int(priority)])
    print("Job added successfully")
    rd.pq.print_q()

#####################################################################
# 3
def displayJobs():
    """This function show jobs registered in the system starting from today"""
    timestamp = date.today().strftime('%Y%m%d')
    current = rd.pq.head
    while current: # O(n)
        if str(current.priority[0]) >= timestamp:
            print(current.value[0])
        current = current.next

#####################################################################
# 4
def changeJobsPriority():
    """This function change a job priority"""
    print()
    job_id = input("Enter the job id:")
    current = rd.pq.head
    flag = False

    while current: # O(n)
        if current.value[0] == job_id:
            priority = input("Enter the job priority:")
            username = current.value[1]
            date = current.priority[0]
            rd.pq.remove(current.value)
            rd.pq.enqueue([job_id, username], [date, int(priority)])
            print("Priority changed successfully")
            flag = True
            break
        current = current.next
    if flag==False:
        print("Job id not found")
        changeJobsPriority()
    # rd.pq.print_q()

#####################################################################
# 5
def removeJob():
    """This function is used to remove a job"""
    print()
    job_id = input("Enter the job id:")
    
    flag = False
    current = rd.pq.head
    while current: # O(n)
        if current.value[0] == job_id:
            rd.pq.remove(current.value)
            print("Job removed successfully") 
            flag=True
            break
        current = current.next
    if flag==False:
        print("Job id not found")
        removeJob()
    # rd.pq.print_q()

#####################################################################
# 6
def runPrinter():
    """This function is used to run the printer"""
    timestamp = date.today().strftime('%Y%m%d')
    current = rd.pq.head
    while current: # O(n)
        if current.priority[0] == int(timestamp):
            rd.pq.dequeue(current.priority)
            print(current.value[0], current.priority[1])
        current = current.next
    # rd.pq.print_q()

#####################################################################
# 7
def exit():
    """This function exit the running task"""
    print("You have logged out")
    sys.exit()



#####################################################################
#####################################################################
#####################################################################

"""
This bloc contains the admin functions
"""

# 1
def addNewJob(user_name):
    """This function add new job"""
    username = user_name
    timestamp = date.today().strftime('%Y%m%d')
    rd.pq.max_job_id = rd.pq.max_job_id + 1
    job_id = "job"+str(rd.pq.max_job_id)
    rd.pq.enqueue([job_id, username], [int(timestamp), 0])
    rd.pq.print_q()

#####################################################################
# 2
def exit2():
    """This function is used to save data to the text file and exit the task"""

    file = open("database.txt", "w")
    current = rd.pq.head
    while current: # O(n)
        my_line = f"{current.value[0]}, {current.value[1]}, {str(current.priority[0])}, {str(current.priority[1])}\n"
        if current.next == None:
            my_line = f"{current.value[0]}, {current.value[1]}, {str(current.priority[0])}, {str(current.priority[1])}"
        file.write(my_line)
        current = current.next
    file.close()

    sys.exit()