numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

#t=numbers[:3]
#print(t)
#t=numbers[5:]
#print(t)


sum_of_numbers=sum(numbers[:4])+sum(numbers[5:])
count_of_numbers=len(numbers)
numbers[4]=sum_of_numbers/count_of_numbers

print("Измененный список:", numbers)