"""Bitmap Message
Displays a text message according to the provided bitmap image.

Tags: Tiny, beginner, artistic"""

import sys

# (!) Change the below image to anything

# There are 68 periods along the top and bottom of this string:


bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print("bitmap message")
print("Enter a message to display with the bitmap.")
message = input("> ")
if message == "":
    sys.exit()

# Loop over each line in the bitmap
for line in bitmap.splitlines():
    # Loop over each char in the line
    for i, bit in enumerate(line):
        if bit == ' ':
            # Print an empty space since there's a space in the bitmap
            print(' ', end='')
        else:
            # Print a character from the message
            print(message[i % len(message)], end='')
    print()