"""
code_survey.py
Clean and recode the Online Shopping Belgium survey for SPSS multiple linear regression.
Output: coded_survey_data.xlsx  (data sheet + Codebook sheet)
"""

import pandas as pd
import numpy as np
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
import warnings
warnings.filterwarnings("ignore")

INPUT  = "/root/.claude/uploads/e94137eb-3d50-4739-9278-ab949b2eb732/93fc5ac7-Online_Shopping_Habits_of_Young_Adults_in_Belgium_Responses_new.xlsx"
OUTPUT = "/home/user/BabyPluto/coded_survey_data.xlsx"

# ── 1. Load raw data ──────────────────────────────────────────────────────────
raw = pd.read_excel(INPUT)
print(f"Raw shape: {raw.shape}")
print("Columns:")
for i, c in enumerate(raw.columns):
    print(f"  [{i}] {c}")

df = raw.copy()

# Collector for unmatched values
unmatched = {}

def track_unmatched(col_name, series, mapping):
    """Return mapped series; track any values not in mapping."""
    cleaned = series.copy()
    bad = cleaned[~cleaned.isna() & ~cleaned.isin(mapping.keys())]
    if not bad.empty:
        unmatched[col_name] = bad.unique().tolist()
    return cleaned.map(mapping)

# ── 2. DROP columns ───────────────────────────────────────────────────────────
# Col 0: Timestamp, Col 4: dependents yes/no, Col 5: how many dependents
drop_cols = [df.columns[0], df.columns[4], df.columns[5]]
df.drop(columns=drop_cols, inplace=True)
# After drop the positional indices shift; work by name from here.
# For clarity, let's reset with named access using original column list.

# Reload and work from scratch with explicit column references
raw = pd.read_excel(INPUT)
cols = raw.columns.tolist()

# ── 3. Extract each column by original position ───────────────────────────────
age_raw          = raw.iloc[:, 1].copy()
situation_raw    = raw.iloc[:, 2].copy()
relationship_raw = raw.iloc[:, 3].copy()
income_mo_raw    = raw.iloc[:, 6].copy()
disposable_raw   = raw.iloc[:, 7].copy()
income_src_raw   = raw.iloc[:, 8].copy()
shop_freq_raw    = raw.iloc[:, 9].copy()
avg_per_raw      = raw.iloc[:,10].copy()
monthly_spend_raw= raw.iloc[:,11].copy()
buy_raw          = raw.iloc[:,12].copy()
likert_cols_raw  = [raw.iloc[:,i].copy() for i in range(13, 39)]  # 13-38 inclusive
hours_raw        = raw.iloc[:,38].copy()
social_raw       = raw.iloc[:,39].copy()

# ── 4. AGE (col 1) ───────────────────────────────────────────────────────────
def clean_age(val):
    if pd.isna(val):
        return np.nan
    s = str(val).strip().lower().replace("ans", "").replace("years", "").strip()
    try:
        return int(float(s))
    except:
        return np.nan

age = age_raw.apply(clean_age)
bad_age = age_raw[age.isna() & ~age_raw.isna()]
if not bad_age.empty:
    unmatched["Age"] = bad_age.tolist()

# ── 5. SITUATION (col 2) ─────────────────────────────────────────────────────
situation_map = {
    "Student (non-working)": 1,
    "Student (working)":     2,
    "Employed full-time":    3,
    "Employed part-time":    4,
    "Self-employed":         5,
    "Unemployed":            6,
    "Stay-at-home":          7,
}
situation = track_unmatched("Situation", situation_raw.str.strip(), situation_map)

# ── 6. RELATIONSHIP STATUS (col 3) ───────────────────────────────────────────
def clean_relationship(val):
    if pd.isna(val):
        return np.nan
    s = str(val).strip()
    # Fix messy values
    messy_to_clean = {
        "Yep still single": "Single",
        "Situationship": "In a relationship",
        "hella toxic situationship with my ex gf (guess who this is) ": "In a relationship",
    }
    for messy, clean in messy_to_clean.items():
        if s.lower() == messy.lower():
            return clean
    return s

relationship_cleaned = relationship_raw.apply(clean_relationship)
rel_map = {
    "Single":          1,
    "In a relationship": 2,
    "Cohabiting":      3,
    "Married":         4,
}
relationship = track_unmatched("RelationshipStatus", relationship_cleaned, rel_map)

