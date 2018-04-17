def execute(sheet, libFiles):
  sheetFiles = sheet.col_values(1)
  # transposedLibFiles = list(map(list, zip(*libFiles)))
  filesToUpdate = sortFiles(sheetFiles, libFiles)  

  lastRowIdx = len(sheetFiles) + 1
  # Remove if some files depracated in sheet
  # [TASK]: убедиться что при неполной подчистке новые записи корректны
  # [TASK]: remove empty row from depracated
  if len(filesToUpdate["depracated"]) > 0:
    deletedQnt = removeDepracated(sheet, filesToUpdate["depracated"], 15)
    lastRowIdx += deletedQnt
  
  # Add new files
  if len(filesToUpdate["new"]) > 0:
    addNewFile(sheet, filesToUpdate["new"], lastRowIdx)
  
  sheetCells = chunk(sheet.range("A1:C{0}".format(lastRowIdx)), 3)
  updatedFiles = filesToUpdate["exist"]
  # Update existing files
  for row in sheetCells:
    for f in updatedFiles:
      fileName = f[0]
      filePath = f[1]
      fileMod = f[2]

      if fileName == row[0].value:
        # Write new data to a cell
        # Write path to a family
        row[1].value = filePath
        # Update modification time
        if fileMod not in row[2].value:
          if row[2].value == "":
            row[2].value += fileMod
          else:
            row[2].value += "\n" + fileMod
          
        break

  # Update flattened cell list
  sheet.update_cells([c for row in sheetCells for c in row])



def addNewFile(sheet, libNewFiles, lastRowIdx):
  newCells = sheet.range("A{0}:C{1}".format(lastRowIdx, lastRowIdx + len(libNewFiles) - 1))

  # Fill cell values with lib data
  for i, row in enumerate(chunk(newCells, 3)):
    for j, cell in enumerate(row):
      cell.value = libNewFiles[i][j]

  sheet.update_cells(newCells)

def sortFiles(sheetFiles, libFiles):
  filesToUpdate = {"exist": [], "new": [], "depracated": []}
  transposedLibFiles = list(map(list, zip(*libFiles)))
  # Find depracated files from sheet
  fIdx = 0
  while len(sheetFiles) > fIdx:
    f = sheetFiles[fIdx]
    if f not in transposedLibFiles[0]:
      filesToUpdate["depracated"].append(fIdx + 1)
    fIdx += 1
  # Check new and existing in sheet files from library
  for i, file in enumerate(libFiles):
    if file[0] not in sheetFiles:
      filesToUpdate["new"].append(libFiles[i])
    else:
      filesToUpdate["exist"].append(libFiles[i])

  return filesToUpdate

def removeDepracated(sheet, filesToRemove, limit):
  # Find and limit file's cells to be deleted
  depracatedCells = list(map(lambda i: sheet.acell("A{0}".format(i)), filesToRemove[:limit]))
  # Remove obsolete files
  rowCorrection = 0
  for c in depracatedCells:
    # Shift row index while remove
    sheet.delete_row(c.row + rowCorrection)
    rowCorrection -= 1

  return rowCorrection
# Helpers
def chunk(lst, size):
  length = len(lst)
  return [lst[part:part+size] for part in range(0, length, size)]


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