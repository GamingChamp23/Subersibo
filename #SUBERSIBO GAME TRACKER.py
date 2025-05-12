#SUBERSIBO GAME TRACKER

points = {
  'Subversive Power Points' : 4000,
  'Colonialist Power Points' : 4000,
  'Subversive CV' : 200,
  'Colonialist CV' : 200,
}

print("""================================================================================
                SUBERSIBO: ANG ANINONG REBOLUSYON - POINTS TRACKER""")
print("Subversive Power Points: " + str(points['Subversive Power Points']))
print("Colonialist Power Points: " + str(points['Colonialist Power Points']))
print("Subversive CV: " + str(points['Subversive CV']))
print("Colonialist CV: " + str(points['Colonialist CV']))
print("""================================================================================
""")


while True:
  allegiance = input("Allegiance (Subversive, Colonialist): ")
  x = input("Target Stat (PP, CV):")
  value = input("Points: ")
  operation = input("Operation (+ for add or - for subtract): ")
  if allegiance == 'Subversive':
    if x == 'PP':
      try: 
        int(value)
        if int(value) > 0:
          if operation == '-':
            points['Subversive Power Points'] = int(points['Subversive Power Points']) - int(value)
            if points['Subversive Power Points'] > 0:
              print("""================================================================================
                SUBERSIBO: ANG ANINONG REBOLUSYON - POINTS TRACKER""")
              print("Subversive Power Points: " + str(points['Subversive Power Points']))
              print("Colonialist Power Points: " + str(points['Colonialist Power Points']))
              print("Subversive CV: " + str(points['Subversive CV']))
              print("Colonialist CV: " + str(points['Colonialist CV']))
              print("""================================================================================
              """)
            elif points['Subversive Power Points'] <= 0:
              print("""================================================================================
                SUBERSIBO: ANG ANINONG REBOLUSYON - POINTS TRACKER""")
              print("Subversive Power Points: " + 'LOST THE GAME')
              print("Colonialist Power Points: " + 'WINNER!')
              print("Subversive CV: " + str(points['Subversive CV']))
              print("Colonialist CV: " + str(points['Colonialist CV']))
              print("The Colonialists have won the game!")
              print("""================================================================================
              """)
              break

          elif operation == '+':
            points['Subversive Power Points'] = int(points['Subversive Power Points']) + int(value)
            print("""================================================================================
              SUBERSIBO: ANG ANINONG REBOLUSYON - POINTS TRACKER                  """)
            print("Subversive Power Points: " + str(points['Subversive Power Points']))
            print("Colonialist Power Points: " + str(points['Colonialist Power Points']))
            print("Subversive CV: " + str(points['Subversive CV']))
            print("Colonialist CV: " + str(points['Colonialist CV']))
            print("""================================================================================
            """)
          else:
            print("Invalid operation. Please enter + or -.")
        else:
          print("Invalid value. Please enter a positive integer.")
      except ValueError:
        print("Invalid value. Please enter a positive integer.")
    elif x == 'CV':
      try:
        int(value)
        if int(value) > 0:
          if operation == '-':
            points['Subversive CV'] = int(points['Subversive CV']) - int(value)
            if points['Subversive CV'] > 0:
              print("""================================================================================
                SUBERSIBO: ANG ANINONG REBOLUSYON - POINTS TRACKER                   """)
              print("Subversive Power Points: " + str(points['Subversive Power Points']))
              print("Colonialist Power Points: " + str(points['Colonialist Power Points']))
              print("Subversive CV: " + str(points['Subversive CV']))
              print("Colonialist CV: " + str(points['Colonialist CV']))
              print("""================================================================================
              """)
            elif points['Subversive CV'] <= 0:
              points['Subversive CV'] = int(points['Subversive CV']) + int(value)
              print("""================================================================================
                SUBERSIBO: ANG ANINONG REBOLUSYON - POINTS TRACKER   """)
              print("Subversive Power Points: " + str(points['Subversive Power Points']))
              print("Colonialist Power Points: " + str(points['Colonialist Power Points']))
              print("Subversive CV: " + str(points['Subversive CV']) + " (NOT ENOUGH COINS; CANNOT BUY)")
              print("Colonialist CV: " + str(points['Colonialist CV']))
              print("""================================================================================
              """)
          elif operation == '+':
            points['Subversive CV'] = int(points['Subversive CV']) + int(value)
            print("""================================================================================
              SUBERSIBO: ANG ANINONG REBOLUSYON - POINTS TRACKER""")
            print("Subversive Power Points: " + str(points['Subversive Power Points']))
            print("Colonialist Power Points: " + str(points['Colonialist Power Points']))
            print("Subversive CV: " + str(points['Subversive CV']))
            print("Colonialist CV: " + str(points['Colonialist CV']))
            print("""================================================================================
            """)
          else:
            print("Invalid operation. Please enter + or -.")
        else:
          print("Invalid value. Please enter a positive integer.")
      except ValueError:
        print("Invalid value. Please enter a positive integer.")
    else:
      print("Invalid input. Please enter PP or CV.")
  elif allegiance == 'Colonialist':
    if x == 'PP':
      try:
        int(value)
        if int(value) > 0:
          if operation == '-':
            points['Colonialist Power Points'] = int(points['Colonialist Power Points']) - int(value)
            if points['Colonialist Power Points'] > 0:
              print("""================================================================================
                SUBERSIBO: ANG ANINONG REBOLUSYON - POINTS TRACKER""")
              print("Subversive Power Points: " + str(points['Subversive Power Points']))
              print("Colonialist Power Points: " + str(points['Colonialist Power Points']))
              print("Subversive CV: " + str(points['Subversive CV']))
              print("Colonialist CV: " + str(points['Colonialist CV']))
              print("""================================================================================
              """)
            elif points['Colonialist Power Points'] <= 0:
              print("""================================================================================
                SUBERSIBO: ANG ANINONG REBOLUSYON - POINTS TRACKER""")
              print("Subversive Power Points: " + 'WINNER!')
              print("Colonialist Power Points: " + 'LOST THE GAME')
              print("Subversive CV: " + str(points['Subversive CV']))
              print("Colonialist CV: " + str(points['Colonialist CV']))
              print("The Subversives have won the game!")
              print("""================================================================================
              """)
              break

          elif operation == '+':
            points['Colonialist Power Points'] = int(points['Colonialist Power Points']) + int(value)
            print("""================================================================================
               SUBERSIBO: ANG ANINONG REBOLUSYON - POINTS TRACKER                  """)
            print("Subversive Power Points: " + str(points['Subversive Power Points']))
            print("Colonialist Power Points: " + str(points['Colonialist Power Points']))
            print("Subversive CV: " + str(points['Subversive CV']))
            print("Colonialist CV: " + str(points['Colonialist CV']))
            print("""================================================================================
            """)
          else:
            print("Invalid operation. Please enter + or -.")
        else:
          print("Invalid value. Please enter a positive integer.")
      except ValueError:
        print("Invalid value. Please enter a positive integer.")
    elif x == 'CV':
      try:
        int(value)
        if int(value) > 0:
          if operation == '-':
            points['Colonialist CV'] = int(points['Colonialist CV']) - int(value)
            if points['Colonialist CV'] > 0:
              print("""================================================================================
                SUBERSIBO: ANG ANINONG REBOLUSYON - POINTS TRACKER                   """)
              print("Subversive Power Points: " + str(points['Subversive Power Points']))
              print("Colonialist Power Points: " + str(points['Colonialist Power Points']))
              print("Subversive CV: " + str(points['Subversive CV']))
              print("Colonialist CV: " + str(points['Colonialist CV']))
              print("""================================================================================
              """)
            elif points['Colonialist CV'] <= 0:
              points['Colonialist CV'] = int(points['Colonialist CV']) + int(value)
              print("""================================================================================
                SUBERSIBO: ANG ANINONG REBOLUSYON - POINTS TRACKER   """)
              print("Subversive Power Points: " + str(points['Subversive Power Points']))
              print("Colonialist Power Points: " + str(points['Colonialist Power Points']))
              print("Subversive CV: " + str(points['Subversive CV']))
              print("Colonialist CV: " + str(points['Colonialist CV']) + " (NOT ENOUGH COINS; CANNOT BUY)")
              print("""================================================================================
              """)
          elif operation == '+':
            points['Colonialist CV'] = int(points['Colonialist CV']) + int(value)
            print("""================================================================================
              SUBERSIBO: ANG ANINONG REBOLUSYON - POINTS TRACKER""")
            print("Subversive Power Points: " + str(points['Subversive Power Points']))
            print("Colonialist Power Points: " + str(points['Colonialist Power Points']))
            print("Subversive CV: " + str(points['Subversive CV']))
            print("Colonialist CV: " + str(points['Colonialist CV']))
            print("""================================================================================
            """)
          else:
            print("Invalid operation. Please enter + or -.")
        else:
          print("Invalid value. Please enter a positive integer.")
      except ValueError:
        print("Invalid value. Please enter a positive integer.")
    else:
      print("Invalid input. Please enter PP or CV.")
  else:
    print("Invalid allegiance. Please enter Subversive or Colonialist.")
  continue