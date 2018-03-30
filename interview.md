# Interview Problems

## Code, Consult, Communicate

Todo List

Let’s start with the good-old trusty todo list, the “Hello, World” of full programs. You’re going to write a command-line todo list program that meets the following specifications:

1. Prompt the user to enter a chore or task. Store the task in a permanent location so that the task persists when the program is restarted.
2. Allow the user to enter as many tasks as desired but stop entering tasks by entering a blank task. Do not store the blank task.
3. Display all the tasks.
4. Allow the user to remove a task, to signify it’s been
completed.
5. Persist todos to Redis

## Easy
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
n=3   n=4    n=6
*     *      *
**    **     **
***   ***    ***
      ****   ****
             *****
             ******
```

  * 3.2
```
n=3    n=4      n=6
  *      *        *
 **     **       **
***    ***      ***
      ****     ****
              *****
             ******
```

  * 3.3
```
n=1    n=2      n=3    	  n=4       n=5
*       *        *         *         *
       * *      * * 	  * *       * *
               *   *	 *   *     *   * 		    
                        *     *   *     *
                                 *       *          
        
```

  * 3.4
```
n=1	n=2	n=3	n=4     n=5
*	**	* *	*  *	*   *
	**	 * 	 **      * *
		* *	 **       *  
			*  *	 * *
					*   *
```

  * 3.5  (NB: Not easy)
```
n=1  n=2  n=3   n=4    n=5        n=9
*    *     *     *      *          *
     *    ***   ***    ***        ***
           *    ***   *****      *****
                 *     ***      *******
                        *      *********
                                *******
                                 *****
                                  ***
                                   *
```
  * 3.6
```
n=1		n=2     n=3         n=4
+       A+B     AA+BB       AAA+BBB
        +E+     A+E+B       AA+E+BB
        C+D  	+EEE+       A+EEE+B
                C+E+D       +EEEEE+
                CC+DD       C+EEE+D	
                            CC+E+DD
                            CCC+DDD
```

4. (Python specific) In Python, what is the difference between `else` and `finally` in exception handling?

## Medium
1. Write a program that finds all prime numbers up to n for input n.
**Example Output:**
```
20 -> 2 3 5 7 11 13 17 19
```

## Hard
