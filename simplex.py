
import numpy                as np


class Configuration:

    def __init__(self):

        # Problem setting (in canonical form)
        # self.constraint = [
        #     # [coefficient_1, coefficient_2, ... , constant_value]
        #     [ 4,     1,     22],
        #     [ 2,    -1,      8],
        #     [ 1,     2,     10]
        # ]
        # self.object = [-1, -2, 12]   # [coefficient_1, coefficient_2, ... , constant_value]

        self.constraint = [
            # [coefficient_1, coefficient_2, ... , constant_value]
            [ 5,    -2,     11],
            [ 4,     2,     28],
            [-3,     3,      6]
        ]
        self.object = [-4, -5, 4]   # [coefficient_1, coefficient_2, ... , constant_value]



class Simplex:

    def __init__(self, cnf):
        
        self.cnf    = cnf

        # Make dictionary (= Basis form expression)
        stack       = np.vstack((self.cnf.constraint, self.cnf.object))
        slack       = np.eye(stack.shape[0])
        self.prob   = np.insert(stack, [-1], slack, axis=1)

        print("Initial Dictionary:")
        print(self.prob)


    def run(self):
        count = 0
        while any(self.prob[-1] < 0):   # while having space to be optimized
            # Title
            count += 1
            print("\n<Operation " + str(count) + ">")

            # Decide colmun ID with Dantzig's selection method
            col_id = self.prob[-1].argmin()

            # Decide row ID
            cand = self.prob[:,-1]/self.prob[:,col_id]
            cand[cand<0] = np.inf
            row_id = cand.argmin()

            # Calculate a variable to be assigned
            pivot_row = self.prob[row_id] / self.prob[row_id,col_id]

            # Assign
            for i in range(self.prob.shape[0]):
                if i == row_id:
                    self.prob[i] = pivot_row
                else:
                    self.prob[i] = self.prob[i] - (pivot_row * self.prob[i,col_id])
            
            # Show temporary result
            print(" Dictionary:")
            print(self.prob)

            # Avoid infinity loop
            if count > 100:
                print("\n Failed")
                break
        
        # Show final result
        if not count > 100:
            print("\n <Final result> \n Objective value = " + str(self.prob[-1,-1]) + "\n")


 

# run
if __name__ == '__main__':
    
    cnf = Configuration()

    print("\n\t\t[ Simplex Method ]\n")
    slx = Simplex(cnf)
    slx.run()
