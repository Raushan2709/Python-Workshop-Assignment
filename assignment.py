import pandas as p
a=p.read_csv("Physics.csv")

# Highest attendance in first five rows
f=a.head(5)
b=a.iloc[:5].loc[a["Attendance"].iloc[:5].idxmax()]
print("\n1 - Highest attendance in first five row")
print(b)

# Highest attendance in last five row

c=a.iloc[-5:].loc[a["Attendance"].iloc[-5:].idxmax()]
print("\n2 - Highest attendance in last five row")
print(c)

# Highest attendance student between row 10-20

d=a.iloc[9:20].loc[a["Attendance"].iloc[9:20].idxmax()]
print("\n3 - Highest attendance in row 10-20")
print(d)


# Highest attendance overall

e=a.loc[a["Attendance"].idxmax()]
print("\n4 - Student Having Highest attendance overall")
print(e)