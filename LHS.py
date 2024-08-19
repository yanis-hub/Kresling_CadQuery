import numpy as np
from scipy.stats import qmc

def latin_hypercube_sampling(n_samples, parameter_ranges):
    parameter_names = list(parameter_ranges.keys())
    n_parameters = len(parameter_ranges)
    ranges = list(parameter_ranges.values())
    
    sampler = qmc.LatinHypercube(d=n_parameters)
    sample = sampler.random(n=n_samples)
    
    # Scale the sample to the parameter ranges and round
    for i in range(n_parameters):
        min_val, max_val = ranges[i]
        if parameter_names[i] == 'num_sides':
            sample[:, i] = np.round(sample[:, i] * (max_val - min_val) + min_val).astype(int)
        else:
            sample[:, i] = np.round(sample[:, i] * (max_val - min_val) + min_val, 1)
    
    # Convert samples to a list of dictionaries
    samples = []
    for i in range(n_samples):
        sample_dict = {parameter_names[j]: sample[i, j] for j in range(n_parameters)}
        diameter = sample_dict['diameter']
        
        # Ensure that hole_diameter is smaller than diameter
        hole_diameter = np.round(diameter * np.random.uniform(0.3, 0.9), 1)
        sample_dict['hole_diameter'] = hole_diameter
        
        # Ensure that scale_factor_top is smaller than scale_factor_base
        scale_factor_base = sample_dict['scale_factor_base']
        scale_factor_top = np.round(scale_factor_base * np.random.uniform(0.5, 0.9), 1)
        sample_dict['scale_factor_top'] = scale_factor_top
        
        samples.append(sample_dict)
    
    return samples

# Parameter ranges are conservative, you can modify if you find better values 
n_samples = 3   # number of samples 
parameter_ranges = {
    'num_sides': (3, 10),
    'diameter': (35, 100),
    'height': (35, 100),
    'theta': (1, 60),
    'base_extrusion': (1, 10),
    'scale_factor_base': (0.3, 0.9),
    'triangle_thickness': (0.2, 1.0),
    'small_triangle_thickness': (0.2, 1.0)
}

samples = latin_hypercube_sampling(n_samples, parameter_ranges)
for i, sample in enumerate(samples):
    print(f"Sample {i+1}: {sample}")
