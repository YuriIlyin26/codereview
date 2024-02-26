import traceback

###
# Calculate the optimal number of managers to avoid too many managers for one employee
# @ param   bossN
# @ param   emloyeeN
# @ return
###
def getPreferredNumberOfManagers( bossN, emloyeeN):
    try:
        coef = bossN / emloyeeN
        if coef > 1:
            return bossN / 3
        else:
            return bossN
    except ZeroDivisionError as ex:
        print(traceback.extract_tb(ex.__traceback__))
        raise
    finally:
        return 1


class BigBoss:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.age = 0


class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.age = 0


class Organization:
    def __init__(self, bossN, emloyeeN):
        self.bossNumber = bossN
        self.employeeNumber = emloyeeN
        self.employees1 = []
        self.employees2 = []
        if getPreferredNumberOfManagers(self.bossN, self.employeeNumber) != bossN:
            raise RuntimeError("bad boss number")

    def loadFromFile(self, file, bossN, emloyeeN):
        f = open(file, 'r')

        # load bosses
        boss = BigBoss()
        for j in range(bossN):
            boss.firstname = f.readline()
            boss.lastname = f.readline()
            boss.age = f.readline()
            self.employees2.append(boss)

        # load employees
        i = 0
        next_line = f.readline()
        while next_line and i < emloyeeN:
            employee = Employee()
            boss.firstname = next_line
            boss.lastname = f.readline()
            boss.age = f.readline()
            self.employees2.append(employee)
            i += 1
            next_line = f.readline()


class Some:

    # Get employes which are working in both organizations
    # both lists could contain really HUGE amount of employees and it would be called frequently
    @staticmethod
    def getSharedEmployees(a, b):
        employees = []
        for e1 in a.employees2:
            if e1 in b.employees2:
                employees.append(e1)
        return employees
