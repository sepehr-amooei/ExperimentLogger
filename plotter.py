import matplotlib.pyplot as plt
import numpy as np

def plot_weight_changes(labels, durations, zero_list, w_start, w_end):
    fig, ax = plt.subplots()
    ax.scatter(zero_list, w_start, color='b')
    ax.scatter(durations, w_end, color='r')

    for i in range(len(labels)):
        ax.plot([durations[i], zero_list[i]], [w_end[i], w_start[i]], color='black')
        ax.text(zero_list[i], w_start[i], labels[i], color='b')
        ax.text(durations[i], w_end[i], labels[i], color='r')

    plt.title("Test Duration vs Weight Change")
    plt.xlabel("Test Duration (days)")
    plt.ylabel("Weight (lbs)")
    ax.legend(['Before test', 'After test', 'Duration'])
    plt.savefig('output/Test Duration vs Weight Change')
    plt.show()


def plot_weight_loss_bubble_chart(labels, ages, durations, w_start, w_end):

    raw_weight_loss = [abs(s - e) for s, e in zip(w_start, w_end)]
    weight_loss = [np.log(w + 1) * 1000 for w in raw_weight_loss]
    colors = np.random.rand(len(ages), 3)


    fig, ax = plt.subplots()
    ax.scatter(ages, durations, s=weight_loss, c = colors)
    ax.set_xlim(10,40)
    ax.set_ylim(100,220)
    for age, duration, label in zip(ages, durations, labels):
        ax.text(age, duration, label, fontsize=9, ha='center', va='center')
    


    plt.title("Test age vs duration bubble chart")
    plt.xlabel("Subject Age (years)")
    plt.ylabel("Test Duration  (days)")
    plt.savefig('output/Test age vs duration bubble chart')
    plt.show()
