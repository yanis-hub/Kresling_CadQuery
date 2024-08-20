# Kresling_CadQuery
This repository discusses the use of the python library Cadquery to create Kresling units and Kresling arrays.

## CadQuery 
CadQuery is an open-source, easy-to-use Python library for building parametric 3D CAD models.

Here I present two examples to see the use of CadQuery as a powerful yet simple object oriented library. 

#### Example 1
```python
thickness = 0.5
width = 2.0
result = Workplane("front").box(width, width, thickness).faces(">Z").hole(thickness)
```


#### Example 2
```python
result = (
    cq.Workplane("front")
    .box(3.0, 4.0, 0.25)
    .pushPoints([(0, 0.75), (0, -0.75)])
    .polygon(6, 1.0)
    .cutThruAll()
)
```


For more details, see the official repository: [CadQuery on GitHub](https://github.com/CadQuery/cadquery/tree/master).

## Installing CadQuery & Cq-Editor GUI 

For installation instructions, please consult the [Install.md](Install.md) file.


## Kresling units 

The following code [Kresling_unit]() generates a kresling unit, the parameters are highlighted in the begining 

![Example of a Kresling unit](images/dessin.svg)


## Kresling arrays

The following code [Kresling_array]() generates a kresling unit, the parameters are highlighted in the begining 

![Example of a Kresling array](images/Kresling_array.svg)


## LHS Algorithm 

Latin hypercube is a statistical method for generating a near-random sample of parameter values from a multidimensional distribution. 

This file [LHS_algorithm](LHS.py) is a python code that creates the desired number of samples to facilitates the exploration of the design space.

## Contact 

Author's Email : yanis.abad@polymtl.ca 