# ── 7. MONTHLY INCOME (col 6) ────────────────────────────────────────────────
income_map = {
    "€0 – €999":    1,
    "€1000 – €1999": 2,
    "€2000 – €2999": 3,
    "€3000 – €3999": 4,
    "€4000+":        5,
    "Prefer not to say": np.nan,
}
def map_income(val):
    if pd.isna(val):
        return np.nan
    s = str(val).strip()
    if s == "Prefer not to say":
        return np.nan
    return income_map.get(s, "__UNMATCHED__")

monthly_income = income_mo_raw.apply(map_income)
bad_mi = income_mo_raw[monthly_income == "__UNMATCHED__"]
if not bad_mi.empty:
    unmatched["MonthlyIncome"] = bad_mi.tolist()
monthly_income = monthly_income.replace("__UNMATCHED__", np.nan).astype(float)

# ── 8. DISPOSABLE INCOME (col 7) ─────────────────────────────────────────────
disp_map = {
    "€0 – €499":   1,
    "€500 – €999": 2,
    "€1000 – €1499": 3,
    "€1500+":      4,
    "Not sure":    np.nan,
}
def map_disp(val):
    if pd.isna(val):
        return np.nan
    s = str(val).strip()
    if s == "Not sure":
        return np.nan
    return disp_map.get(s, "__UNMATCHED__")

disposable = income_mo_raw.copy()  # placeholder
disposable = disposable_raw.apply(map_disp)
bad_disp = disposable_raw[disposable == "__UNMATCHED__"]
if not bad_disp.empty:
    unmatched["DisposableIncome"] = bad_disp.tolist()
disposable = disposable.replace("__UNMATCHED__", np.nan).astype(float)

# ── 9. INCOME SOURCE dummies (col 8) ─────────────────────────────────────────
income_src_key = {
    "Salary":                      "Income_Salary",
    "Student allowance":           "Income_StudentAllowance",
    "Family support":              "Income_FamilySupport",
    "Freelance/self-employment":   "Income_Freelance",
    "Student job":                 "Income_StudentJob",
    "Government support/benefits": "Income_GovernmentBenefits",
    "Volunteer work":              "Income_VolunteerWork",
    "Nothing":                     "Income_Nothing",
}
income_dummy_cols = list(income_src_key.values())
n = len(income_src_raw)
income_dummies = pd.DataFrame(0, index=range(n), columns=income_dummy_cols)

income_unmatched_vals = set()
for i, cell in enumerate(income_src_raw):
    if pd.isna(cell):
        continue
    parts = [p.strip() for p in str(cell).split(",")]
    for part in parts:
        if part in income_src_key:
            income_dummies.at[i, income_src_key[part]] = 1
        else:
            income_unmatched_vals.add(part)
if income_unmatched_vals:
    unmatched["Income_source"] = list(income_unmatched_vals)

# ── 10. SHOPPING FREQUENCY (col 9) ───────────────────────────────────────────
shop_freq_map = {
    "Less than once a month": 1,
    "1–2 times per month":    2,
    "3–5 times per month":    3,
    "6–10 times per month":   4,
    "More than 10 times per month": 5,
}
shop_freq = track_unmatched("ShoppingFrequency", shop_freq_raw.str.strip(), shop_freq_map)

# ── 11. AVG SPEND PER PURCHASE (col 10) ──────────────────────────────────────
avg_per_map = {
    "€0 – €25":    12,
    "€26 – €50":   38,
    "€51 – €75":   63,
    "€76 – €100":  88,
    "€100+":       125,
}
avg_per = track_unmatched("AvgPerPurchase", avg_per_raw.str.strip(), avg_per_map)

# ── 12. MONTHLY ONLINE SPEND – Y variable (col 11) ───────────────────────────
monthly_spend_map = {
    "€0 – €50":    25,
    "€51 – €100":  75,
    "€101 – €150": 125,
    "€151 – €200": 175,
    "€200+":       225,
}
monthly_spend_Y = track_unmatched("MonthlyOnlineSpend_Y", monthly_spend_raw.str.strip(), monthly_spend_map)

# ── 13. BUY category dummies (col 12) ────────────────────────────────────────
buy_key = {
    "Clothing":                                "Buy_Clothing",
    "Technology/electronics":                  "Buy_Technology",
    "Home items":                              "Buy_HomeItems",
    "Kitchen items":                           "Buy_KitchenItems",
    "Beauty/personal care":                    "Buy_Beauty",
    "Entertainment (games, subscriptions, etc.)": "Buy_Entertainment",
    "Merchandise":                             "Buy_Merchandise",
}
buy_dummy_cols = list(buy_key.values())
buy_dummies = pd.DataFrame(0, index=range(n), columns=buy_dummy_cols)

