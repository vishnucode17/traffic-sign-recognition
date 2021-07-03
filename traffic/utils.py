import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('UTF-8')
    buffer.close()
    return graph

def get_plot(x,y):
    plt.switch_backend('AGGR')
    plt.figure(figsize=(13, 4), dpi=80)
    plt.bar(x,y,width=0.5)
    plt.title("Accuracy Percentage")
    plt.xlabel("Label")
    plt.xticks(x)
    plt.ylabel("Accuracy")
    graph =get_graph()
    return graph