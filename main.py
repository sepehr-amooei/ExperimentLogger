from reader import read_text_file, split_data
from processor import process_dates_and_weights, combine_experiment_data
from plotter import plot_weight_changes, plot_weight_loss_bubble_chart
from models import CreateCatalog
from exporter import export_csv, export_excel, save_pickle, load_pickle, load_csv_as_df

# 1. Load and parse data
read_datas = read_text_file("data/Text_file.txt")
Header, Birth_date, E_start, E_end, W_start, W_end = split_data(read_datas)

# 2. Process
Birth_date, E_start, E_end, W_start, W_end, Duration, Age, Zeros, Labels = process_dates_and_weights(Birth_date, E_start, E_end, W_start, W_end)

# 3. Combine
experiment_data = combine_experiment_data(Labels, Birth_date, E_start, E_end, Age, Duration, W_start, W_end)
TestSubjects = [
    ["Joe", "joe@gmail.com"],
    ["Anand", "anand@gmail.com"],
    ["Lisa", "lisa@gmail.com"],
    ["Mohammad", "mohammad@gmail.com"]
]
data_records = [[name, email, row] for (name, email), row in zip(TestSubjects, experiment_data)]
print(data_records)
# 4. Object Model
Mail_c = CreateCatalog(data_records)
save_pickle(Mail_c, "output/Mail_c.obj")

# 5. Reload and Serialize
Mail_c = load_pickle("output/Mail_c.obj")
csv_data = Mail_c.serialize()
export_csv(csv_data, "output/mail_cat.csv")
export_excel(csv_data, "output/mail_cat.xlsx")
df = load_csv_as_df("output/mail_cat.csv")
print(df)

# 6. Plots
plot_weight_changes(Labels, Duration, Zeros, W_start, W_end)
plot_weight_loss_bubble_chart(Labels, Age, Duration,W_start, W_end)