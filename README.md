# Tame_Of_Thrones
This is oops solution for the problem [A Golden Crown](https://www.geektrust.in/coding-problem/backend/tame-of-thrones).
### Solution with build file
```python
pip install -r requirements.txt
python -m geektrust <absolute_path_to_input_file>
```
### Input
Input files are available in the input folder.<br/>
### Test
Test code in in ./tests package.It can be tested using following commands:<br/>
1. To run tests from module :
```python
python -m unittest tests/<test_module_name>
```
You can run tests with more detail (higher verbosity) by passing in the -v flag:<br/>
```python
python -m unittest -v tests/<test_module_name>
```
2. To run tests from class:
```python
python -m unittest tests/<test_module_name.class_name>
```
3. To run individual test method:
```python
python -m unittest tests/<test_module_name.class_name.method_name>
```