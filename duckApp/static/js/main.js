const model = document.getElementById("model");
const closeModelBtn = document.getElementById("close");
const editBtn = document.querySelector("#edit");

editBtn.addEventListener("click", (e) => {
  //   console.log(e.target);
  console.log("You clicked me");
  model.classList.add("is-active");
});
closeModelBtn.addEventListener("click", () => {
  model.classList.remove("is-active");
});
