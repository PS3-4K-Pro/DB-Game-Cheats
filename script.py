import os
import re
import shutil

path = "codelists/"
dirs = os.listdir(path)

for file in dirs:
   rege = re.findall(r'.*?(BL.*?[0-9]+.*?\.ncl)|.*?(NP.*?\.ncl)|.*?(BC.*?\.ncl)|.*?(MR.*?[0-9]+.*?\.ncl)', file)
   for x in rege:
      test_list = [i for i in list(x) if i]
      if len(test_list)==0:
         continue
      else:
         name_formated = test_list[0].replace(' ', '_')
         shutil.move(f"codelists/{file}", f"codelists_gerado/{name_formated}")