"""Name:Matthew Harris"""
"""Date:9/7/24"""
"""Assignment:loop fun"""
"""Description:use loops to create a function to draw a box get mean between the heights and print pictures of them """
def main():
      while True:
       box_height = int(input("Enter the height for the box (3-12): "))
       if 3 <= box_height <= 12:
            break 
       else:
            print("Please enter a number between 3 and 12.")
      while True:
       box_width = int(input("Enter the width for the box (bigger than the height but less than 20): "))
       if box_height <= box_width <= 20:
            break 
       else:
            print("Please enter a number bigger than your box height and smaaller than 20.")
      print("The integers between those numbers are ")
      for i in range(box_height, box_width+1):
          print(i,end=" ")
           
      
      average = (box_height + box_width) / 2
      print(f"the average of these numbers is {average}")
      
      
      print("*" * box_width)
      for i in range(box_height - 2):
          print("*" + " " * (box_width - 2) + "*")
      print("*" * box_width)


      for i in range(1, box_height+1):
          print("*"*(2*i))
                

if __name__ == '__main__':
    main() # don't change this