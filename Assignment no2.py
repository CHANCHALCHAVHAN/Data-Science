#####################################################################################
#######################################################################################
'''1. Prompt the user to enter the number of employees (residents).
2. For each employee, collect:
o Name
o Age
o Designation
o Band (should be one of 'A', 'B', 'C', or 'D'; case-insensitive input but stored in uppercase)
3. Validate the following:
o Number of residents must be greater than 0.
o Age must be between 21 and 58 (both inclusive).
o Band must be one of 'A', 'B', 'C', or 'D'.
If any validation fails, print "Invalid" and terminate the function immediately.
Test Case No.
Input                                                          Expected Output
TC1                              Number of residents: 0        Invalid
TC2                              Number of residents: -2       Invalid
TC3                        Number of residents: 1, Age: 20     Invalid
TC4                       Number of residents: 1, Age: 59      Invalid
TC5                       Number of residents: 1, Band: E      Invalid
TC6                Number of residents: 1, Age: 30, Band: b    (Valid input, continue)
TC7                     Number of residents: 2,                Invalid
                   First entry valid, Second entry Age: 60

TC8                Number of residents: 2, First entry valid,  Invalid
                    Second Band: F

TC9              Number of residents: 2,                  All inputs valid (Name, Age, Designation, Band)
                                                          Function completes without printing Invalid
                                                          Write'''


def collect_employee_data():
    try:
        # Prompt for user to enter the number of employees
        num_employees = int(input("Enter the number of employees (residents): "))
        if num_employees <= 0:
            print("Invalid")
            return

        employees = []

        for i in range(num_employees):
            print(f"Enter details for Employee {i + 1}:")
            
            # Collecting Name, Age, Designation, and Band
            name = input("Name: ")
            age = int(input("Age: "))
            designation = input("Designation: ")
            band = input("Band (A, B, C, or D): ").upper()

            # Validation checks
            if age < 21 or age > 58 or band not in ['A', 'B', 'C', 'D']:
                print("Invalid")
                return
            
            # Storing employee data
            employees.append({
                "Name": name,
                "Age": age,
                "Designation": designation,
                "Band": band
            })

        print("Employee data collected successfully!")
        print(employees)

    except ValueError:
        print("Invalid")

# Example usage
collect_employee_data()


#####################################################################################
#######################################################################################
'''Write a Python function longest_negative_sum(input1, input2) that takes two parameters:
 input1: A list of integers.
 input2: (length of list)
Your task is to identify all contiguous negative number sequences in the list input1, and:
1. Find the longest such sequence(s) (i.e., the ones with the most consecutive negative numbers).
2. If multiple sequences share the same maximum length, include all of them.
3. Calculate and return the sum of the individual sums of these longest sequences.
4. If there are no negative numbers, return -1.'''

def longest_negative_sequence(list,n):
    i=1
    negative_list=[]
    for j in list:
        if j>=0:
            i+=1
            break;
        else:
            negative_list.append(j)
            i+=1
    if i == n:
        print(sum(negative_list))
         
    
    #if there are two negative list
    if i<n:
        negative_list2=[]
        for j in range(i,n+1):
            if j>=0:
                i+=1
                break;
            else:
                negative_list2.append(list[j])
                i+=1 
        n1=len(negative_list)
        n2=len(negative_list2)
        if n1>n2:
            print("\n \n #######Sum of Longest Sequence is : ",sum(negative_list),"\n And the Sequence is :",negative_list)
        else:
            print("\n \n #######Sum of Longest Sequence is : ",sum(negative_list2),"\n And the Sequence is :",negative_list2)
        
        
    #if there are three negative list    
    if i<n:
        negative_list3=[]
        for j in range(i,n+1):
            if j>=0:
                i+=1
                break;
            else:
                negative_list3.append(list[j])
                i+=1
        n1=len(negative_list)
        n2=len(negative_list2)
        n3=len(negative_list3)
        if n1>n2 and n1>n3:
            print("\n \n #######Sum of Longest Sequence is : ",sum(negative_list),"\n And the Sequence is :",negative_list)
        elif n2>n1 and n2>n3:
            print("\n #######Sum of Longest Sequence is : ",sum(negative_list2),"\n And the Sequence is :",negative_list2)
        else:
            print("\n #######Sum of Longest Sequence is : ",sum(negative_list3),"\n And the Sequence is :",negative_list3)
        
            
list=[-1,-2,-3,2,-1,-2]
n=len(list)
longest_negative_sequence(list, n)
