records = []


def collect_student_info():
    keepAdding = "y"
    count = 0
    while keepAdding == "y":
        name = input("Enter your name: ")
        first_score = int(input("Enter math score: "))
        second_score = int(input("Enter english score: "))
        total = first_score + second_score
        average_score = total / 2
        count += 1

        student_grades = {
            "name": name,
            "first_score": first_score,
            "second_score": second_score,
            "total": total,
            "average": average_score,
            "position": count
        }

        records.append(student_grades)

        keepAdding = input("Do you want to continue adding student grades? y/n: ")


def print_grades():

    for i in range(len(records)):
        print(records[i]["name"], "\t", records[i]["first_score"], "\t", records[i]["second_score"], "\t",
              records[i]["total"], "\t", records[i]["average"], "\t", records[i]["position"])


def sort_position():
    for i in range(len(records)):
        for j in range(i + 1, len(records)):
            if records[j]['average'] > records[i]['average']:
                records[i], records[j] = records[j], records[i]

    for i in range(len(records)):
        records[i]["position"] = i + 1


collect_student_info()
sort_position()
print_grades()
