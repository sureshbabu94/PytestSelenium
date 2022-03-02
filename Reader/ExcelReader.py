import openpyxl

# Give the location of the file
path = "C:\\Users\\Admin\\Desktop\\demo.xlsx"

# To open the workbook
# workbook object is created
wb_obj = openpyxl.load_workbook(path)

# Get workbook active sheet object
# from the active attribute
sheet_obj = wb_obj.active


# Cell object is created by using
# sheet object's cell() method.
cell_obj = sheet_obj.cell(row=1, column=1)

# Print value of cell object
# using the value attribute
print(cell_obj.value)