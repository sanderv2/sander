window.addEventListener("load", function () {
  console.log("Web Loaded!");
  const toggleBtn = document.querySelector(".toggle_btn");
  const toggleBtnIcon = document.querySelector(".toggle_btn i")
  const dropDownMenu = document.querySelector(".dropdown_menu");

  toggleBtn.onclick = function () {
    console.log("Working!");
    dropDownMenu.classList.toggle("open");
    const isOpen = dropDownMenu.classList.contains('open')

    toggleBtnIcon.classList = isOpen
      ? 'fa-solid fa-xmark'
      : 'fa-solid fa-bars'
  };
});





/* window.addEventListener("load", function () {
  console.log("Web Loaded!");
  const toggleBtn = document.querySelector(".toggle_btn");
  const dropDownMenu = document.querySelector(".dropdown_menu");

  toggleBtn.onclick = function () {
    console.log("Working!");
    dropDownMenu.classList.toggle("open");
    //const isOpen = dropDownMenu.classList.contains('open');
  };
});
 */