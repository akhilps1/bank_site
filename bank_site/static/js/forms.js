let districts = ["Thiruvananthapuram","Pathanamthitta","Alappuzha","Kottayam","Kollam","Kochi",];
let tvpmBranchs = ["Chirayinkeezhu","Nedumangadu","Varkala","Kattakada"];
let pBranch =["Aranmula","Adoor","Pandalam"];
let alpBranch = ["Alappuzha West","Ambalappuzha","Aryadu Thekku"];
let ktymBranch = ["Kottayam", "Changanassery","Kanjirappally"];
let klmBranch = ["Shakthikulangara","Perinad","East Kallada"];
let kochBranch = ["Kalamassery","Aluva","Angamaly"];

let select1 = document.getElementById("select1");
let select2 = document.getElementById("select2");

districts.forEach(function addDistricts(item) {
  let option = document.createElement("option");
  option.text = item;
  option.value = item;
  select1.appendChild(option)

  
});
select1.onchange = function () {
  select2.innerHTML = "<option></option>";

  if (this.value == "Thiruvananthapuram") {
    addToSelect2(tvpmBranchs);

  }
  else if (this.value == "Pathanamthitta") {
    addToSelect2(pBranch);

  }
  else if (this.value == "Alappuzha") {
    addToSelect2(alpBranch);

  }
  else if (this.value == "Kottayam") {
    addToSelect2(ktymBranch);

  }
  else if (this.value == "Kollam") {
    addToSelect2(klmBranch);

  }
  else if (this.value == "Kochi") {
    addToSelect2(kochBranch);

  }
}

function addToSelect2 (arr) {
  arr.forEach(function (item) {
    let option = document.createElement("option");
    option.text = item;
    option.value = item;
    select2.appendChild(option)
    
  });
}