earth_weight=float(input())
moon_weight=earth_weight*0.165
years_at_start=0
full_years=15
while years_at_start <full_years:
    earth_weight +=1 
    moon_weight = earth_weight *0.165
    years_at_start +=1
    print(moon_weight)