te20d = ['Adolfsson Vincent',
              'Alfredsson Sebastian',
              'Andersson Linus',
              'Bergholtz Nils',
              'Carpio Flores Mattias',
              'Hama Gareb Adam',
              'Hellström Petersson Theo',
              'Henriksson Viggo',
              'Hermansson Isak',
              'Hermansson Lukas',
              'Hultén Tristan',
              'Kaminski Artur',
              'Klein Alexander',
              'Korzepa Dominik',
              'Lindholm Matthias',
              'Lithner Eskil',
              'Lundgren Oscar',
              'Matic Viktor',
              'Miftaraj Albin',
              'Nilsson Tobias',
              'Olsson Filippa',
              'Pålsson Isak',
              'Rogö Albert',
              'Ruan Kenny',
              'Sajadi Arien',
              'Stamnes Oliver',
              'Stude Adrian',
              'Tholence Etienne',
              'Vadi Elliot',
              'Vazae Nina',
              'Vidos Leon',
              'Zahirovic Adam']

import os
os.chdir('../utvecklingssamtal/')
for student in te20d:
    path = './' + student
    if not os.path.exists(path):
        os.makedirs(path)



"""
for class_name, students in classes.items():
    for student in students:
        student_name = student.split()
        student_name = student_name[0] + '_' + student_name[1]
        student_folder = './' + class_name + '/' + student_name
        if not os.path.exists(student_folder):
   """
