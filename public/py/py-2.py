
function initGame() {

  y = player.y
  
  for (x = 0, msg=''; x< tiles.length; x++) {
    msg += tiles[x][y].type + ' '
  }
  showMessage(msg)
}




