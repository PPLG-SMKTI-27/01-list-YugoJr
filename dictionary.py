student1 ={"nama" : "ibni","asal,": "samarinda", "nilai": 90 }
student2 ={"nama": "glenn", "asal": "samarinda", "nilai": 75}
student3 = {"nama": "syabil", "asal": "Samarinda", "nilai": 66}

students = [student1, student2, student3]
print(students)

for i in range(len(students)):
    print("siswa ke-", i, "", students[i]["nama"]) 
    
for i in range(len(students)):
    print("asal siswa ke-", i, "", students[2]["asal"]) 
    
sum = 0
for i in range(len(students)):
    sum = sum + students[i]["nilai"]
print("Total nilai semua siswa", sum)

ratarata = sum/len(students)
print("nilai rata-rata", ratarata)

nama = str(input())
asal = str(input())
nilai = str(input())

#crud add
student4 = {"nama":nama, "asal":asal, "nilai":nilai}
students.append(student4)
print(students)

#crud - read
print("No\tnama\tAsal\tNilai")
for i in range(len(students)):
    print(1+1, "\t", students[i]["nama"], "\t", students[i]["asal"], "\t", students[i]["nilai"])
    
print("nama\tasal\tnilai")
for s in students:
    print(s("nama"), "\t", s("asal"), "\t", s("nilai"))
    
    
