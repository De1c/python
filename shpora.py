

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
