#synarthsh->input x lista -> return mean_avg pos num
#synarthsh->input by user 3 pos_num that calc+print mean_Avg

def pos_mean_avg(x):
    y=[]
    for i in x:
        if i>0:
            y.append(i)
    try:
        return sum(y)/len(y)
    except Exception as e:
        print(e)
        return 0



def input_mean_avg():
    x = []
    for i in range(3):
        y = float(input("give pos num"))
        if y>0:
            x.append(y)
        else:
            print("give pos num (given neg)")
            return 0
    mean_avg_pos = sum(x)/len(x)
    print (mean_avg_pos)
    return mean_avg_pos