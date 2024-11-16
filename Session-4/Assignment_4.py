### Exercise
'''Given a zip file with a subfolder with multiple annotations, where the name convention for each one of them is: 

{DATE}_{TIME}_SN{SATELLITE_NUMBER}_QUICKVIEW_VISUAL_{VERSION}_{UNIQUE_REGION}.txt

where:

- DATE expressed as YYYYMMDD (year, month and day), e.g. 20241201, 20230321 ...
- TIME expressed as HHMMSS (hour, minutes and seconds), e.g. 2134307
- SATELLITE_NUMBER an integer that represents the satellite number.
- VERSION provides the version of the pipeline, e.g. "0_1_2", "1_3_1" ...
- UNIQUE_REGION provides a unique location in the form of a string, e.g SATL-2KM-10N_552_4164

Find out the following thing about your data:

'''


# 1. How many files the annotations folder has.

import os
annotations_folder = r'/Users/konstantinospapathanasiou/Downloads'
files = os.listdir(annotations_folder)
total_files = len(files)
print(f"Total files in annotations folder: {total_files}")


# 2. How many of them follow the name convention expressed above.

valid_files = []
invalid_files = []

def is_valid_number_part(part, length):
    return part.isdigit() and len(part) == length

for file in files:
    parts = file.replace(".txt", "").split("_")
    if (
        len(parts) >= 7 and 
        is_valid_number_part(parts[0], 8) and  
        is_valid_number_part(parts[1], 6) and  
        parts[2].startswith("SN") and parts[2][2:].isdigit() and  
        parts[3] == "QUICKVIEW" and  
        parts[4] == "VISUAL" and  
        parts[5].isdigit() and
        parts[6].isdigit() and
        parts[7].isdigit()
    ):
        valid_files.append(file)
    else:
        invalid_files.append(file)

valid_files_count = len(valid_files)
print(f"Files following the name convention: {valid_files_count}")

len(invalid_files)

# 3. How many of annotations you have per month and year. Which month has more annotation files.

for file in valid_files:
    parts = file.replace(".txt", "").split("_")
    year = parts[0][:4]
    month = parts[0][4:6]
    year_month = f"{year}-{month}"
    annotations_count[year_month] = annotations_count.get(year_month, 0) + 1

print("Annotations per month and year:")
for year_month, count in sorted(annotations_count.items()):
    print(f"{year_month}: {count} annotations")


max_month = max(annotations_count, key=annotations_count.get)
print(f"Month with the most annotations: {max_month} with {annotations_count[max_month]} annotations")


# 4. Create a new annotations folder with multiple folders corresponding to a month.

import shutil

new_annotations_folder = './new_annotations'
if os.path.exists(new_annotations_folder):
    shutil.rmtree(new_annotations_folder)

os.makedirs(new_annotations_folder)

for month in range(1, 13):
    month_folder = f"{new_annotations_folder}/{month:02}"
    os.makedirs(month_folder, exist_ok=True)



# 5. Print all the annotations from the most recent to the oldest one. 

sorted_files = sorted(
    valid_files,
    key=lambda f: (f[:8], f[9:14]),     
    reverse=True
    )

print("Annotations from most recent to oldest:")

for file in sorted_files:
    print(file)

# 6. How many different satellites there are, how many annotations we have per satellite number, and which one was used in the most recent annotation file.
satellite_count = {}                  
latest_file = None
latest_date = "" 


for file in valid_files:
    parts = file.replace(".txt", "").split("_")
    satellite_number = parts[2][2:] 
    satellite_count[satellite_number] = satellite_count.get(satellite_number, 0) + 1

    
    file_date = parts[0]
    if file_date > latest_date:
        latest_date = file_date        
        latest_file = file             


different_satellites_count = len(satellite_count)  
latest_satellite_number = latest_file.split("_")[2][2:] if latest_file else None  
print(f"Total different satellites: {different_satellites_count}")
print(f"Most recent Satellite number: SN{latest_satellite_number}") 


# 7. How many unique regions there are.

unique_regions = set()
for file in valid_files:
    parts = file.replace(".txt", "").split("_")
    unique_region = "_".join(parts[8:])
    unique_regions.add(unique_region)

unique_regions_count = len(unique_regions)
print(f"Number of unique regions: {unique_regions_count}")

''' some tips:
- str class has a method called split, you can use it to get each field per annotation.
- you can use sort from numpy on strings. '''

