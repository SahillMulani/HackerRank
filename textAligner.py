thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#Bottom Cone
for i in range(thickness):
     print((c*(thickness-1)).rjust(thickness)+(c*(thickness-2)).ljust(thickness))
#Mid Part
for i in range(thickness-2):
     print((c*(thickness-1)).rjust(thickness)+(c*(thickness+10)).ljust(thickness)+(c*(thickness)).rjust(thickness+10))
         
for i in range(thickness):
     print((c*(thickness-1)).rjust(thickness)+(c*(thickness-2)).ljust(thickness))

for i in range(thickness -3):
     print((c*(thickness-1)).rjust(thickness)+(c*(thickness-2)).ljust(thickness))

for i in range(thickness):
     print((c*(thickness)).rjust(thickness+10))