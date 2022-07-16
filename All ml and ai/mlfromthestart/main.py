from matplotlib.animation import FuncAnimation
import pandas as pd
import matplotlib.pyplot as plt
import threading

df = pd.read_csv('data.csv')
# print(df.head())

m = 1
b = 1
L = 0.0001
epochs = 1000
def loss_function(m, b, points):
    total_error = 0
    for i in range(len(points)):
        
        x = points.iloc[i, 0]
        y = points.iloc[i, 1]
        total_error += (y - (m * x + b)) ** 2
       
    return total_error / float(len(points))

def gradient_descent(m, b, points, learning_rate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(len(points)):
        x = points.iloc[i, 0]
        y = points.iloc[i, 1]
        b_gradient += -(2/N) * (y - ((m * x) + b))
        m_gradient += -(2/N) * x * (y - ((m * x) + b))
    new_b = b - (learning_rate * b_gradient)
    new_m = m - (learning_rate * m_gradient)
    return [new_b, new_m]


current_loss = 0
xlist = []
ylist = []
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
fig.canvas.draw()
fig.set_facecolor('#121212')
ax1.set_title('Linear Regression', color='white')
ax2.set_title(f'Loss Function current_loss:N/A', color='white')
ax1.grid(True, color='#323232')
ax2.grid(True, color='#323232')
ax1.set_facecolor('black')
ax2.set_facecolor('black')
ax1.tick_params(axis='x', colors='white')
ax1.tick_params(axis='y', colors='white')
ax2.tick_params(axis='x', colors='white')
ax2.tick_params(axis='y', colors='white')

ax2.set_xlim([0,epochs])

points = df
ax1.scatter(points.iloc[:,0], points.iloc[:,1])


def predict(m, b, x):
    return m * x + b


losses = []
m = 1
b = 1
L = 0.0001
epochs = 1000
predicted = [predict(m, b, x) for x in df['x']]
line,line2 = None,None
def plot(i):
    global line,line2,current_loss
    if line!=None:
        ax1.lines.pop(0)
    line = ax1.plot(points.iloc[:,0], predicted, color='red')
    if line2!=None:
        if len(ax2.lines)==1:
            # print(ax2.lines)
            l  = ax2.lines.remove(ax2.lines[0])
    # print(ax2.lines)
    if losses!=[]:
        current_loss = losses[-1]
    ax2.set_title(f'Loss Function Current loss:{current_loss}', color='white')
    line2 = ax2.plot(range(len(losses)),losses,color='red')
import time
a = FuncAnimation(plt.gcf(), plot,interval=1)
plt.tight_layout()

def start_():
    global predicted,line2,ls
    m = 1
    b = 1
    L = 0.0001
    epochs = 1000
    for i in range(epochs):
        time.sleep(0.01)
        m, b = gradient_descent(m, b, df, L)
        predicted = [predict(m, b, x) for x in df['x']]
        losses.append(loss_function(m, b, df))
        
threading.Thread(target=start_).start()
plt.show()










