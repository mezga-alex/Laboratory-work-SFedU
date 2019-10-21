//: ## Лабораторная №1. Основы Swift
import Foundation
//: 1. Дана строка: "студент1 группа1; студент2 группа2; ..."
let studentsStr = "Хаустова Екатерина 4.1; Кириллова Елена 4.1; Марков Иван 4.1; Пашков Данил 4.1; Бакуменко Олег 4.1; Кириченко Анастасия 4.1; Гусев Евгений 4.1; Белоконь Александр 4.2; Архипов Антон 4.1; Кравцов Роман 4.1; Нинидзе Давид 4.2; Кашилов Иван 4.2; Кравцов Максим 4.2; Коваленко Алексей 4.2; Бочкарёва Дария 4.2; Ульянов Михаил 4.2; Сенчукова Ангелина 4.1; Лебедев Евгений 4.1; Галайчук Виталий 4.2"
//: Сформировать массив студентов в алфавитном поряке.
//:
//: _Для разделения строки можно использовать `String.components(separatedBy: String) -> [String]`._
//:
//: _Для сортировки подойдёт стандартный метод `Sequence.sort()`._
var studentsArray: [String] = studentsStr.components(separatedBy: "; ")
studentsArray.sort()
//: Cформировать словарь группа : студенты в группе.
//:
//: _Перед использованием массив нужно инициализировать_
//: ```
//: if studentsGroups["1.1"] == nil {
//:     studentsGroups["1.1"] = []
//: }
//:```
var studentsGroups: [String : [String]] = [:]
for student in studentsArray {
    let studentComponents = student.components(separatedBy: " ")
    if studentsGroups[studentComponents[2]] == nil {
        studentsGroups[studentComponents[2]] = []
    }
    studentsGroups[studentComponents[2]]?.append("\(studentComponents[0]) \(studentComponents[1])")
}
studentsGroups
//: 2. Дан словарь баллов по лабораторным.
//:
//: _Получить доступ к последовательности ключей или значений словаря можно,
//: используя поля `Dictionary.keys` и `Dictionary.values`._
let points: [String: Int] = ["Основы Swift" : 5,
                             "Классы Swift" : 5,
                             "Делегирование" : 10,
                             "Интерфейс" : 10,
                             "Хранение данных" : 10,
                             "Core Data" : 10,
                             "Лаб 7" : 10,
                             "Лаб 8" : 15,
                             "Лаб 9" : 15,
                             "Лаб 10" : 10]
//: Сформировать словарь студент : мaссив баллов по лабораторным.
//:
//: _Баллы заполнить случайными значениями (с учетом максимальных баллов)._
//: ```
//: let randomUInt = arc4random()
//: let randomUpTo5 = arc4random_uniform(5)
//: let randomDouble = drand48()
//: ```
var studentPoints: [String:[Int]] = [:]
for students in studentsGroups.values {
    for stName in students {
        studentPoints[stName] = []
        for labPoints in points.values {
            let randomPoints = Int(arc4random_uniform(UInt32(labPoints)))
            studentPoints[stName]?.append(randomPoints)
        }
    }
}
studentPoints


var sumPoints: [String:Int] = [:]
for (name, points) in studentPoints {
    var sum = 0
    for point in points {
        sum += point
    }
    sumPoints[name] = sum
}
sumPoints
var notPassed = sumPoints.filter() {
    pair in return pair.value < 40
}


//: Для каждой группы посчитать средний балл, массив студентов сдавших и не сдавших курс.
var groupAvg: [String:Float] = [:]
points.count
for (group, students) in studentsGroups {
    var sum = 0
    for stName in students {
        sum += sumPoints[stName]!
    }
    let averageSum = Float(sum) / Float(students.count * points.count)
    groupAvg[group] = averageSum
}
   groupAvg

var passedPerGroup: [String:[String]] = [:]
var restOfStudentsPerGroup: [String:[String]] = [:]

for (group, students) in studentsGroups {
    if passedPerGroup[group] == nil {
        passedPerGroup[group] = []
    }
    
    if restOfStudentsPerGroup[group] == nil {
        restOfStudentsPerGroup[group] = []
    }
    
    for stName in students {
        if notPassed[stName] == nil {
            passedPerGroup[group]?.append(stName)
        } else {
            restOfStudentsPerGroup[group]?.append(stName)
        }
    }
}
passedPerGroup
restOfStudentsPerGroup

    
    
