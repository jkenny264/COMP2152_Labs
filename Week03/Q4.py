monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}
#these are sets

print(f"Monday class: {monday_class}")
print(f"Wednesday class: {wednesday_class}")
print(f"Attend both classes: {monday_class & wednesday_class}")
print(f"Attend either class: {monday_class | wednesday_class}")
print(f"Only Monday: {monday_class - wednesday_class}")
# print(f"Only Wednesday: {wednesday_class - monday_class}")
print(f"Only one class: {monday_class ^ wednesday_class}")
all_students = monday_class | wednesday_class
print(f"Is Monday subset of all students: ", monday_class <= all_students)