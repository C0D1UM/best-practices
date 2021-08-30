# Interview Problems for Flutter.

## Solve (No.1 - 4 just make the function to show in the console - no need to make UI)
`(You can do in any languages you need such as Dart, Python , Typescript etc.)`
1. Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

  **Example Output:**
  ```
  1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz
  Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz
  41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz
  61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz
  Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz
  ```

2. Write a program that determine whether or not an integer input is a leap year.
  - Definition of leap year:
    - Rule 1: A year is called leap year if it is divisible by 400.

      **Example:** 1600, 2000 etc. are leap year while 1500, 1700 are not leap year.
    - Rule 2: If year is not divisible by 400 as well as 100 but it is divisible by 4 then that year are also leap year.

      **Example:**  2004, 2008, 1012 are leap year.

  **Example Output:**
  ```
  1600 -> true
  2000 -> true
  1500 -> false
  2004 -> true
  2008 -> true
  2010 -> false
  ```

3. Write a program that produce the following output giving an integer input n.

  * 3.1
```
n=3    n=4      n=6
  *      *        *
 **     **       **
***    ***      ***
      ****     ****
              *****
             ******
```

  * 3.2
```
n=1    n=2      n=3    	  n=4       n=5
*       *        *         *         *
       * *      * * 	  * *       * *
               *   *	 *   *     *   * 		    
                        *     *   *     *
                                 *       *          
        
```

  * 3.3
```
n=1	n=2	n=3	n=4     n=5
*	**	* *	*  *	*   *
	**	 * 	 **      * *
		* *	 **       *  
			*  *	 * *
			        *   *
```


4. Write a program that finds all prime numbers up to n for input n.
**Example Output:**
```
20 -> 2 3 5 7 11 13 17 19
```
## Solve (No.5 - 7 make UI from Flutter)
5. <b>Basic layout</b>
- Create application following to the layout like the photo1 below.<br><br>
![photo1.png](/photos/photo1.png)<br><br>
- Use Linear layout (Row, Column)<br>
- The widgets in the photo are consisted of : <br>
  - Container with Text, <br>
  - Font size = 14, <br>
  - Text-Alignment inside the widget = center and appropriate distance (padding), <br>
  - Distance between widgets = 4 pixels, <br>
  - Manage color component clearly and easy to understand. <br>
  - Be able to rotate the screens and show widgets in each positions properly. (photo2 to show landscape)<br><br>
![photo2.png](/photos/photo2.png)

<br>
References : https://www.youtube.com/watch?v=_rnZaagadyo <br><br>

  
  ---
6. <b>CODIUM Login page.</b><br><br>
Create login page that consisted of:

Components:
- 1 x Logo
- 2 x Text Fields for username and password (password field need to secure text by using *).
  - hardcode username = 'CODIUM'<br>
  - hardcode password = 'CODIUM'
- 1 x Button for login.
  - After press button if username or password is incorrect will popup the AlertDialog to inform user.
  - If username and password are correct go to next page (can be blank page).<br><br>

---

7. <b>Create a small app that has 2 pages (Person page and Edit Profile page) similar to an example below.</b><br>

- **Person page** : Collect the info in Card widget and show in this page (there are name, e-mail, address in the card), when pressing the card, it will navigate to Edit Profile page for editing data.
- **Edit Profile page** : For editing data, user can fill the new data and press save button, then it will save and navigate to Person page (make everything on Flutter - nothing Backend).
- The validation of each field is not defined (it's up to you).

Components:
- 2 x Buttons for 'BACK' and 'SAVE'
- 1 x Image field
- 4 x Text fields for input (name, e-mail, birthday, address)
- Cards to collect person info.
- Etc.<br>

![flutter-exam.png](/photos/flutter-exam.png)<br><br><br>
## Please do all the tests in your github repo and share us only your repo together with explaining a bit in readme about what did you do, how to test, anything you would like to tell.
