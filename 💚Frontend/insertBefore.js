if( up && down) {
    tbody.insertBefore(up, down); // put up before down
    var temp = up.firstElementChild.textContent; // swap first cells' text content
    up.firstElementChild.textContent = down.firstElementChild.textContent;
    down.firstElementChild.textContent = temp;
  }
