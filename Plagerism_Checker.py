p1 = 'Deep within the heart of the dense woodland, a lithe and nimble brown fox effortlessly executes a graceful leap, soaring above the slumbering dog with an air of agility and speed. The fox\'s movements are a testament to its inherent prowess, navigating through the dense foliage with a seamless blend of precision and swiftness. Meanwhile, the lazy canine, undisturbed by the fox\'s acrobatic display, remains in its peaceful repose, blissfully unaware of the dynamic performance taking place overhead'
p2 = 'Within the heart of the dense forest, a nimble and lithe brown fox effortlessly executes a leap of grace, soaring over the peacefully dozing dog with an air of speed and agility. The fox\'s motions bear witness to its innate prowess, gliding through the thick foliage with a harmonious fusion of precision and swiftness. Simultaneously, the lethargic dog, undisturbed by the fox\'s acrobatic showcase, continues in its undisturbed repose, completely oblivious to the energetic spectacle transpiring just above.'
p1 = list(p1)
for i in p1:
  if i == '.' or i == ',':
    p1.remove(i)
p1 = (''.join(p1)).split()
p2 = list(p2)
for i in p2:
  if i == '.' or i == ',':
    p2.remove(i)
p2 = (''.join(p2)).split()
#print(p1, p2)
for i in range(len(p1)):
  try:
    if p1[i] in p2:
      x = p1[i], p1[i+1], p1[i+2], p1[i+3], p1[i+4]
      if ''.join(x) in ''.join(p2):
        print('Plagerized:', ' '.join(x))
  except IndexError:
    print()
  
