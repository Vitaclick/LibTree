def execute(sheet, files):
  sheetFiles = sheet.col_values(1)

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
