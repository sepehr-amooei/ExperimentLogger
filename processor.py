import datetime as dt

def process_dates_and_weights(birthdates, Esd, Eed, Wsd, Wed):
    birthdates = [dt.datetime.strptime(b, '%Y/%m/%d') for b in birthdates]
    Esd = [dt.datetime.strptime(d, '%Y-%m-%d') for d in Esd]
    Eed = [dt.datetime.strptime(d, '%Y-%m-%d') for d in Eed]
    Wsd = list(map(int, Wsd))
    Wed = list(map(int, Wed))

    E_Duration_days = [(e - s).days for s, e in zip(Esd, Eed)]
    Age_at_E_years = [(e - b).days // 365 for b, e in zip(birthdates, Eed)]
    Zero_list = [0] * len(birthdates)
    E_labels = [f"E{i+1}" for i in range(len(birthdates))]

    return birthdates, Esd, Eed, Wsd, Wed, E_Duration_days, Age_at_E_years, Zero_list, E_labels

def combine_experiment_data(labels, birth, start, end, age, duration, w_start, w_end):
    return [[label, b.date(), s.date(), e.date(), a, d, ws, we] for label, b, s, e, a, d, ws, we in zip(labels, birth, start, end, age, duration, w_start, w_end)]
