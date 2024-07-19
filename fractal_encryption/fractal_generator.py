import random
import hashlib

def generate_mandelbrot(width, height, max_iter, seed, iv):
    combined = f"{seed}{iv}".encode('utf-8')
    hashed_seed = int(hashlib.sha256(combined).hexdigest(), 16)
    random.seed(hashed_seed)
    
    x_min, x_max = -2.0, 1.0
    y_min, y_max = -1.5, 1.5
    pixels = [[0 for _ in range(width)] for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            a = x_min + (x / width) * (x_max - x_min)
            b = y_min + (y / height) * (y_max - y_min)
            c = complex(a + random.uniform(-0.001, 0.001), b + random.uniform(-0.001, 0.001))
            z = 0
            for i in range(max_iter):
                if abs(z) > 2.0:
                    break
                z = z*z + c
            pixels[y][x] = i
    return pixels

def generate_julia(width, height, max_iter, seed, iv, c_real, c_imag):
    combined = f"{seed}{iv}".encode('utf-8')
    hashed_seed = int(hashlib.sha256(combined).hexdigest(), 16)
    random.seed(hashed_seed)
    
    x_min, x_max = -2.0, 2.0
    y_min, y_max = -2.0, 2.0
    c = complex(c_real, c_imag)
    pixels = [[0 for _ in range(width)] for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            z = complex(x_min + (x / width) * (x_max - x_min), y_min + (y / height) * (y_max - y_min))
            for i in range(max_iter):
                if abs(z) > 2.0:
                    break
                z = z*z + c
            pixels[y][x] = i
    return pixels

def generate_burningship(width, height, max_iter, seed, iv):
    combined = f"{seed}{iv}".encode('utf-8')
    hashed_seed = int(hashlib.sha256(combined).hexdigest(), 16)
    random.seed(hashed_seed)
    
    x_min, x_max = -2.0, 1.0
    y_min, y_max = -1.5, 1.5
    pixels = [[0 for _ in range(width)] for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            a = x_min + (x / width) * (x_max - x_min)
            b = y_min + (y / height) * (y_max - y_min)
            c = complex(a + random.uniform(-0.001, 0.001), b + random.uniform(-0.001, 0.001))
            z = 0
            for i in range(max_iter):
                if abs(z) > 2.0:
                    break
                z = complex(abs(z.real), abs(z.imag))**2 + c
            pixels[y][x] = i
    return pixels
