import random
CP = 0.6
MP = 0.05
POP = 6
# Could change the Data Struture to dict
LONG = 10
CLONG = 3 #cut point count from the end of string
def random_ones():#fine
    #return a binary number of ones
    """

    :rtype : object
    """
    list = []
    for i in range(POP):
        list.append(bin(random.randrange(0,2^LONG-1,1))[2:].zfill(LONG))
    return list

def fitness(ones): #fine
    #return the fitness to each ones
    value = 0
    for i in ones:
        if int(i)!= 0:
            value += 1
    return value

def choose_ones(lists):#can be modify
    temp_list = []
    chosen_list = []
    for i in range(len(lists)):
        temp_list += [lists[i]]*fitness(lists[i])
    #print(temp_list)
    for i in range(len(lists)):
        chosen_list.append(random.choice(temp_list))
    return chosen_list
def crossover(list):
    cut_point_one = random.randint(0,LONG-2)
    cut_point_two = random.randint(cut_point_one,LONG-1)

"""def crossover(lists):  #chongxie
    #this will generate a crossovered result of given list
    #n is the rate of crossover
    temp_list = ''
    n = random.uniform(0,1)
    if n <= CP:
        for i in range(0,len(lists)-1,2):
            temp_list = lists[i]
            lists[i] = lists[i][0:LONG-CLONG]+lists[i+1][LONG-CLONG:LONG]
            lists[i+1] = lists[i+1][0:LONG-CLONG] + temp_list[LONG-CLONG:LONG]

        return lists
    if n > 1-CP:

        for i in range(0,len(lists)-3,2):
            temp_list = lists[i]
            lists[i] = lists[i][0:LONG-CLONG]+lists[i+1][LONG-CLONG:LONG]
            lists[i+1] = lists[i+1][0:LONG-CLONG] + temp_list[LONG-CLONG:LONG]
        return lists
        """

def mutate(lists): # change the mutate rate counting method
    mutate_rate = MP
    random_predict = random.uniform(0, 1)
    if random_predict <= mutate_rate:
        for i in range(len(lists)-2):
            raise_pos = random.randint(0, LONG-1)
            if lists[i][raise_pos] == '1':
                lists[i] = lists[i][0:raise_pos]+'0'+lists[i][raise_pos+1:LONG]
            else:
                lists[i] = lists[i][0:raise_pos]+'1'+lists[i][raise_pos+1:LONG]

            if lists[i][raise_pos] == '0':
                lists[i] = lists[i][0:raise_pos]+'0'+lists[i][raise_pos+1:LONG]
            else:
                lists[i] = lists[i][0:raise_pos]+'1'+lists[i][raise_pos+1:LONG]
    return lists

def best_fit(list):
    fitList = []
    for item in list:
        fitList.append(fitness(item))
    return max(fitList)

def max_one():
    lists=random_ones()
    temp = 0
    it = 0
    addup = 0
    while temp == 0:
        it = it + 1
        lists=choose_ones(lists)
        lists=crossover(lists)
        lists = mutate(lists)
        #if best_fit(lists) > 150:
         #   break
        #print(best_fit(lists))
        for i in range(len(lists)):
          if fitness(lists[i]) >= LONG:
              #print(lists,'\n',it)
                print('\n',it)
                temp = 1
                break


    return lists

print(max_one())




