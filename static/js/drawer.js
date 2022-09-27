// Burger menus
document.addEventListener('DOMContentLoaded', function () {
    // open
    const burger = document.querySelectorAll('.drawer-burger');
    const menu = document.querySelectorAll('.drawer-menu');
  
    console.log(burger)
    console.log(menu)

    if (burger.length && menu.length) {
      for (var i = 0; i < burger.length; i++) {
        burger[i].addEventListener('click', function () {
            console.log('button pressed')
          for (var j = 0; j < menu.length; j++) {
            menu[j].classList.toggle('hidden');
          }
        });
      }
    }
  
    // close
    const close = document.querySelectorAll('.drawer-close');
    const backdrop = document.querySelectorAll('.drawer-backdrop');
  
    if (close.length) {
      for (var i = 0; i < close.length; i++) {
        close[i].addEventListener('click', function () {
          for (var j = 0; j < menu.length; j++) {
            menu[j].classList.toggle('hidden');
          }
        });
      }
    }
  
    if (backdrop.length) {
      for (var i = 0; i < backdrop.length; i++) {
        backdrop[i].addEventListener('click', function () {
          for (var j = 0; j < menu.length; j++) {
            menu[j].classList.toggle('hidden');
          }
        });
      }
    }
  });