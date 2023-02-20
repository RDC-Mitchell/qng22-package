## Development vs Testing
In `qe_radar_connector.py` there are two class objects that determine which simulator/dataset you will be targeting with any function - `DevSimulator` and `TestSimulator`

In `DevSimulator`, the example targets are known to you, and can be gathered using the `.dataset( int )` function. This is to develop a technique that gets as close as possible to that target.

In `TestSimulator`, the example targets are unknown,  and you will test your technique and solution to produce an estimate of the targets. Your estimates will be used to create your score and your configurations will be assessed for their validity. 

## Development Phase

Before using any function in the `DevSimulator` class, you must first initialise an object of it. All simulator functions are then called from this created object. 
#### **Example**
```python
simulator = qe_radar_connector.DevSimulator()
```

### `simulate(pulse, measure, example)`

Send a radar configuration of pulse and measurement to the simulator and receive a normalised signal.

#### **Example**:
Running the development simulator against target `81` with a pulse that runs from `0 us` to `10 us` and measures from `3 us` to `7 us` adjusted by phase 0.
```python
import qe_radar_connector

dev_radar = qe_radar_connector.DevSimulator()

pulse = [0,10]
measure = [3,7,0]

print(dev_radar.simulate(pulse, measure, 81))

>>> 0.455132
```

### `mass_simulate(configurations)`

Send a series of radar configurations for any number of example targets to be calculated concurrently, built to resolve issues found with high volume `simulate()` functions

#### **Example**:
Running the development simulator against targets `0`, `1` and `2` with a series of pulses and measurement windows. 
**Note**: If your pulse array and measurement array are not the same length, the target will be skipped and returned as an empty array.

*This uses the same structure as the configuration variable used for scoring.*


```python
import qe_radar_connector

dev_radar = qe_radar_connector.DevSimulator()

configurations = [[[[0,10],[10,15],[18,45]], [[2,8,1.1],[14,15,0.32],[30,40,0.82]], 0],
            [[[0,10],[10,15],[18,45]], [[2,8,1.1],[14,15,0.32],[30,40,0.82]], 1],
            [[[0,10],[10,15],[18,45]], [[2,8,1.1],[14,15,0.32],[30,40,0.82]], 2]
    ]

print (dev_radar.mass_simulate(configurations))

>>> [[[0.4862452504328871, 0.44162776172386153, 0.4698766184129937], 0],
        [[0.6225279509448354, 0.5342460580864783, 0.5543953308621907], 1],
        [[0.6180526680838897, 0.46747499721776037, 0.7819312044113694],2]]
```


### `dataset(example)`

Get the Rabi (Mrads), Detuning (Mrads), and Time of Flight (us) for the chosen example target.

#### **Example**:
Finding the details of the development target `1`
```python
import qe_radar_connector

dev_radar = qe_radar_connector.DevSimulator()

print(dev_radar.dataset(1))

>>> [0.0002964523714059984, -0.015549490574576096, 643.6452780943542]
```

### `mass_dataset()`

Get the Rabi (Mrads), Detuning (Mrads), and Time of Flight (us) for all `1000` example targets.

#### **Example**:
Finding the details of all the development targets
```python
import qe_radar_connector

dev_radar = qe_radar_connector.DevSimulator()

print(dev_radar.mass_dataset())

>>> [[0.028673456087970624, 0.020654261919863595, 114.56192252357387], [0.004362934265967196, 0.002677350985962326, 294.4095906800092], [8.695558202400441, -0.014455475799572943, 6.826695544782684], [0.0035707199667561473, 0.005648601112502126, 275.9207207606593], [0.00571397602555852, 0.018227046293772402, 300.03252768384533], [0.010949375111358607, 0.019777267521890768, 175.52652141984706], [0.104468109897097, -0.020920991278669906, 69.4709382036059]...
```

### `validate_config(configuration)`

To provide Team's guidance on how they need to format their submission and if their method produces a valid configuration list structure before submission in the Testing stage.

It does not confirm if the configuration list has all thousand (needed) entries or if estimates are formatted correctly.

#### **Example**:
```python
import qe_radar_connector

dev_radar = qe_radar_connector.DevSimulator()

configs = [[[[0,10],[10,15],[18,45]...], [[2,8,0],[14,15,0],[30,40,0]...], 0],
            [[[0,10],[10,15],[18,45]...], [[2,8,0],[14,15,0],[30,40,0]...], 2],
            [[[0,10],[10,15],[18,45]...], [[2,8,0],[14,15,0],[30,40,0]...], 1]...]

print(dev_radar.validate_config(configs))

>>> 'Submitted configurations are unordered'
>>> False
```

### `validate_estimate(estimates)`

