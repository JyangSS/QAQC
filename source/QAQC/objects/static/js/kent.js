ar elm = document.getElementById('delete-object');
var objectID = elm.getAttribute('data-object-id');
var resultDiv = document.getElementById('result');
elm.addEventListener('click', function() {
  var ask = confirm('r u sure?');
  if (ask && objectID) {
    var r = "Page will be redirected to </object/delete/" + objectID + "/>";
    resultDiv.textContent = r;
  } else {
    resultDiv.textContent = "User cancelled the dialog box...";
  }
  return false;
});
.delete-link {
  background-color: red;
  color: white;
  border: 1px solid white;
  cursor: pointer;
  padding: 3px;
}
#result {
  margin: 20px;
  padding: 10px;
  border: 1px solid orange;
}