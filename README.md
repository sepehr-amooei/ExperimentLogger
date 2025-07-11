# ExperimentLogger  

A Python-based project to analyze and visualize experimental data (birthdates, test durations, and weight changes) with export capabilities to CSV, Excel, and Pickle formats.  

---

## 📁 Project Structure  
```bash
ExperimentLogger/  
├── data/                   # Raw data input  
│   └── Text_file.txt       # Experiment records (birthdates, test dates, weights)  
├── output/                 # Generated files  
│   ├── mail_cat.csv        # Exported CSV of processed data  
│   ├── mail_cat.xlsx       # Exported Excel file  
│   ├── Test Duration vs Weight Change.png       # Plot 1  
│   └── Test age vs duration bubble chart.png    # Plot 2  
├── reader.py               # Reads and splits raw data  
├── processor.py            # Processes dates/weights into structured formats  
├── plotter.py              # Generates visualizations  
├── exporter.py             # Exports data to CSV/Excel/Pickle  
├── models.py               # Object models for data serialization  
└── main.py                 # Orchestrates the workflow  
```

---

## 🛠️ Installation  
1. **Clone the repository**:  
   ```bash
   git clone https://github.com/sepehr-amooei/ExperimentLogger.git
   cd ExperimentLogger  
   ```

2. **Install dependencies**:  
   ```bash
   pip install openpyxl pandas matplotlib  
   ```

---

## 🚀 Usage  
Run the pipeline:  
```bash
python main.py  
```

### What it does:  
1. **Loads data** from `data/Text_file.txt`.  
2. **Processes** dates, weights, and calculates test durations/ages.  
3. **Exports** structured data to CSV/Excel/Pickle.  
4. **Generates plots**:  
   - **Weight Change vs. Test Duration** (Line-scatter hybrid).  
   - **Age vs. Duration Bubble Chart** (Log-scaled weight loss).  

---

## 📊 Plots & Visualizations  
### 1. Test Duration vs Weight Change  
<img width="640" height="480" alt="Test Duration vs Weight Change" src="https://github.com/user-attachments/assets/643d1bd3-1faa-4326-be1c-f7c7b1213dd4" />

- **Blue dots**: Initial weight (`W_start`).  
- **Red dots**: Final weight (`W_end`).  
- **Black lines**: Weight change over test duration.  

### 2. Age vs. Duration Bubble Chart  
<img width="640" height="480" alt="Test age vs duration bubble chart" src="https://github.com/user-attachments/assets/3799ed25-8328-48c9-8d54-3d9dfeaeef23" />

- **Bubble size**: Log-scaled weight loss.  
- **Labels**: Experiment IDs (`E1`, `E2`, etc.).  

---

## 📦 Modules  
| File         | Description |  
|--------------|-------------|  
| `reader.py`  | Parses raw text data into lists. |  
| `processor.py` | Computes durations, ages, and formats dates. |  
| `plotter.py` | Generates matplotlib visualizations. |  
| `exporter.py` | Exports to CSV/Excel/Pickle. |  
| `models.py`  | Object model for serialization (`MailcatObject`). |  

---

## 📝 Data Format (Input)  
```plaintext
Birth_date E_start_date E_end_date W_start_date W_end_date  
1992/11/09 2022-04-23 2022-09-17 221 208  
1987/02/13 2022-07-12 2023-01-09 198 191  
... 
