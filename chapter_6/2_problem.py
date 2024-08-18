sub_1 = int(input("Enter your first sub number :"))
sub_2 = int(input("Enter second first sub number :"))
sub_3 = int(input("Enter third first sub number :"))

# cehck total percentage

total_percentage = (100*(sub_1+ sub_2+ sub_3))/300

if(total_percentage>=40 and sub_1 >=33 and sub_2 >=33 and sub_3 >=33):
  print('your\'e passed.' 'your percentage is', total_percentage )
else:
  print('your\'e failed,\n\t try again next year ')
