import { askQuestion } from './util'

export async function start(){
  console.log("##### EASY ####")

  console.log("Exercise 1")
  for (let index = 0; index <= 100; index++) {
    if (index % 3 == 0) process.stdout.write("Fizz ");
    else if (index % 5 == 0) process.stdout.write("Buzz ");
    else process.stdout.write(index + " ");
  }
  console.log();

  console.log("Exercise 2");
  const year:number = Number(await askQuestion("Enter year to check for leap year: "));
  if (((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0)) console.log(year, "is a leap year");
  else console.log(year, "is not a leap year");

  console.log("Exercise 3");
  console.log("3.1");
  const n:number = Number(await askQuestion("n value for star exercise: "));
  for (let i = 1; i <= n; i++) {
    let stars:string = '';
    for (let j = 0; j < i; j++) {
      stars += "*";
    }
    console.log(stars);
  }

  console.log("3.2");
  for (let i = 1; i <= n; i++) {
    let stars:string = ''.padStart(n-i);
    for (let j = 0; j < i; j++) {
      stars += "*";
    }
    console.log(stars);
  }

  console.log("3.3");
  {
    let cols = n*2-1;
    for (let i = 0; i <= n; i++) {
      let stars:string = '';
      for (let j = 1; j <= cols ; j++) {
        if(i == 0){
          if(j == n) stars += "*";
          else stars += " ";
        }else{
          if(j == n-i || j == n+i) stars += "*";
          else stars += " ";
        }
      }
      console.log(stars);
    }
  }

  console.log("3.4")
  for (let i = 1; i <= n; i++) {
    let stars:string = '';
    for (let j = 1; j <= n ; j++) {
      if(i == j || j-1 == n-i) stars += "*";
      else stars += " ";
    }
    console.log(stars);
  }

  console.log("3.5")
  {
    let starCount = 1;
    let spaceCount = Math.ceil(n/2)-1;
    for (let i = 1; i <= n; i++) {
      let stars:string = '';
      for (let j = 0; j < spaceCount; j++) {
        stars += " ";
      }
      for (let l = 0; l < starCount; l++) {
        stars += "*";
      }
      console.log(stars);

      if (i != n/2){
        if(i < Math.ceil(n/2)){
          starCount += 2;
          spaceCount--;
        } else{
          starCount -= 2;
          spaceCount++;
        }
      }
    }
  }

  console.log("3.6")
  {
    let lines = n*2-1;
    let aCount = n-1;
    let bCount = n-1;
    let eCount = 0;
    let cCount = -aCount;
    let dCount = -bCount;
    for (let i = 0; i < lines; i++) {
      let letters:string = '';

      for (let index = 0; index < aCount; index++) {
        letters += "A";
      }
      for (let index = 0; index < cCount; index++) {
        letters += "C";
      }
      letters += "+";

      for (let index = 0; index < eCount; index++) {
        letters += "E";
      }
      if(eCount > 0) letters += "+";
      
      for (let index = 0; index < bCount; index++) {
        letters += "B";
      }
      
      for (let index = 0; index < dCount; index++) {
        letters += "D";
      }

      aCount--;
      bCount--;
      cCount++;
      dCount++;

      if (i == 0) eCount++;
      else if(i < n-1) eCount+=2;
      else if(i == lines-1) eCount--;
      else eCount -=2;
      console.log(letters);
    }
  }


  
  console.log("##### MEDIUM ####")

  console.log("Exercise 1");
  const number:number = Number(await askQuestion("Find prime numbers up to: "));
  let primeNumbers = [];
  for (let numberToCheck = 2; numberToCheck <= number; numberToCheck++) {
    let isPrime = true;
    for(let i = 2; i <= numberToCheck/2; i++)
    {
        if(numberToCheck%i == 0)
        {
            isPrime = false;
            break;
        }
  }
  if (isPrime) primeNumbers.push(numberToCheck);
}

console.log("Prime number found up to", number);
console.log(primeNumbers);


}