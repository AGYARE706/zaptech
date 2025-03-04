let score = parseFloat(prompt("Enter your score: "));
console.log("Your score is "+ score)

if (isNaN(score)) {
    console.log("Numbers please!");
} else if (score>=0 && score<=100) {
    if (score>=70) {
    console.log("You had an A")
    } else if (score>=60) {
        console.log("You had a B")
    }  else if (score>=50) {
        console.log("You had a C")
    }  else if (score>=45) {
    console.log("you had a D")
    } else if (score>=40) {
        console.log("You had an E")
    } else {
        console.log("You had an F")
    } 
} else{
    console.log("Enter a correct score!!");
}
    



