# ============== PART 1 ============== 
# Write a function called contains_pickle that accepts any number of arguments. 
# The function should return True if it is passed "pickle" as one of the args
# Otherwise it should return False

#  contains_pickle("red", 45, "pickle", [])  --> True
#  contains_pickle(1,2, "blue") ---------------> False
def contains_pickle(*args):
    if "pickle" in args:
        return True
    else:
        return False
print(contains_pickle("red",45,"pickle"))
print(contains_pickle(1,2,"blue"))
    



# ============== PART 2 ============== 
# Write a function called count_fails that counts up the number of failing test scores it is passes
# It should accept any number of arguments
# It should return a count of how many args are less than or equal to 50

# count_fails(99,48,79,36) -------> 2
# count_fails(85,78,91) ----------> 0
# count_fails(50,41,47,74,76,81) -> 3

def count_fails(*args):
    total = 0
    for marks in args:
        if marks <= 50:
            total +=1
    return total

print(count_fails(99,48,79,36))
print(count_fails(85,78,91))
print(count_fails(50,41,47,74,76,81))





# ============== PART 3 ============== 
# Write a function called get_top_students that helps teachers find their A-grade students!
# It should accept any number of student=score keyword arguments like colt=78 or elton=98
# It should return a list containing the names of students who scored 90 or above

# get_top_students(tim=91, stacy=83, carlos=97, jim=69) -> ['tim', 'carlos']
# get_top_students(colt=61, elton=76) -------------------> []
# get_top_students(kitty=80, blue=95, toad=91)-----------> ['blue', 'toad']

def get_top_students(**kwargs):
    lst = []
    for k,v in kwargs.items():
        if v > 90:
            lst.append(k)
    print(lst)

get_top_students(tim=91, stacy=83, carlos=97, jim=69)
get_top_students(colt=61, elton=76)
get_top_students(kitty=80, blue=95, toad=91)