To provide Team's guidance on how they need to format their submission and if their method produces a valid estimate list structure before submission in the Testing stage.

It does not confirm if the estimate list has all thousand (needed) entries or if configurations are formatted correctly.

#### **Example**:
```python
import qe_radar_connector

dev_radar = qe_radar_connector.DevSimulator()

estimates = [[0.00453748376016974, -0.02249823109292496, 153.73902434863788, 0],
        [0.0002964523714059984, -0.015549490574576096, 643.6452780943542, 2],
        [0.000541916391029567, -0.017939610742308935, 549.3026779212704, 1]...]


print(dev_radar.validate_estimate(estimates))

>>> 'Submitted estimates are unordered'
>>> False
```

## Testing Phase

Before using any function in the Test Simulator class, you must first initialise an object of it. All functions are then called from this created object.

#### **Example**
```python
simulator = qe_radar_connector.TestSimulator()
```

### `simulate(pulse, measure, example)`

Send a radar configuration of pulse and measurement to the simulator and receive a normalised signal.

#### **Example**:
Running the test simulator against target `34` with a pulse that runs from `12 us` to `18 us` and measures from `13 us` to `19 us` adjusted by phase 0.
```python
import qe_radar_connector

test_radar = qe_radar_connector.TestSimulator()

pulse = [12,18]
measure = [13,19,0]

print(test_radar.simulate(pulse, measure, 34))

>>> 0.455132
```

### `mass_simulate(configurations)`

Send a series of radar configurations for any number of example targets to be calculated concurrently, built to resolve issues found with high volume `simulate()` functions

#### **Example**:
Running the test simulator against targets `0`, `1` and `2` with a series of pulses and measurement windows. 
**Note**: If your pulse array and measurement array are not the same length, the target will be skipped and returned as an empty array.

*This uses the same structure as the configuration variable used for scoring.*


```python
import qe_radar_connector

test_radar = qe_radar_connector.TestSimulator()

configurations = [[[[0,10],[10,15],[18,45]], [[2,8,1.1],[14,15,0.32],[30,40,0.82]], 0],
            [[[0,10],[10,15],[18,45]], [[2,8,1.1],[14,15,0.32],[30,40,0.82]], 1],
            [[[0,10],[10,15],[18,45]], [[2,8,1.1],[14,15,0.32],[30,40,0.82]], 2]
    ]

print (test_radar.mass_simulate(configurations))

>>> [[[0.4862452504328871, 0.44162776172386153, 0.4698766184129937], 0],
        [[0.6225279509448354, 0.5342460580864783, 0.5543953308621907], 1],
        [[0.6180526680838897, 0.46747499721776037, 0.7819312044113694],2]]
```

### `score(configurations, estimates)`

Submit results with estimates for all targets in the testing dataset and the configurations used to produce the estimates; with intention for them to be scored. The returned results will be one of two options:
- A single integer that represents the number of errors in the configurations

or
- Number of errors in the estimates (hopefully 0), Score (mean squared score with the success approaching 0), precision (standard deviations for Rabi, Detuning and Time of Flight), accuracy (means for Rabi, Detuning and Time of Flight), the scores for all 1000 targets, actual precision (actual standard deviations for Rabi, Detuning and Time of Flight), and actual accuracy (actual mean for Rabi, Detuning, and Time of Flight).

#### **Example**:
```python
import qe_radar_connector

configs = [[[[0,10],[10,15],[18,45]...], [[2,8,0],[14,15,0],[30,40,0]...], 0],
            [[[0,10],[10,15],[18,45]...], [[2,8,0],[14,15,0],[30,40,0]...], 1],
            [[[0,10],[10,15],[18,45]...], [[2,8,0],[14,15,0],[30,40,0]...], 2]...]

estimates = [[0.00453748376016974, -0.02249823109292496, 153.73902434863788, 0],
        [0.0002964523714059984, -0.015549490574576096, 643.6452780943542, 1],
        [0.000541916391029567, -0.017939610742308935, 549.3026779212704, 2]...]

test_radar = qe_radar_connector.TestSimulator()

print(test_radar.score(configs, estimates))

>>> [0, 45, [1.2, 4.2, 0.2], [0.5, 2.1, 1.1], [10, 43, 9, 23, 11...], [1.2, 4.2, 0.2], [0.5, 2.1, 1.1]] # [ Error Count, Score, [Precision (STD) (Rabi, Detuning, Time of Flight)], [Accuracy (Mean) (Rabi, Detuning, Time of Flight)], [List of 1000 Scores], [Actual Precision (STD) (Rabi, Detuning, Time of Flight)], [Actual Accuracy (Mean) (Rabi, Detuning, Time of Flight)]  ]