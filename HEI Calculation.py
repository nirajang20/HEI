import pandas as pd

def process_csv(input_file, output_file):
    """
    Process an input CSV file to calculate Healthy Eating Index (HEI-2015) component scores
    and the total HEI score. Results are appended at the end of the CSV file.

    ----------------------------------------------------------------------------
    REQUIRED INPUT COLUMNS (must exist in the CSV file):
    ----------------------------------------------------------------------------
    - kcal            : Total energy intake (kcal)
    - F_TOTAL         : Total fruits
    - G_WHOLE         : Whole grains
    - V_TOTAL         : Total vegetables
    - V_LEGUMES       : Legumes
    - V_DRKGR         : Dark green vegetables
    - D_TOTAL         : Total dairy
    - PF_TOTAL        : Total protein foods
    - PF_SEAFD_HI     : Seafood (high n-3)
    - PF_SEAFD_LOW    : Seafood (low n-3)
    - PF_SOY          : Soy products
    - PF_NUTSDS       : Nuts and seeds
    - PF_LEGUMES      : Legumes (protein foods category)
    - G_REFINED       : Refined grains
    - ADD_SUGARS      : Added sugars (grams)
    - SOLID_FATS      : Saturated fats (grams)
    - Sodium / SODIUM / NA / sodium : Sodium (mg)

    ----------------------------------------------------------------------------
    OUTPUT COLUMNS (HEI-2015 components):
    ----------------------------------------------------------------------------
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

    - HEI_total : Sum of all 13 components
    ----------------------------------------------------------------------------
    """

    # Read the CSV
    df = pd.read_csv(input_file)

    # ------------------------------
    # HEI COMPONENT CALCULATIONS
    # ------------------------------

    # 1. Total Fruits
    df['HEI_total_fruits'] = ((df['F_TOTAL'] / (df['kcal'] / 1000)) / 0.8) * 5
    df['HEI_total_fruits'] = df['HEI_total_fruits'].clip(upper=5)

    # 2. Whole Fruits
    df['HEI_whole_fruits'] = ((df['G_WHOLE'] / (df['kcal'] / 1000)) / 0.4) * 5
    df['HEI_whole_fruits'] = df['HEI_whole_fruits'].clip(upper=5)

    # 3. Total Vegetables
    df['HEI_total_veg'] = ((df['V_TOTAL'] / (df['kcal'] / 1000)) / 1.1) * 5
    df['HEI_total_veg'] = df['HEI_total_veg'].clip(upper=5)

    # 4. Greens and Beans
    df['HEI_green_and_beans'] = ((df['V_LEGUMES'] + df['V_DRKGR']) / (df['kcal'] / 1000)) / 0.2 * 5
    df['HEI_green_and_beans'] = df['HEI_green_and_beans'].clip(upper=5)

    # 5. Whole Grains
    df['HEI_whole_grains'] = (df['G_WHOLE'] / (df['kcal'] / 1000)) / 1.5 * 10
    df['HEI_whole_grains'] = df['HEI_whole_grains'].clip(upper=10)

    # 6. Dairy
    df['HEI_total_dairy'] = (df['D_TOTAL'] / (df['kcal'] / 1000)) / 1.3 * 10
    df['HEI_total_dairy'] = df['HEI_total_dairy'].clip(upper=10)

    # 7. Total Protein Foods
    df['HEI_total_protein'] = (df['PF_TOTAL'] / (df['kcal'] / 1000)) / 2.5 * 5
    df['HEI_total_protein'] = df['HEI_total_protein'].clip(upper=5)

    # 8. Seafood and Plant Proteins
    df['HEI_sea_food'] = ((df['PF_SEAFD_HI'] + df['PF_SEAFD_LOW'] + df['PF_SOY'] +
                          df['PF_NUTSDS'] + df['PF_LEGUMES']) / (df['kcal'] / 1000)) / 0.8 * 5
    df['HEI_sea_food'] = df['HEI_sea_food'].clip(upper=5)

    # 9. Fatty Acids (placeholder: ratio PUFA+MUFA / SFA — requires correct columns)
    df['HEI_fatty_acids'] = ((df['PF_NUTSDS'] + df['PF_SOY']) / (df['SOLID_FATS'] + 1e-9)) * 10
    df['HEI_fatty_acids'] = df['HEI_fatty_acids'].clip(upper=10)

    # 10. Refined Grains
    df['HEI_refined_grains'] = (df['G_REFINED'] / (df['kcal'] / 1000)) / 1.8 * 10
    df['HEI_refined_grains'] = df['HEI_refined_grains'].clip(upper=10)

    # 11. Sodium
    sodium_col = next((col for col in ['Sodium', 'SODIUM', 'NA', 'sodium'] if col in df.columns), None)
    if sodium_col:
        df['sodium_g'] = df[sodium_col] / 1000  # mg → g
        df['sodium_per_kcal'] = df['sodium_g'] / (df['kcal'] / 1000)
        df['HEI_sodium'] = 0
        df.loc[df['sodium_per_kcal'] <= 1.1, 'HEI_sodium'] = 10
        df.loc[(df['sodium_per_kcal'] > 1.1) & (df['sodium_per_kcal'] <= 1.99),
               'HEI_sodium'] = 10 - ((df['sodium_per_kcal'] - 1.1) / 0.89) * 10
        df.loc[df['sodium_per_kcal'] > 1.99, 'HEI_sodium'] = 0
    else:
        df['HEI_sodium'] = 0
        print("Warning: Sodium column not found - HEI_sodium set to 0")

    # 12. Added Sugars
    df['sugar_pct'] = ((df['ADD_SUGARS'] * 4) / df['kcal']) * 100
    df['HEI_added_sugar'] = 0
    df.loc[df['sugar_pct'] <= 6.5, 'HEI_added_sugar'] = 10
    df.loc[(df['sugar_pct'] > 6.5) & (df['sugar_pct'] <= 26),
           'HEI_added_sugar'] = 10 - ((df['sugar_pct'] - 6.5) / (26 - 6.5)) * 10
    df.loc[df['sugar_pct'] > 26, 'HEI_added_sugar'] = 0

    # 13. Saturated Fat
    df['satfat_pct'] = ((df['SOLID_FATS'] * 9) / df['kcal']) * 100
    df['HEI_saturated_fat'] = ((df['SOLID_FATS'] / df['satfat_pct']) / 8) * 10
    df['HEI_saturated_fat'] = df['HEI_saturated_fat'].clip(upper=10)

    # ------------------------------
    # TOTAL HEI SCORE
    # ------------------------------
    hei_components = [
        'HEI_total_fruits', 'HEI_whole_fruits', 'HEI_total_veg', 'HEI_green_and_beans',
        'HEI_whole_grains', 'HEI_total_dairy', 'HEI_total_protein', 'HEI_sea_food',
        'HEI_fatty_acids', 'HEI_refined_grains', 'HEI_sodium', 'HEI_added_sugar',
        'HEI_saturated_fat'
    ]
    df['HEI_total'] = df[hei_components].sum(axis=1).round(2)

    # Round components
    for col in hei_components + ['HEI_total']:
        df[col] = df[col].round(2)

    # Drop intermediate columns
    df = df.drop(columns=['sugar_pct', 'satfat_pct', 'sodium_g', 'sodium_per_kcal'], errors='ignore')

    # Save
    df.to_csv(output_file, index=False)
    print(f"Processed file saved to {output_file}")
    print(f"Columns added: {hei_components + ['HEI_total']}")

# Example usage
if __name__ == "__main__":
    # Define input and output file paths
    input_csv = "/Users/marsguy/Desktop/Research/CH HEI/FPED_CH_KCAL.csv"
    output_csv = "/Users/marsguy/Desktop/Research/CH HEI/FPED_CH_HEI_COMPLETE.csv"
    process_csv(input_csv, output_csv)
