from PIL import Image
import numpy as np
import random 

class Spheres:
    def __init__(self):
        self.NUM = 3
        self.TOTAL = self.NUM + 1
        self.center     = np.zeros((self.TOTAL, 3 ))
        self.radius     = np.zeros((self.TOTAL))   
        self.color      = np.zeros((self.TOTAL, 3 ))
        self.ambient    = np.zeros((self.TOTAL))   
        self.diffuse    = np.zeros((self.TOTAL))   
        self.specular   = np.zeros((self.TOTAL))   
        self.reflection = np.zeros((self.TOTAL))   

        for i in range(self.NUM):
            self.center[i][0]  = -1.0 + i    #   x
            self.center[i][1]  = 0.0         #   y
            self.center[i][2]  = 1.0         #   z
            self.radius[i]     = 0.1 * (i + 1)
            self.color[i][0]   = random.randint(0, 255)   #   r
            self.color[i][1]   = random.randint(0, 255)   #   g
            self.color[i][2]   = random.randint(0, 255)   #   b
            self.ambient[i]    = 0.05
            self.diffuse[i]    = 0.1 + 0.3 * (i+1)
            self.specular[i]   = 0.1 + 0.3 * (i+1)
            self.reflection[i] = 0.5

        #   ground
            self.center[self.NUM][0]  = 0.0         #   x
            self.center[self.NUM][1]  = 1000.5      #   y
            self.center[self.NUM][2]  = 0.0         #   z
            self.radius[self.NUM]     = 1000.0
            self.color[self.NUM][0]   = random.randint(0, 255)   #   r
            self.color[self.NUM][1]   = random.randint(0, 255)   #   g
            self.color[self.NUM][2]   = random.randint(0, 255)   #   b
            self.ambient[self.NUM]    = 0.3
            self.diffuse[self.NUM]    = 1.0
            self.specular[self.NUM]   = 0.0
            self.reflection[self.NUM] = 0.1

class Lights:
    def __init__(self):
        self.NUM = 3
        self.pos   = np.zeros((self.NUM, 3 ))
        self.color = np.zeros((self.NUM, 3 ))

        for i in range(self.NUM):
            self.pos[i][0]   = -5 + 2 * i   #   x
            self.pos[i][1]   = -5 + 3 * i   #   y
            self.pos[i][2]   = -1.0         #   z
            self.color[i][0] = random.randint(0, 255)   #   r
            self.color[i][1] = random.randint(0, 255)   #   g
            self.color[i][2] = random.randint(0, 255)   #   b

def main():
    WIDTH, HEIGHT = 5, 3
    # WIDTH, HEIGHT = 200, 200
    # WIDTH, HEIGHT = 500, 500
    # WIDTH, HEIGHT = 1920, 1080
    # WIDTH, HEIGHT = 4096, 2160
    # WIDTH, HEIGHT = 7680, 4320
    
    cam = np.array([0.0, 0.0, -4.0])
    spheres = Spheres()
    lights = Lights()

    img = np.zeros((HEIGHT, WIDTH, 3))

    x = np.arange(WIDTH)
    y = np.arange(HEIGHT)

    #   create viewplane rays
    x0 = -1.0
    x1 = 1.0

    aspect_ratio = WIDTH / HEIGHT
    y0 = -1.0 / aspect_ratio
    y1 = 1.0 / aspect_ratio

    viewplane_points_x = np.linspace(x0, x1, WIDTH)
    viewplane_points_y = np.linspace(y0, y1, HEIGHT)

    xs = np.tile(viewplane_points_x, (HEIGHT, 1)).flatten()
    ys = np.tile(viewplane_points_y, (WIDTH, 1)).T.flatten()
    zs = np.zeros((HEIGHT, WIDTH)).flatten()

    plane_targets = np.stack((xs, ys, zs)).T.reshape((HEIGHT *  WIDTH, 3))
    
    #   cast rays
    # origin = np.tile(cam, (HEIGHT, WIDTH, 1))
    ray_dir = plane_targets - cam

    color = np.zeros((HEIGHT, WIDTH, 3))

    #   check all intersections
    sphere_idx = np.arange(spheres.TOTAL)
    sphere_to_ray = cam - spheres.center
    
    b = 2 * ray_dir.dot(sphere_to_ray.T)

    str_dot_str =   sphere_to_ray.T[:][0] ** 2.0 + \
                    sphere_to_ray.T[:][1] ** 2.0 + \
                    sphere_to_ray.T[:][2] ** 2.0
    str_dot_str = str_dot_str.T
    print(str_dot_str)
    print(spheres.radius)
    print(spheres.radius ** 2.0)
    c = str_dot_str - spheres.radius ** 2.0
    print(c)
    quit()



    def intersects(self, ray):
        sphere_to_ray = ray.origin - self.center

        #a = 1
        b = 2 * ray.dir.dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - self.radius ** 2.0
        disc = b * b - 4 * c

        if disc >= 0.0:
            dist =  (-b - math.sqrt(disc)) / 2.0
            if dist > 0:
                return dist
        else:
            return None

    #   keep closest by index


    # print(plane_targets)
    # print(direction)
    quit()



    num_bounces = 1
    for bounce in tqdm(range(num_bounces)):
        img.pixels[row][col] = self.raytrace(ray, scene, max_bounces)

        return img


    quit()

    img = engine.render(scene, max_bounces=10)




    # img.write_as_ppm("raytrace_demo")

    file_image = Image.new('RGB', (WIDTH, HEIGHT), color = 'black')
    pixels = file_image.load()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            pixels[x, y] = (
                int(min(img.pixels[y][x].x, 255)), 
                int(min(img.pixels[y][x].y, 255)), 
                int(min(img.pixels[y][x].z, 255)))

    file_image.show()
    file_image.save("render.png")


if __name__ == "__main__":
    main()