#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = input("Enter a Fahrenheit temperture:")
  tempF = int(tempF)
  tempC = (tempF - 32 ) * 5 / 9

  num = tempC
  num = round(num, 2)
  print(num)

  print(tempF, "is ", num, "degrees celsius.")
if __name__ == '__main__':
  main()
