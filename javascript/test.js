// const audioFile = document.getElementById("audio-file");
// audioFile.addEventListener('change', (event) => {
//   const fileList = event.target.files;
//   console.log(fileList);
// });

function loadAudioFile(e){
  const url = URL.createObjectURL(e.files[0]);
  console.log(url);
  document.getElementById("track").setAttribute("src", url);
}