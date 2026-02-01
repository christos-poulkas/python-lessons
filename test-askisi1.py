def mesos_oros(x):
    mesos = sum(x)/len(x)
    return mesos

def mesos_oros_without_sum(x):
    mesos = 0
    for i in x:   #Voithitiki metavliti px x = [2.3,3.4,56.3] proti timi tou i 2.3, deuteri to 3.4, triti to 56.3
        mesos = mesos + i
    return mesos/len(x)
# list[start:end:step] start starts at zero!!!!!!
