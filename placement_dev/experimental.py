



def example_add_time():
    date = datetime.date
    today = date.today()

    te20d = 'TE20D Placering.xlsx'
    wb = load_workbook(''.format(te20d))
    # wb.create('TE20D Placering {}'.format(today))

"""
for students in range(len(current_class) + 1):
    for row in sheet['A1':'H6']:
        for length, cell in enumerate(row):
            for column in sheet['A1':'H6']:
                print(cell.value)
                if cell.value == 'Placering':
                cell.value = current_class[students]
"""


# Skapa en mall för varje rum, generera sedan utifrån detta
# en placeringarna, du kan sen ladda upp dessa i en mapp på driven
# Så nu kan du slumpa en ny lista för alla klasser, för alla salar
# Det som fattas är om två personer inte kan sitta bredvid varandra
# Flytta alla elever en rad frammåt per vecka

def derpilli_te20d_placeringar_testing(current_klass):
    book = load_workbook('te20d_placeringar.xlsx')
    sheet = book.active

    current_class = te20d

    for students in range(len(current_class) + 1):
        print(students)
        for row in sheet['A1':'H6']:
            print(row)
            for length, cell in enumerate(row):
                if cell.value == 'Placering':
                    cell.value = current_class[students]
                    current_class.remove(students)
                    print(current_class[students])

    # Export to csv and json as well
    book.save('te20d_placeringar_new.xlsx')
    book.close()


    # selected_cell.fill = PatternFill('solid', bgColor='ff5959')
    # selected_cell.font = Font(name='helvetica')
    # selected_cell.fill = fill = GradientFill(stop=("ffffff", "ff5959"))
    # selected_cell.alignment = Alignment(horizontal="center", vertical="center")