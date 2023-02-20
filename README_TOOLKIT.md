## Development vs Testing
In `qe_radar_toolkit.py` there are multiple methods designed that cover the various functions and requirements for the challenge simulator. They follow a very simple naming format: `x_y`

`x` = `dev` or `test` for the relevant dataset you are targeting, `dev` for the Development dataset and `test` for the Testing dataset.

`y` = The function/method you would like to perform on the dataset, each one has their own numerous options and are listed in the documentation below.

## Development Phase

### `dev_sim(pulse, measure, example)`

Send a radar configuration of pulse and measurement to the simulator and receive a normalised signal.

#### **Example**:
Running the development simulator against target `81` with a pulse that runs from `0 us` to `10 us` and measures from `3 us` to `7 us` adjusted by phase 0.
```python
import qe_radar_toolkit

pulse = [0,10]
measure = [3,7,0]

print(qe_radar_toolkit.dev_sim(pulse, measure, 81))

>>> 0.455132
```

### `dev_data(example)`

Get the Rabi (Mrads), Detuning (Mrads), and Time of Flight (us) for the chosen example target.

#### **Example**:
Finding the details of the development target `1`
```python
import qe_radar_toolkit

print(qe_radar_toolkit.dataset(1))

>>> [0.0002964523714059984, -0.015549490574576096, 643.6452780943542]
```

### `dev_config(configuration)`

To provide Team's guidance on how they need to format their submission and if their method produces a valid configuration list structure before submission in the Testing stage. The returned results will be an integer representing the number of errors found in the configuration. 0 means the configuration have no found issues.

It does not confirm if the configuration list has all thousand (needed) entries or if estimates are formatted correctly.

#### **Example**:
```python
import qe_radar_toolkit

configs = [[[[0,10],[10,15],[18,45]...], [[2,8,0],[14,15,0],[30,40,0]...], 0],
            [[[0,10],[10,15],[18,45]...], [[2,8,0],[14,15,0],[30,40,0]...], 2],
            [[[0,10],[10,15],[18,45]...], [[2,8,0],[14,15,0],[30,40,0]...], 1]...]

print(qe_radar_toolkit.dev_config(configs))

>>> 0
```

### `dev_estimates(estimates)`

To provide Team's guidance on how they need to format their submission and if their method produces a valid estimate list structure before submission in the Testing stage. The returned results will be an integer representing the number of errors found in the configuration. 0 means the estimates have no found issues.

It does not confirm if the estimate list has all thousand (needed) entries or if configurations are formatted correctly.

#### **Example**:
```python
import qe_radar_toolkit

estimates = [[0.00453748376016974, -0.02249823109292496, 153.73902434863788, 0],
        [0.0002964523714059984, -0.015549490574576096, 643.6452780943542, 2],
        [0.000541916391029567, -0.017939610742308935, 549.3026779212704, 1]...]


print(qe_radar_toolkit.dev_estimate(estimates))

>>> 0
```

## Testing Phase

### `test_sim(pulse, measure, example)`

Send a radar configuration of pulse and measurement to the simulator and receive a normalised signal.

#### **Example**:
Running the test simulator against target `34` with a pulse that runs from `12 us` to `18 us` and measures from `13 us` to `19 us` adjusted by phase 0.
```python
import qe_radar_toolkit

pulse = [12,18]
measure = [13,19,0]

print(qe_radar_toolkit.test_sim(pulse, measure, 34))

>>> 0.455132
```

### `test_config(configurations)`

Submit configurations used to produce the estimates; with intention for them to be scored in `test_score`. The returned results will be an integer representing the number of errors found in the configuration. 0 means the configuration is good and the estimates produced from it would be considered legitimate in the eyes of the original QNG challenge.

#### **Example**:
```python
import qe_radar_toolkit

configs = [[[[0,10],[10,15],[18,45]...], [[2,8,0],[14,15,0],[30,40,0]...], 0],
            [[[0,10],[10,15],[18,45]...], [[2,8,0],[14,15,0],[30,40,0]...], 1],
            [[[0,10],[10,15],[18,45]...], [[2,8,0],[14,15,0],[30,40,0]...], 2]...]

print(qe_radar_toolkit.test_config(configs))

>>> 0 # No Errors Found
```

### `test_score(estimates)`

Submit results with estimates for all targets in the testing dataset with intention for them to be scored. The returned results will be Score (mean squared score with the success approaching 0), precision (standard deviations for Rabi, Detuning and Time of Flight) and accuracy (means for Rabi, Detuning and Time of Flight).

#### **Example**:
```python
import qe_radar_toolkit

estimates = [[0.00453748376016974, -0.02249823109292496, 153.73902434863788, 0],
        [0.0002964523714059984, -0.015549490574576096, 643.6452780943542, 1],
        [0.000541916391029567, -0.017939610742308935, 549.3026779212704, 2]...]

print(qe_radar_toolkit.test_score(estimates))

>>> [45, [1.2, 4.2, 0.2], [0.5, 2.1, 1.1]] # [ Score, [Precision (STD) (Rabi, Detuning, Time of Flight)], [Accuracy (Mean) (Rabi, Detuning, Time of Flight)] ]