buy_unmatched_vals = set()
for i, cell in enumerate(buy_raw):
    if pd.isna(cell):
        continue
    parts = [p.strip() for p in str(cell).split(",")]
    for part in parts:
        if part in buy_key:
            buy_dummies.at[i, buy_key[part]] = 1
        else:
            buy_unmatched_vals.add(part)
if buy_unmatched_vals:
    unmatched["Buy_categories"] = list(buy_unmatched_vals)

# ── 14. LIKERT columns (cols 13–38) ──────────────────────────────────────────
likert_map_ci = {
    "strongly disagree": 1,
    "disagree":          2,
    "neutral":           3,
    "agree":             4,
    "strongly agree":    5,
}
likert_names = [
    "WhyShop_Convenient",      # 13
    "WhyShop_SavesTime",       # 14
    "WhyShop_BetterPrices",    # 15
    "WhyShop_EnjoyBrowsing",   # 16
    "WhyShop_Habit",           # 17
    "WhyShop_Hobbies",         # 18
    "WhyShop_Curious",         # 19
    "WhyShop_Trending",        # 20
    "Influence_Price",         # 21
    "Influence_Quality",       # 22
    "Influence_Brand",         # 23
    "Influence_SocialMedia",   # 24
    "Influence_OnlineAds",     # 25
    "Influence_WebDesign",     # 26
    "Influence_Reviews",       # 27
    "Influence_Recommendations",# 28
    "Discourages_PoorWebDesign",# 29
    "Discourages_NegativeReviews",# 30
    "Discourages_HighDeliveryCost",# 31
    "Discourages_LongDelivery",  # 32
    "Discourages_PoorReturns",   # 33
    "Discourages_PaymentSecurity",# 34
    "Discourages_LackOfTrust",   # 35
    "Discourages_LackOfProductInfo",# 36
    "Discourages_HiddenCosts",   # 37
    "HoursOnline",               # 38 — will be overridden below
]

def map_likert(series, col_name):
    def _map(val):
        if pd.isna(val):
            return np.nan
        s = str(val).strip().lower()
        return likert_map_ci.get(s, "__UNMATCHED__")
    result = series.apply(_map)
    bad = series[result == "__UNMATCHED__"]
    if not bad.empty:
        unmatched[col_name] = bad.unique().tolist()
    result = result.replace("__UNMATCHED__", np.nan).astype(float)
    return result

likert_series = {}
for idx, (col_raw, name) in enumerate(zip(likert_cols_raw, likert_names)):
    likert_series[name] = map_likert(col_raw, name)

# ── 15. HOURS ONLINE (col 38) ────────────────────────────────────────────────
hours_map = {
    "Less than 2 hours": 1,
    "2–4 hours":         2,
    "5–7 hours":         3,
    "8–10 hours":        4,
    "More than 10 hours": 5,
}
hours_online = track_unmatched("HoursOnline", hours_raw.str.strip(), hours_map)
# Remove the placeholder from likert_series
likert_series.pop("HoursOnline", None)

# ── 16. SOCIAL MEDIA DISCOVERY (col 39) ──────────────────────────────────────
social_map = {
    "Never":          1,
    "Rarely":         2,
    "Sometimes":      3,
    "Often":          4,
    "Very Frequently": 5,
}
social_discovery = track_unmatched("SocialMediaDiscovery", social_raw.str.strip(), social_map)

# ── 17. ASSEMBLE OUTPUT DATAFRAME ────────────────────────────────────────────
out = pd.DataFrame()

# Y first
out["MonthlyOnlineSpend_Y"] = monthly_spend_Y.values

# Demographics
out["Age"]                = age.values
out["Situation"]          = situation.values
out["RelationshipStatus"] = relationship.values
out["MonthlyIncome"]      = monthly_income.values
out["DisposableIncome"]   = disposable.values

# Income source dummies (right after DisposableIncome)
for col in income_dummy_cols:
    out[col] = income_dummies[col].values

# Behavioral
out["ShoppingFrequency"]  = shop_freq.values
out["AvgPerPurchase"]     = avg_per.values

# Buy dummies (right after AvgPerPurchase)
for col in buy_dummy_cols:
    out[col] = buy_dummies[col].values

# Likert – WhyShop block
for name in [
    "WhyShop_Convenient","WhyShop_SavesTime","WhyShop_BetterPrices",
    "WhyShop_EnjoyBrowsing","WhyShop_Habit","WhyShop_Hobbies",
    "WhyShop_Curious","WhyShop_Trending",
]:
    out[name] = likert_series[name].values

