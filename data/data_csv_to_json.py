import pandas as pd
import json

# ----------
# json dosyasının boyutu büyük olduğu için repoya eklemedim ama isteyenler bu scriptle csvyi çevirip kullanabilir. 
# ----------

data = pd.read_csv("universities_departments.csv")

data = data.sort_values(by=["university_name", "department_name"])

data["years"] = data["years"].apply(lambda x: str(x).split(",") if pd.notna(x) else [])
data["tags"] = data["tags"].apply(lambda x: str(x).split(",") if pd.notna(x) else [])

uni_json = {}

for _, row in data.iterrows():
    uni_name = row["university_name"]

    if uni_name not in uni_json:
        uni_json[uni_name] = []

    program_info = {
        "program_code": row["program_code"],
        "department_name": row["department_name"],
        "faculty_name": row["faculty_name"],
        "is_undergraduate": bool(row["is_undergraduate"]),
        "years": row["years"],
        "tags": row["tags"],
        "score_type": row["score_type"],
        "scholarship_type": row["scholarship_type"]
    }

    uni_json[uni_name].append(program_info)

with open("departments_by_university.json", "w", encoding="utf-8") as f:
    json.dump(uni_json, f, ensure_ascii=False, indent=4)







