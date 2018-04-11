import liblog
import os, time, re
import glob

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import httplib2
from oauth2client.contrib import gce

# File statistics
def getFileStat(filepath):  
  fileStats = []
  # Write file path
  fileStats.append(filepath)
  # Calculate modification time
  stats = os.stat(filepath)
  statTime = time.localtime(stats.st_mtime)
  statTime = [str(t) for t in statTime]
  date = f"{statTime[2]}.{statTime[1]}.{statTime[0]} {statTime[3]}:{statTime[4]}"
  fileStats.append(date)
  # Parsing file name
  fullFilename = os.path.basename(filepath)
  fileStats.append(os.path.splitext(fullFilename)[0])

  return fileStats

# Authorization
scope = ["https://spreadsheets.google.com/feeds"]
creds = ServiceAccountCredentials.from_json_keyfile_name("secret.json", scope)
client = gspread.authorize(creds)

# Get spreadsheet
sheet = client.open_by_key('1HLsMD4mmRXiKXQ4wMYcHFYD3BmaoGmmHvZbNIv_Ado8').sheet1

# Time scheduling
# while True:
#   time.sleep(30)

# Extract files statistics
# libpath = r"C:\Drive\BIM4US\Ресурсы\Artpot\Семейства"
libpath = r"D:\#Projects\#REPOS\testLib\АР"
filepaths = glob.glob(libpath + "/**/*.*", recursive=True)
filesStatistics = []
dismissedFiles = []

for f in filepaths:
  if re.search(r"(?<!\d\d\d\d).(rfa|rvt)$", f):
    filesStatistics.append(getFileStat(f))
  else:
    dismissedFiles.append(f)

# Proceed sheet
output = liblog.execute(sheet, filesStatistics)

# Debug
"""
import pprint
pp = pprint.PrettyPrinter()
print(pp.pprint(output))
"""