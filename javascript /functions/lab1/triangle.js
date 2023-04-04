/*
 * Programming Quiz: Build A Triangle (5-3)
 */

/*
 * QUIZ REQUIREMENTS
 * - Your code should have a `buildTriangle()` function
 * - Your `buildTriangle()` function should take one argument (or you can say parameter)
 * - Your `laugh()` function should build the triangle as described above
 */


// creates a line of * for a given length
function makeLine(length) {
    let line = "";
    for (let j = 1; j <= length; j++) {
        line += "* ";
    }
    return line + "\n";
}

// your code goes here.  Make sure you call makeLine() in your own code.

function buildTriangle(length){
  var Triangle = "";
  let lineNumber = 1

  for(lineNumber = 1; lineNumber < length; lineNumber++){
    Triangle = Triangle + makeLine(lineNumber);
  }
  return Triangle;
}


// test your code
console.log(buildTriangle(12));