# Likert – Influence block
for name in [
    "Influence_Price","Influence_Quality","Influence_Brand",
    "Influence_SocialMedia","Influence_OnlineAds","Influence_WebDesign",
    "Influence_Reviews","Influence_Recommendations",
]:
    out[name] = likert_series[name].values

# Likert – Discourages block
for name in [
    "Discourages_PoorWebDesign","Discourages_NegativeReviews",
    "Discourages_HighDeliveryCost","Discourages_LongDelivery",
    "Discourages_PoorReturns","Discourages_PaymentSecurity",
    "Discourages_LackOfTrust","Discourages_LackOfProductInfo",
    "Discourages_HiddenCosts",
]:
    out[name] = likert_series[name].values

# Digital behaviour
out["HoursOnline"]           = hours_online.values
out["SocialMediaDiscovery"]  = social_discovery.values

print(f"\nOutput shape: {out.shape}")
print(f"Output columns ({len(out.columns)}):")
for c in out.columns:
    print(f"  {c}")

# ── 18. BUILD CODEBOOK ───────────────────────────────────────────────────────
likert_labels = "1=Strongly Disagree, 2=Disagree, 3=Neutral, 4=Agree, 5=Strongly Agree"

codebook_rows = [
    # col_name, type, value_labels
    ("MonthlyOnlineSpend_Y", "Scale (midpoints)",
     "25=€0–€50, 75=€51–€100, 125=€101–€150, 175=€151–€200, 225=€200+"),
    ("Age", "Scale", "Numeric integer (years)"),
    ("Situation", "Nominal",
     "1=Student (non-working), 2=Student (working), 3=Employed full-time, "
     "4=Employed part-time, 5=Self-employed, 6=Unemployed, 7=Stay-at-home"),
    ("RelationshipStatus", "Nominal",
     "1=Single, 2=In a relationship, 3=Cohabiting, 4=Married"),
    ("MonthlyIncome", "Ordinal",
     "1=€0–€999, 2=€1000–€1999, 3=€2000–€2999, 4=€3000–€3999, 5=€4000+; NaN=Prefer not to say"),
    ("DisposableIncome", "Ordinal",
     "1=€0–€499, 2=€500–€999, 3=€1000–€1499, 4=€1500+; NaN=Not sure"),
    ("Income_Salary",           "Dummy", "0=No, 1=Yes"),
    ("Income_StudentAllowance", "Dummy", "0=No, 1=Yes"),
    ("Income_FamilySupport",    "Dummy", "0=No, 1=Yes"),
    ("Income_Freelance",        "Dummy", "0=No, 1=Yes"),
    ("Income_StudentJob",       "Dummy", "0=No, 1=Yes"),
    ("Income_GovernmentBenefits","Dummy","0=No, 1=Yes"),
    ("Income_VolunteerWork",    "Dummy", "0=No, 1=Yes"),
    ("Income_Nothing",          "Dummy", "0=No, 1=Yes"),
    ("ShoppingFrequency", "Ordinal",
     "1=Less than once a month, 2=1–2/month, 3=3–5/month, 4=6–10/month, 5=More than 10/month"),
    ("AvgPerPurchase", "Scale (midpoints)",
     "12=€0–€25, 38=€26–€50, 63=€51–€75, 88=€76–€100, 125=€100+"),
    ("Buy_Clothing",     "Dummy", "0=No, 1=Yes"),
    ("Buy_Technology",   "Dummy", "0=No, 1=Yes (Technology/electronics)"),
    ("Buy_HomeItems",    "Dummy", "0=No, 1=Yes (Home items)"),
    ("Buy_KitchenItems", "Dummy", "0=No, 1=Yes (Kitchen items)"),
    ("Buy_Beauty",       "Dummy", "0=No, 1=Yes (Beauty/personal care)"),
    ("Buy_Entertainment","Dummy", "0=No, 1=Yes (Entertainment)"),
    ("Buy_Merchandise",  "Dummy", "0=No, 1=Yes"),
    ("WhyShop_Convenient",       "Scale (Likert)", likert_labels),
    ("WhyShop_SavesTime",        "Scale (Likert)", likert_labels),
    ("WhyShop_BetterPrices",     "Scale (Likert)", likert_labels),
    ("WhyShop_EnjoyBrowsing",    "Scale (Likert)", likert_labels),
    ("WhyShop_Habit",            "Scale (Likert)", likert_labels),
    ("WhyShop_Hobbies",          "Scale (Likert)", likert_labels),
    ("WhyShop_Curious",          "Scale (Likert)", likert_labels),
    ("WhyShop_Trending",         "Scale (Likert)", likert_labels),
    ("Influence_Price",          "Scale (Likert)", likert_labels),
    ("Influence_Quality",        "Scale (Likert)", likert_labels),
    ("Influence_Brand",          "Scale (Likert)", likert_labels),
    ("Influence_SocialMedia",    "Scale (Likert)", likert_labels),
    ("Influence_OnlineAds",      "Scale (Likert)", likert_labels),
    ("Influence_WebDesign",      "Scale (Likert)", likert_labels),
    ("Influence_Reviews",        "Scale (Likert)", likert_labels),
    ("Influence_Recommendations","Scale (Likert)", likert_labels),
    ("Discourages_PoorWebDesign",       "Scale (Likert)", likert_labels),
    ("Discourages_NegativeReviews",     "Scale (Likert)", likert_labels),
    ("Discourages_HighDeliveryCost",    "Scale (Likert)", likert_labels),
    ("Discourages_LongDelivery",        "Scale (Likert)", likert_labels),
    ("Discourages_PoorReturns",         "Scale (Likert)", likert_labels),
    ("Discourages_PaymentSecurity",     "Scale (Likert)", likert_labels),
    ("Discourages_LackOfTrust",         "Scale (Likert)", likert_labels),
    ("Discourages_LackOfProductInfo",   "Scale (Likert)", likert_labels),
    ("Discourages_HiddenCosts",         "Scale (Likert)", likert_labels),
    ("HoursOnline", "Ordinal",
     "1=Less than 2 hours, 2=2–4 hours, 3=5–7 hours, 4=8–10 hours, 5=More than 10 hours"),
    ("SocialMediaDiscovery", "Ordinal",
     "1=Never, 2=Rarely, 3=Sometimes, 4=Often, 5=Very Frequently"),
]

