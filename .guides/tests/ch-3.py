
var fs = require('fs');

global.result = [];

global.output = function(val) {
  global.result = val;
}

var mazeWidth = 8;
var mazeHeight = 6;
var tiles = [mazeWidth];

for (var x = 0; x < mazeWidth; x++) {
  tiles[x] = [mazeHeight];
  for (var y = 0; y < mazeHeight; y++) {
    tiles[x][y] = {
      x: x,
      y: y,
      _type: Math.random() > 0 ? 'floor': 'wall'
    };

    Object.defineProperty(tiles[x][y], 'type', {
      get: function() {
        if(this.entity) {
          return this.entity.type;
        }
        return this._type; 
      },
      set: function(val) { this._type = val; }
    }); 
  }
}

try {
  var data = fs.readFileSync('/home/codio/workspace/public/js/ch-3.js', 'utf8');
  eval(data);
  
  initGame();
   
  if(Array.isArray(result)) {
    
    for(var i = 0; i < mazeWidth; i++) {
      if(tiles[i][3].type != result[i]) {
        process.stdout.write('Not quite right, try again!');  
        process.exit(1);
      }
    }
  } 
  else {
    process.stdout.write('Not quite right, try again!');  
    process.exit(1);
  }
  
  process.stdout.write('Well done!');  
  process.exit(0);

}
catch(e) {
  console.log(e)
}

process.stdout.write('Not quite right, try again!');  
process.exit(1);
