import matplotlib.pyplot as plt

def visualize(x, y): #data visualization
    fig, ax = plt.subplots(figsize = (12, 7))
    ax.scatter(x, y)
    ax.grid()
    ax.set_xlabel('Net Score')
    ax.set_ylabel('Number of Retweets')
    ax.set_title('Result')
    plt.show()    
    fig.savefig('Visualize data.jpg')


x, y, i = [], [], None
with open('resulting_data.csv', 'r') as resl:
    for line in resl:
        if i == None: # skipping the first line in csv file
            i = 'pass'
            continue
        line = line.split(',')
        x.append(int(line[-1]))
        y.append(int(line[0]))
    visualize(x, y)
