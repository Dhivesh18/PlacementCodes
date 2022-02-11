# Replace Space to _+_
s=input().split(",") # Input = Zoom healthcare,17
print(s)
# Output = Zoom_+_healthcare
t=s[0].replace(" ","_+_")
print(t)
