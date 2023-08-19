import matplotlib.pyplot as plt 

def generate_pie_chart():
    labels = ['A','B','C']
    Values = [200,34,300]

    fig, ax =plt.subplots()
    ax.pie(Values, labels=labels)
    plt.savefig("img.png")
    plt.close()