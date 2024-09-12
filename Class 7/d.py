d = {"Gender":"Female", "Age":"13"}
print(d)
print(d.get("Age"))
d["Age"] = "12"
print(d)
d["Adress"] = "Sunshine Society"
print(d)
print(d.get("Gender"))
d.clear()
print(d)