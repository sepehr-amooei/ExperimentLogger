def read_text_file(filepath):
    with open(filepath) as file:
        return file.readlines()

def split_data(dataList):
    header = dataList[0].strip().split()
    data_rows = dataList[1:]
    birthdate, Esd, Eed, Wsd, Wed = [], [], [], [], []

    for row in data_rows:
        fields = row.strip().split()
        if len(fields) >= 5:
            birthdate.append(fields[0])
            Esd.append(fields[1])
            Eed.append(fields[2])
            Wsd.append(fields[3])
            Wed.append(fields[4])

    return header, birthdate, Esd, Eed, Wsd, Wed