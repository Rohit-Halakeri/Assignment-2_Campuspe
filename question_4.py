from datetime import date

# Ask full birth date
day = int(input("Enter birth day: "))
month = int(input("Enter birth month: "))
year = int(input("Enter birth year: "))

birth_date = date(year, month, day)
today = date.today()

# Exact age in days
total_days = (today - birth_date).days

# Converting 
years = total_days // 365
months = total_days // 30
hours = total_days * 24
minutes = hours * 60

years_to_100 = 100 - years

print("\nExact age details:")
print("Current age:", years)
print("Age in months (approx):", months)
print("Age in days:", total_days)
print("Age in hours:", hours)
print("Age in minutes:", minutes)
print("Years until 100:", years_to_100)