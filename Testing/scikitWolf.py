from random import seed,shuffle

def train_test_split( *arrays , test_size : float = 0, train_size : float = 0, random_state : int = 0) -> list:
    """Splits the array into train and test data"""

    seed(random_state)

    if(test_size == 0 and train_size == 0):
        print("Train/Test Size not set")
        return
    elif(test_size + train_size < -1 or train_size + test_size > 1):
        print("Invalid Train/Test Size")
        return
    elif(test_size != 0 and train_size == 0):   # If test size set and train size isn't, calculates it automatically
        train_size = 1 - test_size
    elif(test_size == 0 and train_size != 0):   # If train size set and test size isn't, calculates it automatically
        test_size = 1 - train_size

    splitted = []

    for array in arrays:
        shuffle(array)
        tmp_train = []
        tmp_test = []
        n = len(array)
        for i in range(int(n*train_size)):
            if(len(array) == 0):
                break
            tmp_train.append(array.pop())
        for i in range(int(n*test_size)):
            if(len(array) == 0):
                break
            tmp_test.append(array.pop())

        splitted.append(tmp_train)
        splitted.append(tmp_test)

    return splitted