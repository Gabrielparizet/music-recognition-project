const audioFile = document.getElementById("input");
// console.log(audioFile.value);
// audioFile.addEventListener();
  audioFile.addEventListener('change', (event) => {
    const fileList = event.target.files;
    console.log(fileList);
  });
// console.log('pathToMyAudioFile:' + audioFile.value);