def execute(sheet, files):
  sheetFiles = sheet.col_values(1)
  transposedFiles = list(map(list, zip(*files)))
  # Remove if some files depracated in sheet
  removeDepracated(sheet, sheetFiles, transposedFiles)
  
def removeDepracated(sheet, sheetFiles, files):
  depracatedFiles = []
  fIdx = 0
  while len(sheetFiles) > fIdx:
    f = sheetFiles[fIdx]
    if f not in files[2]:
      depracatedFiles.append(fIdx + 1)
    # Limit files to delete
    if len(depracatedFiles) > 30:
      break
    fIdx += 1
  
  if len(depracatedFiles) > 0:
    depracatedCells = list(map(lambda i: sheet.acell("A{0}".format(i)), depracatedFiles))
    # Remove obsole files
    rowIndex = 0
    for c in depracatedCells:
      # Shift row index while remove
      sheet.delete_row(c.row + rowIndex)
      rowIndex -= 1


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