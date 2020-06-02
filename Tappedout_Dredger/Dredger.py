import re
import psycopg2 as psy
import sys

def dredger(file):
    """
    :param file: The file we are going to use as a reference for sets
    :return: None, it's a void function

    The whole functionality of this function is to insert a list of cards using a certain website's format to a PostGreSQL
    database. More concrete info in the attached document.
    """
    def to_list(fi):
        """
        :param fi: the file we are to prepare to be used as query
        :return: zero, list containing all the values for the query
        What this function does is to translate from the website format to one more query-like, as to facilitate
        the creation of the query itself
        """
        zero = []
        for e in fi:
            e = e.replace("\n", "")
            quant = list(e)[0]
            set = re.findall(r"\(.*\)", e)[0].replace("(", "").replace(")", "")
            status = re.findall("0st.*st0", e)[0].replace("0st", "").replace("st0", "")
            name = e.replace("(" + set + ")", "").replace(quant + "x ", "").replace(" 0st" + status + "st0", "").replace("\'", " ")
            zero.append([quant, name, set, status])
        return zero

    def createdic(fil):
        """
        :param fil: the file we are going to use to create our sets dictionary
        :return: dic0, dictionary containing all the values for our sets

        This functions creates a dictionary which relates the set names to the set abbreviation,
        which is the one actually reflected in the reference file
        """
        dic0 = {}
        for e in list(open(fil)):
            splits = e.split(".")
            dic0[splits[0]] = splits[1].replace("\n", "")
        return dic0

    conn = psy.connect("dbname=postgres user=postgres password=P0RnO53i")
    cur = conn.cursor()

    par = to_list(list(open(file)))
    setdic = createdic("sets_dictionary.txt")



    #Query creation & execution
    for e in par:
        insert_query = "INSERT INTO cartas (quantity, name, set, status) VALUES " \
                       "(" + e[0] + ",\'" + e[1] + "\',\'" + setdic[e[2]] + "\',\'" + e[3] + "\');"

        cur.execute(insert_query)
        conn.commit()

#To run it through command or not
if len(sys.argv) > 0:
    dredger(sys.argv[1])
else:
    target = input("Insert file to dredge into database: ")
    dredger(target)
