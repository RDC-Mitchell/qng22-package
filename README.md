# Quantum Radar Challenge Local Package

The follow document contains key information to access and use the underlying algorthims that powered the Quantum Next Generation 2022 Radar Challenge.

No longer will there be a technical requirement that requires the user to connect to the simulator online. Instead you be able to freely compile and run the code on any Python supported platform and run calculations at the maximum possible pace you can achieve.

Included in this package are two python files; the first (`qe_radar_toolkit.py`) is the algorthim (or engine) that actually produced the simulations the server was running. The second (`qe_radar_connector.py`) is another wrapper, this time instead of a wrapper for the `requests` package, it is a wrapper for `qe_radar_toolkit.py`, designed to keep the most of the same language, inputs, and outputs that you used during the challenge for minimum disruption. Users are encouraged to use whichever one they are more comfortable with, the documentation will remain comprehensive for both.

# Getting Started

Minimum Python Version Required: `3.7`

Recommended Python Version Required: `3.9+`

## Installation Process
This package can be imported into custom python script using the standard `import` feature. The documentation will outline the functions you need to call to invoke functions in the simulator, as well as providing explanations about their parameters, their returns, and their role in the challenge. 

To install and use this package, download/clone from GitHub and place the Python files within your project folder:
```bash
example-qng22-team-solution-folder
|   example-solution-code.py
|   qe_radar_toolkit.py
|   qe_radar_connector.py
```
 and input into your custom python script:
```python
import qe_radar_toolkit
```
or
```python
import qe_radar_connector
```
This will allow you to run the functions listed in `Documentation` that will help you engage with the simulation server.

## Software Dependencies
`qe_radar_toolkit.py` heavily relies on the `numpy` module, which will need to be installed so you can engage with the simulator.
You can install `numpy` *(if you do not already have it)* using `pip` or your choice of package manager.
```
python -m pip install numpy
```

# Valid Variables and Data Structures

As outlined in the problem brief, the variables used will have certain restrictions and expectations. Listed below is the structure of every variable, and can be used as reference in the later functions.

### Radar Configuration (Pulse, Measurement, Example)
* Pulse | List: Length 2
    * Start | Integer: 0-500000 us (microseconds)
    * End | Integer: 0-500000 us (microseconds)
* Measurement | List: Length 3
    * Start | Integer: 0-500000 us (microseconds)
    * End | Integer: 0-500000 us (microseconds)
    * Phase | Float: Radians
* Example Target | Integer: 0-999

#### **Example**: 
Configuration for a pulse that runs from `2 us` to `13 us`, with a measurement window from `5 us` to `6 us`, adjusted by `2.1 radians` against target `1`:

    [2, 13], [5, 6, 2.1], 1


### Results (Configuration, Estimates)
* Configurations | List: Length 1000
    * Pulses | List: Length > 0
        * Pulse | List: Length 2
            * Pulse Start | Integer: 0-500000 us (microseconds)
            * Pulse End | Integer: 0-500000 us (microseconds)
    * Measurements | List: Length > 0
        * Measurement | List: Length 3
            * Measure Start | Integer: 0-500000 us (microseconds)
            * Measure End | Integer: 0-500000 us (microseconds)
            * Phase | Float: 0 to 2*pi radians
    * Example Target | Integer: 0-999 
* Estimates | List: Length 1000
    * Estimate | List: Length 4
        * Rabi |  Float: $1/10^4$ to $13$ Mrads
        * Detuning | Float: $-24$ to $24$ krads
        * Time of Flight | Float: $6$ to $335$ us (microseconds)
        * Example Target | Integer: 0-999


#### **Example**:
Results for development dataset, showing only a few items for configurations and estimates:
```python
Configurations=[
    Example0=[
        Pulses=[[Start=Int, End=Int]],
        Measurements=[[Start=Int, End=Int, Phase=Float]],
        ExampleID=Int
    ],
    Example1=[
        Pulses=[[Start=Int, End=Int]],
        Measurements=[[Start=Int, End=Int, Phase=Float]],
        ExampleID=Int
    ],
    #...Configuration for Example 2 to Example 999
],
Estimates=[
    Estimate0=[Rabi=Float, Detuning=Float, T_Flight=Float, ExampleID=Int],
    Estimate1=[Rabi=Float, Detuning=Float, T_Flight=Float, ExampleID=Int],
    Estimate2=[Rabi=Float, Detuning=Float, T_Flight=Float, ExampleID=Int],
    #...Estimate for Examples 3 to 999
]
```
```python
[
    [
        [[1, 20],[21, 100],[140, 500],[1000, 2000],[2000, 10000]...],
        [[10, 36, 0],[45, 99, 0],[100, 300, 0],[400, 800, 0],[5000, 25000, 0]...],
        0
    ],
    [
        [[1, 20],[21, 100],[140, 500],[1000, 2000],[2000, 10000]...],
        [[10, 36, 0],[45, 99, 0],[100, 300, 0],[400, 800, 0],[5000, 25000, 0]...],
        1
    ],
    #...Configuration for Example 2 to Example 999
],
[
    [0.00453748376016974, -0.02249823109292496, 153.73902434863788, 0],
    [0.0002964523714059984, -0.015549490574576096, 643.6452780943542, 1],
    [0.000541916391029567, -0.017939610742308935, 549.3026779212704, 2],
    #...Estimate for Examples 3 to 999
]
```
# Documentation for Toolkit

You can find the detailed documentation for the quantum radar toolkit (`qe_radar_toolkit.py`) [here](README_TOOLKIT.md)

# Documentation for Connector

You can find the detailed documentation for the connector (`qe_radar_connector.py`) [here](README_CONNECTOR.md)