codebook_df = pd.DataFrame(codebook_rows, columns=["ColumnName", "Type", "ValueLabels"])

# ── 19. WRITE EXCEL ──────────────────────────────────────────────────────────
with pd.ExcelWriter(OUTPUT, engine="openpyxl") as writer:
    out.to_excel(writer, sheet_name="Data", index=False)
    codebook_df.to_excel(writer, sheet_name="Codebook", index=False)

# ── 20. FORMAT with openpyxl ─────────────────────────────────────────────────
wb = load_workbook(OUTPUT)

# --- Data sheet header formatting ---
ws_data = wb["Data"]
header_fill = PatternFill(fill_type="solid", fgColor="1F497D")
header_font = Font(color="FFFFFF", bold=True, size=10)
for cell in ws_data[1]:
    cell.fill  = header_fill
    cell.font  = header_font
    cell.alignment = Alignment(horizontal="center", wrap_text=True)
# Auto-width (approximate)
for col_cells in ws_data.columns:
    max_len = max(len(str(c.value)) if c.value is not None else 0 for c in col_cells)
    ws_data.column_dimensions[col_cells[0].column_letter].width = min(max_len + 2, 22)
ws_data.freeze_panes = "A2"

# --- Codebook sheet formatting ---
ws_cb = wb["Codebook"]
cb_fill = PatternFill(fill_type="solid", fgColor="375623")
cb_font = Font(color="FFFFFF", bold=True, size=10)
for cell in ws_cb[1]:
    cell.fill  = cb_fill
    cell.font  = cb_font
    cell.alignment = Alignment(horizontal="center")
ws_cb.column_dimensions["A"].width = 30
ws_cb.column_dimensions["B"].width = 18
ws_cb.column_dimensions["C"].width = 80
for row in ws_cb.iter_rows(min_row=2):
    for cell in row:
        cell.alignment = Alignment(wrap_text=True, vertical="top")
ws_cb.freeze_panes = "A2"

wb.save(OUTPUT)
print(f"\nSaved → {OUTPUT}")

# ── 21. SUMMARY ───────────────────────────────────────────────────────────────
print("\n" + "="*60)
print("SUMMARY")
print("="*60)
print(f"  Total rows    : {len(out)}")
print(f"  Total columns : {len(out.columns)}")
print(f"\n  Missing-value counts per column:")
miss = out.isnull().sum()
miss_cols = miss[miss > 0]
if miss_cols.empty:
    print("    (none)")
else:
    for c, v in miss_cols.items():
        print(f"    {c}: {v} missing")

print(f"\n  Unmatched / dirty values found:")
if not unmatched:
    print("    (none – all values mapped cleanly)")
else:
    for col, vals in unmatched.items():
        print(f"    [{col}] → {vals}")
