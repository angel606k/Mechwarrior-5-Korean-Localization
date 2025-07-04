import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 인증
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# 시트 이름 → 출력 파일명 매핑
sheet_to_filename = {
    "Translate Result": ".github/build/Korean/Game_Release.locres.txt",
    "Translate Result(Debug)": ".github/build/Korean/Game_Debug.locres.txt"
}

# 각 시트 처리
for sheet_name, file_name in sheet_to_filename.items():
    worksheet = client.open("멕워리어 5 한글 번역 시트 V1.1").worksheet(sheet_name)
    a_column = worksheet.col_values(1)

    with open(file_name, "w", encoding="utf-8") as f:
        for line in a_column:
            f.write(line + "\n")
