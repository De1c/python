

# def token_parser(s):

    # final_list = []
    # my_list = re.findall(r'\d+', s)
    # my_list2 = re.findall(r'\+|\-|\/|\*', s)
    # for el1, el2 in zip(my_list, my_list2):
        # final_list.append(el1)
        # final_list.append(el2)
    # las_el = my_list[-1]
    # final_list.append(las_el)
    # return final_list


# print(token_parser("2+ 34 -5 * 3"))

# my_list = []
# my_list.append(None)
# print(my_list)


# #Debugging with logging
# import logging

# #Default level is third, but we can change with logging.basicConfig()
# logging.basicConfig(level=logging.DEBUG)

# logging.debug('Debug is the lowest log level in severity')
# logging.info('Info is the second lowest log level')
# logging.warning('Warning is the third level')
# logging.error('Errod is the fourth level')
# logging.critical('Critical is the fifth ahd hightest level

# import shutil
# shutil.make_archive()

# my_list = []
# my_list.append([6])
# print(my_list)
# list(6)

# for i, index in enumerate(my_list):
#     print(i, index)


# print(my_list)

# TYPES = [
#         ['jpeg', 'png', 'jpg', 'svg'],
#         ['avi', 'mp4', 'mov', 'mkv'],
#         ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'],
#         ['mp3', 'ogg', 'wav', 'amr'],
#         ['zip', 'gz', 'tar']
# ]

# for e_type in TYPES:
#     for ee in e_type:
#         with open(f"C:\\Users\\Deic\\Desktop\\ForHW\\New_file.{ee}", 'w') as ph:
#             pass

# f = {'a': 1}
# print(dir(f))

# some_str = 'aaAbbB C F DDd EEe'
# for i in filter(lambda x: x.islower(), some_str):
    # print(i) - Only Lower

# string = 'Hello'
# lst = ['world', 'friend', 'Yehor']
# for el in map(lambda x: x, lst):
#     print(f'{string} {el}', end = ' ')


# my_object = True
# print(isinstance(my_object, int)) -> True (WTF?????)

# import csv


# with open('names.csv', 'w', newline='') as fh:
#     field_names = ['first_name', 'last_name']
#     writer = csv.DictWriter(fh, fieldnames=field_names)
#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


# with open('names.csv', newline='') as fh:
#     reader = csv.DictReader(fh)
#     for row in reader:
#         print(row['first_name'], row['last_name'])

# import csv

# with open('eggs.csv', 'w', newline='') as fh:
#     spam_writer = csv.writer(fh)
#     spam_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spam_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

# with open('eggs.csv', newline='') as fh:
#     spam_reader = csv.reader(fh)
#     for row in spam_reader:
#         print(', '.join(row))


