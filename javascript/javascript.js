// To pass data from JS to Python, we are going to need a node package named "child_process".
const spawner = require('child_process').spawn;

// Here is the data we will pass to Python.
const dataToPassIn = "Send this to python script.";

// console.log('Data sent to python script: ', dataToPassIn);

// Creation of the process. 
// We call the spawner function we defined earlier. 
// spawner accepts two arguments, the first is the command it is going to run, the second is an array with the location of the python script we will run and the data we will pass in. 
const python_process = spawner('python', ['python/bpm_and_time.py', dataToPassIn]);

// We set a callback function on the python_process to trigger when data is returned.
python_process.stdout.on('data', (data) => {
    console.log('Data received from python script:', data.toString());
});
