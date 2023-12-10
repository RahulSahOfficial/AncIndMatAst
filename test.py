from AncIndMatAst import BM,AC,BA,Eclipse


data=AC.encode(364224)
print(data.get("sabd"))
print(data.get("length"))
print(data.get("allSabd"))


# ढुङ्विध्व
# ढुङिविघव
# खिच्युभ
# भदिलझुनुखृ
# ख्युघृ
# जषबिखुछृ
# सुगुशिथृन
# चयगियिङुशुछृलृ
word="जषबिखुछृ"
value=AC.decode(word)
print(f"Value of {word} = {value}")




# Bhaskara Method 
# Square Root 
num=144
sq=BM.squareRoot(num)
print("Square Root By Bhaskara Method = ",sq)

# Cube Root 
num=175616
sq=BM.cubeRoot(num)
print("Cube Root By Bhaskara Method = ",sq)


# Bodhaayana Approximation Method 
num=200
sq=BA.squareRoot(num)
print("Square Root By Bodhaayana Approximation Method = ",sq)

# Sidhantic Procedure For Eclipse 
# Lunar Eclipse
# Example 1
date = (2006, 10, 7)
time = (24,12,0)
trueMoon=(321,3,27)
trueRahu=(331,21,11)
Eclipse.LunarEclipse(date,time,trueMoon,trueRahu)

# Solar Eclipse 
date = (2008, 8, 1)
iONMoon=(15,42,0)
trueMoon=(105,33,0)
trueRahu=(294,37,26)

Eclipse.SolarEclipse(date,iONMoon,trueMoon,trueRahu)