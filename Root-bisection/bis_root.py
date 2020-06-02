import re

class rootFinder:

    def __init__(self, file):
        """
        :param file: the file we're going to use to store the data. Preferibly in .csv format, although it can be .txt
                    as well

        Just the constructor with the parameters of the class.
        The file stores the values in the following standard: value1;value2;value3;value4;value5 , which are as follows

        value1: the n-th root we have found
        value2: the base number
        value3: the sensibility, 4 by default
        value4: the value of the n-th root of the base
        value5: the denormalization mode (properly explained on the terms documentation)

        Example gratia, the square root of 4 would be stored as '2;4;4;2;normal'
        """
        self.roots = file

    def writeRoot(self, root, base, sens, result, type):
        """
        :param root: int, the n-th root we are to find
        :param base: int, the base number. E.g., the square root of 5 has base 5
        :param sens: int, the sensibility, given as a negative exponent with base 10 E.g., if sens == 4, our sensibility
                     will be 10^(-4), 0.0001. It's by default 4 given the way it's used in the script
        :param result: float, the n-th root of the base number
        :param type: string, the type of the root (for normalization purposes
        :return: None, void method

        The idea of this method is to store a new result on the storage file as to create a quick access for further use
        """
        rootsfile = open(self.roots, "a+")
        string = [str(root), str(base), str(sens), str(result), type]
        rootsfile.write(";".join(string) + "\n")

    def updateRoot(self, root, base, sens, result, type):
        """
        :param root: int, the n-th root we are to find
        :param base: int, the base number. E.g., the square root of 5 has base 5
        :param sens: int, the sensibility, given as a negative exponent with base 10 E.g., if sens == 4, our sensibility
                     will be 10^(-4), 0.0001. It's by default 4 given the way it's used in the script
        :param result: float, the n-th root of the base number
        :param type: string, the type of the root (for normalization purposes
        :return: None, void method

        This function allows of a result to be updated were it to be found a more precise result
        """
        rootsfile = list(open(self.roots, "r"))
        string = [str(root), str(base), str(sens), str(result), type]
        newroots = open(self.roots, "w+")

        for e in range(len(rootsfile)):
            if len(re.findall(";".join(string[:1]), rootsfile[e])) > 0:
                rootsfile[e].replace(rootsfile[e], ";".join(string) + "\n")
            newroots.write(rootsfile[e])


    def rootSearch(self, root, base, sens=4, mode="print"):
        """
        :param root: int, the n-th root we are to find
        :param base: int, the base number. E.g., the square root of 5 has base 5
        :param sens: int the sensibility, given as a negative exponent with base 10 E.g., if sens == 4, our sensibility
                     will be 10^(-4), 0.0001. It's 4 by default
        :param mode: string, the mode we want to make te search for. If it's 'print', it's for console display.
                     If it's 'return' it's to be returned to be used
        :return: None, void method

        The function works this way: we first check if we have currently a registry with that data. Then, if we don't,
        we calculate it.

        If we do, we then check of it has better sensibility than the one we are asking for (the higher
        'sens' is, the higher our sensibility). If it doesn't, we just search the result in the registry. If it has, we
        calculate the root within the environment of the less precise result.

        Also, given the storage standard, we have to give it as its proper result.
        E.g., the cubic root of -27 would be stored as '3;-27;4;3;uneven-negative' so in order to display '-3'
        we have to multiply the fourth element of the values by (-1). This process ir referred as "denormalization"
        and shall be explained properly in the terms documentation
        """
        def find_to_update():
            """
            No parameters are used as every single one used here is imported from the parent function
            :return: [ret, val], list of the check values.
                     'ret' alludes to if we already have such a registry or not. If we do, it's True, if not it's False.
                     'val' is the value, in case we have a matching registry. If not, it's None


            """
            pattern = ";".join([str(root), str(base)])
            ret = False
            val = None
            for e in list(self.roots):

                base_sens = e.split(";")[2]

                if len(re.findall(pattern, e)) > 0 and sens >= int(base_sens):
                    ret = True
                    val = e.split(";")[3]
                elif len(re.findall(pattern, e)) > 0:
                    ret = True

            return [ret, val]

        def find_root(utmost): #Search function, aka 'Applied bisection algorithm'
            """
            :param utmost: either int or list. If it's an int, it's the number whose n-th root we are to find.
                           if it's a list, it's the range of values where we seek a more precise result.
            :return: [midpoint, type]. 'midpoint' is the value of the n-th root normalized,
                     'type' is the kind of normalization we are to use

            The whole explanation of how this function works is explained in the theorical basis documentation
            although critical points of the process have been signaled in order to help in the logical process
            """
            def target_function(number): #Target function
                """
                :param number: float or int, the number we are to check
                :return: float, The difference between the normalized base and our number up to the root number

                This function is our target function. In a mathematical sense this would be equivalent
                to when we speak of f(x) where x would be the 'number' parameter.
                Lambda functions use is discouraged in this case by PEP8 so I discarded the use of it
                """
                return ba - number ** root

            #Normalization process
            if root%2 == 0 and utmost < 0:
                print ("Error, no real root avaliable for this number")
                return None
            elif root%2 == 0:
                type = "even"
            elif root%2 ==1 and utmost < 0:
                type = "uneven-negative"
            else:
                type = "normal"

            #Finding process
            qzero = 10**(-sens)

            if isinstance(utmost, int) or isinstance(utmost, float):
                ba = abs(utmost)
                interval = [qzero, ba]
            elif isinstance(utmost, list) and 0 <= utmost[0] < utmost[1]:
                rext = abs(utmost[1])
                lext = abs(utmost[0])
                interval = [lext, rext]
            else:
                print("No correct interval")
                return None

            midpoint = (interval[0] + interval[1])/2
            diff = abs(target_function(midpoint))

            while diff > qzero:
                if target_function(interval[0])*target_function(midpoint) < 0:
                    interval = [interval[0], midpoint]
                    midpoint = (interval[0] + interval[1]) / 2
                    diff = abs(target_function(midpoint))
                elif target_function(interval[1])*target_function(midpoint) < 0:
                    interval = [midpoint, interval[1]]
                    midpoint = (interval[0] + interval[1]) / 2
                    diff = abs(target_function(midpoint))
                else:
                    print("this cannot be")
                    return None



            return [midpoint, type]

        #Case discussion
        chk = find_to_update()

        if not chk[0]: #We don't have such registry
            results = find_root(base)
            self.writeRoot(root, base, sens, results[0], results[1])
        elif chk[0] and chk[1] is not None: #We have such registry but we are asked for a more precise one
            results = find_root([chk[1] - 0.1, chk[1] + 0.1])
            self.updateRoot(root, base, sens, results[0], results[1])
        else: #We have such registry and we are asked for a less or equally precise one
            results = None
            pattern = ";".join([str(root), str(base)])
            for e in list(self.roots):
                if len(re.findall(pattern, e)) > 0:
                    results = [None, None, None, int(e.replace("\n", "").split(";")[3]), e.replace("\n", "").split(";")[4]]
            if results is None:
                print("No can do")
                return None

        ro = results[3]
        ty = results[4]

        # Denormalization process
        if ty == "even" and mode == "print":
            print("The roots are " + str(ro) + " and " + str(-ro))

        elif ty == "even":
            return [ro, -ro]

        elif ty == "uneven-negative" and mode == "print":
            print("The root is " + str(-ro))

        elif ty == "uneven-negative":
            return -ro

        elif ty == "normal" and mode == "print":
            print("The root is " + str(ro))

        elif ty == "normal":
            return ro

    def rootReturn(self, root, base, sens=4):
        """
        :param root: int, the n-th root we are to find
        :param base: int, the base number. E.g., the square root of 5 has base 5
        :param sens: int, the sensibility, given as a negative exponent with base 10 E.g., if sens == 4, our sensibility
                     will be 10^(-4), 0.0001. It's by default 4 given the way it's used in the script
        :return: float, the n-th root of the base number, returned

        The purpose of this function is to return the value, just in case we were to need it
        """
        return self.rootSearch(root, base, sens, "return")