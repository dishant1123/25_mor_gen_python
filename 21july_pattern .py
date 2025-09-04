#pattern  : 
"""          
* * * * *    *           * * * * *    1          5 4 3 2 1   1 2 3 4 5
* * * * *    * *         * * * *      1 2        5 4 3 2     2 3 4 5
* * * * *    * * *       * * *        1 2 3      5 4 3       3 4 5
* * * * *    * * * *     * *          1 2 3 4    5 4         4 5
* * * * *    * * * * *   *            1 2 3 4 5  5           5
"""
#1 : 
"""
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()
"""
#2:
"""
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""
#3
"""
for i in range(1,6):
    for j in range(5,i-1,-1): #start  stop step 
        print("*",end=" ")
    print()
"""

#6 .
"""
for i in range(1,6):
    for j in range(i,6): #start  stop step 
        print(j,end=" ")
    print()
"""

"""
* * * * *   * * * * *        *         *              * 
  * * * *    * * * *       * *        * *            * *
    * * *     * * *      * * *       * * *          * * *
      * *      * *     * * * *      * * * *        * * * *
        *       *    * * * * *     * * * * *      * * * * *
                                                   * * * *
                                                    * * *
                                                     * *
                                                      *
"""
#7.
"""for i in range(1,6):
    for  k in range(1,i):
        print(" ",end=" ")
    for j in range(5,i-1,-1): #start  stop step 
        print("*",end=" ")
    print()
"""

#8. 
"""
for i in range(1,6):
    for  k in range(1,i):
        print(" ",end="")
    for j in range(5,i-1,-1): #start  stop step 
        print("*",end=" ")
    print()
"""

#9.
"""
for i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""

#10:
"""
for i in range(1,5):
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,6):
    for  k in range(1,i):
        print(" ",end="")
    for j in range(5,i-1,-1): #start  stop step 
        print("*",end=" ")
    print()
"""