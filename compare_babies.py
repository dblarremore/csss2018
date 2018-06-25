# put this in a jupyter notebook.
# thanks to  Javier Garcia-Bernardo <garcia@uva.nl>


from IPython.display import clear_output
from IPython.display import Image, display
import matplotlib.image as mpimg
%matplotlib inline

with open("babies_results.csv","w+") as f:
    while 1:
        a,b = np.random.randint(0,42,2)
        if a == b:
            continue
        plt.figure(figsize=(10,5))
        images = [mpimg.imread('babies/{}.jpg'.format(a)),
                  mpimg.imread('babies/{}.jpg'.format(b))]
        for i in range(2):
            plt.subplot(1,2,i+1)
            plt.imshow(images[i])
            plt.axis("off")
        plt.show()
        #display(Image(filename='babies/{}.jpg'.format(a),width=200),Image(filename='babies/{}.jpg'.format(b),width=200)  )
        try:
            av,bv = input("numbers").strip().split()
        except:
            break
            
        for i in range(int(av)):
            f.write("{} {}\n".format(a,b))
        for j in range(int(bv)):
            f.write("{} {}\n".format(b,a))

        clear_output()
