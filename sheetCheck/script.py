import textract

available = ['02.20/2020.2-943']
cfg = {
    '02.20/2020.2-943': {
        '1': ['п/п\n', 'id'],
        '2': ['Номер студенческого\nбилета\n', 'ticket'],
        '3': ['Фамилия, имя, отчество студента\n', 'FIO'],
        '4': ['Оценка по 5балльной шкале\n(текст)\n', 'mark'],
    }
}


def get_dict(url, format, columns):
    try:
        raw_text = textract.process(url).decode('utf-8', 'ignore')
        if format not in raw_text:
            return 1
        columns = columns.split(',')
        cols = cfg.get(format, None)
        if not cols:
            return 2
        students = []
        for column in columns:
            tmp = cols.get(str(column))
            if not tmp:
                continue
            index = raw_text.find(tmp[0]) + len(tmp[0]) + 1
            blank = raw_text.find('\n\n', index)
            for i, value in enumerate(raw_text[index:blank].split('\n')):
                if column == columns[0]:
                    student = dict()
                    students.append(student)
                students[i][tmp[1]] = value
        return students
    except Exception as e:
        print(str(e))
        return 3
