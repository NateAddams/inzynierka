import imageio

with imageio.get_writer('zdjecia/gifNate.gif', mode='I') as writer:
    for filename in ['zdjecia/test4.png', 'zdjecia/test5.png', 'zdjecia/test6.png', 'zdjecia/test6.png']:
        image = imageio.imread(filename)
        writer.append_data(image)





