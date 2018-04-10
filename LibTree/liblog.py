def execute(sheet, files):
  sheetFiles = sheet.col_values(1)
  # Determinate files that will be removed from sheet
  transposedFiles = list(map(list, zip(*files)))
  depracatedFiles = [sheetFiles.index(f) + 1 for f in sheetFiles if f not in transposedFiles[2]]
  if len(depracatedFiles) > 0:
    depracatedCells = list(map(lambda i: sheet.acell("A{0}".format(i)), depracatedFiles))
    # Remove old rows
    for c in depracatedCells:
      # c.value += "kek"
      sheet.delete_row(c.index)
    sheet.update_cells(depracatedCells)
  ke = 1
  # filesBuffer = []
  # # Update existing rows
  # for sheetFile in sheetFiles:
  #   if sheetFile not in files:
  #     pass
      

  # for i, f in enumerate(files):
  #   filename = f[2]
    # Search for existing files
    
    # for j, sheetFile in enumerate(sheetFiles):
    #   if filename == sheetFile:
    #     sheet.update_cell(j + 1, 2, filename)
    #   else:
    #     sheet.update_cell(j + 1, 2, "WILL BE DELETED")



    # if filename in sheetFiles:
    #   fileRowIndx = sheetFiles.index(filename))
    #   sheet.update_cell(fileRowIndx + 1, 2, filename)
    # else:
    #   filesBuffer.append(f)
  # Add new file


  return sheet.get_all_records()