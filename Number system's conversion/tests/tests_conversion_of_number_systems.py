import sys
sys.path.insert(1, "/Users/Svetlana/PythonLearning/Number system's conversion/application")
import conversion_of_number_systems as convertor
    



ce.set_values()

print('covert_into_10_and_back:')
for i in range(2, 36):
    number_in_10 = convertor.covert_into_10('11111', i)
    interim_number = convertor.convert_into_required_system(number_in_10, i+1)
    interim_number_10 = convertor.covert_into_10(str(interim_number), i+1)
    original_number = convertor.convert_into_required_system(interim_number_10, i)
    print(original_number == '11111')

