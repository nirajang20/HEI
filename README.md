# Healthy Eating Index (HEI-2015) Calculator

This repository provides a **Python script** to calculate the **Healthy Eating Index (HEI-2015)** from dietary intake data stored in a CSV file.  
It is designed for **researchers, students, and public health professionals** who want to evaluate diet quality without needing advanced coding skills.

---

## 📖 What is HEI-2015?

The **Healthy Eating Index (HEI-2015)** is a scoring system (0–100 points) that measures how closely a diet follows the **2015–2020 Dietary Guidelines for Americans**.  
It includes **13 components** that cover fruits, vegetables, proteins, grains, fats, and sugars.  

- **Higher scores** → Better diet quality  
- **Lower scores** → Poorer diet quality  

---

## 📝 Input File Requirements

The script requires a **CSV file** (spreadsheet format) with the following columns:  

| Column Name | Description |
|-------------|-------------|
| `kcal` | Total energy intake (kcal) |
| `F_TOTAL` | Total fruits |
| `G_WHOLE` | Whole grains |
| `V_TOTAL` | Total vegetables |
| `V_LEGUMES` | Legumes |
| `V_DRKGR` | Dark green vegetables |
| `D_TOTAL` | Total dairy |
| `PF_TOTAL` | Total protein foods |
| `PF_SEAFD_HI` | Seafood (high in n-3 fats) |
| `PF_SEAFD_LOW` | Seafood (low in n-3 fats) |
| `PF_SOY` | Soy products |
| `PF_NUTSDS` | Nuts and seeds |
| `PF_LEGUMES` | Legumes (protein category) |
| `G_REFINED` | Refined grains |
| `ADD_SUGARS` | Added sugars (grams) |
| `SOLID_FATS` | Saturated fats (grams) |
| `Sodium` / `SODIUM` / `NA` / `sodium` | Sodium (mg) |

---

## 📊 Output

The script will calculate **13 HEI-2015 component scores** and one **total score**:

1. HEI_total_fruits  
2. HEI_whole_fruits  
3. HEI_total_veg  
4. HEI_green_and_beans  
5. HEI_whole_grains  
6. HEI_total_dairy  
7. HEI_total_protein  
8. HEI_sea_food  
9. HEI_fatty_acids  
10. HEI_refined_grains  
11. HEI_sodium  
12. HEI_added_sugar  
13. HEI_saturated_fat  

➡️ **HEI_total** = Sum of all 13 components  

The results are saved in a **new CSV file** with these extra columns added.

---

## ⚙️ How to Use

1. Make sure you have **Python 3** installed.  
2. Install the required package:  
   ```bash
   pip install pandas
   ```  
3. Save your dietary data as a CSV file (with required columns).  
4. Run the script:  
   ```bash
   python your_script_name.py
   ```  
5. The processed CSV with HEI scores will be saved in the location you specify in the code.

---

## 📌 Example

If your input file is:  

```
/Users/yourname/Desktop/FPED_CH_KCAL.csv
```

And you want to save results as:  

```
/Users/yourname/Desktop/FPED_CH_HEI_COMPLETE.csv
```

Then the script will create the new file with all 13 component scores and the **total HEI score**.

---

## 👩‍🔬 Who Can Use This?

- **Researchers** working with dietary survey data  
- **Public health professionals** evaluating nutrition programs  
- **Students** learning about diet quality assessment  
- **Anyone** interested in applying the HEI-2015 scoring system to their own dataset  

---

## 📢 Notes

- Ensure all required columns are present in your CSV file.  
- If the script cannot find sodium values, it will set HEI_sodium = 0 and display a warning.  
- Calculations are based on HEI-2015 scoring standards.  

---

## 📜 License

This project is provided under the MIT License. Feel free to use and modify it for your own work.
