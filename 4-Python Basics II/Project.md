For the following project we will create three programs. Specifications are given below.

Program 1:
 - This is used for inserting ID numbers and names into a file named `database.csv`
 - User will be asked to enter ID number until a valid ID number is entered (number with 7 digits)
 - User will be asked to enter a name, and a last name (any value is accepted for both of these)
 - The program will open the `database.csv` file and will append the values given in the corresponding columns

Program 2:
- This is used for adding a note to an student
- User will be asked to enter an ID number until a value present in the document is given.
- User will be asked to enter a score until a valid score is entered (0-100), This score will be added to the corresponding column for the student that has that id.
- If the id number has already 4 scores assigned it won't allow any more scores.


Program 3:
- This is used for classifying students into approved, reproved, extension test categories
- If student has less that 3 scores no classification is given
- If user has more than 3 scores, only the greatest values are taking into consideration
- Use the 3 selected scores to compute the mean value. Student will be classified according to the following:
    * reproved: mean is below 55, including 55
    * extension test: mean is between 55 and 65, excluding 55 but including 65
    * approved: mean is above 65

- The classification label must be added to the corresponding column
