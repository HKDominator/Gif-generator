import imageio.v3 as imageio

filenames = [r"images\nyan-cat1.png", r'images\nyan-cat2.png', r'images\nyan-cat3.png']
images = []
name = "Test3"

for filename in filenames:
    images.append(imageio.imread(filename)) #the imageio.imread method loads the images from their filepath
imageio.imwrite(f"{name}.gif", images, duration = 300, loop = 1 ) #the loop determines for how many times it loops
#loop = 0 infinity otherwise the specified amount



